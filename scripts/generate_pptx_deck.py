"""
SENTINEL — Visual PowerPoint (.pptx) Pitch Deck Generator
Generates a dark-mode, visual, card-based PowerPoint presentation (.pptx) directly on Desktop.
"""
import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def create_visual_pptx(output_path=r"C:\Users\siva2\Desktop\SENTINEL_Visual_Pitch_Deck_2026.pptx"):
    prs = Presentation()
    # Widescreen 16:9 (13.33 x 7.5 inches)
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    BG_NAVY = RGBColor(9, 13, 22)         # #090d16
    CARD_BG = RGBColor(15, 23, 42)        # #0f172a
    CARD_BORDER = RGBColor(59, 130, 246)  # #3b82f6
    TEXT_WHITE = RGBColor(248, 250, 252)  # #f8fafc
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94a3b8
    ACCENT_CYAN = RGBColor(6, 182, 212)   # #06b6d4
    ACCENT_BLUE = RGBColor(96, 165, 250)  # #60a5fa
    ACCENT_YELLOW = RGBColor(234, 179, 8) # #eab308

    slides_content = [
        {
            "slide_title": "SENTINEL — Autonomous AI SOC Triage & Privacy Platform",
            "subtitle": "Security Event Network Triage Investigation with Neural Engine and LLM",
            "cards": [
                {"icon": "👤", "title": "Solo Presenter & Lead", "text": "Sivabalan T\nLead Security Engineer & System Architect"},
                {"icon": "🏛️", "title": "Event & Venue", "text": "Hac'KP 2026 (7th National Cyberdome Hackathon)\nVenue: Zoho Corporation Campus"},
                {"icon": "🚀", "title": "Core Breakthrough", "text": "Zero-Trust Privacy Shield + 3-Tier MoE Router + AST Sandbox Guard + Courtroom PDF Briefs"}
            ],
            "notes": "Good morning respected judges. I am Sivabalan T, Lead Architect of SENTINEL. Today I present SENTINEL—a privacy-preserving, 3-tier AI SOC triage platform built from first principles."
        },
        {
            "slide_title": "🚨 The Crisis in Digital Investigations",
            "subtitle": "Why Legacy SOC Workflows & Commercial AI Wrappers Fail",
            "cards": [
                {"icon": "⚡", "title": "Alert Fatigue", "text": "SOC analysts handle 5,000+ raw logs daily. Manual log parsing takes 30-45 minutes per alert, causing zero-day threats to slip through."},
                {"icon": "🔓", "title": "Privacy & Legal Leakage", "text": "Basic AI wrappers leak raw police emails, passwords, and internal IPs to public cloud LLMs, violating DPDP Act 2023 and GDPR."},
                {"icon": "💸", "title": "Uncontrolled Token Costs", "text": "Sending raw multi-megabyte SIEM log streams to commercial cloud APIs per token costs thousands of dollars monthly."}
            ],
            "notes": "Cyber investigators drown in raw JSON logs daily. When teams use basic commercial AI, they leak confidential police PII to public cloud servers, violating privacy laws while burning thousands of dollars in token fees."
        },
        {
            "slide_title": "💡 The SENTINEL Architecture Solution",
            "subtitle": "4 Technical Pillars of First-Principles AI Engineering",
            "cards": [
                {"icon": "🔒", "title": "1. Zero-Trust Sanitizer", "text": "Replaces PII with synthetic tokens ([USER_1], [INTERNAL_IP_1]) in encrypted local RAM before network transit."},
                {"icon": "🛡️", "title": "2. Prompt Injection Firewall", "text": "Neutralizes log-embedded attack phrases ([NEUTRALIZED_PROMPT_INJECTION]) before AI model processing."},
                {"icon": "🤖", "title": "3. 3-Tier System-Level MoE", "text": "Triages 90% routine alerts offline on workstation GPUs for $0 software cost, cascading to cloud models only when needed."},
                {"icon": "🔒", "title": "4. AST Code Sandbox Guard", "text": "Inspects AI code syntax trees (ast.parse) to block dangerous shell calls (os.system) before execution."}
            ],
            "notes": "SENTINEL solves this through 4 technical pillars: Zero-Trust Data Sanitization, Prompt Injection Neutralization, 3-Tier AI Cost Optimization, and AST Code Execution Guarding."
        },
        {
            "slide_title": "🔒 Zero-Trust Sanitizer & Dual-View Interface",
            "subtitle": "Zero PII Cloud Exposure + Courtroom Evidence Integrity",
            "code_box": "❌ RAW LOG (Local Workstation Only):\n\"Failed SSH login for officer.sharma@keralapolice.gov.in from 192.168.1.45 on port 22.\"\n\n✅ [Cloud / AI View] (Sent to Groq / Gemini / OpenRouter):\n\"Failed SSH login for [USER_1] from [INTERNAL_IP_1] on port 22.\"\n\n🔑 [Officer Re-Identified View] (Authorized Police Officer Only):\n\"Failed SSH login for officer.sharma@keralapolice.gov.in from 192.168.1.45 on port 22.\"",
            "notes": "Cloud AI engines only ever see sanitized tokens like [USER_1] from [INTERNAL_IP_1]. The unmasking key lives strictly inside local RAM, accessible only by authorized officers with role tokens."
        },
        {
            "slide_title": "🤖 3-Tier System-Level MoE AI Routing Engine",
            "subtitle": "85%+ Software Cost Savings + Smart Cascade Failover",
            "cards": [
                {"icon": "🖥️", "title": "Tier 1: Local GPU Ollama", "text": "deepseek-r1:8b / llama3.2:1b\n100% Offline GPU AI execution ($0.00 cost, 90% routine triage)."},
                {"icon": "⚡", "title": "Tier 2: Groq & Gemini Flash", "text": "DeepSeek 70B @ 300 t/s & Gemini Flash 2M Context Window\nUltra-fast reasoning & massive log file ingestion."},
                {"icon": "🌌", "title": "Tier 3: OpenRouter Free 550B", "text": "nvidia/nemotron-3-ultra-550b-a55b:free\n550 Billion Parameter intelligence for zero-day threat analysis."}
            ],
            "notes": "Our 3-Tier Router processes 90% of routine alerts locally on GPU for $0 cost. For zero-day threats, SENTINEL cascades to Groq 70B, Gemini 2M Context, or OpenRouter 550B models."
        },
        {
            "slide_title": "🕸️ Incident Correlation & Attack Graph Builder",
            "subtitle": "Multi-Factor Scoring & Machine-Readable JSON Graphs",
            "cards": [
                {"icon": "📊", "title": "Multi-Factor Scoring", "text": "Evaluates entity similarity, temporal proximity, and MITRE tactics into a 0.0 - 1.0 correlation score."},
                {"icon": "🕸️", "title": "JSON Attack Graph", "text": "Builds machine-readable attack graph nodes and edges mapping lateral movement across networks."},
                {"icon": "🧠", "title": "ChromaDB RAG Memory", "text": "Persists sanitized threat vectors in data/chroma/, retrieving top 3 historical threat patterns."}
            ],
            "notes": "Instead of presenting isolated alerts, SENTINEL correlates thousands of events into single incident clusters, building visual attack graphs showing lateral movement."
        },
        {
            "slide_title": "🔒 AST Safe AI Code Execution Sandbox Guard",
            "subtitle": "Syntax Tree Inspection Blocking Command Injection",
            "code_box": "AI Code Input ──► ast.parse() ──► ASTSecurityVisitor Inspection\n\n✅ SAFE CODE: base64.b64decode(\"aGVsbG8=\") ──► EXECUTED IN RESTRICTED NAMESPACE\n❌ MALICIOUS: os.system(\"rm -rf /\")         ──► BLOCKED INSTANTLY (AST Security Violation)",
            "notes": "When AI generates Python scripts to de-obfuscate malware payloads, SENTINEL inspects the Python AST syntax tree first. If dangerous calls like os.system() are detected, SENTINEL blocks them instantly."
        },
        {
            "slide_title": "🛡️ Active Defense Containment & HITL Gateway",
            "subtitle": "Controlled Adapters + Strict Server RBAC",
            "cards": [
                {"icon": "🔥", "title": "Firewall Controller", "text": "IP blocking rules in safe simulation mode (SENTINEL_RESPONSE_MODE=mock)."},
                {"icon": "⚡", "title": "Process Controller", "text": "Process termination adapters for malicious executable command strings."},
                {"icon": "🔒", "title": "Host Isolator", "text": "Network isolation adapters for compromised internal host systems."}
            ],
            "notes": "SENTINEL never allows AI to execute arbitrary OS commands. All containment recommendations must pass through a server-side Human-in-the-Loop approval gateway."
        },
        {
            "slide_title": "📜 Courtroom PDF Briefs & Immutable Audit Trail",
            "subtitle": "Courtroom-Ready Reports Generated in < 30 Seconds",
            "cards": [
                {"icon": "📄", "title": "Courtroom PDF Briefs", "text": "Generates 1-page executive PDF incident briefs using ReportLab for law enforcement and judicial review."},
                {"icon": "📜", "title": "Immutable Audit Trail", "text": "Writes append-only JSON logs (data/audit/sentinel_audit_trail.jsonl) with zero identity_map exposure."}
            ],
            "notes": "SENTINEL logs every triage event to an append-only audit trail and generates a 1-page courtroom-ready executive PDF report in under 30 seconds."
        },
        {
            "slide_title": "🏆 Competitive Victory: Why SENTINEL Wins",
            "subtitle": "10/10 Architectural Level Verification PASSED",
            "cards": [
                {"icon": "🟢", "title": "Zero-Trust PII Isolation", "text": "Competitors leak police PII; SENTINEL is 100% privacy-compliant."},
                {"icon": "🟢", "title": "85%+ Cost Optimization", "text": "Competitors burn cloud API fees; SENTINEL runs local GPU AI ($0)."},
                {"icon": "🟢", "title": "AST Code Safety", "text": "Competitors risk command injection; SENTINEL enforces syntax safety."},
                {"icon": "🟢", "title": "10/10 Passed", "text": "All 10 architectural levels verified operational and live on GitHub master branch."}
            ],
            "notes": "To conclude, judges: SENTINEL delivers Zero-Trust Privacy, 3-Tier AI Cost Optimization, AST Code Security, and Courtroom PDF Briefs. All 10 architectural levels are verified live. Thank you!"
        }
    ]

    for data in slides_content:
        slide = prs.slides.add_slide(blank_layout)

        # Set Slide Background Color to Dark Navy
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_NAVY

        # Slide Header Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True

        p_t = tf_t.paragraphs[0]
        p_t.text = data["slide_title"]
        p_t.font.name = "Helvetica"
        p_t.font.bold = True
        p_t.font.size = Pt(24)
        p_t.font.color.rgb = TEXT_WHITE

        p_sub = tf_t.add_paragraph()
        p_sub.text = data["subtitle"]
        p_sub.font.name = "Helvetica"
        p_sub.font.bold = True
        p_sub.font.size = Pt(13)
        p_sub.font.color.rgb = ACCENT_CYAN
        p_sub.space_before = Pt(4)

        # Render Visual Cards or Code Box
        if "code_box" in data:
            code_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
            tf_c = code_box.text_frame
            tf_c.word_wrap = True
            p_code = tf_c.paragraphs[0]
            p_code.text = data["code_box"]
            p_code.font.name = "Courier New"
            p_code.font.size = Pt(14)
            p_code.font.color.rgb = ACCENT_BLUE
        else:
            cards = data.get("cards", [])
            num_cards = len(cards)
            card_width = Inches(3.6) if num_cards >= 3 else Inches(5.5)
            gap = Inches(0.4)
            start_left = Inches(0.8)

            for i, c_data in enumerate(cards):
                left = start_left + i * (card_width + gap) if num_cards <= 3 else start_left + (i % 2) * (Inches(5.6) + gap)
                top = Inches(2.0) if i < 3 else Inches(4.5)

                card_box = slide.shapes.add_textbox(left, top, card_width, Inches(2.2))
                tf_card = card_box.text_frame
                tf_card.word_wrap = True

                p_c_title = tf_card.paragraphs[0]
                p_c_title.text = f"{c_data['icon']} {c_data['title']}"
                p_c_title.font.name = "Helvetica"
                p_c_title.font.bold = True
                p_c_title.font.size = Pt(15)
                p_c_title.font.color.rgb = ACCENT_YELLOW
                p_c_title.space_after = Pt(6)

                p_c_text = tf_card.add_paragraph()
                p_c_text.text = c_data["text"]
                p_c_text.font.name = "Helvetica"
                p_c_text.font.size = Pt(11)
                p_c_text.font.color.rgb = TEXT_MUTED

        # Presenter Notes Section
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        tf_notes.text = data.get("notes", "")

    prs.save(output_path)
    print(f"🎉 Dark-Mode Visual PowerPoint Deck created successfully at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_visual_pptx()
