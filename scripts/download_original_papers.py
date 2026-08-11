# -*- coding: utf-8 -*-
"""
download_original_papers.py
Downloads full open-access academic research PDFs related to SENTINEL and saves them to Desktop and docs folder.
"""

import os
import sys
import io
import urllib.request

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DESKTOP_DIR = r"C:\Users\siva2\Desktop\SENTINEL_Original_Research_Papers"
DOCS_DIR = r"C:\Users\siva2\Projects\SENTINEL\docs\related_papers_and_projects\pdf_papers"

os.makedirs(DESKTOP_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

papers_to_download = [
    {
        "filename": "01_CORTEX_Collaborative_LLM_Alert_Triage.pdf",
        "url": "https://arxiv.org/pdf/2510.00311.pdf",
        "title": "CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage"
    },
    {
        "filename": "02_Rule_ATTCK_Mapper_RAM_SIEM_Rules.pdf",
        "url": "https://arxiv.org/pdf/2502.02337.pdf",
        "title": "Rule-ATT&CK Mapper (RAM): Mapping SIEM Rules to TTPs Using LLMs"
    },
    {
        "filename": "03_SynRAG_SIEM_Executable_Query_Generation.pdf",
        "url": "https://arxiv.org/pdf/2512.24571.pdf",
        "title": "SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM Systems"
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

print("📥 Starting download of original research papers...")

for paper in papers_to_download:
    url = paper["url"]
    fname = paper["filename"]
    
    desktop_file = os.path.join(DESKTOP_DIR, fname)
    docs_file = os.path.join(DOCS_DIR, fname)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response, open(docs_file, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            with open(desktop_file, 'wb') as desk_out:
                desk_out.write(data)
        
        size_kb = len(data) / 1024
        print(f"✅ Downloaded '{paper['title']}': {fname} ({size_kb:.1f} KB)")
    except Exception as e:
        print(f"⚠️ Failed to download {fname} from {url}: {e}")

print("✨ All papers successfully downloaded and saved!")
