# -*- coding: utf-8 -*-
"""
export_conversation.py
Master Conversation Exporter for SENTINEL
Strictly exports ONLY SENTINEL project conversations into the project's conversations folder.
Ignores all other non-SENTINEL chats.
"""

import json
import sys
import io
import os
import re
import subprocess
from datetime import datetime, timezone, timedelta

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BRAIN_DIR = r"C:\Users\siva2\.gemini\antigravity-ide\brain"
PROJECT_DIR = r"C:\Users\siva2\Projects\SENTINEL"

def format_timestamp(ts):
    """Convert ISO timestamp string to IST format."""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        ist = timezone(timedelta(hours=5, minutes=30))
        dt_ist = dt.astimezone(ist)
        return dt_ist.strftime("%d %b %Y, %I:%M %p IST")
    except Exception:
        return ts

def get_iso_ts(ts):
    """Convert ISO timestamp to numerical float for sorting."""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.timestamp()
    except Exception:
        return 0.0

def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(item.get("text", item.get("content", "")))
        return "\n".join(parts)
    return str(content)

def clean_user_text(text):
    if not text:
        return ""
    match = re.search(r"<USER_REQUEST>\s*(.*?)\s*</USER_REQUEST>", text, re.DOTALL)
    if match:
        text = match.group(1)
    text = re.sub(r"<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>", "", text, flags=re.DOTALL)
    text = re.sub(r"<USER_SETTINGS_CHANGE>.*?</USER_SETTINGS_CHANGE>", "", text, flags=re.DOTALL)
    text = re.sub(r"<EPHEMERAL_MESSAGE>.*?</EPHEMERAL_MESSAGE>", "", text, flags=re.DOTALL)
    lines = text.splitlines()
    cleaned = []
    blank_count = 0
    for l in lines:
        if not l.strip():
            blank_count += 1
            if blank_count <= 2:
                cleaned.append("")
        else:
            blank_count = 0
            cleaned.append(l)
    return "\n".join(cleaned).strip()

def clean_ai_text(text):
    if not text:
        return ""
    lines = text.splitlines()
    cleaned = []
    blank_count = 0
    for l in lines:
        if not l.strip():
            blank_count += 1
            if blank_count <= 2:
                cleaned.append("")
        else:
            blank_count = 0
            cleaned.append(l)
    return "\n".join(cleaned).strip()

def export_sentinel_conversation():
    conversations_dir = os.path.join(PROJECT_DIR, "conversations")
    os.makedirs(conversations_dir, exist_ok=True)

    # 1. Load base historical content from git HEAD if available
    base_md = ""
    try:
        base_md = subprocess.check_output(
            ["git", "show", "HEAD:SENTINEL_Conversation.md"],
            cwd=PROJECT_DIR, text=True, encoding="utf-8"
        )
    except Exception as e:
        print(f"Notice: Could not load base git history: {e}")

    # Remove old stats block from base_md
    if base_md:
        stats_idx = base_md.rfind("## 📊 Stats")
        if stats_idx != -1:
            base_md = base_md[:stats_idx].strip()

    # 2. Gather entries strictly from SENTINEL project sessions
    new_entries = []
    if os.path.exists(BRAIN_DIR):
        for d in os.listdir(BRAIN_DIR):
            full_path = os.path.join(BRAIN_DIR, d)
            if os.path.isdir(full_path) and d != "tempmediaStorage":
                log_path = os.path.join(full_path, ".system_generated", "logs", "transcript_full.jsonl")
                if not os.path.exists(log_path):
                    log_path = os.path.join(full_path, ".system_generated", "logs", "transcript.jsonl")
                if os.path.exists(log_path):
                    with open(log_path, "r", encoding="utf-8") as f:
                        log_text = f.read()
                    
                    # Strictly include ONLY chats associated with the SENTINEL project workspace
                    if "SENTINEL" not in log_text:
                        continue
                    # Ignore non-SENTINEL system troubleshooting chats
                    if "msi not opening" in log_text or "BlueStacks" in log_text:
                        continue

                    # Parse entries from filtered SENTINEL transcript
                    with open(log_path, "r", encoding="utf-8") as f:
                        for line in f:
                            try:
                                step = json.loads(line.strip())
                                stype = step.get("type", "")
                                content_raw = step.get("content", "")
                                ts = step.get("created_at", "")
                                if stype == "USER_INPUT" and content_raw:
                                    txt = clean_user_text(extract_text(content_raw))
                                    if txt:
                                        new_entries.append((get_iso_ts(ts), ts, "USER", txt))
                                elif stype == "PLANNER_RESPONSE" and content_raw:
                                    txt = clean_ai_text(extract_text(content_raw))
                                    if txt and len(txt) > 2:
                                        new_entries.append((get_iso_ts(ts), ts, "AI", txt))
                            except Exception:
                                pass

    # Sort entries by timestamp
    new_entries.sort(key=lambda x: x[0])

    output_parts = []
    if base_md:
        output_parts.append(base_md)
        output_parts.append("")
        output_parts.append("---")
        output_parts.append("")
        output_parts.append("## 🗓️ Subsequent Sessions (07 Aug 2026 onwards)")
        output_parts.append("")
    else:
        output_parts.append("# 🔵 SENTINEL Project — Full Conversation Log")
        output_parts.append("")

    user_new_count = 0
    ai_new_count = 0

    for sort_key, ts, role, text in new_entries:
        ts_str = format_timestamp(ts) if ts else ""
        if role == "USER":
            user_new_count += 1
            output_parts.append(f"## 👤 You  `{ts_str}`" if ts_str else "## 👤 You")
            output_parts.append("")
            output_parts.append(text)
            output_parts.append("")
            output_parts.append("---")
            output_parts.append("")
        elif role == "AI":
            ai_new_count += 1
            output_parts.append(f"## 🤖 Antigravity  `{ts_str}`" if ts_str else "## 🤖 Antigravity")
            output_parts.append("")
            output_parts.append(text)
            output_parts.append("")
            output_parts.append("---")
            output_parts.append("")

    now_ist = datetime.now(timezone(timedelta(hours=5, minutes=30))).strftime("%d %b %Y, %I:%M %p IST")
    
    hist_user = 94 if base_md else 0
    hist_ai = 133 if base_md else 0

    output_parts.append("")
    output_parts.append("---")
    output_parts.append("## 📊 Stats (SENTINEL Master Log)")
    output_parts.append(f"- **User messages**: {hist_user + user_new_count}")
    output_parts.append(f"- **AI responses**: {hist_ai + ai_new_count}")
    output_parts.append(f"- **Export time**: {now_ist}")
    output_parts.append("")
    output_parts.append("*Generated by export_conversation.py*")

    final_content = "\n".join(output_parts)

    target_file = os.path.join(conversations_dir, "SENTINEL_Conversation.md")

    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(final_content)
        size_kb = os.path.getsize(target_file) / 1024
        lines_cnt = len(final_content.splitlines())
        print(f"✅ Saved SENTINEL Conversation: {target_file} ({size_kb:.1f} KB, {lines_cnt} lines)")
    except Exception as e:
        print(f"⚠️ Failed to write {target_file}: {e}")

if __name__ == "__main__":
    export_sentinel_conversation()
