---
title: 'second-brain-ingest-curation'
date: 2026-06-28
tags: [Trivium-Logic, Seven-Liberal-Arts, second-brain, ingest, four-cs, evergreen, data-curation]
type: principle
sources: [YouTube — Every Level of a Claude Second Brain Explained (https://youtu.be/DTCyvo6cC54) and YouTube — I Turned Claude Into the Ultimate Second Brain (https://m.youtube.com/watch?v=8QQ_INxAhRs)]
status: stable
liberal_art: Trivium-Logic
---

# Ingest Curation — Four C's and the Evergreen Filter

## Insight
Most second-brain failures aren't retrieval failures — they're ingest failures. People blame the AI for not finding things, but the deeper problem is they never got the relevant nuance out of their head and into the vault in the first place. Before you blame retrieval, ask: does this vault actually have all the nuance I carry in my brain?

Two filters govern what belongs in the second brain.

**The Four C's framework:** context, connections, capabilities, cadence — taken in order. The first two are the second brain (knowledge layer): *context* is what's going on in the business (decisions, statuses, OTAs, locked-in priorities) plus your routing tree — `claude.md` pointing the agent to skills, references, wikis, and other projects (see [[claude-md-routing-rules]]); *connections* are live data sources (Stripe, ClickUp, Slack, Google Workspace) that change constantly vs. the static context in the vault. The second two are the AIOS (action layer): *capabilities* are skills, agents, and automations built on top of the brain; *cadence* is when those capabilities run on their own (scheduled, event-triggered, or loop) without you babysitting them. Conflating these is why people end up with action triggers and cron jobs inside their knowledge vault — wrong layer.

Two gut checks from the second source. (1) **Adoption before architecture** — an OS doesn't start with architecture, it starts with a default. Close out the tabs for separate AI tools and custom GPTs; default to your one harness (Claude Code, Codex, whatever) for everything. Context and memory only build up if you stop context-switching. (2) **The stranger-vs-teammate test** — open your Claude Code and ask it about your business. If it sounds like a stranger, you're missing context; if it sounds like a co-founder, you're there. When the agent takes 5 minutes searching for a file you could find in 5 seconds, the architecture needs work. "Architecture engineering" as a discipline is just the practice of keeping the routing tree intuitive to both you and the agent.

**The evergreen-vs-ephemeral filter:** the second brain should hold data you'd still want in a year. Locked-in decisions. Project charters. Decision logs. Entity profiles. Ephemeral data — Slack threads, current emails, live customer status — does *not* belong in the brain; it's noise that ages out weekly. Instead, leave it as a callable source: the agent knows to query ClickUp or Slack on demand when the second brain doesn't have the answer. The retrieval chain becomes: vault first, then wiki, then meeting transcripts, then live source (ClickUp/Slack/email) — only the last step hits the ephemeral data, and only when needed.

The curation test the video gives: "in a year, will it be good for me to have this memory here? Yes. Otherwise, it's just adding noise." If you ingest Slack threads wholesale, you'll be deleting old ones every month — a maintenance burden that compounds. If you leave Slack as a callable source and only ingest the *decisions* that emerged from those threads, the vault stays evergreen and the agent still has access to the live data when a question demands it.

The Grill Me skill (originally from Matt Pocock) is one tactic for getting evergreen knowledge out of your head: it interviews you relentlessly about a topic until it knows everything, and writes the result to a brainstorm file. Useful when you've identified a knowledge gap — "Grill me about client A" — and need to extract tacit knowledge into explicit form.

## Context
From "Every Level of a Claude Second Brain Explained" and "I Turned Claude Into the Ultimate Second Brain" (Nate Herk, Fable release day June 9, 2026). The Four C's and evergreen filter come from the first; the layered second-brain-vs-AIOS mapping, the adoption-first mindset, and the stranger-vs-teammate gut check come from the second.

## Related
- [[second-brain-obsidian-foundations]] — what the brain *is*
- [[second-brain-business-os-wiring]] — capabilities and cadence live here, not in the brain
- [[claude-md-routing-rules]] — the routing-tree pattern for the *context* C
- [[hermes-persistent-memory]] — the agent-side memory mirror
- [[claude-fable-gets-it]] — the model that landed on the same day this video was published
- [[InaAI]]
