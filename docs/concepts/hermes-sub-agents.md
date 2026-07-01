---
title: 'hermes-sub-agents'
date: 2026-06-27
tags: [Trivium-Logic, Seven-Liberal-Arts, hermes-agent, sub-agents, parallel, context-isolation, agents]
type: concept
sources: [YouTube — Hermes Agent Explained In 5 Minutes (https://www.youtube.com/watch?v=9GpWELm3_XI)]
status: stable
liberal_art: Trivium-Logic
---

# Hermes — Sub-Agents

## Insight
Sub-agents are the underappreciated feature in Hermes Agent. The problem they solve: a single AI session handling five things at once → context stretches, earlier parts drop off.

Hermes spins up **isolated workers** for specific tasks, each with its own focus, context, and tool set. Results come back to the main agent and get assembled. You ask for one thing; a whole process runs in the background.

This is the same architectural pattern as [[deerflow-lead-agent-dynamic-subagents]] (lead agent + dynamically invoked subagents) and the same operational pattern as [[hermes-background-subagents]] (background sub-agents that run while you keep chatting).

The reason this works: isolation is the point. A sub-agent doesn't inherit the parent's context — it gets only what it needs. This matters for three reasons:

1. **Context efficiency** — the parent's context stays lean. Heavy lifting happens in workers, results come back as summaries.
2. **Tool isolation** — a sub-agent can be given a narrow tool surface (least privilege) so a compromised sub-agent can't escalate. This is the [[prompt-injection-defense-in-depth]] pattern.
3. **Parallelism** — multiple sub-agents can run concurrently. Demo from the Hermes update video: a complex research request spawned 5 agents / 28 tool calls running concurrently.

The architectural insight: sub-agents are a context-management tool, not just a parallelism tool. Even if you only ever ran one sub-agent at a time, you'd still benefit from the context isolation — the parent's context doesn't get polluted with the sub-agent's working memory.

The modular skill system in Hermes (built on the open agentskills.io standard — same spec as [[skills-sh-markdown-spec]]) is what makes sub-agents practical. A sub-agent can be given a specific skill + a specific tool set + a specific task, and the isolation makes it safe to dispatch.

## Context
From "Hermes Agent Explained In 5 Minutes"; sub-agents are the third of Hermes's core features (after persistent memory and self-improving skills).

## Related
- [[hermes-persistent-memory]]
- [[hermes-background-subagents]]
- [[deerflow-lead-agent-dynamic-subagents]]
- [[prompt-injection-defense-in-depth]]
- [[InaAI]]
