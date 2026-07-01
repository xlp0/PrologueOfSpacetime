---
title: 'second-brain-obsidian-foundations'
date: 2026-06-26
tags: [Trivium-Grammar, Seven-Liberal-Arts, second-brain, obsidian, claude-code, karpathy, business-os, markdown]
type: concept
sources: [YouTube — How To Build The Ultimate AI Second Brain (Claude Code + Obsidian) (https://www.youtube.com/watch?v=C6b1bX1HNg8)]
status: stable
liberal_art: Trivium-Grammar
---

# Second Brain — Obsidian Foundations

## Insight
The recipe for a $40k-style **AI second brain**: an Obsidian vault of `.md` files that Claude Code reads, organizes, and queries. The concept was popularized by Andrej Karpathy (now at Anthropic).

**Why markdown files:**

- Cheap to ingest.
- Low token cost.
- Queryable by any LLM (Claude, Codex, Gemini) — no vendor lock-in.

**Suggested folder structure** (with a `readme.md` in each so any AI knows what each folder is for):

- `inbox/` — raw capture (emails, files, meetings).
- `contacts/`.
- `wiki/` — the actual second brain.
- `projects/`.
- `skills/`.
- `meta/`.

Add a `claude.md` at root: who you are, your businesses, the vault map, rules.

**Building the brain:**

1. Use Claude Code to create the folders + write readmes for each.
2. Dump raw `.md` files into `inbox/` (meeting notes, etc.).
3. Prompt Claude: "read everything in `inbox/`, turn each into a clean linked wiki note in `wiki/`. Cite source files. One note per document."
4. Claude processes inbox → writes structured notes into `wiki/` with backlinks.
5. Use Obsidian's **graph view** to watch the brain grow.

The pattern: the vault *is* the harness Google describes (see [[agentic-harness-90-percent]]). Structured context the agent reads instead of re-skimming every session. Same as [[graphify-codebase-knowledge-graph]] but for personal knowledge instead of code, and same as [[karpathy-llm-wiki-vs-rag]] but framed as a business OS rather than a learning wiki.

The foundations are deliberately simple: a folder of markdown files, a `claude.md` schema, an inbox-to-wiki pipeline. That's the floor. The ceiling (see [[second-brain-business-os-wiring]]) is connecting it to Gmail/Calendar/Drive via MCP and running scheduled sub-agents on it.

## Context
From the "How To Build The Ultimate AI Second Brain" recipe; the foundations layer of the business-OS pitch.

## Related
- [[second-brain-business-os-wiring]]
- [[karpathy-llm-wiki-vs-rag]]
- [[graphify-codebase-knowledge-graph]]
- [[nick-milo-aios-three-layers]]
- [[five-levels-second-brain]] — this is the Level 1-2 floor of the five-level ladder
- [[claude-md-routing-rules]] — claude.md as router, not just schema
- [[reverse-engineer-data-shape]] — the design principle behind folder shape
- [[visual-graph-layer-second-brain]] — a visual graph rendered on top of this foundation
- [[InaAI]]
