---
title: 'session-start-prompt-pattern'
date: 2026-06-27
tags: [Trivium-Rhetoric, Seven-Liberal-Arts, nick-milo, ai-os, session-start, prompt, amnesia, future-proofing]
type: principle
sources: [YouTube — How I Use Obsidian + Claude Cowork to Run My Life (https://youtu.be/rRa9td4oe7k)]
status: stable
liberal_art: Trivium-Rhetoric
---

# Session-Start Prompt Pattern

## Insight
The session-start prompt is bound to a hotkey (TextExpander on Mac, equivalent elsewhere):

> "First, please read the me.md file [in Ideaverse]. Then review the vault map and skill map for relevant context. Confirm you've read, then await instruction."

Why this matters: **even frontier models have amnesia.** Without an explicit load step, the model will *claim* to have read your context files and *actually* have skimmed or skipped them. The pattern forces the model to:

1. Read `me.md` (see [[me-md-vault-map-skill-map]]) — your identity, how you work.
2. Review the vault map — the index of what's in the vault.
3. Review the skill map — the index of which skill is for what.
4. **Confirm you've read** — the explicit confirmation is the verification step. If the model can't summarize what it read, it didn't read it.
5. **Then await instruction** — don't start doing work before the human asks. The load step is for context, not for action.

This is the same pattern as the AGENTS.md file in this very vault — it loads at the start of every session to give the agent the rules + pointers. Same logic: don't trust the model to remember across sessions; make the context-load explicit and verifiable.

It's also the same pattern as the Karpathy LLM Wiki's `claude.md` schema (see [[karpathy-llm-wiki-vs-rag]]) and the `claude.md` in the [[second-brain-obsidian-foundations]] blueprint. All the same move: a small markdown file at the root, read at session start, gives the agent the rules of the road before you ask it anything.

The hotkey binding is the operational layer. Without a hotkey, you'll forget to load context some sessions, and the agent will confidently hallucinate based on stale memory. With a hotkey, every session starts the same way: load context, confirm, await. The discipline is in the repetition.

This is the workflow layer of [[nick-milo-aios-three-layers]] — the three files exist; the session-start prompt is what makes them actually load.

## Context
From Nick Milo's "How I Use Obsidian + Claude Cowork to Run My Life"; the session-start prompt is the operational pattern that makes the three maps actually fire.

## Related
- [[nick-milo-aios-three-layers]]
- [[me-md-vault-map-skill-map]]
- [[karpathy-llm-wiki-vs-rag]]
- [[InaAI]]
