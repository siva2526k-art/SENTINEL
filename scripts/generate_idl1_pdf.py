import os
import sys
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
        self.drawString(36, 756, "SAIRAM INSTITUTIONS — INNOVATIVE DESIGN LAB (IDL) - I")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 748, 576, 748)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 30, "Student Activity File | Academic Year 2026-2027")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 30, page_text)
        self.line(36, 42, 576, 42)
        self.restoreState()

def build_pdf():
    pdf_path = r"c:\Users\siva2\Projects\SENTINEL\docs\SENTINEL_IDL1_Student_Activity_File.pdf"
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
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2563eb'),
        alignment=1,
        spaceAfter=12
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCellStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )

    story = []

    # Title
    story.append(Paragraph("STUDENT ACTIVITY FILE — INNOVATIVE DESIGN LAB (IDL) - I", title_style))
    story.append(Paragraph("SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine", subtitle_style))
    story.append(Paragraph("<b>Academic Year:</b> 2026-2027 &nbsp;|&nbsp; <b>Lead Innovator:</b> SIVABALAN T & Team &nbsp;|&nbsp; <b>Institution:</b> Sairam Institutions", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563eb"), spaceAfter=10))

    # Section 0: Metadata Fill-in
    story.append(Paragraph("📄 SECTION 0: COVER PAGE & METADATA SHEET", h1_style))
    
    meta_table_data = [
        [Paragraph("Field", table_header_style), Paragraph("Details", table_header_style)],
        [Paragraph("Project Title", table_cell_bold), Paragraph("SENTINEL (Security Event Network Triage Investigation with Neural Engine & LLM)", table_cell_style)],
        [Paragraph("Project ID", table_cell_bold), Paragraph("SAIRAM-IDL1-2026-CYBER-09 (Version 1 - New Project)", table_cell_style)],
        [Paragraph("Team Members", table_cell_bold), Paragraph("1. SIVABALAN T (2026-CSE-CYBER-01) - Lead Innovator<br/>2. Team Member 2 (2026-CSE-CYBER-02) - Cyber Specialist<br/>3. Team Member 3 (2026-CSE-CYBER-03) - Full-Stack Developer", table_cell_style)],
        [Paragraph("Primary SDG", table_cell_bold), Paragraph("<b>SDG 9: Industry, Innovation, and Infrastructure</b> (SAP-SDG9-CYBER-01)", table_cell_style)],
        [Paragraph("Secondary SDG", table_cell_bold), Paragraph("<b>SDG 16: Peace, Justice, and Strong Institutions</b> (SAP-SDG16-SEC-02)", table_cell_style)],
        [Paragraph("Tertiary SDG", table_cell_bold), Paragraph("<b>SDG 8: Decent Work and Economic Growth</b> (SAP-SDG8-AUTO-03)", table_cell_style)],
        [Paragraph("Competitions", table_cell_bold), Paragraph("Hac'KP 2026 @ Zoho Corporation Campus (In-Person Pitching Round)", table_cell_style)]
    ]

    t_meta = Table(meta_table_data, colWidths=[130, 410])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # Section 1: Week 1
    story.append(Paragraph("📘 WEEK – 1: ORIENTATION & ENTREPRENEURIAL MINDSET", h1_style))
    w1_text = (
        "<b>1. Innovation & Entrepreneurship Analysis:</b><br/>"
        "• <b>Core Problem:</b> Security analysts suffer from severe alert fatigue (10,000+ daily logs). Commercial AI tools (ChatGPT/Claude) cannot be used directly because corporate/government data leaks to cloud servers.<br/>"
        "• <b>Innovation:</b> SENTINEL invents Reversible Tokenized Pseudonymization — scrubbing 100% of sensitive PII locally before AI reasoning occurs.<br/>"
        "• <b>Value Proposition:</b> Delivering enterprise-grade autonomous triage at $0 operational cost for 90% of routine alerts on local consumer GPUs (NVIDIA RTX 3050).<br/><br/>"
        "<b>2. Growth Mindset & Market Size:</b><br/>"
        "• <b>TAM / SAM:</b> $13.2 Billion+ Global SIEM Automation & Threat Intel Market (18.5% CAGR).<br/>"
        "• <b>Target Customers:</b> Enterprise SOCs, MSSPs, Air-Gapped Government Labs, Cyber Police Cells, Startups.<br/>"
        "• <b>Entrepreneurial Traits:</b> Quantizing 70B models down to 4-bit (IQ3_M) to run flagship AI on edge hardware."
    )
    story.append(Paragraph(w1_text, body_style))
    story.append(Spacer(1, 8))

    # Section 2: Week 2
    story.append(Paragraph("📙 WEEK – 2: PROBLEM IDENTIFICATION & PASSION CV", h1_style))
    w2_text = (
        "<b>1. Real-World Societal Need:</b><br/>"
        "Small businesses, hospitals, and public institutions cannot afford $100k+/year enterprise SIEM subscriptions (like Splunk or Palo Alto Cortex XSOAR), leaving them vulnerable to ransomware. SENTINEL provides an open-source, self-hosted, autonomous AI SOC co-pilot running on standard workstation hardware.<br/><br/>"
        "<b>2. Passion CV — SIVABALAN T (Lead Innovator):</b><br/>"
        "• <b>Technical Specialization:</b> Cybersecurity & SIEM (Wazuh, Linux Hardening, MITRE ATT&CK), AI Engine (Ollama, GGUF Quantization Q4_K_M/IQ3_M, 3-Tier Router, ChromaDB RAG), Zero-Trust Privacy Engineering.<br/>"
        "• <b>Project Experience:</b> Lead Innovator of SENTINEL (reduced triage from 45 mins to < 30s); Hac'KP 2026 National Finalist @ Zoho; HackTronix 2.0 Vision & Agent Track.<br/>"
        "• <b>5-Year Vision:</b> Publish IEEE research, launch SENTINEL as an open-source enterprise engine on GitHub, and establish a deep-tech cybersecurity venture."
    )
    story.append(Paragraph(w2_text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Generated PDF Document: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
