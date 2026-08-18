import os
import sys
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, HRFlowable
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
        self.setFillColor(colors.black)
        
        # Black Header Line & Text
        self.drawString(36, 756, "SHIELD AI — TECHNICAL ABSTRACT & SYSTEM SPECIFICATION")
        self.setStrokeColor(colors.black)
        self.setLineWidth(0.75)
        self.line(36, 748, 576, 748)
        
        # Black Footer Line & Text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.black)
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
        fontSize=14,
        leading=18,
        textColor=colors.black,
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.black,
        alignment=1,
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.black,
        alignment=1,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.black,
        spaceBefore=8,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.black,
        spaceAfter=8
    )

    story = []

    # Title Banner (Strict B&W Monochrome - Humanized Style)
    story.append(Paragraph("SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM", title_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Sri Sai Ram Engineering College, Chennai", subtitle_style))
    story.append(Paragraph("<b>Academic Year:</b> 2026–2027 &nbsp;|&nbsp; <b>Domain:</b> Cybersecurity, Artificial Intelligence & Autonomous Systems", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.black, spaceAfter=8))

    # Executive Abstract Heading
    story.append(Paragraph("EXECUTIVE ABSTRACT", h1_style))

    p1 = (
        "Security Operations Centers (SOCs) struggle daily with excessive alert volume and analyst burnout. Enterprise networks routinely generate over 5,000 security logs every 24 hours, "
        "taking 30 to 45 minutes of manual triage per incident. Because of this delay, nearly 70% of alerts end up unexamined. At the same time, sending raw log data—full of internal IP maps, "
        "staff emails, and auth tokens—to public cloud AI models risks major privacy leaks and violates data protection laws."
    )
    story.append(Paragraph(p1, body_style))

    p2 = (
        "<b>SHIELD AI</b> addresses these operational and privacy hurdles through a zero-trust, hybrid architecture. Built around non-blocking FastAPI webhooks, the system processes raw SIEM logs locally. "
        "An inline Data Sanitizer uses regular expressions to strip out IP addresses, email handles, MAC addresses, and API keys, replacing them with dummy tokens like <code>[USER_1]</code> or <code>[INTERNAL_IP_1]</code>. "
        "Sensitive mapping dictionaries stay isolated in volatile RAM. Before any reasoning occurs, an integrated firewall scans for and neutralizes prompt-injection commands inside raw log strings."
    )
    story.append(Paragraph(p2, body_style))

    p3 = (
        "A three-tier model router directs the anonymized logs. Routine alerts run 100% offline on local workstation GPUs using Ollama (<code>deepseek-r1:8b</code>) at zero marginal cost. "
        "Higher-severity incidents escalate to cloud APIs (Groq or Gemini) using scrubbed tokens only. The platform maps alerts to MITRE ATT&CK tactics, correlates events into attack graphs (DAGs), "
        "and retrieves similar past incidents via ChromaDB vector embeddings. Safe Python AST parsing checks de-obfuscation scripts before execution, and a human-in-the-loop gate mandates explicit analyst "
        "approval for any containment action. Finally, JSONL audit trails log system milestones while ReportLab compiles clean PDF reports."
    )
    story.append(Paragraph(p3, body_style))

    keywords = "<b>Keywords:</b> Privacy-Preserving AI, SOC Triage, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Sandbox, Human-in-the-Loop."
    story.append(Paragraph(keywords, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    shutil.copy2(pdf_path, desktop_path)
    print(f"✅ Generated & Saved Humanized B&W Abstract PDF to Desktop: {desktop_path}")

if __name__ == "__main__":
    build_pdf()
