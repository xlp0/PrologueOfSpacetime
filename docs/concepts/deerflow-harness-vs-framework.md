---
title: 'deerflow-harness-vs-framework'
date: 2026-06-27
tags: [Trivium-Logic, Seven-Liberal-Arts, deer-flow, bytedance, harness, super-agent, langgraph, open-source]
type: concept
sources: [Web research — DeerFlow 2.0 by bytedance (https://github.com/bytedance/deer-flow)]
status: stable
liberal_art: Trivium-Logic
---

# DeerFlow — Harness, Not Framework

## Insight
**DeerFlow** (Deep Exploration and Efficient Research Flow) is bytedance's open-source **Super Agent harness** — an opinionated runtime that gives an agent everything it needs to do real work: sandboxed execution, persistent memory, sub-agents, an extensible skill system, MCP tool integration, and multi-channel IM bridges. Hit #1 on GitHub Trending on Feb 28, 2026 after the 2.0 launch. **2.0 is a ground-up rewrite** (released June 15, 2026, 180 PRs) — v1 was a Deep Research framework; v2 made research just *one skill among many* and turned the runtime underneath into the actual product. 74.9k stars, MIT licensed.

The big distinction: a **framework** gives you abstractions and building blocks. A **harness** goes further: it packages the infrastructure an agent needs to plan, act, use tools, manage files, and operate across long tasks without you rebuilding the same plumbing each time.

This is the same thesis as [[agentic-harness-90-percent]] ("model = 10%, harness = 90%") and the same pattern as Hermes / Karpathy's LLM Wiki / Nick Milo's AIOS — DeerFlow just productionizes it as a Python SDK + reference app.

**Two-layer architecture:**

- **DeerFlow Harness** — the runtime layer (Python SDK + library). For teams building their own agent system or integrating DeerFlow into an existing product.
- **DeerFlow App** — the reference Super Agent application built on the Harness. For teams that want a ready-to-deploy product. Self-hostable.

One system, two entry points: Harness for builders, App for operators.

The 7 + 1 core concepts (harness / long-horizon agent / skill / sandbox / subagent / context engineering / memory / artifact) all hang off this distinction. Skills are loaded progressively to keep context lean (see [[static-vs-dynamic-context]]). Sub-agents get only what they need (see [[deerflow-lead-agent-dynamic-subagents]]). The sandbox gives the agent a real computer (see [[deerflow-sandbox-architecture]]).

## Context
From web research on the DeerFlow 2.0 release; the harness-vs-framework distinction is the central architectural argument.

## Related
- [[agentic-harness-90-percent]]
- [[deerflow-sandbox-architecture]]
- [[deerflow-lead-agent-dynamic-subagents]]
- [[hermes-persistent-memory]]
- [[InaAI]]
