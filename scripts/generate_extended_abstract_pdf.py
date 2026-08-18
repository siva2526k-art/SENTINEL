import os
import sys
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#0f172a"))
        
        # Header
        self.drawString(36, 756, "SHIELD AI — TECHNICAL ABSTRACT & ARCHITECTURE SPECIFICATION")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 748, 576, 748)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 30, "Sri Sai Ram Engineering College | Academic Year 2026–2027")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 30, page_text)
        self.line(36, 42, 576, 42)
        self.restoreState()

def build_pdf():
    pdf_path = r"c:\Users\siva2\Projects\SENTINEL\docs\SENTINEL_Extended_Abstract_2000Words.pdf"
    desktop_path = r"C:\Users\siva2\OneDrive\Desktop\SENTINEL_Extended_Abstract_2000Words.pdf"

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor('#2563eb'),
        alignment=1,
        spaceAfter=6
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    story = []

    # Title Banner (NO AUTHOR NAME)
    story.append(Paragraph("SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM", title_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Sri Sai Ram Engineering College (TNEA Code: 1419)", subtitle_style))
    story.append(Paragraph("<b>Academic Year:</b> 2026–2027 &nbsp;|&nbsp; <b>Repository:</b> github.com/siva2526k-art/SENTINEL &nbsp;|&nbsp; <b>Target:</b> Hac'KP 2026 Technical Abstract", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563eb"), spaceAfter=8))

    # Section 1: Abstract
    story.append(Paragraph("1. ABSTRACT / EXECUTIVE SUMMARY", h1_style))
    s1_text = (
        "Security Operations Centers (SOCs) face acute operational bottlenecks driven by overwhelming telemetry volume, high false-positive rates, "
        "and analyst burnout. In typical enterprise environments, security analysts spend between 30 and 45 minutes investigating individual alerts, "
        "leading to significant delays and leaving a major portion of security notifications unreviewed. Concurrently, while Generative Artificial "
        "Intelligence and Large Language Models (LLMs) offer advanced natural-language reasoning for threat analysis, transmitting raw security "
        "telemetry to commercial cloud APIs creates severe data privacy vulnerabilities and risks exposing sensitive credentials, internal IP topographies, "
        "and employee data to external endpoints.<br/><br/>"
        "This paper presents <b>SHIELD AI</b> (<i>Autonomous Cyber Defence and Security Intelligence Platform</i>, formerly SENTINEL), an open-source "
        "research prototype designed to evaluate a privacy-aware, human-supervised approach to automated SOC alert triage. SHIELD AI implements an asynchronous "
        "SIEM syslog ingestion bridge, a local zero-trust regex sanitizer with an inline prompt-injection firewall, a three-tier AI routing module, an embedded "
        "vector threat memory store (ChromaDB), a temporal entity correlator with directed attack-graph construction, an Abstract Syntax Tree (AST) Python code "
        "execution sandbox, human-in-the-loop (HITL) authorization gates, mock-mode active response controllers, JSONL audit logging, and automated executive PDF "
        "incident report generation via ReportLab.<br/><br/>"
        "By retaining token de-anonymization lookup dictionaries strictly within volatile local RAM, SHIELD AI prevents sensitive network identifiers from "
        "traversing external boundaries during AI triage. SHIELD AI is currently implemented as an early-stage Minimum Viable Product (MVP) to demonstrate "
        "architectural feasibility. Future work will focus on empirical evaluation against labeled SIEM datasets, production-grade security hardening, and "
        "formal bench-testing prior to operational deployment.<br/><br/>"
        "<b>Keywords:</b> Privacy-Preserving AI, SOC Alert Triage, Multi-Tier Model Cascading, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Code Sandbox, Human-in-the-Loop, Digital Forensics."
    )
    story.append(Paragraph(s1_text, body_style))

    # Section 2: Problem Statement
    story.append(Paragraph("2. PROBLEM STATEMENT", h1_style))
    s2_text = (
        "Modern enterprise, municipal, and government computer networks rely on SIEM platforms—such as Wazuh, Elastic, or Splunk—to aggregate logs. "
        "However, security teams face three fundamental systemic challenges:<br/>"
        "1. <b>Alert Fatigue & Manual Triage Delay:</b> Rule-based detection signatures trigger thousands of notifications daily. Tier-1 analysts spend 30 to 45 minutes per alert, causing severe cognitive burnout and extended attacker dwell time.<br/>"
        "2. <b>Data Privacy & Telemetry Leakage Risks:</b> Ingesting un-scrubbed security logs into commercial cloud LLM APIs introduces compliance risks. Telemetry contains Personal Identifiable Information (PII), employee emails, internal IPs (RFC 1918), MAC addresses, and API/JWT tokens that violate statutory data privacy mandates.<br/>"
        "3. <b>Requirement for Offline & Air-Gapped Operation:</b> Defense networks, law enforcement labs, and critical infrastructure operate within strict air-gapped physical boundaries requiring local, self-hosted AI reasoning capabilities."
    )
    story.append(Paragraph(s2_text, body_style))

    # Section 3: Proposed System
    story.append(Paragraph("3. PROPOSED SYSTEM", h1_style))
    s3_text = (
        "SHIELD AI is engineered as a modular Python framework incorporating the following core technical components:<br/>"
        "• <b>Wazuh / SIEM Webhook Ingestion</b> (<code>src/ingestion/wazuh_listener.py</code>): Non-blocking asynchronous FastAPI listener.<br/>"
        "• <b>Local Zero-Trust Data Sanitizer</b> (<code>src/sanitizer.py</code>): Regex pattern matching scrubbing IPs, emails, MACs, and API tokens (e.g., <code>[USER_1]</code>, <code>[INTERNAL_IP_1]</code>), holding lookup tables in volatile RAM.<br/>"
        "• <b>Prompt Injection Firewall Guard</b> (<code>src/sanitizer.py</code>): Detects adversarial prompt overrides, replacing them with a <code>[NEUTRALIZED_PROMPT_INJECTION]</code> marker.<br/>"
        "• <b>Three-Tier AI Router</b> (<code>src/router.py</code>, <code>src/ai_client.py</code>): Routes queries to local Tier 1 Ollama (defaulting to <code>deepseek-r1:8b</code> with a <code>llama3.2:1b</code> fallback) or policy-controlled cloud endpoints (Groq, Gemini, OpenRouter, OpenAI).<br/>"
        "• <b>MITRE ATT&CK Mapper</b> (<code>src/mitre_mapper.py</code>): Correlates log attributes with tactics (e.g., Credential Access) and technique IDs (e.g., <code>T1110</code> Brute Force).<br/>"
        "• <b>Vector Threat Memory / RAG</b> (<code>src/memory.py</code>): Embedded ChromaDB store calculating cosine similarity against historical incidents.<br/>"
        "• <b>Entity, Temporal & Attack-Graph Correlation</b> (<code>src/correlation/</code>): Clusters events into Directed Acyclic Graphs (DAGs).<br/>"
        "• <b>AST Code Execution Sandbox</b> (<code>src/sandbox.py</code>): Inspects script syntax trees with <code>ast.parse()</code>, blocking dangerous primitives (<code>os</code>, <code>sys</code>, <code>subprocess</code>, <code>eval</code>).<br/>"
        "• <b>FastAPI REST API</b> (<code>src/api/main.py</code>): Application gateway for REST and real-time WebSockets integration.<br/>"
        "• <b>Human-in-the-Loop Authorization Gate</b> (<code>src/response/response_engine.py</code>): Requires explicit analyst sign-off before containment actions proceed.<br/>"
        "• <b>Mock-Mode Active Response Controllers</b> (<code>src/response/</code>): Simulated containment modules (firewall, process kill, host isolation).<br/>"
        "• <b>JSONL Audit Logger</b> (<code>src/audit_logger.py</code>): File-backed audit logger (<code>sentinel_audit_trail.jsonl</code>).<br/>"
        "• <b>Executive PDF Generator</b> (<code>src/reports/pdf_generator.py</code>): Compiles ReportLab PDF incident summaries.<br/>"
        "• <b>Discord SOC Notifier</b> (<code>src/integrations/discord_bot.py</code>): Dispatches real-time alerts and HITL approval pings."
    )
    story.append(Paragraph(s3_text, body_style))

    # Section 4: End-to-End Architecture
    story.append(Paragraph("4. END-TO-END SYSTEM ARCHITECTURE", h1_style))
    s4_text = (
        "<b>Stage 1: Ingestion & Privacy Boundary:</b> Telemetry arrives via FastAPI syslog webhooks. <code>DataSanitizer</code> neutralizes prompt injections and tokenizes PII via regex. Lookup tables reside exclusively in volatile RAM.<br/>"
        "<b>Stage 2: Context, RAG, Correlation & Attack Graph:</b> Sanitized logs are mapped to MITRE ATT&CK TTPs, queried against ChromaDB embeddings, and clustered into Directed Acyclic Graphs (DAGs).<br/>"
        "<b>Stage 3: AI Triage, Human Approval, Controlled Response, Audit & Reporting:</b> <code>SentinelRouter</code> dispatches to Tier-1 local Ollama or cloud endpoints. AST Code Sandbox inspects de-obfuscation scripts. Containment recommendations require analyst HITL authorization before mock response execution. Audit milestones append to JSONL, and ReportLab compiles incident PDFs."
    )
    story.append(Paragraph(s4_text, body_style))

    # Section 5: Current Prototype Status
    story.append(Paragraph("5. CURRENT PROTOTYPE STATUS", h1_style))
    s5_text = (
        "SHIELD AI is an early-stage <b>research prototype and Minimum Viable Product (MVP)</b> designed to evaluate privacy-preserving AI triage workflows. "
        "It is <b>not</b> a production-ready SOC platform, commercial SOAR software, or verified legal forensics tool. Current capabilities represent architectural proofs-of-concept."
    )
    story.append(Paragraph(s5_text, body_style))

    # Section 6: Limitations & Future Work
    story.append(Paragraph("6. LIMITATIONS AND FUTURE WORK", h1_style))
    s6_text = (
        "<b>Current Limitations:</b><br/>"
        "1. <i>Sanitizer Scope & RAM Security:</i> Relies on Regex rather than Named Entity Recognition (NER); RAM identity maps are stored in unencrypted volatile memory.<br/>"
        "2. <i>Security Hardening & RBAC:</i> Lacks production-grade Role-Based Access Control (RBAC), multi-factor authentication, and encrypted secret stores.<br/>"
        "3. <i>Audit Log Verification:</i> Audit records are stored in a standard local JSONL text file without cryptographic signatures or hardware tamper-evident enforcement.<br/>"
        "4. <i>Model Output Schema & Containment Controls:</i> Model outputs require strict JSON schema validation. Active containment runs in mock mode by default.<br/><br/>"
        "<b>Future Work Roadmap:</b><br/>"
        "• Construct a labeled benchmark dataset using Wazuh SIEM logs to measure triage accuracy, latency, and false-positive reduction.<br/>"
        "• Integrate lightweight local NER models (spaCy / ONNX) and encrypt RAM lookup tables.<br/>"
        "• Implement JWT-based RBAC, TLS-encrypted webhooks, tamper-evident audit logs, mandatory IP allowlists, and containerization (Docker/CI/CD)."
    )
    story.append(Paragraph(s6_text, body_style))

    # Section 7: Conclusion
    story.append(Paragraph("7. CONCLUSION", h1_style))
    s7_text = (
        "SHIELD AI demonstrates a privacy-preserving, human-supervised approach to AI-assisted SIEM alert triage. "
        "By combining local regex data sanitization, prompt-injection neutralization, three-tier model routing, vector threat memory, and mandatory human authorization gates, "
        "the framework illustrates how organizations can leverage language models while retaining control over sensitive telemetry. "
        "SHIELD AI requires rigorous, reproducible benchmark evaluation and extensive security hardening before any real-world operational deployment."
    )
    story.append(Paragraph(s7_text, body_style))

    # Section 8: References
    story.append(Paragraph("8. REFERENCES", h1_style))
    ref_text = (
        "1. <b>MITRE ATT&CK Framework:</b> MITRE Corporation, 'MITRE ATT&CK Enterprise Matrix,' 2024. Available: attack.mitre.org<br/>"
        "2. <b>Wazuh Open Source SIEM:</b> Wazuh Inc., 'Wazuh Documentation & Active Response Architecture,' 2024. Available: documentation.wazuh.com<br/>"
        "3. <b>ChromaDB Vector Store:</b> Chroma Core Inc., 'Chroma: The Open-Source Embedding Database,' 2024. Available: docs.trychroma.com<br/>"
        "4. <b>FastAPI Framework:</b> S. Ramírez, 'FastAPI High Performance Web Framework,' 2024. Available: fastapi.tiangolo.com<br/>"
        "5. <b>Ollama Local LLM Runtime:</b> Ollama Project, 'Ollama: Get up and running with Llama 3.2 and DeepSeek locally,' 2024. Available: ollama.com<br/>"
        "6. <b>ReportLab PDF Library:</b> ReportLab Software Ltd., 'ReportLab Open Source PDF Toolkit,' 2024. Available: www.reportlab.com"
    )
    story.append(Paragraph(ref_text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    shutil.copy2(pdf_path, desktop_path)
    print(f"✅ Generated & Saved to Desktop: {desktop_path}")

if __name__ == "__main__":
    build_pdf()
