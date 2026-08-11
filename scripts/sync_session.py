# -*- coding: utf-8 -*-
"""
sync_session.py
Automated Start & End Session Lifecycle Manager for SENTINEL

Automates pulling team updates when starting an AI session with Antigravity,
and exports, organizes, commits, and pushes updated logs when closing the session.

Usage:
  python scripts/sync_session.py --start [--member <name>]
  python scripts/sync_session.py --end [--member <name>] [--commit-msg "optional summary"]
"""

import os
import sys
import io
import argparse
import subprocess
import re
from datetime import datetime, timezone, timedelta

# Safely set UTF-8 output encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_DIR)

# Import exporter module functions
from scripts.export_conversation import export_member_conversation, generate_team_overview, DEFAULT_BRAIN_DIR

def run_git_cmd(cmd_list, cwd=PROJECT_DIR, ignore_error=False):
    """Run a git command and return stdout string."""
    try:
        res = subprocess.run(
            cmd_list,
            cwd=cwd,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        if res.returncode != 0 and not ignore_error:
            if res.stderr.strip():
                print(f"⚠️ Git Notice: {res.stderr.strip()}")
        return res.stdout.strip()
    except Exception as e:
        if not ignore_error:
            print(f"⚠️ Git Execution Error: {e}")
        return ""

def get_ist_time():
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist).strftime("%d %b %Y, %I:%M %p IST")

def handle_start_session(member_name):
    print("=" * 70)
    print(f"🚀 STARTING SENTINEL AI WORK SESSION — Member: '{member_name.capitalize()}'")
    print("=" * 70)
    print("📥 Pulling latest updates from GitHub (team logs & features)...")

    # 1. Attempt git pull
    pull_output = run_git_cmd(["git", "pull", "origin", "main"], ignore_error=True)
    if not pull_output:
        pull_output = run_git_cmd(["git", "pull"], ignore_error=True)

    if pull_output:
        print(f"✅ Git Pull Status: {pull_output}")
    else:
        print("ℹ️ Git workspace clean / local mode.")

    # 2. Display recent activity feed from docs/TEAM_PROJECT_ACTIVITY.md
    activity_file = os.path.join(PROJECT_DIR, "docs", "TEAM_PROJECT_ACTIVITY.md")
    if os.path.exists(activity_file):
        print("\n🔔 Latest Team Activity Feed:")
        print("-" * 50)
        try:
            with open(activity_file, "r", encoding="utf-8") as f:
                content = f.read()
                feed_idx = content.find("## 🔔 Latest Activity Feed")
                if feed_idx != -1:
                    feed_text = content[feed_idx + len("## 🔔 Latest Activity Feed"):].strip()
                    lines = feed_text.splitlines()
                    snippet = "\n".join(lines[:15])
                    print(snippet)
        except Exception as e:
            print(f"Notice: Could not read activity feed: {e}")
        print("-" * 50)

    print(f"\n💡 Workspace Ready! Your Antigravity session will log to: conversations/{member_name.lower()}/")
    print("👉 At the end of your session, run: python scripts/sync_session.py --end")
    print("=" * 70)

def handle_end_session(member_name, brain_dir, custom_commit_msg=None, push_to_git=True):
    print("=" * 70)
    print(f"🛑 CLOSING SENTINEL AI WORK SESSION — Member: '{member_name.capitalize()}'")
    print("=" * 70)

    # 1. Export conversation transcript to conversations/<member_name>/
    print(f"📦 Step 1: Exporting conversation transcript to conversations/{member_name.lower()}/...")
    res = export_member_conversation(member_name, brain_dir)

    # 2. Regenerate master team overview
    print("📊 Step 2: Regenerating master team overview (conversations/TEAM_OVERVIEW.md)...")
    generate_team_overview()

    # 3. Stage and commit changes in Git if repository exists
    print("🧹 Step 3: Organizing and committing updated logs...")
    
    status_output = run_git_cmd(["git", "status", "--porcelain"])

    if status_output:
        member_folder = f"conversations/{member_name.lower()}/"
        run_git_cmd(["git", "add", member_folder])
        run_git_cmd(["git", "add", "conversations/TEAM_OVERVIEW.md"])
        run_git_cmd(["git", "add", "docs/TEAM_PROJECT_ACTIVITY.md"])
        run_git_cmd(["git", "add", "docs/MULTI_AGENT_TEAM_SYNC_GUIDE.md"])
        run_git_cmd(["git", "add", ".agents/"])
        run_git_cmd(["git", "add", "scripts/"])

        now_str = get_ist_time()
        commit_msg = custom_commit_msg or f"docs(sync): update logs & team activity for {member_name.capitalize()} [{now_str}]"

        commit_res = run_git_cmd(["git", "commit", "-m", commit_msg])
        print(f"✅ Local Commit Created: '{commit_msg}'")

        if push_to_git:
            print("🚀 Step 4: Pushing organized updates to GitHub...")
            push_res = run_git_cmd(["git", "push", "origin", "main"], ignore_error=True)
            if not push_res:
                push_res = run_git_cmd(["git", "push"], ignore_error=True)
            
            if push_res:
                print(f"🎉 Successfully Pushed to GitHub!\n{push_res}")
            else:
                print("ℹ️ Note: Local commit saved. Pushing will execute once GitHub remote is linked.")
    else:
        print("✨ Everything up to date! No unsaved changes detected.")

    print("\n✅ Session successfully closed & synchronized!")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="SENTINEL Start/End Work Session Manager")
    parser.add_argument("--start", action="store_true", help="Start session: pull latest team data and show activity")
    parser.add_argument("--end", action="store_true", help="End session: export logs, rebuild overview, commit & push")
    parser.add_argument("--member", type=str, default=None, help="Member name (e.g., siva, alex, priya)")
    parser.add_argument("--commit-msg", type=str, default=None, help="Custom commit message for end session")
    parser.add_argument("--no-push", action="store_true", help="Skip pushing to git remote on end session")
    parser.add_argument("--brain-dir", type=str, default=DEFAULT_BRAIN_DIR, help="Path to Antigravity brain dir")

    args = parser.parse_args()

    member_name = args.member
    if not member_name:
        member_name = os.environ.get("SENTINEL_MEMBER_NAME")
    if not member_name:
        member_name = os.environ.get("USERNAME", os.environ.get("USER", "siva"))

    member_name = re.sub(r"[^a-zA-Z0-9_-]", "", member_name.lower()) or "siva"

    if args.start:
        handle_start_session(member_name)
    elif args.end:
        handle_end_session(member_name, args.brain_dir, custom_commit_msg=args.commit_msg, push_to_git=not args.no_push)
    else:
        print("💡 Usage:")
        print("  python scripts/sync_session.py --start [--member <name>]")
        print("  python scripts/sync_session.py --end [--member <name>]")

if __name__ == "__main__":
    main()
