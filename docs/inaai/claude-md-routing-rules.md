---
concept: claude-md-routing-rules
tags: [claude-code, claude-md, routing, codex, tool-agnostic]
source: YouTube — Every Level of a Claude Second Brain Explained (https://youtu.be/DTCyvo6cC54); also confirmed in "The Next Era of Second Brains Is Here" (https://www.youtube.com/watch?v=xHAZo1SmnhM)
date: 2026-06-28
---

# claude.md Is a Router, Not a System Prompt

## Insight
The `claude.md` (or `agents.md`, or `CLAUDE.md`) at the project root does double duty. The obvious half is identity: who you are, what the project is, the rules of the road. The under-used half is **routing rules** — explicit pointers telling the agent where each kind of information lives in the vault.

Without routing rules you get the most common Claude Code failure mode: you ask it something, and instead of looking in your folders it asks you for more info. The agent will not autonomously grep your entire codebase — that wastes tokens and time, and you wouldn't want it to. So if it doesn't know a thing lives somewhere, it won't find it. The fix is a few lines in `claude.md`: "if you need information about me personally, look in `context/`; if you need Q1 priorities, look in `projects/q1/`." When this is set up properly you stop re-explaining things — the agent just knows where to go and why.

Two operational details from the video:

**Auto-memory.** Claude Code has a `/memory` command that toggles auto-memory on/off. When on, the AI writes and updates `memory.md` itself — you don't have to maintain it. This is Claude-specific; Codex doesn't have the equivalent, so for tool portability you keep `memory.md` and add a routing rule in `agents.md` telling Codex to look there for memories.

**Tool-agnostic portability.** Because the second brain is just files and folders, moving from Claude Code to Codex (or any other agent harness) is a copy operation: clone `claude.md` as `agents.md`, point them at each other if you want, and the rest of the vault is unchanged. The author keeps both `claude.md` and `agents.md` in Herc 2 — same content, different filename — so each harness reads its expected file. The vault itself is the portable substrate; the root instruction file is just the entry point each harness expects to find.

The extreme version of the same point: a model can get **banned outright** and the brain survives untouched. The "Next Era of Second Brains" author built his setup on Claude Fable 5, which got shut down the same week — he just pointed a different model at the same files and kept going. Same triad he names for why this matters: no more amnesia (every new chat stops re-explaining the business), it compounds (every note makes future answers better), and it outlasts the hype (it's just files — swap the engine, keep the brain). That third leg is the [[agentic-harness-90-percent]] thesis in plain language: own the brain, rent the model.

## Context
From "Every Level of a Claude Second Brain Explained"; routing rules are framed as the difference between a `claude.md` that feels ignored and one that just works. Tool-agnostic portability is a recurring theme — the author explicitly uses the second brain with Codex and Hermes, not just Claude.

## Related
- [[second-brain-obsidian-foundations]] — the foundational `claude.md` schema pattern
- [[me-md-vault-map-skill-map]] — Nick Milo's tool-agnostic `me.md` move
- [[session-start-prompt-pattern]] — explicit load step before any work
- [[InaAI]]
