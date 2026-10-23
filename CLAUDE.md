# omni

A plugin and skill pack, and its own project. The skills belong to omni.

## Two versions of each skill

| Version | Source | Where it goes |
|---|---|---|
| Standalone `explain` | `standalone/explain/SKILL.md` | claude.ai, ChatGPT, the Gemini app, and `~/.agents/skills` (Codex, Antigravity) |
| Plugin `omni:explain` | `skills/explain/SKILL.md` | The omni plugin for Claude Code |

- **Standalone:** the initial, generic version, made for promotion. It is free and public, a showcase for the author. Keep names, cloud IDs, and environment details from the author's other projects out of it.
- **Plugin:** omni's own version. It started identical to the standalone one and may grow beyond it. Decide each time whether a change goes into one version or both.

## Workflow

- **After editing the standalone version:**
  1. Run `python scripts/build.py --install`.
  2. Upload `dist/<name>.zip` to claude.ai, ChatGPT, and the Gemini app. claude.ai asks before replacing and keeps a version history. In ChatGPT and Gemini, replacing means editing or recreating the skill there.
- **After editing the plugin version:** run `claude plugin validate . --strict`.

## Rules

- Repo: https://github.com/lucaslfa1/omni (public, MIT).
- `npx skills add` finds only one `explain`, even though `skills/` and `standalone/` both have one. When the two versions diverge, check which folder it installs from.
- Skills are written in English. Descriptions also carry Portuguese trigger words (organograma, explique).
- Author: `metadata.author` and `metadata.instagram` in every `SKILL.md`, and the `author` field in `.claude-plugin/plugin.json`. The Gemini app's form drops `metadata`.
- Reply to the author in Brazilian Portuguese.
- Use names exactly as the author picks them.
- Push and publish only with the author's explicit OK.
