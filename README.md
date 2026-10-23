# omni

Agent skills by Lucas Felipe Afonso ([@lucas_lfa](https://www.instagram.com/lucas_lfa/)).

| Skill | What it does |
|---|---|
| `explain` | X-ray any topic into a visual explainer: your project's architecture, a codebase, a concept, a technology, or a process, drawn as a diagram with checked facts. |

Each skill comes in two forms: a standalone skill that works in any app or agent that supports the open Agent Skills format (`standalone/`), and the omni plugin for Claude Code (`skills/`, called as `/omni:explain`).

## Install

| Where | How |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add lucaslfa1/omni`, then `/plugin install omni@omni` |
| Codex, Antigravity CLI, Cursor, and other agents | `npx skills add lucaslfa1/omni --skill explain` |
| claude.ai, ChatGPT, Gemini app | Download `standalone/explain` as a zip, then upload it on the app's Skills page |

## License

MIT © Lucas Felipe Afonso
