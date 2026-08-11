# 🤖 SENTINEL Workspace Agent Rules & Sync Protocol

## 🎯 Multi-Agent Team Collaboration Rules

All AI Agents (Antigravity or equivalent) operating within the SENTINEL repository MUST observe the following rules:

1. **Member Isolation for Conversation Exports**:
   - Never overwrite or merge directly into a central `SENTINEL_Conversation.md` file if a member-specific folder is used.
   - Always run `python scripts/export_conversation.py --member <member_name>` to place conversation logs into `conversations/<member_name>/Conversation_Log.md`.
   - This ensures zero Git merge collisions when multiple team members work on the project simultaneously.

2. **Feature Activity Logging**:
   - Whenever completing a significant task, feature, or architectural change, append a brief entry to the top of `docs/TEAM_PROJECT_ACTIVITY.md` under `## 🔔 Latest Activity Feed`.
   - Include: Timestamp (IST), Author/Agent, Components modified, and Key Changes.

3. **Master Dashboard Updates**:
   - The master dashboard at `conversations/TEAM_OVERVIEW.md` is automatically maintained by `scripts/export_conversation.py`.

4. **Zero-Trust & Privacy Alignment**:
   - All log parsing code or AI prompt templates developed within `src/` must adhere to the Zero-Trust Data Sanitizer guidelines defined in `src/sanitizer.py`.
