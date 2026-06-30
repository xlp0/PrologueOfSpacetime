---
concept: static-vs-dynamic-context
tags: [agentic, context, skills, progressive-disclosure, google]
source: YouTube — Google Just Dropped a Masterclass on Agentic Engineering (https://www.youtube.com/watch?v=zbmuiaPuiNM)
date: 2026-06-27
---

# Static vs Dynamic Context

## Insight
Google distinguishes two kinds of agent context:

- **Static context** — rules, guardrails, system prompt. Loaded every session. Reliable but expensive; keep it lean.
- **Dynamic context** — skills loaded on-demand, RAG searches, conventions loaded per codebase region. Efficient and scalable; the only risk is the agent not grabbing for it when it should.

The key move: **one generalist agent + skills**, not a zoo of specialized sub-agents. Skills = progressive disclosure. The agent stays lightweight and flexes into planner / code reviewer / debugger roles as needed. The industry is moving away from complicated multi-agent systems.

Why this beats the multi-agent zoo: each specialized sub-agent is a fixed cost (its own context, its own prompt, its own tool surface, its own coordination overhead). One generalist with skills is variable cost — you only pay for the skill when it's relevant. The same logic applies at the file level: a per-codebase-region conventions file only loads when the agent is working in that region.

The risk to watch: the agent not grabbing for a skill when it should. With a fixed zoo of specialists, the orchestration graph guarantees every capability is reachable. With dynamic context, the agent has to *decide* to load the skill — and if it doesn't recognize the situation as skill-relevant, the skill might as well not exist. That's why skill descriptions matter (see [[skills-sh-markdown-spec]]) — they're the only thing the agent sees before deciding to load.

This is also the architectural shift [[deerflow-lead-agent-dynamic-subagents]] formalizes: earlier agent systems modeled work as a fixed graph of specialized roles (rigid, hard to extend); DeerFlow moved to a lead agent + middleware + dynamically invoked subagents. New capabilities become new skills / tools / runtime policies instead of requiring orchestration-graph redesign.

Pair with [[plan-build-eval-review-split]] for how dynamic context flows through the workflow, and with [[agentic-harness-90-percent]] for why this matters.

## Context
From the Google Agentic Engineering masterclass; the static/dynamic context distinction is the architecture section.

## Related
- [[agentic-harness-90-percent]]
- [[skills-sh-markdown-spec]]
- [[deerflow-lead-agent-dynamic-subagents]]
- [[InaAI]]
