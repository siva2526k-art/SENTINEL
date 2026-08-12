"""
SENTINEL — Official Demo Execution Script for Pitching & Presentations
Ingests sample JSON attack telemetry, runs zero-trust sanitization, MITRE mapping, 3-tier routing, dual-view, and PDF report generation!
"""
import os
import sys
import json
from triage_agent import SentinelTriageAgent
from reports.pdf_generator import SentinelReportGenerator

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def run_sentinel_demo():
    agent = SentinelTriageAgent()
    reporter = SentinelReportGenerator()
    
    samples_dir = os.path.join(os.path.dirname(__file__), "samples")
    sample_files = [
        "1_ssh_bruteforce.json",
        "2_powershell_cradle.json",
        "3_data_exfiltration.json"
    ]

    print("\n" + "🚀"*35)
    print("      SENTINEL LIVE DEMO & PITCH EXECUTION SUITE")
    print("🚀"*35 + "\n")

    for idx, fname in enumerate(sample_files, 1):
        fpath = os.path.join(samples_dir, fname)
        if not os.path.exists(fpath):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        raw_text = data.get("raw_alert", "")
        print(f"\n🔹 [DEMO SCENARIO {idx}/3]: {data.get('source', 'Security Log')}")
        
        # Execute Triage Pipeline
        result = agent.process_alert(raw_text)
        
        # Generate PDF Report
        pdf_name = f"SENTINEL_Demo_Report_Scenario_{idx}.pdf"
        pdf_path = reporter.generate_pdf(result, filename=pdf_name)

    print("\n" + "✅"*35)
    print("   ALL 3 DEMO SCENARIOS TRIAGED & PDF REPORTS GENERATED!")
    print("✅"*35 + "\n")

if __name__ == "__main__":
    run_sentinel_demo()
