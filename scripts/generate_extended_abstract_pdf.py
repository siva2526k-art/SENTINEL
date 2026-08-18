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
        self.drawString(36, 756, "SHIELD AI — TECHNICAL ABSTRACT & SYSTEM SPECIFICATION")
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
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#2563eb'),
        alignment=1,
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )

    story = []

    # Title Banner (No Author Name, No Hackathon Mentions)
    story.append(Paragraph("SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM", title_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Sri Sai Ram Engineering College, Chennai", subtitle_style))
    story.append(Paragraph("<b>Academic Year:</b> 2026–2027 &nbsp;|&nbsp; <b>Domain:</b> Cybersecurity, Artificial Intelligence & Autonomous Systems", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563eb"), spaceAfter=10))

    # Executive Abstract Heading
    story.append(Paragraph("EXECUTIVE ABSTRACT", h1_style))

    p1 = (
        "Security Operations Centers (SOCs) face critical operational bottlenecks caused by overwhelming alert volume, high false-positive rates, and severe analyst fatigue. "
        "Enterprise networks routinely ingest over 5,000 security logs daily, requiring 30 to 45 minutes of manual investigation per incident. Consequently, nearly 70% of security "
        "notifications remain unexamined, expanding attacker dwell time. Furthermore, transmitting raw telemetry containing internal IP topographies, employee emails, and credentials "
        "to commercial cloud AI services introduces catastrophic data privacy leakage and violates statutory regulations."
    )
    story.append(Paragraph(p1, body_style))

    p2 = (
        "<b>SHIELD AI</b> is a privacy-preserving, AI-assisted SOC triage and security intelligence framework engineered to solve these challenges. Operating on a Zero-Trust architecture, "
        "SHIELD AI ingests real-time SIEM logs via non-blocking FastAPI webhooks. An inline Data Sanitizer performs local regular-expression (Regex) tokenization—scrubbing IPv4/v6 addresses, "
        "emails, MAC addresses, and API keys into synthetic handles (<code>[USER_1]</code>, <code>[INTERNAL_IP_1]</code>) while holding lookup tables strictly within volatile RAM memory. "
        "An integrated Prompt-Injection Firewall neutralizes adversarial prompt overrides in raw logs before processing."
    )
    story.append(Paragraph(p2, body_style))

    p3 = (
        "Triage queries are dispatched through a Three-Tier AI Router: Tier 1 executes locally on workstation GPUs using open-weights models (Ollama <code>deepseek-r1:8b</code>) for 100% offline "
        "triage with zero data egress, while policy-controlled cloud fallbacks (Groq/Gemini) receive only anonymized tokens. Sanitized incidents are mapped to MITRE ATT&CK tactics and techniques, "
        "correlated into Directed Acyclic Attack Graphs (DAGs), and matched against historical cases via ChromaDB vector embeddings. To ensure safety, an AST Code Sandbox parses script syntax trees "
        "to block dangerous primitives, and a Human-in-the-Loop (HITL) gate requires explicit analyst approval before executing containment actions. Audit milestones are recorded in append-only JSONL "
        "trails, and ReportLab compiles executive PDF incident briefs."
    )
    story.append(Paragraph(p3, body_style))

    keywords = "<b>Keywords:</b> Privacy-Preserving AI, SOC Triage, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Sandbox, Human-in-the-Loop."
    story.append(Paragraph(keywords, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    shutil.copy2(pdf_path, desktop_path)
    print(f"✅ Generated & Saved Solvethon Abstract PDF to Desktop: {desktop_path}")

if __name__ == "__main__":
    build_pdf()
