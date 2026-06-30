---
concept: hermes-self-improving-skills
tags: [hermes, self-improving, skills, memory, agentskills, persistent-memory]
source: YouTube — The new Hermes Agent update has me speechless (https://www.youtube.com/watch?v=bQ1LCFrwj08) and Hermes Agent Explained In 5 Minutes (https://www.youtube.com/watch?v=9GpWELm3_XI)
date: 2026-06-26
---

# Hermes Self-Improving Skills Loop

## Insight
Two things allegedly separate Hermes Agent from "the other AI agent peasants": **persistent memory** that survives across every session (see [[hermes-persistent-memory]]), and a **self-improving skills loop** where each solved problem gets saved as a reusable capability.

The loop: every time Hermes works through something complex, it saves that solution as a **reusable skill**. It doesn't figure out the same thing twice. The June 2026 update sharpened this further — Hermes now creates and updates its own skills far more aggressively, with frequent "self-improvement review, patch this skill" events.

The author's concrete experience with the UE 5.8 MCP skill is telling: it was rough at first, but after a few conversations Hermes kept patching its own skill and now it's excellent. The skill improved itself through use.

Net effect: not just remembering you, getting more capable the longer it runs. Day 1 = capable agent. Six months in = "knows your workflow better than tools you spent years setting up." This is the same compounding pattern [[agentic-harness-90-percent]] codifies for harnesses generally — except in Hermes the harness is the agent's own skill library, growing itself.

Modular skill system: skills = reusable modules built on the open **agentskills.io** standard (same spec as [[skills-sh-markdown-spec]]). ~90 built-in, 81 optional, 500+ community skills across 18 categories at recording time. You can install community skills, build your own, or tell Hermes to set up a **cron job that checks agentskills.io** and suggests whatever's relevant based on what it already knows about you. The tool literally looks for its own upgrades.

This is also the contrast axis in [[catalog-vs-curator]]: Hermes bets on the agent improving itself (Curator), OpenClaw bets on a community catalog (ClawHub).

## Context
From both the Hermes Agent update deep-dive and the 5-minute explainer; the self-improving skills loop is Hermes's core differentiator.

## Related
- [[hermes-persistent-memory]]
- [[catalog-vs-curator]]
- [[skills-sh-markdown-spec]]
- [[hermes-ue5-mcp]]
- [[InaAI]]
