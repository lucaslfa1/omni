# omni

Agent skills by Lucas Felipe Afonso ([@lucas_lfa](https://www.instagram.com/lucas_lfa/)). Website: https://lucaslfa1.github.io/omni/

| Skill | What it does |
|---|---|
| `explain` | X-ray any topic into a visual explainer: your project's architecture, a codebase, a concept, a technology, or a process, drawn as a diagram with checked facts. |

Each skill comes in two forms: a standalone skill that works in any app or agent that supports the open Agent Skills format (`standalone/`), and the omni plugin for Claude Code (`skills/`, called as `/omni:explain`).

## Install

| Where | How |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add lucaslfa1/omni`, then `/plugin install omni@omni` |
| Codex, Antigravity CLI, Cursor, and other agents | `npx skills add lucaslfa1/omni --skill explain` |
| claude.ai, ChatGPT, Gemini app | Download [explain.zip](https://github.com/lucaslfa1/omni/releases/latest/download/explain.zip), then upload it on the app's Skills page |

## What it does when it runs

explain contains no code that runs on its own. It is a set of instructions that the agent follows:

- It reads what it needs to explain the topic: files in your repository, `git` status, and read-only status commands of the hosting CLI you already use (list and describe, never commands that change anything).
- It may search the web to check recent or numeric facts, and it links every source it uses.
- It writes one thing, the explainer page: an artifact or canvas in chat apps, or a single self-contained HTML file in coding agents.
- It sends no data anywhere, collects nothing, and never deploys, changes, or deletes anything.

## License

MIT © Lucas Felipe Afonso
