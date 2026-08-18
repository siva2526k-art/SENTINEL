import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
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
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5
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
    story.append(Paragraph("STUDENT ACTIVITY FILE", title_style))
    story.append(Paragraph("INNOVATIVE DESIGN LAB (IDL) - I", subtitle_style))
    story.append(Paragraph("<b>Academic year:</b> 2026-2027 &nbsp;|&nbsp; <b>Department:</b> Computer Science & Engineering", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2563eb"), spaceAfter=8))

    # COVER PAGE TABLE
    meta_table_data = [
        [Paragraph("Field", table_header_style), Paragraph("Details", table_header_style)],
        [Paragraph("Academic Year", table_cell_bold), Paragraph("2026-2027", table_cell_style)],
        [Paragraph("Department & Section", table_cell_bold), Paragraph("Computer Science and Engineering &nbsp;|&nbsp; Section: A & C", table_cell_style)],
        [Paragraph("Innovation Ecosystem Project ID", table_cell_bold), Paragraph("SAIRAM-IDL1-2026-CSE-09", table_cell_style)],
        [Paragraph("Title of the Project", table_cell_bold), Paragraph("<b>SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine</b>", table_cell_style)],
        [Paragraph("Inter disciplinary Project", table_cell_bold), Paragraph("[X] Yes &nbsp;&nbsp; [ ] No Team", table_cell_style)],
        [Paragraph("Members (Max. 3)", table_cell_bold), Paragraph("1. <b>Gokula Kannan M</b> — SEC25CS196<br/>2. <b>Lakshan M</b> — SEC25CS036<br/>3. <b>Sivabalan T</b> — SEC25CS101", table_cell_style)],
        [Paragraph("Project Version", table_cell_bold), Paragraph("[X] Version 1 – New Project &nbsp;&nbsp; [ ] Version 2 – Pass out Student Project", table_cell_style)],
        [Paragraph("Domain Name", table_cell_bold), Paragraph("Cybersecurity, Artificial Intelligence & Autonomous Systems", table_cell_style)],
        [Paragraph("IEEE Society & Community", table_cell_bold), Paragraph("IEEE Computer Society &nbsp;|&nbsp; IEEE Student Branch Sairam", table_cell_style)],
        [Paragraph("Club and Cells", table_cell_bold), Paragraph("Sairam Innovation Ecosystem / Cyber Security Club", table_cell_style)],
        [Paragraph("Name of Department IDL - I Coordinator", table_cell_bold), Paragraph("Dr. A. SHEELA &nbsp;|&nbsp; Faculty ID: IDL-FAC-01", table_cell_style)],
        [Paragraph("Name of the Supervisor", table_cell_bold), Paragraph("Dr. A. SHEELA &nbsp;|&nbsp; Faculty ID: IDL-FAC-02", table_cell_style)],
        [Paragraph("Name of External Guide", table_cell_bold), Paragraph("Senior Tech Leads & Cyber Forensic Specialists", table_cell_style)],
        [Paragraph("Designation & Organization", table_cell_bold), Paragraph("Cyberdome Investigations / Zoho Corporation", table_cell_style)]
    ]

    t_meta = Table(meta_table_data, colWidths=[140, 400])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_meta)
    story.append(PageBreak())

    # PAGE 2: SDG & INDEX TABLE
    story.append(Paragraph("SUSTAINABLE DEVELOPMENT GOALS (SDG) MAPPING", h1_style))
    
    sdg_data = [
        [Paragraph("SDG", table_header_style), Paragraph("Goal Number With Name", table_header_style), Paragraph("SAP Code with Explanation", table_header_style)],
        [Paragraph("Primary SDG:", table_cell_bold), Paragraph("SDG 9: Industry, Innovation, and Infrastructure", table_cell_style), Paragraph("1. SAP-SDG9-CYBER-01: Resilient cyber infrastructure & AI SOC automation.<br/>2. SAP-SDG9-CYBER-02: Zero-trust cloud-edge security architecture.<br/>3. SAP-SDG9-CYBER-03: Scalable threat intelligence platform.", table_cell_style)],
        [Paragraph("Secondary SDG:", table_cell_bold), Paragraph("SDG 16: Peace, Justice, and Strong Institutions", table_cell_style), Paragraph("1. SAP-SDG16-SEC-01: Evidence privacy & chain-of-custody enforcement.<br/>2. SAP-SDG16-SEC-02: Citizen PII protection in digital investigation.<br/>3. SAP-SDG16-SEC-03: Transparent forensic audit logging.", table_cell_style)],
        [Paragraph("Tertiary SDG:", table_cell_bold), Paragraph("SDG 8: Decent Work and Economic Growth", table_cell_style), Paragraph("1. SAP-SDG8-AUTO-01: Reduction of SOC analyst alert fatigue.<br/>2. SAP-SDG8-AUTO-02: Decreasing MTTR from 45 mins to < 30 seconds.<br/>3. SAP-SDG8-AUTO-03: Workforce efficiency & burnout prevention.", table_cell_style)]
    ]
    t_sdg = Table(sdg_data, colWidths=[80, 180, 280])
    t_sdg.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_sdg)
    story.append(Spacer(1, 10))

    story.append(Paragraph("ACTIVITY LOG INDEX TABLE (WEEKS 1 - 13)", h1_style))
    log_table_data = [
        [Paragraph("S.No.", table_header_style), Paragraph("Title", table_header_style), Paragraph("Start Date", table_header_style), Paragraph("Completion Date", table_header_style), Paragraph("Mark (Out of 10)", table_header_style), Paragraph("Remarks", table_header_style), Paragraph("Signature of IDL - I Coordinator", table_header_style)],
        [Paragraph("1", table_cell_bold), Paragraph("Orientation & Entrepreneurial Mindset", table_cell_bold), Paragraph("01/08/2026", table_cell_style), Paragraph("07/08/2026", table_cell_style), Paragraph("10", table_cell_bold), Paragraph("Completed", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("2", table_cell_bold), Paragraph("Problem Identification & Passion CV", table_cell_bold), Paragraph("08/08/2026", table_cell_style), Paragraph("14/08/2026", table_cell_style), Paragraph("10", table_cell_bold), Paragraph("Completed", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("3", table_cell_style), Paragraph("Customer Segmentation & Persona Creation & JTBD", table_cell_style), Paragraph("15/08/2026", table_cell_style), Paragraph("21/08/2026", table_cell_style), Paragraph("", table_cell_style), Paragraph("In Progress", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("4", table_cell_style), Paragraph("Ideation, Market Size & Competitor Analysis", table_cell_style), Paragraph("22/08/2026", table_cell_style), Paragraph("28/08/2026", table_cell_style), Paragraph("", table_cell_style), Paragraph("Upcoming", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("5", table_cell_style), Paragraph("Milestone1:Problem-Solution Fit Presentation", table_cell_style), Paragraph("29/08/2026", table_cell_style), Paragraph("04/09/2026", table_cell_style), Paragraph("", table_cell_style), Paragraph("Upcoming", table_cell_style), Paragraph("", table_cell_style)]
    ]
    t_log = Table(log_table_data, colWidths=[25, 175, 60, 65, 55, 60, 100])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0, 1), (-1, 2), colors.HexColor('#e0f2fe')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_log)
    story.append(PageBreak())

    # PAGE 3: OUTSIDE WORLD PROJECTION & SIGNATURES
    story.append(Paragraph("OUTSIDE WORLD PROJECTION", h1_style))
    story.append(Paragraph("<b>Details of the Competition Attended (Hackathon / Idea Pitching)</b>", body_style))
    
    comp_data = [
        [Paragraph("S.No", table_header_style), Paragraph("Name", table_header_style), Paragraph("Date", table_header_style), Paragraph("Place", table_header_style), Paragraph("Remark", table_header_style), Paragraph("Signature", table_header_style)],
        [Paragraph("1", table_cell_style), Paragraph("Hac'KP 2026 (7th Edition National Hackathon by Kerala Police Cyberdome)", table_cell_style), Paragraph("14/08/2026", table_cell_style), Paragraph("Zoho Corporation, Chennai", table_cell_style), Paragraph("Selected for National In-Person Pitching Round", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("2", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style)]
    ]
    t_comp = Table(comp_data, colWidths=[30, 180, 65, 110, 100, 55])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Design Patent / Idea Patent Publication / Conference Paper</b>", body_style))
    pub_data = [
        [Paragraph("S.No", table_header_style), Paragraph("Title / Forum", table_header_style), Paragraph("Date", table_header_style), Paragraph("Place / Journal", table_header_style), Paragraph("Remark", table_header_style), Paragraph("Signature", table_header_style)],
        [Paragraph("1", table_cell_style), Paragraph("Confidentiality-Preserving Autonomous SOC Triage via Tokenized Edge-Cloud Multi-Agent Systems", table_cell_style), Paragraph("August 2026", table_cell_style), Paragraph("IEEE / USENIX Track", table_cell_style), Paragraph("Paper Manuscript & Patent Drafted", table_cell_style), Paragraph("", table_cell_style)],
        [Paragraph("2", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style), Paragraph("", table_cell_style)]
    ]
    t_pub = Table(pub_data, colWidths=[30, 180, 65, 110, 100, 55])
    t_pub.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_pub)
    story.append(Spacer(1, 30))

    # Signature Row
    sig_data = [
        [Paragraph("<b>IDL – I Coordinator</b>", table_cell_bold), Paragraph("<b>Creative Innovator</b>", table_cell_bold), Paragraph("<b>H.O.D</b>", table_cell_bold)],
        [Paragraph("<br/><br/>Dr. A. SHEELA", table_cell_style), Paragraph("<br/><br/>Gokula Kannan M (Team Lead)", table_cell_style), Paragraph("<br/><br/>Head of Department", table_cell_style)]
    ]
    t_sig = Table(sig_data, colWidths=[180, 180, 180])
    t_sig.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_sig)
    story.append(PageBreak())

    # WEEK 1 ACTIVITY PAGE
    story.append(Paragraph("WEEK – 1", subtitle_style))
    story.append(Paragraph("1. Orientation & Entrepreneurial Mindset", h1_style))
    
    w1_content = (
        "<b>• Understand entrepreneurship & innovation</b><br/>"
        "Security Operations Centers (SOCs) generate over 10,000 security logs daily, creating severe alert fatigue where human analysts spend 30–45 minutes manually triaging single events. "
        "Commercial AI endpoints cannot be deployed directly due to data privacy regulations and risks of uploading confidential network payloads to external servers.<br/>"
        "The proposed solution, SENTINEL, introduces Reversible Tokenized Pseudonymization, scrubbing 100% of sensitive PII, IP addresses, and hostnames locally before AI reasoning occurs. "
        "This enables enterprise-grade autonomous triage at $0 operational cost for 90% of routine alerts using local consumer GPU hardware (NVIDIA RTX 3050).<br/><br/>"
        "<b>• Opportunity recognition, entrepreneurial traits and growth mindset</b><br/>"
        "The global SIEM automation and threat intelligence market is valued at $13.2 Billion+ with an 18.5% CAGR. "
        "Primary target markets include Enterprise SOCs, Managed Security Service Providers (MSSPs), Air-Gapped Defense Networks, Cyber Crime Units, and Startups. "
        "Technical resourcefulness is demonstrated by quantizing 70B parameter models down to 4-bit (IQ3_M) GGUF format to execute high-capacity intelligence on edge workstations.<br/><br/>"
        "<b>• Startup journey from idea to venture</b><br/>"
        "1. Problem Formulation: Identifying SOC alert fatigue and data privacy constraints.<br/>"
        "2. Proof-of-Concept: Engineering local Zero-Trust Data Sanitizer (src/sanitizer.py).<br/>"
        "3. MVP Architecture: Building 3-Tier Hybrid AI Router (src/router.py).<br/>"
        "4. Validation & Pitching: Selected for National Pitching Round at Hac'KP 2026 @ Zoho Corporation.<br/>"
        "5. Commercialization: Deploying open-source SaaS framework and enterprise MSSP engine."
    )
    story.append(Paragraph(w1_content, body_style))
    story.append(PageBreak())

    # WEEK 2 ACTIVITY PAGE
    story.append(Paragraph("WEEK – 2", subtitle_style))
    story.append(Paragraph("2. Problem Identification & Passion CV", h1_style))
    
    w2_content = (
        "<b>• Identify real-world problems based on personal interests</b><br/>"
        "Modern digital investigations face a severe bottleneck where human triage speed cannot match machine-speed cyber attacks. "
        "Public commercial cloud LLMs violate legal data privacy and chain-of-custody mandates when processing un-sanitized evidence.<br/><br/>"
        "<b>• Skills, experiences, and societal needs</b><br/>"
        "Small businesses, hospitals, and educational institutions are unable to afford $100k+/year enterprise SIEM subscriptions (e.g., Splunk or Cortex XSOAR), leaving critical infrastructure vulnerable to ransomware. "
        "SENTINEL addresses this societal gap by delivering a self-hosted, privacy-compliant, autonomous AI co-pilot operating on standard hardware.<br/><br/>"
        "<b>• Prepare a Passion CV to identify potential entrepreneurial opportunities</b><br/><br/>"
        "<b>Team Lead: Gokula Kannan M (SEC25CS196 | CSE-A)</b><br/>"
        "• Domain: Software Architecture, Systems Engineering, Project Governance & Venture Strategy.<br/>"
        "• Project Contribution: Overall system architecture, sprint management, and leading the national pitch at Hac'KP 2026 @ Zoho Corporation.<br/><br/>"
        "<b>Team Member 1: Lakshan M (SEC25CS036 | CSE-A)</b><br/>"
        "• Domain: Full-Stack Web Development, React.js UI, WebSockets Integrations.<br/>"
        "• Project Contribution: Real-time incident dashboard engineering and Human-in-the-Loop (HITL) action approval interface.<br/><br/>"
        "<b>Team Member 2: Sivabalan T (SEC25CS101 | CSE-C)</b><br/>"
        "• Domain: AI Engine Architecture, Zero-Trust Privacy Engineering, Quantization & Vector RAG.<br/>"
        "• Project Contribution: Development of Zero-Trust Data Sanitizer (src/sanitizer.py) and 3-Tier AI Router (src/router.py)."
    )
    story.append(Paragraph(w2_content, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Generated Professional Submission PDF: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
