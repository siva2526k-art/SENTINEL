# 🤖 SENTINEL Workspace Agent Rules & Automated Sync Protocol

## 🎯 Multi-Agent Team Collaboration Protocol

All AI Agents (Antigravity or equivalent) operating within the SENTINEL repository MUST observe the following rules:

1. **Automated Session Start Protocol**:
   - At the beginning of a coding session, the AI agent MUST execute:
     ```bash
     python scripts/sync_session.py --start
     ```
   - This automatically pulls the latest team changes from GitHub and displays the activity feed so the member and agent know what teammates worked on recently.

2. **Member Isolation for Conversation Exports**:
   - Never overwrite or merge directly into a central `SENTINEL_Conversation.md` file.
   - Always export conversation logs to `conversations/<member_name>/Conversation_Log.md` via `python scripts/sync_session.py --end --member <member_name>`.
   - This guarantees zero Git merge collisions when multiple team members work on the project simultaneously.

3. **Feature Activity Logging**:
   - Whenever completing a significant task, feature, or architectural change, append a brief entry to the top of [docs/TEAM_PROJECT_ACTIVITY.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/TEAM_PROJECT_ACTIVITY.md) under `## 🔔 Latest Activity Feed`.
   - Include: Timestamp (IST), Author/Agent, Components modified, and Key Changes.

4. **Automated Session End Protocol**:
   - At the end of a task or session, the AI agent MUST execute:
     ```bash
     python scripts/sync_session.py --end
     ```
   - This automatically exports conversation transcripts into `conversations/<member_name>/Conversation_Log.md`, updates `conversations/TEAM_OVERVIEW.md`, stages files, creates an organized Git commit, and pushes to GitHub.

5. **Zero-Trust & Privacy Alignment**:
   - All log parsing code or AI prompt templates developed within `src/` must adhere to the Zero-Trust Data Sanitizer guidelines defined in `src/sanitizer.py`.
