---
concept: wiki-backlinks-vs-kg-edges
tags: [knowledge-graph, llm-wiki, obsidian, lightrag, second-brain]
source: YouTube — Every Level of a Claude Second Brain Explained (https://youtu.be/DTCyvo6cC54)
date: 2026-06-28
---

# Wiki Backlinks Are Not Knowledge-Graph Edges

## Insight
An LLM Wiki with `[[wikilinks]]` and a knowledge graph with typed edges look similar in a graph view — nodes connected by lines — but they encode fundamentally different amounts of information. Conflating the two is the most common reason people under-build (assuming a wiki is already a knowledge graph) or over-build (reaching for a KG when backlinks would do).

The distinction is in the *relationship type*. Wiki backlinks are untyped "see also" pointers: note A links to note B because they're related, but the link doesn't say *how*. A knowledge graph edge is typed: "Jordan **works at** Acme," "Acme **is endorsed by** Postpilot," "Postpilot **is a competitor of** Cadently." Those bolded verbs carry the semantic payload — without them, the graph is just a cluster of "stuff that touches other stuff."

The practical payoff of typed edges is relationship-chain queries. "Trace topic X back to topic A" — the path itself is the answer. Untyped backlinks let you follow a trail by reading each page in its entirety; typed edges let the agent reason over the path *without* reading every node. The video's example: LightRAG rendering the chain "our 7-day AI challenge → provided from YouTube → connects to onboarding process of AIS Plus → developed by Aiden" — the verbs (provided from, connects to, developed by) are what make the chain traversable as a single fact, not just a reading list.

The trade-off: typed edges cost more upfront. You have to define a schema, ingest with entity extraction, and maintain the graph. Backlinks cost almost nothing — just write `[[wikilink]]` and Obsidian handles the rest. For most personal-knowledge work (project-based, content-heavy), backlinks are enough. For relationship-rich domains (CRM, multi-client businesses, supply chains), the typed edges pay back the upfront cost.

This is also why the Koo vault explicitly removed Anthropic's `@modelcontextprotocol/server-memory` MCP — typed SPO triples were overkill at the projected scale of 250–500 notes/year. Wikilinks plus mem0 semantic search cover 95% of retrieval needs; typed edges can be re-added later if scale demands.

## Context
From "Every Level of a Claude Second Brain Explained"; the distinction is framed as "level 2 wiki vs level 4 knowledge graph." LightRAG is demoed as the level 4 visualization of the author's full Herc 2 vault.

## Related
- [[graphify-codebase-knowledge-graph]] — typed edges done right, in a codebase domain
- [[karpathy-llm-wiki-vs-rag]] — the wiki pattern with untyped backlinks
- [[second-brain-obsidian-foundations]] — backlink-first vault pattern
- [[InaAI]]
