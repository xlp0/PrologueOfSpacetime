---
title: 'karpathy-llm-wiki-vs-rag'
date: 2026-06-27
tags: [Trivium-Logic, Seven-Liberal-Arts, karpathy, llm-wiki, rag, obsidian, claude-code, second-brain]
type: concept
sources: [YouTube — Karpathy's LLM Wiki - Full Beginner Setup Guide (https://www.youtube.com/watch?v=iXd0t60YmMw)]
status: stable
liberal_art: Trivium-Logic
---

# Karpathy LLM Wiki vs RAG

## Insight
Andrej Karpathy's **LLM Wiki** idea fixes the fundamental flaw in RAG: every question starts from zero, nothing compounds. Instead of having the AI search raw docs each time, you have it read them once and build a persistent, interlinked markdown wiki. Every new source gets integrated into existing pages, contradictions get flagged, and questions get answered from a pre-synthesized knowledge base.

Karpathy's framing: **"Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase."** You rarely write the wiki yourself — the AI does the writing and organizing.

The RAG-vs-wiki distinction is the load-bearing insight:

- **RAG** — every query retrieves raw chunks. The AI does the synthesis fresh each time. Pros: handles new sources immediately. Cons: nothing compounds; the AI re-derives the same connections every query; token-expensive; no quality improvement over time.
- **LLM Wiki** — the AI reads sources once, synthesizes them into interlinked pages, and queries pull from the pre-synthesized wiki. Pros: compounding knowledge; queries are cheap; contradictions surface during synthesis, not at query time. Cons: requires the AI to actually maintain the wiki; you have to ingest sources before you can query.

The wiki pattern is the same as [[second-brain-obsidian-foundations]] (vault as harness) and [[graphify-codebase-knowledge-graph]] (codebase knowledge graph instead of personal-knowledge wiki). All three are saying the same thing: pre-synthesize knowledge into a structure the AI can query, instead of having the AI re-derive it every session. It's the harness-vs-no-harness distinction (see [[agentic-harness-90-percent]]) applied to knowledge management.

Pair with [[llm-wiki-three-layers]] for the architecture and [[llm-wiki-lint-pass]] for the maintenance discipline. The setup is three folders and one markdown schema file — the trick isn't the tooling, it's the discipline of letting the AI synthesize instead of just retrieve.

## Context
From "Karpathy's LLM Wiki - Full Beginner Setup Guide"; the RAG-vs-wiki framing is the spine of the video.

## Related
- [[llm-wiki-three-layers]]
- [[llm-wiki-lint-pass]]
- [[second-brain-obsidian-foundations]]
- [[vector-retrieval-chunking-limit]] — RAG's chunking failure mode made concrete
- [[five-levels-second-brain]] — the LLM Wiki is the Level 2 mechanism
- [[gitops-git-as-source-of-truth]] — GitOps applies the same wiki-compounds thesis to infrastructure state
- [[InaAI]]
