---
title: 'five-levels-second-brain'
date: 2026-06-28
tags: [Quadrivium-Arithmetic, Seven-Liberal-Arts, second-brain, claude-code, semantic-search, knowledge-graph, framework]
type: concept
sources: [YouTube — Every Level of a Claude Second Brain Explained (https://youtu.be/DTCyvo6cC54)]
status: stable
liberal_art: Quadrivium-Arithmetic
---

# Five Levels of a Second Brain

## Insight
A second brain is not one architecture — it's a ladder of five retrieval mechanisms, each solving a distinct failure mode of the level below it. The levels are defined by the *question they answer*, not by the tool they use.

- **Level 1 — exact word/file match.** A `claude.md` (or `agents.md`) at the vault root, plus folders. The root file is treated as a router: "if you need info about me, look here; if you need Q1 priorities, look here." Works until the vault grows too big to feel intuitive, at which point files start to feel ignored.
- **Level 2 — topic aggregation.** Add an LLM Wiki (see [[karpathy-llm-wiki-vs-rag]]) plus `references/` and `memory.md`. Now the agent can pull everything on a topic together instead of grepping for one word. Auto-memory in Claude Code keeps `memory.md` updated without human intervention.
- **Level 3 — semantic search.** Vectorize chunks of the data that benefits from meaning-based retrieval (Pinecone, Supabase, Qdrant). The agent finds notes you wrote even when your search used different words. The catch: vector retrieval breaks on questions that need full-context reasoning (see [[vector-retrieval-chunking-limit]]).
- **Level 4 — relationship chains.** Knowledge graph with typed edges: "Jordan works at Acme; Acme is endorsed by Postpilot; Postpilot competes with Cadently." Now you can ask "topic X" and trace it back to "topic A" through the relationship graph. Distinct from wiki backlinks (see [[wiki-backlinks-vs-kg-edges]]).
- **Level 5 — always-on Brain OS.** Gbrain (Garry Tan's tool, paired with Gstack) and Hermes (see [[hermes-persistent-memory]]) keep memory constantly syncing and refreshing in the background. Autonomous ingestion rather than human-triggered.

The non-obvious rule: **level 5 is not the goal.** Pick the *lowest* level that fixes your current pain. If you have no pain at level 2, building a knowledge graph is waste. The video's author sits his entire Herc 2 project at level 2 because routing files plus the LLM Wiki already cover his project-based content work — a CRM-heavy business would justify level 4, a 24/7 agent fleet would justify level 5.

A single project can also mix levels: this folder at level 2, that folder at level 3, another at level 4. The decision is per-data-type, not per-vault.

## Context
From "Every Level of a Claude Second Brain Explained"; the five-level framing is the spine of the entire video. Author's working setup is level 2 (Herc 2 project), with level 5 (Gbrain + Hermes) being experimented with but not in daily use.

## Related
- [[second-brain-obsidian-foundations]] — Level 1-2 foundations
- [[second-brain-business-os-wiring]] — Level 5 territory (always-on sub-agents + MCP)
- [[karpathy-llm-wiki-vs-rag]] — Level 2 LLM Wiki pattern
- [[hermes-persistent-memory]] — Level 5 runtime mirror
- [[InaAI]]
