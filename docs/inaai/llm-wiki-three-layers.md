---
concept: llm-wiki-three-layers
tags: [karpathy, llm-wiki, obsidian, claude-code, three-layers, schema]
source: YouTube — Karpathy's LLM Wiki - Full Beginner Setup Guide (https://www.youtube.com/watch?v=iXd0t60YmMw)
date: 2026-06-27
---

# LLM Wiki Three Layers

## Insight
Karpathy's LLM Wiki has three layers (see [[karpathy-llm-wiki-vs-rag]] for the why):

1. **Raw sources** (read-only) — PDFs, articles, meeting notes. The AI reads but never modifies. Your source of truth.
2. **The wiki** — a folder of markdown files the AI creates and maintains: index page, concept pages, entity pages, comparison pages, all interlinked.
3. **The schema** — a rules document telling the AI how to structure the wiki, handle new sources, and format pages. In Claude Code this is `claude.md`.

The separation matters. Raw sources are read-only so the AI can't rewrite your source of truth. The wiki is AI-maintained so the synthesis work happens once. The schema is the contract that keeps the wiki structured — without it, the AI drifts into inconsistent page formats, broken links, and orphan notes.

This is the same three-layer pattern as [[nick-milo-aios-three-layers]] (Ideaverse / translation layer / external AI) and the same logic as the [[second-brain-obsidian-foundations]] folder structure (`inbox/` / `wiki/` / `claude.md`). All three are saying: separate the source of truth from the AI-generated synthesis, and use a schema file as the contract.

**Setup steps:**

- Install **Obsidian** (free, obsidian.md) — used as the viewer for the markdown files. VS Code or any text editor also works; Obsidian's graph view is the payoff.
- Install an AI coding agent — **Claude Code** (used in the demo), but Codex, Cursor, or anything that reads/writes files works.
- Create a new Obsidian vault (just a folder) — e.g. `LLM wiki`.
- Inside it, create three folders: `raw/`, `wiki/`, `templates/` (templates is optional — only if you want to manually author notes).
- Drop a `claude.md` schema file in the vault root. The only line you must customize is the **purpose** (e.g. "planning a trip to Japan" → "researching renewable energy"). The rest covers folder structure, ingest workflow, page formatting rules, and Q&A behavior.
- Install the **Obsidian Web Clipper** Chrome extension — converts web articles into markdown files you can drop into `raw/`.

Pair with [[llm-wiki-lint-pass]] for keeping the wiki healthy as it scales.

## Context
From "Karpathy's LLM Wiki - Full Beginner Setup Guide"; the three-layer setup is the architecture section of the video.

## Related
- [[karpathy-llm-wiki-vs-rag]]
- [[llm-wiki-lint-pass]]
- [[nick-milo-aios-three-layers]]
- [[second-brain-obsidian-foundations]]
- [[InaAI]]
