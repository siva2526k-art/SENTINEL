"""
SENTINEL — Professional Visual PowerPoint (.pptx) Deck Generator
Follows the Top-Down Presentation Structure & Enterprise Product Layout.
Includes dedicated Slide 4: Open-Source Feature Adaptation & Provenance.
Front page is 100% clean enterprise product software platform (No venue/hackathon text).
"""
import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def create_topdown_enterprise_pptx(output_path=r"C:\Users\siva2\Desktop\SENTINEL_Enterprise_Pitch_Deck.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Enterprise Dark Palette
    BG_NAVY = RGBColor(9, 13, 22)
    TEXT_WHITE = RGBColor(248, 250, 252)
    TEXT_MUTED = RGBColor(148, 163, 184)
    ACCENT_CYAN = RGBColor(6, 182, 212)
    ACCENT_BLUE = RGBColor(96, 165, 250)
    ACCENT_YELLOW = RGBColor(234, 179, 8)

    slides_content = [
        # SLIDE 1: PURE ENTERPRISE PRODUCT TITLE (No Venue / Hackathon text)
        {
            "is_title_slide": True,
            "slide_title": "SENTINEL",
            "subtitle": "Autonomous AI SOC Triage & Zero-Trust Privacy Platform",
            "version_tag": "Enterprise Product Brief • Version 1.0",
            "cards": [
                {"icon": "🛡️", "title": "Product Platform", "text": "Autonomous Security Operations Center Triage Engine"},
                {"icon": "👤", "title": "System Architect", "text": "Sivabalan T\nLead Security Engineer & System Architect"},
                {"icon": "🚀", "title": "Core Architecture", "text": "Zero-Trust Privacy Shield + 3-Tier MoE Router + AST Sandbox Guard"}
            ],
            "notes": "Good morning. I am Sivabalan T, Lead Architect of SENTINEL. Today I introduce SENTINEL—an enterprise-grade autonomous AI SOC triage and privacy platform engineered for next-generation cyber defense."
        },
        # SLIDE 2
        {
            "takeaway": "TOP TAKEAWAY: Manual log parsing drowns analysts while basic AI wrappers leak sensitive police data to public clouds.",
            "slide_title": "🚨 The Crisis in Digital Incident Triage",
            "subtitle": "Alert Fatigue, Data Leakage & Uncontrolled Cloud Token Costs",
            "cards": [
                {"icon": "⚡", "title": "5,000+ Daily Alerts", "text": "Analysts handle 5,000+ raw SIEM logs daily, spending 40 mins per alert."},
                {"icon": "🔓", "title": "Public Cloud PII Leakage", "text": "Commercial AI wrappers leak real police emails & internal IPs to public LLMs."},
                {"icon": "💸", "title": "High Monthly API Costs", "text": "Sending raw multi-megabyte log files to commercial APIs costs thousands monthly."}
            ],
            "notes": "Cyber investigators drown in raw JSON logs daily. When teams use basic commercial AI, they leak confidential police PII to public cloud servers while burning thousands of dollars in API fees."
        },
        # SLIDE 3
        {
            "takeaway": "TOP TAKEAWAY: SENTINEL unifies Zero-Trust Privacy, 3-Tier AI Cost Control, and AST Code Execution Guarding.",
            "slide_title": "💡 SENTINEL Architecture Matrix",
            "subtitle": "First-Principles AI System Architecture for Cyber Operations",
            "cards": [
                {"icon": "🔒", "title": "1. Zero-Trust Sanitizer", "text": "Replaces PII with synthetic tokens ([USER_1], [INTERNAL_IP_1]) in encrypted local RAM before transit."},
                {"icon": "🛡️", "title": "2. Injection Neutralizer", "text": "Neutralizes log-embedded attack phrases ([NEUTRALIZED_PROMPT_INJECTION]) before AI processing."},
                {"icon": "🤖", "title": "3. 3-Tier System MoE", "text": "Triages 90% routine alerts offline on workstation GPUs for $0 software cost."},
                {"icon": "🔒", "title": "4. AST Code Sandbox", "text": "Parses Python AST syntax trees to block dangerous shell execution (os.system)."}
            ],
            "notes": "SENTINEL solves this through 4 technical pillars: Zero-Trust Data Sanitization, Prompt Injection Neutralization, 3-Tier AI Cost Optimization, and AST Code Execution Guarding."
        },
        # SLIDE 4: OPEN-SOURCE FEATURE ADAPTATION & PROVENANCE (NEW!)
        {
            "takeaway": "TOP TAKEAWAY: SENTINEL adapts industry open-source standards, fixing critical privacy, security, and cost flaws.",
            "slide_title": "🏛️ Architectural Provenance & Open-Source Adaptation",
            "subtitle": "How SENTINEL Improves Upon Established Open-Source Projects",
            "cards": [
                {"icon": "🔒", "title": "Sanitizer (from Presidio)", "text": "<b>Presidio Flaw</b>: Destroys PII or sends raw text.\n<b>SENTINEL Innovation</b>: Reversible token mapping ([USER_1]) stored in local RAM."},
                {"icon": "🤖", "title": "AI Router (from RouteLLM)", "text": "<b>RouteLLM Flaw</b>: Leaks prompt metadata to cloud.\n<b>SENTINEL Innovation</b>: Sanitizes prompts first; processes 90% offline on local GPU ($0)."},
                {"icon": "🔒", "title": "AST Guard (from PyInquirer)", "text": "<b>PyInquirer Flaw</b>: Unsafe eval() wrappers.\n<b>SENTINEL Innovation</b>: AST syntax tree parsing (ast.parse) blocking os.system()."},
                {"icon": "🧠", "title": "RAG Memory (from ChromaDB)", "text": "<b>LangChain Flaw</b>: Stores raw PII in vectors.\n<b>SENTINEL Innovation</b>: Embeds only PII-scrubbed threat vectors in ChromaDB."}
            ],
            "notes": "To ensure maximum robustness, we adapted established open-source projects—Microsoft Presidio for sanitization, RouteLLM for routing, and ChromaDB for vector memory—while fixing their security and privacy limitations."
        },
        # SLIDE 5
        {
            "takeaway": "TOP TAKEAWAY: Cloud AI models only see synthetic tokens; unmasking keys stay inside local RAM.",
            "slide_title": "🔒 Zero-Trust Sanitizer & Dual-View Interface",
            "subtitle": "Complete PII Isolation + Authorized Police Unmasking",
            "code_box": "❌ RAW LOG (Local Workstation Only):\n\"Failed SSH login for officer.sharma@keralapolice.gov.in from 192.168.1.45 on port 22.\"\n\n✅ [Cloud / AI View] (Sent to Groq / Gemini / OpenRouter):\n\"Failed SSH login for [USER_1] from [INTERNAL_IP_1] on port 22.\"\n\n🔑 [Officer Re-Identified View] (Authorized Police Officer Only):\n\"Failed SSH login for officer.sharma@keralapolice.gov.in from 192.168.1.45 on port 22.\"",
            "notes": "Cloud AI engines only ever see PII-free tokens like [USER_1] from [INTERNAL_IP_1]. The unmasking key lives strictly inside local RAM, accessible only by authorized officers with role tokens."
        },
        # SLIDE 6
        {
            "takeaway": "TOP TAKEAWAY: Local GPU AI handles 90% routine alerts for $0 cost, cascading to 550B models for zero-day threats.",
            "slide_title": "🤖 3-Tier System-Level MoE AI Routing Engine",
            "subtitle": "85%+ Software Cost Optimization + Automatic Failover",
            "cards": [
                {"icon": "🖥️", "title": "Tier 1: Local GPU Ollama", "text": "deepseek-r1:8b / llama3.2:1b\n100% Offline GPU AI execution ($0.00 cost, 90% routine triage)."},
                {"icon": "⚡", "title": "Tier 2: Groq & Gemini Flash", "text": "DeepSeek 70B @ 300 t/s & Gemini Flash 2M Context Window\nUltra-fast reasoning & massive log file ingestion."},
                {"icon": "🌌", "title": "Tier 3: OpenRouter Free 550B", "text": "nvidia/nemotron-3-ultra-550b-a55b:free\n550 Billion Parameter intelligence for zero-day threat analysis."}
            ],
            "notes": "Our 3-Tier Router processes 90% of routine alerts locally on GPU for $0 cost. For zero-day threats, SENTINEL cascades to Groq 70B, Gemini 2M Context, or OpenRouter 550B models."
        },
        # SLIDE 7
        {
            "takeaway": "TOP TAKEAWAY: Multi-factor scoring groups isolated alerts into single visual attack graphs.",
            "slide_title": "🕸️ Incident Correlation & Attack Graph Builder",
            "subtitle": "Multi-Factor Scoring & Machine-Readable JSON Graphs",
            "cards": [
                {"icon": "📊", "title": "Multi-Factor Scoring", "text": "Evaluates entity similarity, temporal proximity, and MITRE tactics into a 0.0 - 1.0 correlation score."},
                {"icon": "🕸️", "title": "JSON Attack Graph", "text": "Builds machine-readable attack graph nodes and edges mapping lateral movement across networks."},
                {"icon": "🧠", "title": "ChromaDB RAG Memory", "text": "Persists sanitized threat vectors in data/chroma/, retrieving top 3 historical threat patterns."}
            ],
            "notes": "Instead of presenting isolated alerts, SENTINEL correlates thousands of events into single incident clusters, building visual attack graphs showing lateral movement."
        },
        # SLIDE 8
        {
            "takeaway": "TOP TAKEAWAY: AST syntax tree parsing prevents malicious AI-generated code execution.",
            "slide_title": "🔒 AST Safe AI Code Execution Sandbox Guard",
            "subtitle": "Syntax Tree Inspection Blocking Unsafe Shell Commands",
            "code_box": "AI Code Input ──► ast.parse() ──► ASTSecurityVisitor Inspection\n\n✅ SAFE CODE: base64.b64decode(\"aGVsbG8=\") ──► EXECUTED IN RESTRICTED NAMESPACE\n❌ MALICIOUS: os.system(\"rm -rf /\")         ──► BLOCKED INSTANTLY (AST Security Violation)",
            "notes": "When AI generates Python scripts to de-obfuscate malware payloads, SENTINEL inspects the Python AST syntax tree first. If dangerous calls like os.system() are detected, SENTINEL blocks them instantly."
        },
        # SLIDE 9
        {
            "takeaway": "TOP TAKEAWAY: Containment actions require explicit Human-in-the-Loop officer approval.",
            "slide_title": "🛡️ Active Defense Containment & HITL Gateway",
            "subtitle": "Controlled Containment Adapters + Strict Server RBAC",
            "cards": [
                {"icon": "🔥", "title": "Firewall Controller", "text": "IP blocking rules in safe simulation mode (SENTINEL_RESPONSE_MODE=mock)."},
                {"icon": "⚡", "title": "Process Controller", "text": "Process termination adapters for malicious executable command strings."},
                {"icon": "🔒", "title": "Host Isolator", "text": "Network isolation adapters for compromised internal host systems."}
            ],
            "notes": "SENTINEL never allows AI to execute arbitrary OS commands. All containment recommendations must pass through a server-side Human-in-the-Loop approval gateway."
        },
        # SLIDE 10
        {
            "takeaway": "TOP TAKEAWAY: Courtroom-ready 1-page PDF briefs are generated in under 30 seconds.",
            "slide_title": "📜 Courtroom PDF Briefs & Immutable Audit Trail",
            "subtitle": "Courtroom-Ready Reports Generated in < 30 Seconds",
            "cards": [
                {"icon": "📄", "title": "Courtroom PDF Briefs", "text": "Generates 1-page executive PDF incident briefs using ReportLab for law enforcement and judicial review."},
                {"icon": "📜", "title": "Immutable Audit Trail", "text": "Writes append-only JSON logs (data/audit/sentinel_audit_trail.jsonl) with zero identity_map exposure."}
            ],
            "notes": "SENTINEL logs every triage event to an append-only audit trail and generates a 1-page courtroom-ready executive PDF report in under 30 seconds."
        },
        # SLIDE 11
        {
            "takeaway": "TOP TAKEAWAY: SENTINEL is 100% verified operational across all 10 architectural levels.",
            "slide_title": "🏆 Enterprise Impact & System Verification",
            "subtitle": "All 10 Architectural Levels Verified Operational",
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

        # Set Background Color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_NAVY

        # Slide Header Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.4))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True

        p_t = tf_t.paragraphs[0]
        p_t.text = data["slide_title"]
        p_t.font.name = "Helvetica"
        p_t.font.bold = True
        p_t.font.size = Pt(24)
        p_t.font.color.rgb = TEXT_WHITE

        p_sub = tf_t.add_paragraph()
        p_sub.text = data.get("subtitle", "")
        p_sub.font.name = "Helvetica"
        p_sub.font.bold = True
        p_sub.font.size = Pt(13)
        p_sub.font.color.rgb = ACCENT_CYAN
        p_sub.space_before = Pt(3)

        if "takeaway" in data:
            p_take = tf_t.add_paragraph()
            p_take.text = f"📌 {data['takeaway']}"
            p_take.font.name = "Helvetica"
            p_take.font.bold = True
            p_take.font.size = Pt(11)
            p_take.font.color.rgb = ACCENT_YELLOW
            p_take.space_before = Pt(4)

        # Render Visual Cards or Code Box
        if "code_box" in data:
            code_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.7), Inches(4.5))
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
            card_width = Inches(2.7) if num_cards == 4 else (Inches(3.6) if num_cards == 3 else Inches(5.5))
            gap = Inches(0.3)
            start_left = Inches(0.8)

            for i, c_data in enumerate(cards):
                left = start_left + i * (card_width + gap) if num_cards <= 4 else start_left + (i % 2) * (Inches(5.6) + gap)
                top = Inches(2.3) if i < 4 else Inches(4.6)

                card_box = slide.shapes.add_textbox(left, top, card_width, Inches(2.1))
                tf_card = card_box.text_frame
                tf_card.word_wrap = True

                p_c_title = tf_card.paragraphs[0]
                p_c_title.text = f"{c_data['icon']} {c_data['title']}"
                p_c_title.font.name = "Helvetica"
                p_c_title.font.bold = True
                p_c_title.font.size = Pt(14)
                p_c_title.font.color.rgb = ACCENT_YELLOW
                p_c_title.space_after = Pt(4)

                p_c_text = tf_card.add_paragraph()
                p_c_text.text = c_data["text"]
                p_c_text.font.name = "Helvetica"
                p_c_text.font.size = Pt(10.5)
                p_c_text.font.color.rgb = TEXT_MUTED

        # Speaker Notes Section
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        tf_notes.text = data.get("notes", "")

    prs.save(output_path)
    print(f"🎉 Enterprise Top-Down PowerPoint Deck (with Provenance) created successfully at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_topdown_enterprise_pptx()
