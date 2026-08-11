# 🤝 SENTINEL Multi-Agent Team Synchronization Guide
> **How to collaborate with friends using Antigravity without Git conversation collisions or lost updates.**

---

## 💡 Overview

When multiple team members work on SENTINEL using AI agents (like Antigravity), each person's agent generates conversation logs and updates code/docs. 

If all agents wrote to a single `SENTINEL_Conversation.md` file, committing to Git would cause **nasty merge conflicts**!

**The Solution**:
1. **Isolated Member Folders**: Each teammate exports conversation logs into `conversations/<member_name>/`.
2. **Zero Collision Git Workflow**: `git push` and `git pull` cleanly merge because everyone owns their own folder.
3. **Master Dashboard**: `conversations/TEAM_OVERVIEW.md` automatically aggregates stats and links to everyone's logs.
4. **Feature Activity Feed**: `docs/TEAM_PROJECT_ACTIVITY.md` lets everyone see what features each friend's AI agent built.

---

## 🛠️ Step-by-Step Instructions for Friends & Teammates

### Step 1: Clone or Pull the SENTINEL Repository
```bash
git pull origin main
```

### Step 2: Set Your Member Name (Optional but Recommended)
Set an environment variable or pass your name directly to the export script:
- **On Windows (PowerShell)**:
  ```powershell
  $env:SENTINEL_MEMBER_NAME="alex" # Replace 'alex' with your name
  ```
- **On Windows (Command Prompt)**:
  ```cmd
  set SENTINEL_MEMBER_NAME=alex
  ```

### Step 3: Run the Conversation Exporter
At any point during or after your work session with Antigravity, run:
```bash
python scripts/export_conversation.py --member <your_name>
```
*Example*:
```bash
python scripts/export_conversation.py --member alex
```

**What this does automatically**:
- Creates `conversations/alex/Conversation_Log.md` with your agent's exact chat history.
- Scans all member folders and regenerates `conversations/TEAM_OVERVIEW.md`.

### Step 4: Log New Features in `docs/TEAM_PROJECT_ACTIVITY.md`
Whenever you or your Antigravity agent implement a new feature or fix a bug, instruct your agent:
> *"Update `docs/TEAM_PROJECT_ACTIVITY.md` with our latest feature changes under the Latest Activity Feed."*

### Step 5: Commit and Push to GitHub
```bash
git add .
git commit -m "feat: updated alex conversation log and privacy sanitizer rules"
git push origin main
```

Because your logs are in `conversations/alex/`, your push will succeed smoothly without merge conflicts!

---

## 🔍 How to See What Teammates Are Doing

1. Open [conversations/TEAM_OVERVIEW.md](file:///c:/Users/siva2/Projects/SENTINEL/conversations/TEAM_OVERVIEW.md) to see live message counts, active team members, and direct links to their logs.
2. Open [docs/TEAM_PROJECT_ACTIVITY.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/TEAM_PROJECT_ACTIVITY.md) to view the chronological log of all feature updates written by team members and their AI agents.
3. Open any friend's log (e.g. `conversations/siva/Conversation_Log.md`) to read their agent's prompts and responses.
