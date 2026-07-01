---
title: 'reverse-engineer-data-shape'
date: 2026-06-28
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, second-brain, ingest, design-principle, retrieval, harness]
type: concept
sources: [YouTube — Every Level of a Claude Second Brain Explained (https://youtu.be/DTCyvo6cC54)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Reverse-Engineer the Data Shape From the Question

## Insight
Before deciding how to ingest a piece of data, work backwards from how it will be retrieved. The shape of the question dictates the shape of the storage — not the other way around.

The video's analogy: a basketball hoop and a basketball. We know what shape the hoop is, and we know the ball needs to go through. So why would we design the ball to be a giant square? It just wouldn't fit. You start with the end in mind, then design the input.

This sounds obvious until you watch people do the opposite: dump meeting transcripts into a vector database because "vector DB = good," then ask the agent "summarize the March 5th meeting." The chunking produces 20 vector points; the agent pulls the five chunks most similar to "March 5th meeting summary" and summarizes those five — missing the actual holistic content of the transcript. The retrieval shape (chunk similarity) didn't match the question shape (give me the whole meeting). For that question, a single markdown file of the March 5th meeting read in its entirety is more accurate than 20 vector chunks.

The decision rule: for each new data type, ask "how will I want to recall this?" If you'll need exact snippets from a 1,000-rule document — vector search. If you'll need the entire document read holistically — markdown file, no chunking. If you'll need relationship chains across entities (people, companies, projects) — knowledge graph. If you'll need everything on a topic pulled together — LLM Wiki. If you'll need real-time data the agent doesn't need to remember but might need to query — leave it as a callable source (Slack, ClickUp, email) and route the agent to it on demand.

This is the ingest-side equivalent of the harness-vs-model thesis (see [[agentic-harness-90-percent]]): the work you do upfront shaping the data pays compounding returns every time the agent retrieves it correctly. Skip the upfront work and no amount of model horsepower will rescue you.

## Context
From "Every Level of a Claude Second Brain Explained"; the basketball-hoop analogy opens the video and recurs as the justification for mixing levels within one vault.

## Related
- [[agentic-harness-90-percent]] — same harness-first mindset applied to agent design
- [[second-brain-obsidian-foundations]] — folder shape is the ingest-side decision
- [[vector-retrieval-chunking-limit]] — the failure mode this principle prevents
- [[InaAI]]
