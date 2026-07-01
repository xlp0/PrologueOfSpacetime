---
title: 'graphify-codebase-knowledge-graph'
date: 2026-06-26
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, graphify, claude-code, knowledge-graph, codebase, cost-saving, agentic-os]
type: concept
sources: [YouTube — Claude Code + Graphify = Insane Agentic OS (https://www.youtube.com/watch?v=Owv503rTqYY)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Graphify — Codebase Knowledge Graph

## Insight
**Graphify** is a skill that builds a **knowledge graph** of any project so Claude Code can query relationships instead of re-reading the whole repo every conversation. Saves tokens, cost, and time.

The map metaphor: every codebase is like a foreign country; without the map you have to translate/re-learn it each conversation. Graphify gives Claude that map. It reads (not summarizes), clusters into modules, ranks **"god nodes"** (load-bearing files), and labels **facts** vs **guesses**. Result: Claude answers from summaries instead of re-skimming the whole repo every turn.

What the map enables:

- **Instant orientation** — understand any new repo (ClaudeBot, Hermes, etc.) immediately.
- **Grounded answers** — no hallucinations; Claude reasons from the actual graph.
- **Blast-radius analysis** — see every dependency of a file before editing it.
- **Query instead of grep** — ask questions instead of searching flat code.
- **Always fresh** — re-index on demand.
- **Beyond code** — understands intent, not just source files.

Setup: copy the Graphify install snippet from the GitHub repo. In Claude Code: "clone this repo, open `<project>` as a test, open the Graphify window." Claude downloads + indexes the project. Query: "summarize what this repo is using the Graphify skill."

The token economics are the load-bearing argument. Without the map: Claude either re-skims the whole repo each conversation (expensive) or sits in context (token bloat). With the map: answers from summaries; **every session compounds**. Saving = no re-reading tax.

This is a lighter-weight version of [[understand-anything-multi-agent-pipeline]] (which adds a dashboard and a multi-agent analysis pipeline). Graphify stops at the graph + query layer; Understand-Anything adds the [[codebase-knowledge-graph-dashboard]]. Both are concrete instantiations of [[agentic-harness-90-percent]] — the graph is harness, the model is swappable.

## Context
From the "Claude Code + Graphify = Insane Agentic OS" walkthrough; Graphify is the skill that builds the codebase knowledge graph.

## Related
- [[agentic-os-shared-brain]]
- [[understand-anything-multi-agent-pipeline]]
- [[agentic-harness-90-percent]]
- [[wiki-backlinks-vs-kg-edges]] — typed edges vs untyped backlinks, in the personal-knowledge domain
- [[InaAI]]
