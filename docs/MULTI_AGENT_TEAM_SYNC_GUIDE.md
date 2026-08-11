# 🤝 SENTINEL Multi-Agent Team Synchronization Guide
> **How to collaborate with friends using Antigravity without Git conversation collisions or lost updates.**

---

## 💡 Overview & Automated Lifecycle

When multiple team members work on SENTINEL using AI agents (like Antigravity), each person's agent generates conversation logs and updates code/docs.

We have built an automated **Session Lifecycle Manager** (`scripts/sync_session.py`):
1. **Starting a Session (`--start`)**: Automatically pulls the latest team updates from GitHub and displays the activity feed so you know what teammates worked on.
2. **Closing a Session (`--end`)**: Automatically exports your agent's conversation log to your named member folder (`conversations/<member_name>/`), updates the master dashboard, creates an organized Git commit, and pushes to GitHub.

---

## 🛠️ Step-by-Step Instructions for Team Members

### 🟢 1. Starting Work with Antigravity
When you sit down to start working on SENTINEL, open your terminal and run:

```bash
python scripts/sync_session.py --start --member <your_name>
```
*Example for Priya*:
```bash
python scripts/sync_session.py --start --member priya
```

**What this does**:
- Runs `git pull` to fetch all latest features and logs from GitHub.
- Displays a summary of the latest team activity feed from `docs/TEAM_PROJECT_ACTIVITY.md`.

---

### 🟡 2. During Your Work Session
- Chat with Antigravity to build features, fix bugs, or write code.
- Instruct your agent when you complete a feature:
  > *"Update `docs/TEAM_PROJECT_ACTIVITY.md` with our new feature changes."*

---

### 🔴 3. Closing Your Work Session
When you finish your coding session, run:

```bash
python scripts/sync_session.py --end --member <your_name>
```
*Example for Priya*:
```bash
python scripts/sync_session.py --end --member priya
```

**What this does automatically**:
1. Exports your agent's chat history into `conversations/priya/Conversation_Log.md`.
2. Updates `conversations/TEAM_OVERVIEW.md`.
3. Stages and creates an organized Git commit: `docs(sync): update logs & team activity for Priya`.
4. Runs `git push origin main` to publish your updates to GitHub.

---

## 🔍 Checking What Friends Are Doing

1. Open [conversations/TEAM_OVERVIEW.md](file:///c:/Users/siva2/Projects/SENTINEL/conversations/TEAM_OVERVIEW.md) to see active team members, message counts, and direct links to their logs.
2. Open [docs/TEAM_PROJECT_ACTIVITY.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/TEAM_PROJECT_ACTIVITY.md) to view the chronological log of all features written by team members and their AI agents.
