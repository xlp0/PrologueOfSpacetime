---
concept: deerflow-lead-agent-dynamic-subagents
tags: [deer-flow, lead-agent, subagents, dynamic, orchestration, langgraph]
source: Web research — DeerFlow 2.0 by bytedance (https://github.com/bytedance/deer-flow)
date: 2026-06-27
---

# DeerFlow — Lead Agent + Dynamic Subagents

## Insight
Earlier agent systems modeled work as a **fixed graph of specialized roles**. Rigid, hard to extend — adding a new capability meant redesigning the orchestration graph. DeerFlow 2.0 moved to **lead agent + middleware + dynamically invoked subagents**. New capabilities become new skills / tools / runtime policies instead of requiring orchestration-graph redesign.

This mirrors Google's "one generalist agent + skills > zoo of specialists" — see [[static-vs-dynamic-context]].

The sub-agent contract: a focused worker for a delegated subtask. **Isolation is the point** — doesn't inherit parent context, gets only what it needs. Default `max_turns=150`, timeout 30 min. Token usage attributed back to dispatcher.

Why this matters: in a fixed-graph system, every specialist is a permanent cost — its context, its prompt, its tool surface, its coordination overhead, all paid whether or not the specialist is needed this run. In a dynamic-subagent system, you only pay for the subagent when it's actually dispatched. The capability is available without being permanently loaded.

The sub-agent also functions as a **context-management tool**, not just a parallelism tool. The lead agent's context stays lean because heavy lifting happens in isolated workers. Results come back as summaries, not as full transcripts. This is the same pattern as [[hermes-background-subagents]] and [[hermes-sub-agents]] — isolated workers, each with its own focus, results assembled by the lead.

The long-horizon-agent primitive makes this work: built for chains of actions, not single Q&A. Must decide next step, track intermediate state, store work outside context (in the sandbox filesystem — see [[deerflow-sandbox-architecture]]), recover from complexity, return a reviewable artifact. The lead agent isn't a stateless orchestrator — it's a stateful coordinator with persistent working memory.

Pair with [[plan-build-eval-review-split]] for the workflow shape, and [[deerflow-harness-vs-framework]] for the harness this all sits inside.

## Context
From web research on the DeerFlow 2.0 release; the architectural-shift section of the docs.

## Related
- [[deerflow-harness-vs-framework]]
- [[deerflow-sandbox-architecture]]
- [[static-vs-dynamic-context]]
- [[hermes-background-subagents]]
- [[InaAI]]
