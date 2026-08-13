"""
SENTINEL — Master Pitch Deck & Speaker Guide Generator (Desktop PDF)
Generates a 10-Slide Master Presentation & Solo Presenter Script PDF directly on Desktop.
"""
import os
import sys

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def generate_pitch_deck_pdf(output_path=r"C:\Users\siva2\Desktop\SENTINEL_Master_Pitch_Deck_and_Speaker_Guide.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Landscape orientation for slides
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(letter),
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    story = []
    styles = getSampleStyleSheet()

    # Custom Styles
    slide_title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1e3a8a'),
        spaceAfter=10
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1d4ed8'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'SlideBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0f172a')
    )

    script_style = ParagraphStyle(
        'SpeakerScript',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1e293b')
    )

    slides_data = [
        {
            "slide_num": "SLIDE 1",
            "title": "🛡️ SENTINEL — Autonomous AI SOC Triage & Privacy Platform",
            "subtitle": "Security Event Network Triage Investigation with Neural Engine and LLM",
            "bullets": [
                "<b>Presenter</b>: Sivabalan T (Lead Architect)",
                "<b>Venue</b>: Hac'KP 2026 — Zoho Corporation",
                "<b>Core Breakthrough</b>: Privacy-Preserving Zero-Trust Data Sanitizer + 3-Tier MoE AI Router + AST Code Sandbox Guard."
            ],
            "script": "Respected Judges, good morning. I am Sivabalan T, Lead Architect of SENTINEL. Today I am proud to present SENTINEL—the world's first privacy-preserving, 3-tier AI-assisted SOC triage and controlled incident response platform designed specifically for law enforcement and enterprise SOC operations."
        },
        {
            "slide_num": "SLIDE 2",
            "title": "🚨 The Problem: Alert Fatigue, Data Leakage & High AI Costs",
            "subtitle": "Why Current SOC Tools & Basic AI Wrappers Fail",
            "bullets": [
                "<b>Alert Fatigue</b>: SOC analysts handle 5,000+ alerts daily, leading to missed zero-day threats.",
                "<b>Privacy & Legal Risk</b>: Tools like AiSOC send raw police emails, passwords, and internal IPs to commercial cloud APIs, violating DPDP Act and GDPR.",
                "<b>High Token Costs</b>: Sending raw telemetry to cloud LLMs costs thousands of dollars monthly."
            ],
            "script": "Every single day, SOC teams are overwhelmed by thousands of alerts. When security teams try to use commercial AI tools, they unknowingly leak sensitive police emails and internal IP addresses to commercial cloud servers. Furthermore, paying per token for raw SIEM logs creates unsustainable monthly costs."
        },
        {
            "slide_num": "SLIDE 3",
            "title": "💡 The SENTINEL Solution Architecture",
            "subtitle": "Zero-Trust Privacy + 3-Tier System MoE + AST Code Security",
            "bullets": [
                "<b>Zero-Trust Sanitizer</b>: Replaces real PII with synthetic tokens ([USER_1], [INTERNAL_IP_1]) in encrypted local RAM.",
                "<b>Prompt Injection Firewall</b>: Neutralizes log-embedded attack phrases before AI processing.",
                "<b>3-Tier System-Level MoE Router</b>: Processes 90% routine alerts offline on local workstation GPUs for $0 software cost.",
                "<b>AST Code Execution Guard</b>: Inspects AI code syntax tree to block dangerous shell execution."
            ],
            "script": "SENTINEL solves this completely through a 4-pillar architecture: First, a Zero-Trust Data Sanitizer that strips all PII; second, a Prompt Injection Firewall that neutralizes embedded log attacks; third, a 3-Tier AI Router that processes routine alerts locally on GPU for $0 cost; and fourth, an AST Code Sandbox that prevents AI-generated code execution attacks."
        },
        {
            "slide_num": "SLIDE 4",
            "title": "🔒 Zero-Trust Sanitizer & Reversible Dummy Mapping",
            "subtitle": "Zero PII Exposure to Cloud AI & Courtroom Evidence Preservation",
            "bullets": [
                "<b>Deterministic Scrubbing</b>: IPv4, IPv6, Emails, MACs, JWTs, API Keys replaced instantly.",
                "<b>Ephemeral Local RAM Key</b>: Reidentification mapping stays strictly inside local RAM.",
                "<b>Dual-View Interface</b>: [Cloud AI View] displays PII-free tokens; [Officer View] allows authorized 1-click unmasking."
            ],
            "script": "Here is our core privacy engine in action: As raw telemetry enters, SENTINEL replaces real IPs and user names with synthetic tokens. Cloud AI models only ever see abstract tokens like [USER_1] logged in from [INTERNAL_IP_1]. The unmasking key stays strictly inside local RAM, accessible only by authorized officers with valid role tokens."
        },
        {
            "slide_num": "SLIDE 5",
            "title": "🤖 3-Tier System-Level MoE AI Routing Engine",
            "subtitle": "90% Cost Reduction + Multi-Model Failover Cascade",
            "bullets": [
                "<b>Tier 1 (Local GPU Ollama)</b>: deepseek-r1:8b / llama3.2:1b running 100% offline ($0 cost).",
                "<b>Tier 2 (Cloud MoE)</b>: Groq Cloud API (DeepSeek 70B @ 300 t/s) & Google Gemini Flash (2M Context).",
                "<b>Tier 3 (Ultra-Large Models)</b>: OpenRouter FREE Tier (Nemotron-3 550B & DeepSeek 671B).",
                "<b>Automatic Failover</b>: If internet drops or rate limits hit, SENTINEL cascades seamlessly."
            ],
            "script": "Our 3-Tier AI Router cuts software costs by over 85%. 90% of routine alerts are triaged locally on your workstation GPU for zero cost. For complex zero-day threats, SENTINEL cascades to Groq 70B, Google Gemini 2M Context, or OpenRouter 550B models—ensuring zero downtime during operations."
        },
        {
            "slide_num": "SLIDE 6",
            "title": "🕸️ Incident Correlation & Attack Graph Reconstruction",
            "subtitle": "Multi-Factor Correlation Scoring & Machine-Readable Graphs",
            "bullets": [
                "<b>Multi-Factor Scoring</b>: Evaluates entity similarity, temporal proximity, and MITRE tactics (0.0 to 1.0 score).",
                "<b>Attack Graph Builder</b>: Constructs machine-readable JSON attack graphs (Nodes & Edges).",
                "<b>Entity Mapping</b>: Tracks relationships across USER -> HOST -> PROCESS -> DOMAIN."
            ],
            "script": "Instead of presenting isolated alerts, SENTINEL's Correlation Engine groups thousands of events into single incident clusters. It calculates multi-factor correlation scores and constructs visual attack graphs showing exact lateral movement paths across users, hosts, and processes."
        },
        {
            "slide_num": "SLIDE 7",
            "title": "🔒 AST Safe AI Code Execution Sandbox Guard",
            "subtitle": "Syntax Tree Inspection Blocking Command Injection",
            "bullets": [
                "<b>AST Visitor (ast.parse)</b>: Parses Python de-obfuscation code at syntax tree level.",
                "<b>Forbidden Modules Blocked</b>: Automatically rejects os, sys, subprocess, socket, exec, eval.",
                "<b>Safe Execution Namespace</b>: Evaluates safe logic in restricted namespace (base64, json, math, re)."
            ],
            "script": "When AI models generate Python scripts to de-obfuscate malware payloads, executing them blindly is dangerous. SENTINEL inspects the Python AST syntax tree before execution. If the script contains malicious calls like os.system(), SENTINEL blocks it instantly while executing safe base64 decoding logic."
        },
        {
            "slide_num": "SLIDE 8",
            "title": "🛡️ Active Defense Containment & Server-Side HITL Gate",
            "subtitle": "Controlled Adapters + Strict Role-Based Access Control",
            "bullets": [
                "<b>Controlled Adapters</b>: Firewall IP Blocking, Process Termination, Host Network Isolation.",
                "<b>Server-Side HITL Gate</b>: Active defense requires explicit Officer approval token (OFFICER / ADMIN).",
                "<b>Safe Simulation Engine</b>: Operates in SENTINEL_RESPONSE_MODE=mock for production safety."
            ],
            "script": "SENTINEL never allows AI to execute arbitrary OS commands. All containment recommendations must pass through a server-side Human-in-the-Loop approval gateway. Only authorized officers can approve actions, which are executed via controlled, audited adapters."
        },
        {
            "slide_num": "SLIDE 9",
            "title": "📜 Courtroom PDF Incident Reports & Immutable Audit Trail",
            "subtitle": "Courtroom-Ready Evidence Briefs Generated in < 30 Seconds",
            "bullets": [
                "<b>1-Page Executive PDF Briefs</b>: Formatted using ReportLab for law enforcement and judicial review.",
                "<b>Immutable Audit Trail</b>: Writes append-only JSON logs (sentinel_audit_trail.jsonl) with zero PII exposure.",
                "<b>Complete Evidence Record</b>: Documents sanitized alert, reidentified view, MITRE tactics, and HITL authorization."
            ],
            "script": "In law enforcement, evidence integrity is paramount. SENTINEL logs every triage event to an append-only audit trail and generates a 1-page courtroom-ready executive PDF report in under 30 seconds, complete with dual-view evidence and officer sign-offs."
        },
        {
            "slide_num": "SLIDE 10",
            "title": "🏆 Competitive Edge: Why SENTINEL Wins",
            "subtitle": "Defensible Unique Engineering Differentiation",
            "bullets": [
                "<b>Zero-Trust PII Isolation</b>: Competitors leak raw PII; SENTINEL is 100% privacy-compliant.",
                "<b>3-Tier MoE Router</b>: Competitors rely on expensive cloud APIs; SENTINEL saves 85%+ software cost.",
                "<b>AST Sandbox Guard</b>: Competitors execute unsafe code; SENTINEL enforces syntax-level safety.",
                "<b>10/10 Level Verification</b>: All 10 architectural levels verified operational and live on GitHub."
            ],
            "script": "To conclude, judges: While open-source competitors leak police PII and cost thousands in cloud fees, SENTINEL delivers Zero-Trust Privacy, 3-Tier AI Cost Optimization, AST Code Security, and Courtroom PDF Briefs. Thank you, and I am ready for your questions!"
        }
    ]

    for slide in slides_data:
        story.append(Paragraph(f"<b>{slide['slide_num']}</b>", ParagraphStyle('SlideNum', parent=body_style, fontSize=9, textColor=colors.HexColor('#64748b'))))
        story.append(Paragraph(slide["title"], slide_title_style))
        story.append(Paragraph(f"<b>{slide['subtitle']}</b>", section_heading))
        story.append(Spacer(1, 8))

        # Bullet items table
        bullet_rows = []
        for bullet in slide["bullets"]:
            bullet_rows.append([Paragraph("•", body_style), Paragraph(bullet, body_style)])
        
        t_bullets = Table(bullet_rows, colWidths=[15, 680])
        t_bullets.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('PADDING', (0,0), (-1,-1), 3),
        ]))
        story.append(t_bullets)
        story.append(Spacer(1, 12))

        # Speaker Script Box
        story.append(Paragraph("<b>🗣️ SOLO PRESENTER SCRIPT (What to say aloud):</b>", section_heading))
        script_box_data = [[Paragraph(f'"{slide["script"]}"', script_style)]]
        t_script = Table(script_box_data, colWidths=[700])
        t_script.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_script)
        story.append(PageBreak())

    doc.build(story)
    print(f"📄 Master Presentation PDF generated successfully at: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_pitch_deck_pdf()
