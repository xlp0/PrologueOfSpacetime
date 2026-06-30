---
concept: nick-milo-aios-three-layers
tags: [nick-milo, ai-os, obsidian, claude-cowork, ideaverse, future-proofing]
source: YouTube — How I Use Obsidian + Claude Cowork to Run My Life (https://youtu.be/rRa9td4oe7k)
date: 2026-06-27
---

# Nick Milo AIOS — Three Layers

## Insight
Nick Milo's "AIOS" is a 3-layer system. The whole pitch: **own the files (markdown + skills + AI core docs), rent the model.** If Claude goes away tomorrow, you re-point Codex/Gemini/local at the same folder and keep going.

**The three layers:**

1. **Ideaverse** = Obsidian vault, just `.md` files. ACE folders: Atlas (knowledge/ideas), Calendar (daily notes/meetings/journals), Efforts (projects/tasks). Nick's vault is ~17,000 notes.
2. **Translation layer** (the missing middle): an `AIOS/` subfolder inside your vault holding three files. Kept separate so AI-generated content can be isolated and cleared without polluting your own thinking.
3. **External AI**: Claude Co-work pointed at the vault folder. Co-work can read/edit/move/rename/create files — no re-uploading context each session.

The middle layer is the load-bearing piece most people miss. Without it, AI-generated content mixes with your own thinking and you can't tell what's yours vs. what's the model's. The `AIOS/` subfolder isolates the model's output so you can review, accept, or wipe it without disturbing your own notes.

This is a more opinionated version of [[second-brain-obsidian-foundations]] — same blueprint (vault + AI + middle layer), but Nick's version is sharper about isolation. The Karpathy LLM Wiki (see [[karpathy-llm-wiki-vs-rag]]) makes a similar move with its `raw/` (read-only sources) vs `wiki/` (AI-maintained) split — keep the source of truth separate from the AI-generated synthesis.

The three files in the translation layer are the actual load-bearing piece — see [[me-md-vault-map-skill-map]]. And the session-start pattern that uses them is [[session-start-prompt-pattern]].

Future-proofing argument: Claude claims no training on your data; 30-day rolling server retention is the accepted trade-off for frontier access. Real moat is the files. ChatGPT was the default a year ago, Claude today, maybe a local Apple-silicon model in two years — your `.md` files travel to all of them.

## Context
From Nick Milo's "How I Use Obsidian + Claude Cowork to Run My Life" — a lighter, more opinionated take on the [[second-brain-obsidian-foundations]] blueprint.

## Related
- [[me-md-vault-map-skill-map]]
- [[session-start-prompt-pattern]]
- [[second-brain-obsidian-foundations]]
- [[karpathy-llm-wiki-vs-rag]]
- [[claude-fable-gets-it]] — model-of-the-day; the "rent the model" thesis is why Fable swapping in is a non-event
- [[InaAI]]
