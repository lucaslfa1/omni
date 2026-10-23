---
name: explain
description: X-ray any topic into a visual explainer, whether it is your project's architecture, a codebase, a concept, a technology, or a process, drawn as a diagram with checked facts. Use when the user asks to explain, map, or diagram something and wants the explanation itself rather than step-by-step tutoring (explain, how does X work, org chart, organograma, architecture map, explique), or types /explain. Skip it for one-line answers. When the user wants to be quizzed or guided to work it out, use a tutoring skill such as learn instead.
metadata:
  author: Lucas Felipe Afonso
  instagram: "@lucas_lfa"
---

# Explain

## Overview

Turns any topic into a page that explains it visually: a project, a codebase, a concept, a technology, a process, or a decision. The page gives the explanation outright instead of quizzing the user, and a diagram is its backbone. Facts are checked, and anything that could not be checked is marked.

**This skill only reads.** The only thing it writes is the explainer page itself. It never deploys, changes, or deletes anything. If the user asks for a deploy midway, treat that as a separate request that needs its own approval.

**When not to use it:**
- For a question with a one-line answer ("what port does Postgres use?"), answer in chat.
- If the user wants to be tutored, quizzed, or guided to work something out, use a tutoring skill such as `learn`, if one is installed.

## Pick the shape

| Topic | Diagram at the core |
|---|---|
| Project, system, deployment | Org chart: who decides → repository → environments → components (see **Project mode**) |
| Process, pipeline, request path | Left-to-right flow of steps |
| Layered concept (network stack, transformer) | Stacked layers |
| A vs. B | Side-by-side table |
| History, evolution | Timeline |
| Hierarchy, taxonomy | Tree |

## Steps

1. **Get the facts right.**
   - **Any topic:** stable, well-known knowledge is fine to use. Anything recent, version-specific, numeric, or contested needs a check against a primary source (official docs, the paper, the vendor's site) through web search or a connector, and a link to that source. Tag anything you cannot check `unverified`. Never invent numbers, dates, or quotes.
   - **Project mode:** every node needs a source you check during this run. Memory and the README tell you where to look, but they do not count as checks.
     - *With a terminal (Claude Code, Codex, Antigravity, and other coding agents):*
       - Repository: run `git remote -v`, then check the branch, `git status`, the last commit, and the top-level folders along with where each one deploys.
       - Hosting and cloud: use the CLI of whatever provider the project runs on, such as `aws`, `az`, `gcloud`, `firebase`, `vercel`, `netlify`, `fly`, or `kubectl`. Run only its list, describe, and status commands, never a command that changes state.
       - Live vs. main: compare what production is running (revision, deployment, image tag) with HEAD.
       - Access: send a request without logging in. A private service should answer 401 or 403.
     - *Without a terminal (claude.ai, ChatGPT, Gemini):* use the connectors (GitHub, Drive), the uploaded files, and the conversation.
     - *Secrets:* print only environment variable names. To check what a variable points to, compare inside the command without printing the value.
2. **Tag every node truthfully.**
   - Project: `live`, `N commits behind`, `blocked` (with the reason), `vision` (no code yet), `user decision`, `unverified`.
   - Other topics: `settled`, `debated`, `unverified`.
3. **Build the page** in HTML.
   - **In a chat app,** render the page where the app previews HTML: an artifact in claude.ai, canvas in ChatGPT, or canvas in Gemini.
   - **In Claude Code with the Artifact tool:** start with `action: "quickstart"` and `intent: "other"`.
   - **In a coding agent without an artifact tool** (most Claude Code installs, Codex, Antigravity, Cursor), write a single file named `explain-<topic>.html` in the current directory, unless the user names another place:
     - put all CSS and JS inline, so the file opens offline with no build step;
     - support light and dark mode with `prefers-color-scheme`, and make it work at phone width;
     - give the user the path, and open the file in the browser only if they ask.
   - Write in the user's language. If the project has CSS tokens or a brand book, reuse them.
   - Draw the diagram in plain HTML and CSS, and stack it vertically on mobile.
   - Sections:
     1. Header: the title, the date ("state as of DATE" for projects), and a one-sentence thesis.
     2. If the user asked a question, a short answer to it.
     3. The diagram.
     4. One short card per part: what it is, what it does, and why it matters.
     5. A worked example. For a project, the path one request takes. For anything else, one concrete case followed end to end.
     6. Pitfalls. For a project, list what is behind or blocked and the publish order, then add a table of folders and where each one ends up. For any other topic, list common misconceptions.
     7. Sources, except in project mode.
4. **Reply** with the link, the artifact, or the file path plus 3 to 5 lines, and offer to go deeper on any single part. To update the page, republish the same one.

## Common mistakes

| Mistake | Fix |
|---|---|
| Stating structure or facts from memory | Check first; if you can't, tag `unverified` |
| Quizzing the user instead of explaining | This skill explains outright; leave tutoring to a tutoring skill |
| A wall of text with a token diagram | The diagram carries the structure; prose stays short |
| Turning the explainer into a deploy | Read only, apart from the page; deploys and deletions need explicit approval |
| Printing an environment variable's value | Names only; compare without printing |
| Sharing a page with cloud IDs and handles | The page starts out private; warn the user before it is shared |
| Presenting everything as finished or settled | Mark vision vs. code, and debated vs. settled |
