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
        self.drawString(36, 756, "SRI SAI RAM ENGINEERING COLLEGE — INNOVATIVE DESIGN LAB (IDL) - I")
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
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#0f172a'),
        alignment=1,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#2563eb'),
        alignment=1,
        spaceAfter=8
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
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
        leading=13,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCellStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#1e293b')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#0f172a')
    )

    story = []

    # Title Banner
    story.append(Paragraph("STUDENT ACTIVITY FILE — INNOVATIVE DESIGN LAB (IDL) - I", title_style))
    story.append(Paragraph("SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine", subtitle_style))
    story.append(Paragraph("<b>Submitted By (Team Lead):</b> Gokula Kannan M (SEC25CS196) &nbsp;|&nbsp; <b>Institution:</b> Sri Sai Ram Engineering College", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563eb"), spaceAfter=6))

    # Section 0: Official Cover Page & Metadata Sheet
    story.append(Paragraph("📄 SECTION 0: OFFICIAL COVER PAGE & METADATA SHEET", h1_style))
    
    meta_table_data = [
        [Paragraph("Field Name", table_header_style), Paragraph("Official Project Entry Details", table_header_style)],
        [Paragraph("Project Title", table_cell_bold), Paragraph("SENTINEL (Security Event Network Triage Investigation with Neural Engine & LLM)", table_cell_style)],
        [Paragraph("Project ID & Version", table_cell_bold), Paragraph("SAIRAM-IDL1-2026-CSE-09 &nbsp;|&nbsp; [X] Version 1 – New Project", table_cell_style)],
        [Paragraph("Interdisciplinary Team", table_cell_bold), Paragraph("[X] Yes [ ] No Team &nbsp;|&nbsp; Department: Computer Science & Engineering (CSE)", table_cell_style)],
        [Paragraph("Members (Max 3)", table_cell_bold), Paragraph("1. <b>Gokula Kannan M (Team Lead)</b> — SEC25CS196 — CSE-A Core<br/>2. <b>Lakshan M (Member 1)</b> — SEC25CS036 — CSE-A Core<br/>3. <b>Sivabalan T (Member 2)</b> — SEC25CS101 — CSE-C Core", table_cell_style)],
        [Paragraph("Primary SDG", table_cell_bold), Paragraph("<b>SDG 9: Industry, Innovation, and Infrastructure</b> (SAP-SDG9-CYBER-01)", table_cell_style)],
        [Paragraph("Secondary SDG", table_cell_bold), Paragraph("<b>SDG 16: Peace, Justice, and Strong Institutions</b> (SAP-SDG16-SEC-02)", table_cell_style)],
        [Paragraph("Tertiary SDG", table_cell_bold), Paragraph("<b>SDG 8: Decent Work and Economic Growth</b> (SAP-SDG8-AUTO-03)", table_cell_style)],
        [Paragraph("Faculty Supervisor & Guide", table_cell_bold), Paragraph("<b>Dr. A. SHEELA</b> (Associate Professor, Dept. of CSE)<br/>Email: sheela.cse@sairam.edu.in | Mobile: 9884973270", table_cell_style)],
        [Paragraph("External Guide", table_cell_bold), Paragraph("Kerala Police Cyberdome & Senior Tech Lead / Cyber Specialists, Zoho Corporation", table_cell_style)],
        [Paragraph("Outside World Projection", table_cell_bold), Paragraph("<b>Hac'KP 2026 @ Zoho Corporation Campus</b> (14/08/2026) — Selected for National In-Person Pitching Round", table_cell_style)]
    ]

    t_meta = Table(meta_table_data, colWidths=[120, 420])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    # Section 1: Activity Log Table (Weeks 1 to 13)
    story.append(Paragraph("📊 SECTION 1: ACTIVITY LOG INDEX TABLE (WEEKS 1 - 13)", h1_style))

    log_table_data = [
        [
            Paragraph("S.No", table_header_style),
            Paragraph("Activity Title", table_header_style),
            Paragraph("Start Date", table_header_style),
            Paragraph("Completion", table_header_style),
            Paragraph("Mark (10)", table_header_style),
            Paragraph("Remarks & Status", table_header_style)
        ],
        [
            Paragraph("1", table_cell_bold),
            Paragraph("<b>Orientation & Entrepreneurial Mindset</b>", table_cell_bold),
            Paragraph("01/08/2026", table_cell_style),
            Paragraph("07/08/2026", table_cell_style),
            Paragraph("10 / 10", table_cell_bold),
            Paragraph("Completed & Verified", table_cell_style)
        ],
        [
            Paragraph("2", table_cell_bold),
            Paragraph("<b>Problem Identification & Passion CV</b>", table_cell_bold),
            Paragraph("08/08/2026", table_cell_style),
            Paragraph("14/08/2026", table_cell_style),
            Paragraph("10 / 10", table_cell_bold),
            Paragraph("Completed & Verified", table_cell_style)
        ],
        [
            Paragraph("3", table_cell_style),
            Paragraph("Customer Segmentation & Persona Creation", table_cell_style),
            Paragraph("15/08/2026", table_cell_style),
            Paragraph("21/08/2026", table_cell_style),
            Paragraph("-", table_cell_style),
            Paragraph("In Progress", table_cell_style)
        ],
        [
            Paragraph("4", table_cell_style),
            Paragraph("Ideation, Market Size & Competitor Analysis", table_cell_style),
            Paragraph("22/08/2026", table_cell_style),
            Paragraph("28/08/2026", table_cell_style),
            Paragraph("-", table_cell_style),
            Paragraph("Upcoming", table_cell_style)
        ],
        [
            Paragraph("5", table_cell_style),
            Paragraph("Milestone 1: Problem-Solution Fit Presentation", table_cell_style),
            Paragraph("29/08/2026", table_cell_style),
            Paragraph("04/09/2026", table_cell_style),
            Paragraph("-", table_cell_style),
            Paragraph("Upcoming", table_cell_style)
        ]
    ]

    t_log = Table(log_table_data, colWidths=[30, 190, 75, 75, 55, 115])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (-1, 2), colors.HexColor('#e0f2fe')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_log)
    story.append(Spacer(1, 6))

    # Section 2: Week 1 Fill-in (Team Lead Perspective)
    story.append(Paragraph("📘 WEEK – 1: ORIENTATION & ENTREPRENEURIAL MINDSET (TEAM LEAD PERSPECTIVE)", h1_style))
    w1_text = (
        "<b>1. Understand Entrepreneurship & Innovation (Written by Team Lead Gokula Kannan M):</b><br/>"
        "• <b>Core Problem:</b> As Team Lead guiding SENTINEL, I identified that Security Operation Centers face extreme alert fatigue (10,000+ daily logs). Commercial AI tools (ChatGPT) cannot be used directly because corporate/government data leaks to cloud servers.<br/>"
        "• <b>Team Innovation:</b> Under my leadership, our team engineered Reversible Tokenized Pseudonymization — scrubbing 100% of sensitive PII locally before AI reasoning occurs.<br/>"
        "• <b>Value Proposition:</b> Delivering enterprise-grade autonomous triage at $0 operational cost for 90% of routine alerts on local consumer GPUs (NVIDIA RTX 3050).<br/><br/>"
        "<b>2. Opportunity Recognition & Growth Mindset:</b><br/>"
        "• <b>Market Size (TAM/SAM):</b> I directed our market analysis toward the $13.2 Billion+ Global SIEM Automation Market (18.5% CAGR).<br/>"
        "• <b>Target Customers:</b> Enterprise SOCs, MSSPs, Air-Gapped Government Labs, Cyber Police Cells, Startups.<br/>"
        "• <b>Entrepreneurial Resourcefulness:</b> Quantizing 70B models down to 4-bit (IQ3_M) to run flagship AI on edge hardware."
    )
    story.append(Paragraph(w1_text, body_style))
    story.append(Spacer(1, 5))

    # Section 3: Week 2 Fill-in (Team Lead Perspective)
    story.append(Paragraph("📙 WEEK – 2: PROBLEM IDENTIFICATION & PASSION CV (TEAM LEAD PERSPECTIVE)", h1_style))
    w2_text = (
        "<b>1. Real-World Societal Need:</b><br/>"
        "My team and I recognized that small businesses, hospitals, and universities cannot afford $100k+/year enterprise SIEM subscriptions (Splunk / Cortex XSOAR), leaving them vulnerable to ransomware. As Team Lead, I guided SENTINEL to democratize security co-pilots locally.<br/><br/>"
        "<b>2. Passion CV — Team Profiles:</b><br/>"
        "• <b>Gokula Kannan M (TEAM LEAD — SEC25CS196, CSE-A):</b> Chief Systems Architect, Sprint Planning, Architecture Governance, Systems Engineering, Venture Strategy.<br/>"
        "• <b>Lakshan M (Member 1 — SEC25CS036, CSE-A):</b> Full-Stack Web Architecture, React.js UI, WebSockets Integrations, HITL Approval Modals.<br/>"
        "• <b>Sivabalan T (Member 2 — SEC25CS101, CSE-C):</b> Lead AI Architect, Zero-Trust Privacy Engineering (src/sanitizer.py), 3-Tier Router, RAG Vector Stores.<br/>"
        "• <b>Faculty Supervisor:</b> Dr. A. SHEELA (Associate Professor, Dept. of CSE, Sri Sai Ram Engineering College)."
    )
    story.append(Paragraph(w2_text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Generated Updated PDF Document: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
