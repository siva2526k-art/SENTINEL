# -*- coding: utf-8 -*-
"""
export_conversation.py
Master Multi-Member Conversation & Feature Sync Exporter for SENTINEL

Allows team members and their AI agents (Antigravity) to export conversation logs
into their isolated member subfolders (conversations/<member_name>/) to prevent Git merge collisions.
Generates an aggregated TEAM_OVERVIEW.md dashboard so all teammates can see live project updates.
"""

import json
import sys
import io
import os
import re
import argparse
import subprocess
from datetime import datetime, timezone, timedelta

# Safely set UTF-8 output encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Dynamic paths based on environment
USER_PROFILE = os.environ.get("USERPROFILE", r"C:\Users\siva2")
DEFAULT_BRAIN_DIR = os.path.join(USER_PROFILE, ".gemini", "antigravity-ide", "brain")
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

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

def export_member_conversation(member_name, brain_dir):
    conversations_base = os.path.join(PROJECT_DIR, "conversations")
    member_dir = os.path.join(conversations_base, member_name.lower())
    os.makedirs(member_dir, exist_ok=True)

    target_file = os.path.join(member_dir, "Conversation_Log.md")

    # Gather entries strictly from SENTINEL project sessions
    new_entries = []
    if os.path.exists(brain_dir):
        for d in os.listdir(brain_dir):
            full_path = os.path.join(brain_dir, d)
            if os.path.isdir(full_path) and d != "tempmediaStorage":
                log_path = os.path.join(full_path, ".system_generated", "logs", "transcript_full.jsonl")
                if not os.path.exists(log_path):
                    log_path = os.path.join(full_path, ".system_generated", "logs", "transcript.jsonl")
                if os.path.exists(log_path):
                    with open(log_path, "r", encoding="utf-8") as f:
                        log_text = f.read()
                    
                    # Strictly include ONLY chats associated with the SENTINEL project workspace
                    if "SENTINEL" not in log_text and "sentinel" not in log_text.lower():
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
    output_parts.append(f"# 🔵 SENTINEL Project — Conversation Log ({member_name.capitalize()})")
    output_parts.append(f"> Dedicated, collision-free AI conversation log for **{member_name.capitalize()}**.")
    output_parts.append("")

    user_count = 0
    ai_count = 0

    for sort_key, ts, role, text in new_entries:
        ts_str = format_timestamp(ts) if ts else ""
        if role == "USER":
            user_count += 1
            output_parts.append(f"## 👤 {member_name.capitalize()}  `{ts_str}`" if ts_str else f"## 👤 {member_name.capitalize()}")
            output_parts.append("")
            output_parts.append(text)
            output_parts.append("")
            output_parts.append("---")
            output_parts.append("")
        elif role == "AI":
            ai_count += 1
            output_parts.append(f"## 🤖 Antigravity (Agent for {member_name.capitalize()})  `{ts_str}`" if ts_str else f"## 🤖 Antigravity Agent")
            output_parts.append("")
            output_parts.append(text)
            output_parts.append("")
            output_parts.append("---")
            output_parts.append("")

    now_ist = datetime.now(timezone(timedelta(hours=5, minutes=30))).strftime("%d %b %Y, %I:%M %p IST")

    output_parts.append("")
    output_parts.append("---")
    output_parts.append(f"## 📊 Member Stats ({member_name.capitalize()})")
    output_parts.append(f"- **User ({member_name.capitalize()}) messages**: {user_count}")
    output_parts.append(f"- **AI Agent responses**: {ai_count}")
    output_parts.append(f"- **Total messages**: {user_count + ai_count}")
    output_parts.append(f"- **Last Export**: {now_ist}")
    output_parts.append("")
    output_parts.append("*Generated automatically by scripts/export_conversation.py*")

    final_content = "\n".join(output_parts)

    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(final_content)
        size_kb = os.path.getsize(target_file) / 1024
        lines_cnt = len(final_content.splitlines())
        print(f"✅ Saved Member Log: {target_file} ({size_kb:.1f} KB, {lines_cnt} lines)")
    except Exception as e:
        print(f"⚠️ Failed to write {target_file}: {e}")

    # Backward compatibility: if member is siva, also update root SENTINEL_Conversation.md
    if member_name.lower() in ["siva", "siva2"]:
        root_file = os.path.join(conversations_base, "SENTINEL_Conversation.md")
        try:
            with open(root_file, "w", encoding="utf-8") as f:
                f.write(final_content)
            print(f"✅ Updated legacy root conversation log: {root_file}")
        except Exception as e:
            print(f"Notice: Root log update skipped: {e}")

    return {
        "member": member_name.capitalize(),
        "user_count": user_count,
        "ai_count": ai_count,
        "total_count": user_count + ai_count,
        "last_export": now_ist,
        "rel_path": os.path.relpath(target_file, PROJECT_DIR)
    }

