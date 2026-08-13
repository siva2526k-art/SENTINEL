"""
SENTINEL — Native PowerPoint (.pptx) Pitch Deck Generator
Generates a native 10-slide PowerPoint presentation (.pptx) directly on Desktop.
"""
import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def create_humanized_pptx(output_path=r"C:\Users\siva2\Desktop\SENTINEL_HacKP_2026_Pitch_Deck.pptx"):
    prs = Presentation()
    # Set 16:9 widescreen layout (13.33 x 7.5 inches)
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    slides_content = [
        {
            "slide_title": "SENTINEL — Autonomous AI SOC Triage & Privacy Platform",
            "subtitle": "Security Event Network Triage Investigation with Neural Engine and LLM",
            "bullets": [
                "Solo Presenter: Sivabalan T (Lead Architect)",
                "Event: Hac'KP 2026 (Kerala Police Cyberdome Hackathon at Zoho Corporation)",
                "Key Innovation: Zero-Trust Data Sanitizer + 3-Tier MoE AI Router + AST Code Sandbox Guard"
            ],
            "notes": "Good morning respected judges and officers of Kerala Police Cyberdome. I am Sivabalan T, Lead Architect of SENTINEL. Today I present SENTINEL—an autonomous, privacy-preserving AI SOC platform built from first principles."
        },
        {
            "slide_title": "The Crisis in Cyber Investigations",
            "subtitle": "Alert Fatigue, Data Leakage to Cloud LLMs & High API Costs",
            "bullets": [
                "Alert Fatigue: SOC analysts face 5,000+ raw logs daily, leading to missed zero-day threats.",
                "Privacy & Legal Risk: Basic AI wrappers leak raw police emails, passwords, and internal IPs to public cloud LLMs.",
                "High Token Costs: Paying commercial cloud APIs per token for millions of raw logs is financially unsustainable."
            ],
            "notes": "Cyber crime units handle thousands of complex logs daily. Sending raw telemetry to commercial AI like OpenAI leaks sensitive police emails and internal IP addresses, violating privacy laws. Furthermore, cloud token costs quickly run into thousands of dollars."
        },
        {
            "slide_title": "Introducing SENTINEL Architecture",
            "subtitle": "Privacy-Preserving, Local-First Hybrid AI Infrastructure",
            "bullets": [
                "Zero-Trust Data Sanitizer: Scrubs PII & tokenizes IPs/emails into synthetic tokens ([USER_1], [INTERNAL_IP_1]) in local RAM.",
                "Adversarial Prompt Injection Firewall: Neutralizes embedded log attack phrases before AI sees payload.",
                "3-Tier MoE AI Router: Triages 90% routine alerts offline on workstation GPUs for $0 software cost.",
                "AST Code Execution Sandbox Guard: Inspects AI code syntax tree to block dangerous shell calls (os.system)."
            ],
            "notes": "SENTINEL solves this through a 4-pillar architecture: Zero-Trust PII Sanitization, Prompt Injection Firewall, 3-Tier AI Routing, and AST Safe Code Sandbox Guard."
        },
        {
            "slide_title": "Zero-Trust Data Sanitizer & Reversible Tokenization",
            "subtitle": "Zero PII Exposure to Cloud AI + Courtroom Evidence Integrity",
            "bullets": [
                "Deterministic PII Scrubbing: IPv4, IPv6, Emails, MACs, JWTs, API Keys replaced automatically.",
                "Ephemeral Local RAM Identity Mapping: Unmasking keys live strictly inside local workstation RAM.",
                "Dual-View Interface: [Cloud AI View] sees PII-free tokens; [Officer View] allows authorized 1-click unmasking."
            ],
            "notes": "Cloud AI providers only ever see PII-free synthetic tokens like [USER_1] logged in from [INTERNAL_IP_1]. Real identity unmasking stays in encrypted local RAM, accessible only by authorized officers with role tokens."
        },
        {
            "slide_title": "3-Tier System-Level MoE AI Router",
            "subtitle": "85%+ Software Cost Reduction + Multi-Model Failover",
            "bullets": [
                "Tier 1 (Local GPU Ollama): deepseek-r1:8b / llama3.2:1b running 100% offline ($0 cost).",
                "Tier 2 (Cloud MoE Engine): Groq Cloud (DeepSeek 70B @ 300 t/s) & Google Gemini Flash (2M Context).",
                "Tier 3 (Ultra-Large Models): OpenRouter FREE Tier (Nemotron-3 550B & DeepSeek 671B).",
                "Smart Cascade Router: Automatically failover if internet drops or rate limits hit."
            ],
            "notes": "Our 3-Tier AI Router cuts software costs by 85%. 90% of routine alerts are triaged locally on GPU for $0 cost. For zero-day threats, SENTINEL cascades to Groq 70B, Gemini 2M Context, or OpenRouter 550B models."
        },
        {
            "slide_title": "Incident Correlation & Attack Graph Reconstruction",
            "subtitle": "From Unstructured SIEM Telemetry to Actionable Intelligence",
            "bullets": [
                "Multi-Factor Scoring: Correlates entity similarity, temporal proximity, and MITRE tactics (0.0 to 1.0).",
                "Attack Graph Builder: Reconstructs machine-readable JSON attack graphs (Nodes & Edges).",
                "Entity Mapping: Tracks relationships across USER -> HOST -> PROCESS -> DOMAIN."
            ],
            "script": "Instead of showing isolated alerts, SENTINEL groups thousands of events into single incident clusters, building visual attack graphs showing exact lateral movement."
        },
        {
            "slide_title": "AST Safe AI Code Execution Sandbox Guard",
            "subtitle": "Syntax Tree Inspection Blocking Unsafe Shell Commands",
            "bullets": [
                "AST Visitor (ast.parse): Inspects AI-generated Python code at syntax tree level.",
                "Forbidden Modules Blocked: Automatically rejects os, sys, subprocess, socket, exec, eval.",
                "Restricted Namespace Execution: Runs safe de-obfuscation logic in isolated namespace (base64, json, re)."
            ],
            "notes": "Executing AI-generated code directly is dangerous. SENTINEL inspects the Python AST syntax tree first. If dangerous calls like os.system() are detected, SENTINEL blocks them instantly."
        },
        {
            "slide_title": "Active Defense Engine & Server-Side HITL Gateway",
            "subtitle": "Controlled Containment Adapters + Strict Server RBAC",
            "bullets": [
                "Controlled Adapters: Firewall IP Blocking, Process Termination, Host Network Isolation.",
                "Server-Side HITL Gate: Active defense requires explicit Officer approval token (OFFICER / ADMIN).",
                "Safe Simulation Mode: Operates in SENTINEL_RESPONSE_MODE=mock for production safety."
            ],
            "notes": "SENTINEL never lets AI execute arbitrary shell commands. All containment actions require explicit Human-in-the-Loop officer approval, executed through controlled, audited adapters."
        },
        {
            "slide_title": "Courtroom PDF Incident Reports & Immutable Audit Trail",
            "subtitle": "Courtroom-Ready Briefs Generated in < 30 Seconds",
            "bullets": [
                "1-Page Executive PDF Briefs: Formatted using ReportLab for law enforcement and judicial review.",
                "Immutable Audit Trail: Writes append-only JSON logs (sentinel_audit_trail.jsonl) with zero PII exposure.",
                "Complete Evidence Record: Captures sanitized alert, reidentified view, MITRE tactics, and HITL authorization."
            ],
            "notes": "SENTINEL logs every triage event to an append-only audit trail and generates courtroom-ready 1-page PDF reports in under 30 seconds."
        },
        {
            "slide_title": "Competitive Victory: Why SENTINEL Wins",
            "subtitle": "100% Operational & Verified Across All 10 Levels",
            "bullets": [
                "Zero-Trust PII Isolation: Competitors leak police PII; SENTINEL is 100% privacy-compliant.",
                "85%+ Software Cost Savings: Competitors rely on expensive cloud APIs; SENTINEL runs local GPU AI ($0).",
                "AST Sandbox Safety: Competitors risk command injection; SENTINEL enforces syntax safety.",
                "10/10 Verification Passed: All 10 architectural levels verified operational and live on GitHub."
            ],
            "notes": "To conclude, judges: SENTINEL delivers Zero-Trust Privacy, 3-Tier AI Cost Optimization, AST Code Security, and Courtroom PDF Briefs. All 10 architectural levels are verified live. Thank you!"
        }
    ]

    # Theme colors
    NAVY_BLUE = RGBColor(30, 58, 138)
    DARK_TEXT = RGBColor(15, 23, 42)
    ACCENT_BLUE = RGBColor(37, 99, 235)
    LIGHT_BG = RGBColor(248, 250, 252)

    for data in slides_content:
        slide = prs.slides.add_slide(blank_layout)

        # Header Box
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
        tf_h = header_box.text_frame
        tf_h.word_wrap = True

        p_title = tf_h.paragraphs[0]
        p_title.text = data["slide_title"]
        p_title.font.name = "Helvetica"
        p_title.font.bold = True
        p_title.font.size = Pt(24)
        p_title.font.color.rgb = NAVY_BLUE

        p_sub = tf_h.add_paragraph()
        p_sub.text = data["subtitle"]
        p_sub.font.name = "Helvetica"
        p_sub.font.bold = True
        p_sub.font.size = Pt(14)
        p_sub.font.color.rgb = ACCENT_BLUE

        # Bullets Box
        bullet_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.5))
        tf_b = bullet_box.text_frame
        tf_b.word_wrap = True

        for idx, bullet_text in enumerate(data["bullets"]):
            p = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
            p.text = "• " + bullet_text
            p.font.name = "Helvetica"
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(14)

        # Presenter Notes
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        tf_notes.text = data.get("notes", "")

    prs.save(output_path)
    print(f"🎉 Native PowerPoint Presentation created successfully at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_humanized_pptx()
