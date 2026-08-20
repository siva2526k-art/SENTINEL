import os
import sys
import fitz  # PyMuPDF

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def fill_cover_pdf():
    input_path = r"C:\Users\siva2\OneDrive\Desktop\STUDENT ACTITIVITY FILE - IDL 1 (1) (2).pdf"
    output_path = r"C:\Users\siva2\OneDrive\Desktop\STUDENT_ACTIVITY_FILE_IDL1_COVER_FILLED.pdf"
    
    doc = fitz.open(input_path)
    dark = (0.05, 0.1, 0.25)
    font_name = "helv"

    # PAGE 1 FILL-IN
    p1 = doc[0]
    
    # Department & Section (Author: Gokula Kannan M, Section A)
    p1.insert_text(fitz.Point(145, 209), "Computer Science and Engineering", fontsize=8.5, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(400, 209), "A", fontsize=8.5, fontname=font_name, color=dark)

    # Innovation Ecosystem Project ID
    p1.insert_text(fitz.Point(225, 238), "SAIRAM-IDL1-2026-CSE-09", fontsize=8.5, fontname=font_name, color=dark)

    # Title of the Project
    p1.insert_text(fitz.Point(145, 266), "SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine", fontsize=8, fontname=font_name, color=dark)

    # Interdisciplinary Project Checkbox
    p1.insert_text(fitz.Point(228, 292), "X", fontsize=9, fontname=font_name, color=dark)

    # Members Table
    p1.insert_text(fitz.Point(135, 365), "1", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(180, 365), "Gokula Kannan M", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(340, 365), "SEC25CS196", fontsize=8, fontname=font_name, color=dark)

    p1.insert_text(fitz.Point(135, 385), "2", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(180, 385), "Lakshan M", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(340, 385), "SEC25CS036", fontsize=8, fontname=font_name, color=dark)

    p1.insert_text(fitz.Point(135, 405), "3", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(180, 405), "Sivabalan T", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(340, 405), "SEC25CS101", fontsize=8, fontname=font_name, color=dark)

    # Version Checkbox
    p1.insert_text(fitz.Point(72, 431), "X", fontsize=9, fontname=font_name, color=dark)

    # Domain Name & IEEE
    p1.insert_text(fitz.Point(160, 581), "Cybersecurity & Artificial Intelligence", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(160, 607), "IEEE Computer Society", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(175, 633), "IEEE Student Branch Sairam", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(165, 659), "Sairam Innovation Ecosystem / Cyber Security Club", fontsize=8, fontname=font_name, color=dark)

    # Coordinator & Supervisor (Dr. A. SHEELA)
    p1.insert_text(fitz.Point(290, 685), "Dr. A. SHEELA", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(485, 685), "IDL-FAC-01", fontsize=8, fontname=font_name, color=dark)

    p1.insert_text(fitz.Point(215, 711), "Dr. A. SHEELA", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(485, 711), "IDL-FAC-02", fontsize=8, fontname=font_name, color=dark)

    # External Guide & Org
    p1.insert_text(fitz.Point(235, 737), "Cyber Forensic Specialists & Industry Leads", fontsize=8, fontname=font_name, color=dark)
    p1.insert_text(fitz.Point(235, 764), "Cyberdome Investigations / Zoho Corporation", fontsize=8, fontname=font_name, color=dark)

    # PAGE 2 FILL-IN (SDGs & Activity Index)
    p2 = doc[1]

    # Primary SDG
    p2.insert_text(fitz.Point(165, 172), "SDG 9: Industry, Innovation, and Infrastructure", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_textbox(fitz.Rect(355, 160, 520, 210), "1. SAP-SDG9-CYBER-01: Resilient cyber infrastructure & AI SOC automation.\n2. SAP-SDG9-CYBER-02: Zero-trust cloud-edge security architecture.", fontsize=7, fontname=font_name, color=dark)

    # Secondary SDG
    p2.insert_text(fitz.Point(165, 238), "SDG 16: Peace, Justice, and Strong Institutions", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_textbox(fitz.Rect(355, 226, 520, 275), "1. SAP-SDG16-SEC-01: Evidence privacy & chain-of-custody enforcement.\n2. SAP-SDG16-SEC-02: Citizen PII protection in digital investigation.", fontsize=7, fontname=font_name, color=dark)

    # Tertiary SDG
    p2.insert_text(fitz.Point(165, 298), "SDG 8: Decent Work and Economic Growth", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_textbox(fitz.Rect(355, 286, 520, 335), "1. SAP-SDG8-AUTO-01: Reduction of SOC analyst alert fatigue.\n2. SAP-SDG8-AUTO-02: Decreasing MTTR from 45 mins to < 30 seconds.", fontsize=7, fontname=font_name, color=dark)

    # Activity Log Table Entries (Marks left completely BLANK for Coordinator assessment)
    # Row 1 (Orientation)
    p2.insert_text(fitz.Point(265, 412), "01/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(312, 412), "07/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(410, 412), "Completed", fontsize=7.5, fontname=font_name, color=dark)

    # Row 2 (Problem Identification)
    p2.insert_text(fitz.Point(265, 453), "08/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(312, 453), "14/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(410, 453), "Completed", fontsize=7.5, fontname=font_name, color=dark)

    # Row 3 (Customer Segments)
    p2.insert_text(fitz.Point(265, 495), "15/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(312, 495), "21/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(410, 495), "In Progress", fontsize=7.5, fontname=font_name, color=dark)

    # Row 4 (Ideation)
    p2.insert_text(fitz.Point(265, 536), "22/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(312, 536), "28/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(410, 536), "Upcoming", fontsize=7.5, fontname=font_name, color=dark)

    # Row 5 (Milestone 1)
    p2.insert_text(fitz.Point(265, 577), "29/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(312, 577), "04/09/2026", fontsize=7.5, fontname=font_name, color=dark)
    p2.insert_text(fitz.Point(410, 577), "Upcoming", fontsize=7.5, fontname=font_name, color=dark)

    # PAGE 3 FILL-IN (Competitions & Signatures)
    p3 = doc[2]

    # Competition Row 1 (Individual Hackathon entry by Sivabalan T)
    p3.insert_textbox(fitz.Rect(75, 360, 250, 400), "Hac'KP 2026 (7th Edition National Hackathon by Kerala Police Cyberdome)", fontsize=7, fontname=font_name, color=dark)
    p3.insert_text(fitz.Point(260, 375), "14/08/2026", fontsize=7.5, fontname=font_name, color=dark)
    p3.insert_textbox(fitz.Rect(325, 360, 405, 400), "Zoho Corporation, Chennai", fontsize=7.5, fontname=font_name, color=dark)
    p3.insert_textbox(fitz.Rect(415, 360, 490, 400), "Individual Hackathon Finalist (Sivabalan T)", fontsize=7, fontname=font_name, color=dark)

    # Patent Row 1
    p3.insert_textbox(fitz.Rect(75, 470, 250, 510), "Confidentiality-Preserving Autonomous SOC Triage via Tokenized Edge-Cloud Multi-Agent Systems", fontsize=7, fontname=font_name, color=dark)
    p3.insert_text(fitz.Point(260, 485), "August 2026", fontsize=7.5, fontname=font_name, color=dark)
    p3.insert_textbox(fitz.Rect(325, 470, 405, 510), "IEEE / USENIX Track", fontsize=7.5, fontname=font_name, color=dark)
    p3.insert_textbox(fitz.Rect(415, 470, 490, 510), "Paper Manuscript & Patent Drafted", fontsize=7, fontname=font_name, color=dark)

    # Signatures Info
    p3.insert_text(fitz.Point(60, 615), "Dr. A. SHEELA", fontsize=8, fontname=font_name, color=dark)
    p3.insert_text(fitz.Point(230, 615), "Gokula Kannan M", fontsize=8, fontname=font_name, color=dark)
    p3.insert_text(fitz.Point(420, 615), "Head of Department", fontsize=8, fontname=font_name, color=dark)

    doc.save(output_path)
    doc.close()
    print(f"✅ Cover PDF Refined & Filled: {output_path}")
    return output_path

def fill_week1_pdf():
    input_path = r"C:\Users\siva2\OneDrive\Desktop\IDL WEEK 1.pdf"
    output_path = r"C:\Users\siva2\OneDrive\Desktop\IDL_WEEK_1_FILLED.pdf"
    
    doc = fitz.open(input_path)
    dark = (0.05, 0.1, 0.25)

    # Page 1: Bullet 1
    p1 = doc[0]
    w1_p1_text = (
        "Security Operations Centers (SOCs) generate over 10,000 security logs daily, creating severe alert fatigue where human analysts spend 30–45 minutes manually triaging single events. "
        "Commercial AI endpoints cannot be deployed directly due to data privacy regulations and risks of uploading confidential network payloads to external servers.\n\n"
        "The proposed solution, SENTINEL, introduces Reversible Tokenized Pseudonymization, scrubbing 100% of sensitive PII, IP addresses, and hostnames locally before AI reasoning occurs. "
        "This enables enterprise-grade autonomous triage at $0 operational cost for 90% of routine alerts using local consumer GPU hardware (NVIDIA RTX 3050)."
    )
    p1.insert_textbox(fitz.Rect(95, 220, 760, 520), w1_p1_text, fontsize=10, fontname="helv", color=dark)

    # Page 2: Bullet 2
    p2 = doc[1]
    w1_p2_text = (
        "The global SIEM automation and threat intelligence market is valued at $13.2 Billion+ with an 18.5% CAGR. Primary target markets include Enterprise SOCs, Managed Security Service Providers (MSSPs), Air-Gapped Defense Networks, Cyber Crime Units, and Startups.\n\n"
        "Technical resourcefulness is demonstrated by quantizing 70B parameter models down to 4-bit (IQ3_M) GGUF format to execute high-capacity intelligence on edge workstations."
    )
    p2.insert_textbox(fitz.Rect(95, 120, 760, 480), w1_p2_text, fontsize=10, fontname="helv", color=dark)

    # Page 3: Bullet 3
    p3 = doc[2]
    w1_p3_text = (
        "1. Problem Formulation: Identifying SOC alert fatigue and data privacy constraints.\n"
        "2. Proof-of-Concept: Engineering local Zero-Trust Data Sanitizer (src/sanitizer.py).\n"
        "3. MVP Architecture: Building 3-Tier Hybrid AI Router (src/router.py).\n"
        "4. Validation & Pitching: Selected for National Pitching Round at Hac'KP 2026 @ Zoho Corporation.\n"
        "5. Commercialization: Deploying open-source SaaS framework and enterprise MSSP engine."
    )
    p3.insert_textbox(fitz.Rect(95, 160, 760, 480), w1_p3_text, fontsize=10, fontname="helv", color=dark)

    doc.save(output_path)
    doc.close()
    print(f"✅ Week 1 PDF Refined & Filled: {output_path}")
    return output_path

def fill_week2_pdf():
    input_path = r"C:\Users\siva2\OneDrive\Desktop\IDL WEEK 2.pdf"
    output_path = r"C:\Users\siva2\OneDrive\Desktop\IDL_WEEK_2_FILLED.pdf"
    
    doc = fitz.open(input_path)
    dark = (0.05, 0.1, 0.25)
    font_name = "helv"

    # Page 1: Bullet 1 (Identify real-world problems based on personal interests)
    p1 = doc[0]
    w2_p1_text = (
        "A. Personal Interest & Cyber Defense Motivation:\n"
        "• Deep Interest in System Architecture & Defensive Security: As Team Lead (Gokula Kannan M), my primary focus lies in solving critical engineering bottlenecks where human manual triage speed fails to match machine-speed cyber attacks.\n\n"
        "B. Problem Formulation — SOC Alert Fatigue & Telemetry Privacy Dilemma:\n"
        "• The Alert Triage Bottleneck: Modern Security Operations Centers (SOCs) ingest over 5,000 daily security logs from SIEM agents (Wazuh, Elastic). Tier-1 human analysts spend 30 to 45 minutes investigating single alerts, causing ~70% of security notifications to remain completely unexamined.\n"
        "• The Cloud Data Leakage Threat: Transmitting un-scrubbed raw telemetry—containing internal IP topographies (RFC 1918), officer emails, hostnames, and credentials—to commercial cloud AI models creates catastrophic data leakage risks, violating privacy mandates such as India's DPDP Act 2023.\n\n"
        "C. Project SENTINEL Application & Value Proposition:\n"
        "• Autonomous Zero-Trust AI Co-Pilot: Delivering machine-speed incident triage (<30s MTTR) via an in-RAM regex data sanitizer, 3-tier model router, and AST code sandbox, ensuring zero cloud telemetry leakage and $0 Tier-1 compute cost."
    )
    p1.insert_textbox(fitz.Rect(95, 235, 750, 520), w2_p1_text, fontsize=9.5, fontname=font_name, color=dark)

    # Page 2: Bullet 2 (Skills, experiences, and societal needs)
    p2 = doc[1]
    w2_p2_text = (
        "A. Technical Skills & Core Competencies (Gokula Kannan M - Team Lead):\n"
        "• Systems Architecture & Venture Strategy: Expertise in high-throughput asynchronous backend engineering (FastAPI, Python), multi-tier AI model cascading (Ollama local GPU to cloud fallback), and technical project governance.\n"
        "• Defensive Cybersecurity & Threat Intelligence: Applied knowledge in SIEM rule correlation (Wazuh), MITRE ATT&CK TTP taxonomy mapping, and active defense containment workflows.\n\n"
        "B. Critical Societal & Enterprise Needs:\n"
        "• Enterprise & Healthcare Infrastructure Defense: Small-to-medium enterprise (SME) SOCs, public hospitals, and municipal utilities cannot afford $100k+/year enterprise SOAR tools (Splunk, Cortex XSOAR), leaving critical infrastructure vulnerable to ransomware.\n"
        "• Legal Evidence Integrity & Chain-of-Custody: Law enforcement cyber crime cells and air-gapped defense labs require local, tamper-evident JSONL audit logging and courtroom-admissible PDF executive briefs.\n\n"
        "C. Bridging the Societal Gap through Project SENTINEL:\n"
        "• Democratizing Enterprise Security: Providing an open-source, privacy-first AI co-pilot that enables resource-constrained organizations to automate routine threat triage with zero operational cloud licensing overhead."
    )
    p2.insert_textbox(fitz.Rect(95, 120, 750, 510), w2_p2_text, fontsize=9.5, fontname=font_name, color=dark)

    # Page 3: Bullet 3 (Passion CV)
    p3 = doc[2]
    w2_p3_text = (
        "PASSION CV & ENTREPRENEURIAL PROFILE — GOKULA KANNAN M (TEAM LEAD):\n\n"
        "• Role & Designation: Systems Architect & Project Lead | Student ID: SEC25CS196 | Department of Computer Science & Engineering (Section A)\n"
        "• Technical Domain & Core Specialization: Distributed Systems Engineering, AI Pipeline Architecture, Cybersecurity Policy Enforcement, Venture Strategy.\n\n"
        "• Key Accomplishments & Leadership Contributions:\n"
        "  1. System Architecture: Lead architect of Project SENTINEL's 3-Tier AI Router and Zero-Trust Data Sanitizer pipeline.\n"
        "  2. Venture Pitching & National Validation: Selected to represent Sairam Institutions at Hac'KP 2026 (7th Edition National Hackathon by Kerala Police Cyberdome @ Zoho Corporation Campus).\n"
        "  3. Research & Academic Output: Co-author of academic literature survey analyzing 6 peer-reviewed IEEE/ACM papers on autonomous threat triage and privacy-preserving AI.\n\n"
        "• Entrepreneurial Opportunity & Commercialization Roadmap:\n"
        "  • Opportunity Identified: Commercializing SENTINEL as a hybrid open-core / MSSP platform tailored for air-gapped defense labs, municipal SOCs, and police cyber forensic units requiring 100% data sovereignty."
    )
    p3.insert_textbox(fitz.Rect(95, 160, 750, 520), w2_p3_text, fontsize=9.2, fontname=font_name, color=dark)

    doc.save(output_path)
    doc.close()
    print(f"✅ Week 2 PDF Refined & Filled: {output_path}")
    return output_path

def merge_all_pdfs(cover_pdf, week1_pdf, week2_pdf):
    output_master = r"C:\Users\siva2\OneDrive\Desktop\STUDENT_ACTIVITY_FILE_IDL1_COMPLETE_MASTER.pdf"
    sentinel_doc_pdf = r"c:\Users\siva2\Projects\SENTINEL\docs\SENTINEL_IDL1_Student_Activity_File.pdf"

    master = fitz.open()
    for p in [cover_pdf, week1_pdf, week2_pdf]:
        d = fitz.open(p)
        master.insert_pdf(d)
        d.close()

    master.save(output_master)
    master.save(sentinel_doc_pdf)
    master.close()
    print(f"🎉 MASTER COMBINED PDF CREATED: {output_master}")
    return output_master

if __name__ == "__main__":
    c_pdf = fill_cover_pdf()
    w1_pdf = fill_week1_pdf()
    w2_pdf = fill_week2_pdf()
    merge_all_pdfs(c_pdf, w1_pdf, w2_pdf)
