---
concept: hermes-background-subagents
tags: [hermes, background-agents, sub-agents, parallel, agentic-os]
source: YouTube — The new Hermes Agent update has me speechless (https://www.youtube.com/watch?v=bQ1LCFrwj08)
date: 2026-06-26
---

# Hermes Background Sub-Agents

## Insight
Hermes Agent can now spawn **sub-agents that work in the background while you keep chatting.** Previously required flipping a flag manually; now triggered automatically by sufficiently complex prompts.

Demo: a complex research request on multiple portfolio companies → 5 agents / 28 tool calls running concurrently. While they work, you can keep messaging — "add Nvidia to that list" — and Hermes spins up another sub-agent without blocking the chat.

The companion feature is the **sub-agent tree**, a new UI pane showing every spawned sub-agent, all their tool calls, and what they're focused on. Without that visibility, background work is a black box — you'd have no idea what was happening or whether anything was stuck. The tree makes the parallelism inspectable.

The pattern rhymes with [[deerflow-lead-agent-dynamic-subagents]] and [[hermes-sub-agents]]: a single chat session can't hold five concurrent tasks without context stretching and earlier parts dropping off. The fix is isolated workers — each sub-agent gets its own focus, context, and tool set, then results come back to the main agent and get assembled. You ask for one thing; a whole process runs in the background.

This is also the foundation of the [[agentic-os-shared-brain]] story — Hermes + Claude Code + Graphify dashboard reading the same registry. Background sub-agents are what make "agent handles tasks spanning whole codebases, you review outcomes not file diffs" possible.

The architectural shift from "fixed graph of specialized roles" to "lead agent + dynamically invoked subagents" is what [[deerflow-lead-agent-dynamic-subagents]] formalizes — Hermes is one production instantiation of it.

## Context
From "The new Hermes Agent update has me speechless" — the second of 8 updates, paired with the sub-agent tree UI.

## Related
- [[hermes-sub-agents]]
- [[deerflow-lead-agent-dynamic-subagents]]
- [[agentic-os-shared-brain]]
- [[InaAI]]
