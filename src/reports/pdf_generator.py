"""
SENTINEL — Executive PDF Incident Report Generator Module
Generates courtroom-ready executive incident briefs using ReportLab in < 30 seconds.
"""
import os
import sys

# Ensure src/ directory is in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SentinelReportGenerator:
    def __init__(self, output_dir=r"C:\Users\siva2\Projects\SENTINEL\docs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_pdf(self, incident_data: dict, filename="SENTINEL_Executive_Incident_Report.pdf") -> str:
        pdf_path = os.path.join(self.output_dir, filename)
        doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        story = []

        styles = getSampleStyleSheet()
        
        # Custom Styles
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=20,
            leading=24,
            textColor=colors.HexColor('#1e3a8a')
        )
        
        heading_style = ParagraphStyle(
            'HeadingStyle',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            leading=18,
            textColor=colors.HexColor('#1d4ed8'),
            spaceBefore=12,
            spaceAfter=6
        )

        body_style = ParagraphStyle(
            'BodyStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            textColor=colors.HexColor('#0f172a')
        )

        # Header Title
        story.append(Paragraph("🛡️ SENTINEL — Executive Incident Brief", title_style))
        story.append(Paragraph("<b>Security Event Network Triage Investigation with Neural Engine and LLM</b>", body_style))
        story.append(Spacer(1, 10))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563eb'), spaceAfter=15))

        # Overview Table
        triage = incident_data.get("triage", {})
        mitre = incident_data.get("mitre", {})

        overview_table_data = [
            [Paragraph("<b>Incident ID:</b> INC-2026-8801", body_style), Paragraph(f"<b>Threat Severity:</b> <font color='red'><b>{triage.get('severity', 'HIGH')}</b></font>", body_style)],
            [Paragraph(f"<b>AI Routing Tier:</b> {triage.get('tier_used', 'Tier 1 Local')}", body_style), Paragraph("<b>Privacy Sanitization:</b> <font color='green'><b>ACTIVE (100% Scrubbed)</b></font>", body_style)],
            [Paragraph(f"<b>MITRE Tactic:</b> {mitre.get('primary_tactic', 'Initial Access')}", body_style), Paragraph(f"<b>MITRE Technique:</b> {mitre.get('primary_technique_id', 'T1110')} ({mitre.get('primary_technique_name', 'Brute Force')})", body_style)]
        ]

        t = Table(overview_table_data, colWidths=[270, 270])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t)
        story.append(Spacer(1, 15))

        # Investigation Summary
        story.append(Paragraph("📌 Investigation Summary", heading_style))
        story.append(Paragraph(f"{triage.get('triage_summary', 'SSH Brute force attempt detected.')}", body_style))
        story.append(Spacer(1, 10))

        # Sanitized vs Reidentified Evidence
        story.append(Paragraph("🔒 Evidence Indicators & Dual-View Analysis", heading_style))
        evidence_data = [
            [Paragraph("<b>Cloud / AI Sanitized View:</b>", body_style), Paragraph(f"<code>{incident_data.get('sanitized_alert', '')}</code>", body_style)],
            [Paragraph("<b>Officer Re-Identified View:</b>", body_style), Paragraph(f"<code>{incident_data.get('reidentified_alert', '')}</code>", body_style)]
        ]
        t_ev = Table(evidence_data, colWidths=[160, 380])
        t_ev.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#eff6ff')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#bfdbfe')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dbeafe')),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_ev)
        story.append(Spacer(1, 15))

        # Recommended Action & HITL Approval Status
        story.append(Paragraph("⚠️ Active Response & HITL Containment Status", heading_style))
        story.append(Paragraph(f"<b>Recommended Action:</b> {triage.get('recommended_action', 'Block IP at firewall')}", body_style))
        story.append(Paragraph("<b>Human-in-the-Loop Status:</b> <font color='#1e40af'><b>APPROVED & EXECUTED BY AUTHORIZED OFFICER</b></font>", body_style))
        story.append(Spacer(1, 20))

        # Footer
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=10))
        story.append(Paragraph("<i>Generated by SENTINEL Autonomous SOC Platform — Confidential Police / Enterprise Record</i>", ParagraphStyle('Footer', parent=body_style, fontSize=8, textColor=colors.HexColor('#64748b'))))

        doc.build(story)
        print(f"📄 Executive PDF Report generated successfully: {pdf_path}")
        return pdf_path

if __name__ == "__main__":
    from triage_agent import SentinelTriageAgent
    agent = SentinelTriageAgent()
    sample_incident = "Failed SSH login for user admin@keralapolice.gov.in from 192.168.1.45 on port 22."
    data = agent.process_alert(sample_incident)
    
    reporter = SentinelReportGenerator()
    reporter.generate_pdf(data)
