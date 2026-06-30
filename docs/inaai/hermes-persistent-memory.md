---
concept: hermes-persistent-memory
tags: [hermes-agent, persistent-memory, nous-research, agents, second-brain]
source: YouTube — Hermes Agent Explained In 5 Minutes (https://www.youtube.com/watch?v=9GpWELm3_XI)
date: 2026-06-27
---

# Hermes — Persistent Memory

## Insight
Hermes Agent is an open-source autonomous AI agent built by **Nous Research** — not a co-pilot, not a chatbot, not a ChatGPT wrapper. It lives on a server, runs continuously, and you talk to it by texting Telegram / Discord / Slack / WhatsApp like a colleague who's always online.

**Persistent memory** is the first of two things that allegedly separate Hermes from "the other AI agent peasants" (the other is the self-improving skills loop — see [[hermes-self-improving-skills]]).

Hermes remembers everything across every session — not just the last conversation. Projects, preferences, how you like problems explained. The layered memory system builds a **model of you over time**, so every interaction is shaped around you specifically.

Author's framing: most AI tools are a whiteboard that gets wiped each session; Hermes is a notebook that never closes. The whiteboard metaphor is the cleanest way to see why this matters — every ChatGPT/Claude conversation starts from zero. You re-explain your project, your preferences, your context, every time. Hermes doesn't. The notebook accumulates.

This is the runtime half of the [[second-brain-obsidian-foundations]] blueprint. The vault is the file-based second brain; Hermes's persistent memory is the agent-side mirror. Both compound over time. Day 1 = capable agent. Six months in = "knows your workflow better than tools you spent years setting up."

**Install & where to run it:**

- Single `curl` command on Linux, Mac, or WSL2. Under a minute.
- **Do not run it on your main laptop** — exposes you to prompt injection and other vulnerabilities.
- Needs a 24/7 server. Sponsor pitch: Hostinger KVM2 plan with a pre-built Docker template for one-click deploy. API keys, learned skills, and conversation history stay on your own server; no throttling, no per-agent fees, agent stays online even when your laptop is off.

Pair with [[hermes-self-improving-skills]] and [[hermes-sub-agents]] for the full Hermes pitch.

## Context
From "Hermes Agent Explained In 5 Minutes"; persistent memory is the first of Hermes's two core differentiators.

## Related
- [[hermes-self-improving-skills]]
- [[hermes-sub-agents]]
- [[second-brain-obsidian-foundations]]
- [[five-levels-second-brain]] — Hermes's persistent memory is the Level 5 runtime mirror
- [[second-brain-ingest-curation]] — evergreen ingest discipline applies to agent memory too
- [[InaAI]]
