---
concept: me-md-vault-map-skill-map
tags: [nick-milo, ai-os, me-md, vault-map, skill-map, identity, future-proofing]
source: YouTube — How I Use Obsidian + Claude Cowork to Run My Life (https://youtu.be/rRa9td4oe7k)
date: 2026-06-27
---

# me.md, vault map, skill map

## Insight
The three load-bearing files in Nick Milo's AIOS (see [[nick-milo-aios-three-layers]]):

**`me.md`** — portable identity for any AI ("here's who I am, how I think, how I want you to work with me"). Not Claude-specific. The point: it's *portable*. You write it once, point any AI at it, and the AI knows who you are. Compare to the Claude-specific `Claude.md` convention — Nick keeps `Claude.md` at the root with one line: "go read me.md." That way you don't get locked into Claude's `CLAUDE.md` convention; you can re-point Codex/Gemini/local at the same `me.md` and they all read your identity.

**`vault map`** — master TOC. Without it, AI "samples" 17,000 notes and lies about having read them. With it, AI isolates the relevant files, loads them into context, skips the rest. This is the index pattern — same logic as [[graphify-codebase-knowledge-graph]] (map once, query from anywhere) and [[agentic-os-shared-brain]] (shared brain, swappable readers). The vault map is the personal-knowledge version of a codebase knowledge graph. Also the routing-rule substrate — see [[claude-md-routing-rules]] for how `claude.md`/`agents.md` point the agent at files like this.

**`skill map`** — index of skills with explicit "when to use" rules. Skills live in your vault, not in Claude — use AI to write/review them, but storage stays yours. This is [[skills-sh-markdown-spec]] with an extra layer: not just the skill files, but an index of which skill is for what. The skill map is what makes dynamic context (see [[static-vs-dynamic-context]]) actually work — without the map, the agent doesn't know which skill to grab for which situation.

The pattern across all three: **portability over specificity.** Don't write a `Claude.md` that only Claude reads; write a `me.md` any AI can read. Don't store skills in Claude's internal memory; store them as markdown in your vault. Don't let the AI sample your whole vault; give it a map. The files are the moat; the model is the swappable part.

Pair with [[session-start-prompt-pattern]] for the workflow that loads these three files at the start of every chat.

## Context
From Nick Milo's "How I Use Obsidian + Claude Cowork to Run My Life"; the three maps are the load-bearing piece of the AIOS architecture.

## Related
- [[nick-milo-aios-three-layers]]
- [[session-start-prompt-pattern]]
- [[agentic-os-shared-brain]]
- [[skills-sh-markdown-spec]]
- [[InaAI]]
