# ECO Documents

Documents migrated from Notion to Obsidian for the ECO Tokamak Economics team.

## Obsidian Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/tokamak-network/ECO-documents.git
```

### 2. Open as Obsidian Vault

1. Open Obsidian
2. Select **Open folder as vault**
3. Choose the cloned `ECO-documents` folder

### 3. Install Obsidian Git Plugin (Team Sync)

1. Obsidian → Settings → Community plugins → **Turn on community plugins**
2. Browse → Search **Obsidian Git** (by [Vinzent03](https://github.com/Vinzent03/obsidian-git)) → Install → Enable
3. Plugin settings:
   - **Auto pull interval**: `5` (pulls latest changes every 5 minutes)
   - **Auto push interval**: `5` (pushes your changes every 5 minutes)
   - **Pull on startup**: Enable

### 4. Usage

- Obsidian Git automatically commits and pushes your edits
- Changes from other team members are pulled automatically
- Manual sync: `Ctrl+P` (Mac: `Cmd+P`) → "Obsidian Git: Pull" or "Push"

### Notes

- Avoid editing the same file simultaneously to prevent merge conflicts.
- Personal settings in `.obsidian/` are excluded from the repo via `.gitignore`.
