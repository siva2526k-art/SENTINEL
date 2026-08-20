import os
import sys
import shutil
import fitz  # PyMuPDF

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def fill_week2_pdf():
    input_path = r"C:\Users\siva2\OneDrive\Desktop\IDL WEEK 2.pdf"
    output_path = r"C:\Users\siva2\OneDrive\Desktop\IDL_WEEK_2_FILLED.pdf"
    sentinel_doc_path = r"c:\Users\siva2\Projects\SENTINEL\docs\IDL_WEEK_2_FILLED.pdf"
    
    doc = fitz.open(input_path)
    dark = (0.05, 0.1, 0.25)
    bullet_color = (0.02, 0.12, 0.35)
    font_name = "helv"

    # PAGE 1: • Identify real-world problems based on personal interests
    p1 = doc[0]
    
    # Text box for Page 1 below prompt (rect: x=95, y=240, w=710, h=300)
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

    # PAGE 2: • Skills, experiences, and societal needs
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

    # PAGE 3: • Prepare a Passion CV to identify potential entrepreneurial opportunities.
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
    shutil.copy2(output_path, r"C:\Users\siva2\OneDrive\Desktop\IDL WEEK 2.pdf")
    shutil.copy2(output_path, sentinel_doc_path)
    doc.close()
    print(f"✅ Week 2 PDF Filled Successfully: {output_path}")
    return output_path

if __name__ == "__main__":
    fill_week2_pdf()
