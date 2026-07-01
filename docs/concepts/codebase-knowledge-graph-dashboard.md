---
title: 'codebase-knowledge-graph-dashboard'
date: 2026-06-26
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, knowledge-graph, codebase-onboarding, dashboard, guided-tour, understand-anything]
type: concept
sources: [YouTube — Understand-Anything Claude Code Plugin (https://www.youtube.com/watch?v=xkQ9HvGTMpc)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Codebase Knowledge Graph Dashboard

## Insight
The payoff of Understand Anything's analysis pipeline is the dashboard it launches: a force-directed knowledge graph where nodes cluster by community (files that import each other stay close), color-coded by architectural layer (amber = core engine, violet = agent pipeline, teal = skills, etc.). Click any node → plain-English summary, complexity rating, tags, all edges.

Two features lift this above a static graph view:

**Auto-generated guided tour, ordered by dependency** — the dashboard literally teaches you the codebase. Rather than dumping you into a graph and saying "explore," it walks you through dependencies in the order you'd need to understand them. This is a non-trivial UX move; most knowledge-graph tools assume you already know what to look for.

**Domain view** — switch from files (technical) to business processes / domains / flows / steps (semantic). Same graph, two lenses. This matters because the question "what does this code do?" is a different question from "what file is this function in?" and a good code-comprehension tool should answer both.

The 8 commands wrap the dashboard: `/understand` runs analysis, `/understand chat` lets Claude reason from the graph (with file refs), `/understand diff` shows ripple effects of a change (which modules depend on X), and so on.

The reusable pattern: **graph + community clustering + layer color-coding + node-detail pane + dependency-ordered tour + dual file/domain lenses**. That's the architecture, and any tool trying to do "AI-readable codebase overview" should hit most of these — see [[graphify-codebase-knowledge-graph]] for the lighter-weight version that stops at the graph and skips the dashboard.

## Context
From the "Understand-Anything Claude Code Plugin" walkthrough; the dashboard is what differentiates Understand-Anything from [[graphify-codebase-knowledge-graph]].

## Related
- [[understand-anything-multi-agent-pipeline]]
- [[graphify-codebase-knowledge-graph]]
- [[agentic-os-shared-brain]]
- [[visual-graph-layer-second-brain]] — same dashboard pattern ported from codebase to business knowledge
- [[InaAI]]