def generate_team_overview():
    conversations_base = os.path.join(PROJECT_DIR, "conversations")
    members_data = []

    if os.path.exists(conversations_base):
        for item in os.listdir(conversations_base):
            sub_path = os.path.join(conversations_base, item)
            if os.path.isdir(sub_path):
                log_file = os.path.join(sub_path, "Conversation_Log.md")
                if os.path.exists(log_file):
                    # Extract statistics from file
                    user_cnt = 0
                    ai_cnt = 0
                    last_exp = "Unknown"
                    try:
                        with open(log_file, "r", encoding="utf-8") as f:
                            content = f.read()
                            m_user = re.search(r"User.*?messages\*\*: (\d+)", content)
                            if m_user: user_cnt = int(m_user.group(1))
                            m_ai = re.search(r"AI Agent responses\*\*: (\d+)", content)
                            if m_ai: ai_cnt = int(m_ai.group(1))
                            m_exp = re.search(r"Last Export\*\*: (.*)", content)
                            if m_exp: last_exp = m_exp.group(1).strip()
                    except Exception:
                        pass
                    
                    members_data.append({
                        "name": item.capitalize(),
                        "folder": f"conversations/{item}/",
                        "user_cnt": user_cnt,
                        "ai_cnt": ai_cnt,
                        "total": user_cnt + ai_cnt,
                        "last_exp": last_exp,
                        "log_link": f"conversations/{item}/Conversation_Log.md"
                    })

    # Sort members by total messages descending
    members_data.sort(key=lambda x: x["total"], reverse=True)

    overview_parts = []
    overview_parts.append("# 🌐 SENTINEL Team — Master AI Synchronization & Activity Overview")
    overview_parts.append("> Centralized dashboard tracking active team members, conversation stats, and AI agent progress without Git collisions.")
    overview_parts.append("")
    overview_parts.append("## 👥 Active Team Members & Agent Conversation Logs")
    overview_parts.append("")
    overview_parts.append("| Member Name | Member Directory | Total Messages | User / AI Ratio | Last Active Export |")
    overview_parts.append("| :--- | :--- | :--- | :--- | :--- |")

    total_team_msgs = 0
    if members_data:
        for m in members_data:
            total_team_msgs += m["total"]
            overview_parts.append(f"| **[{m['name']}]({m['log_link']})** | `{m['folder']}` | {m['total']} | {m['user_cnt']} U / {m['ai_cnt']} AI | {m['last_exp']} |")
    else:
        overview_parts.append("| *No active member logs found yet* | - | 0 | - | - |")

    now_ist = datetime.now(timezone(timedelta(hours=5, minutes=30))).strftime("%d %b %Y, %I:%M %p IST")

    overview_parts.append("")
    overview_parts.append("---")
    overview_parts.append("## 📢 How Team Synchronization Works")
    overview_parts.append("""
1. **Isolated Member Folders**: Each team member (e.g. `siva`, `alex`, `priya`) exports conversation logs into `conversations/<member_name>/`.
2. **Zero Git Collisions**: Because everyone writes to their own subfolder, running `git push` and `git pull` will **never cause merge conflicts** on conversation logs!
3. **Seeing What's Happening**:
   - Read [TEAM_PROJECT_ACTIVITY.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/TEAM_PROJECT_ACTIVITY.md) for live feature updates.
   - Click on any team member link in the table above to view their agent's conversation log.
4. **Exporting Your Conversations**:
   Run this command in terminal when starting or finishing work:
   ```bash
   python scripts/export_conversation.py --member <your_name>
   ```
""")

    overview_parts.append("---")
    overview_parts.append("## 📊 Team Summary Metrics")
    overview_parts.append(f"- **Total Registered Members/Agents**: {len(members_data)}")
    overview_parts.append(f"- **Total Cumulative Messages across Team**: {total_team_msgs}")
    overview_parts.append(f"- **Dashboard Last Refreshed**: {now_ist}")
    overview_parts.append("")
    overview_parts.append("*Generated by scripts/export_conversation.py*")

    target_overview = os.path.join(conversations_base, "TEAM_OVERVIEW.md")
    try:
        with open(target_overview, "w", encoding="utf-8") as f:
            f.write("\n".join(overview_parts))
        print(f"✅ Generated Master Team Overview: {target_overview}")
    except Exception as e:
        print(f"⚠️ Failed to write team overview: {e}")

def main():
    parser = argparse.ArgumentParser(description="Export SENTINEL conversations per team member and generate team overview.")
    parser.add_argument("--member", type=str, default=None, help="Name of the team member (e.g. siva, alex, priya)")
    parser.add_argument("--brain-dir", type=str, default=DEFAULT_BRAIN_DIR, help="Path to Antigravity brain logs directory")
    args = parser.parse_args()

    # Determine member name
    member_name = args.member
    if not member_name:
        member_name = os.environ.get("SENTINEL_MEMBER_NAME")
    if not member_name:
        member_name = os.environ.get("USERNAME", os.environ.get("USER", "siva"))

    # Normalize member name
    member_name = re.sub(r"[^a-zA-Z0-9_-]", "", member_name.lower()) or "siva"

    print(f"🚀 Exporting SENTINEL conversation log for member: '{member_name}'...")
    print(f"📂 Brain Logs Source: {args.brain_dir}")

    export_member_conversation(member_name, args.brain_dir)
    generate_team_overview()

if __name__ == "__main__":
    main()
