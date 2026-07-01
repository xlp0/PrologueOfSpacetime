---
title: 'llm-wiki-lint-pass'
date: 2026-06-27
tags: [Trivium-Logic, Seven-Liberal-Arts, karpathy, llm-wiki, linting, obsidian, maintenance, contradictions]
type: principle
sources: [YouTube — Karpathy's LLM Wiki - Full Beginner Setup Guide (https://www.youtube.com/watch?v=iXd0t60YmMw)]
status: stable
liberal_art: Trivium-Logic
---

# LLM Wiki Lint Pass

## Insight
Like a code linter, you can periodically ask the AI to lint the wiki: `Please lint the wiki.` It surfaces:

- **Contradictions between pages** — page A says X, page B says not-X. The linter flags both. This is one of the biggest wins of the wiki pattern over RAG — contradictions surface during synthesis, not at query time. With RAG, you might query page A today and page B tomorrow and get contradicting answers without knowing. With a wiki + lint pass, the contradiction is flagged once and you resolve it.
- **Orphan pages** (no inbound links) — a page that nothing links to is effectively invisible. The linter flags it so you can either link to it (if it's useful) or delete it (if it's not).
- **Broken links** — wikilinks pointing to pages that don't exist. The linter flags them so you can either create the missing page or fix the link.
- **Concepts mentioned but without their own page** — a concept that's referenced in multiple places but doesn't have a dedicated page. The linter suggests creating one.

This is the maintenance discipline that makes the wiki pattern actually work over time. Without linting, a wiki drifts — orphans accumulate, contradictions fester, broken links erode trust. With periodic lint passes, the wiki stays healthy as it scales.

The same pattern shows up in code: a linter catches issues the author didn't notice. A wiki linter catches issues the AI author didn't notice when it was writing pages one at a time. The cross-page checks (contradictions, orphans, broken links) require a global view that no single-page-write operation has.

Pair with [[karpathy-llm-wiki-vs-rag]] for the why and [[llm-wiki-three-layers]] for the architecture. The lint pass is the operational discipline that keeps the architecture honest.

**Limitations to keep in mind:**

- **Personal scale** — Karpathy suggests ~100 articles per wiki. Tens of thousands of pages needs real infrastructure.
- **Garbage in, garbage out** — you still curate sources. The linter doesn't fix bad source material.
- **Requires a coding agent** — Obsidian alone does nothing; the AI is the engine.
- **AI makes mistakes** — mis-categorization, bad links. That's what the lint pass is for.

## Context
From "Karpathy's LLM Wiki - Full Beginner Setup Guide"; the lint pass is the maintenance-discipline section near the end of the video.

## Related
- [[karpathy-llm-wiki-vs-rag]]
- [[llm-wiki-three-layers]]
- [[InaAI]]
