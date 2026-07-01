---
title: 'Chapter 10 — The Tools People Use'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 10
liberal_art: Trivium-Rhetoric
audience: professional
---

# Chapter 10 — The Tools People Use

## A snapshot, not a guide

This chapter is a portrait of the AI coding tool landscape as of mid-2026. It will be out of date in some details by the time you read it — tools ship fast, names change, features get cloned across vendors in weeks. Treat it as a map of the *categories* and a starting point for your own evaluation, not as a buyer's guide.

The categories themselves are more stable than the tools in them. Once you can name the categories, you can place any new tool you encounter.

---

## The categories

### 1. IDE-integrated assistants

A plugin or fork of an existing editor, with the agent living inside it. The defining trait: the agent is one part of a normal editing experience, not the whole experience.

- **GitHub Copilot** — the original, still everywhere. Started as inline autocomplete, now has chat, edit, and agent modes. Reads `.github/copilot-instructions.md`. Strong default for teams already on GitHub's ecosystem.
- **Cursor** — a fork of VS Code reorganized around the agent. Often cited as the tool that made agentic IDE editing feel good. Reads `.cursor/rules/` (current) and `.cursorrules` (legacy). Supports slash commands in `.cursor/commands/`.
- **Windsurf** — Codeium's agent-first editor, also a VS Code derivative. Reads `.windsurfrules`. Positioning is similar to Cursor; differences are mostly in UX philosophy.
- **Cline** — an open-source agent extension for VS Code. Reads `.clinerules`. A common choice for people who want Cursor-style behavior without leaving their existing editor.
- **Continue** — an open-source extension that works across multiple editors. Config-driven, model-agnostic.

These tools live at the **client layer** (Chapter 3) and ship their own harness; the model is usually selectable.

### 2. Terminal-first agents

A CLI that runs the agentic loop in your terminal, often against your current working directory. The defining trait: keyboard-first, no editor chrome, treats your shell as the surface.

- **Claude Code** — Anthropic's terminal agent, tightly integrated with Claude models. Reads `CLAUDE.md` (project, user, and enterprise tiers). Supports slash commands, custom commands, [[mcp-anthropic-standard|MCP]] servers, and skills. Has become a default reference point for "what a good terminal agent feels like."
- **Codex CLI** — OpenAI's equivalent, tied to OpenAI models. Reads `AGENTS.md`. The OpenAI-flavored counterpoint to Claude Code.
- **opencode** — an open-source, model-agnostic terminal agent. Reads `AGENTS.md`. Notable for being vendor-neutral: you bring the model, the harness is the product. Used as the basis for several editor integrations.
- **Gemini CLI** — Google's terminal agent, tied to Gemini models. Reads `GEMINI.md`.
- **Aider** — an older, well-respected open-source terminal agent. Pioneered many patterns now standard elsewhere. Notable for its git-integrated workflow (every edit is a commit).
- **Goose** — an open-source agent from Block, notable for its MCP-first architecture.

Terminal agents are where harness engineering is most visible: the loop, the context curation, the permissions, the subagent orchestration are all exposed and configurable. If you want to understand how the tools actually work, run one of these for a week.

### 3. Web-based agents

A web app where you describe what you want and the agent builds it, often in a hosted environment. The defining trait: you don't bring your laptop; the agent runs somewhere else.

- **ChatGPT (with code interpreter / agent mode)** — the mass-market surface. Good for exploration, prototyping, and one-off tasks. Limited as a real coding tool because the harness can't see your repo or run your tests (unless you upload everything).
- **Claude.ai** — similar positioning, similar constraints. Excellent for thinking, planning, and writing prose about code; weaker than its terminal sibling for actual coding against a real repo.
- **v0, bolt, lovable, and similar** — web-based "describe an app, get a running app" tools. Useful for prototypes and frontends; the gap between "it works in the sandbox" and "it ships in my codebase" is still real.

Web-based agents are the natural home of "vibe coding" (Chapter 1) — quick, exploratory, low-stakes. They struggle for real engineering work because they can't reach your codebase, your tests, your CI, or your MCP servers (Chapter 7). The fix is usually to export the result and bring it into a terminal agent for the real work.

### 4. Background / CI agents

Agents that run on a schedule or on a trigger (a PR, an issue, a commit), doing work without you driving them. The defining trait: asynchronous; you find out about the work after it's done (or when it needs you).

- **GitHub Copilot's automated workflows** — review, security scan, dependency bumps, on PRs or schedule.
- **Claude Code's background agents** — long-running tasks you kick off and check on later.
- **Custom CI agents** — many teams wire their own: an agent runs on every PR, reads the diff, comments on it, runs extra checks. This is the agentic loop in a pipeline.

Background agents are where slot-4 autonomy (Chapter 9) actually earns its keep — gated behind a PR review, so the human checkpoint is built in.

### 5. Domain-specific agents and MCP-powered tools

Not coding tools per se, but tools built on the same model + harness + MCP pattern, for a specific domain. Worth knowing about because they show where the pattern is going:

- **Palmier** — an AI-native video editor, referenced elsewhere in this guide. A Palmier MCP server exposes the timeline as tools, so a coding agent can drive the editor. A clean example of "the agent stack, applied to a non-coding domain."
- **Domain-specific agentic products** — legal research agents, financial-analysis agents, customer-support agents, data-analysis agents. All built on the same model + harness + MCP + skills pattern. The vocabulary you're learning in this guide is portable.

The point of mentioning these: **"AI coding" is the leading edge of a broader pattern.** The same stack — model, harness, [[static-vs-dynamic-context|context engineering]], MCP, skills, workflows — is showing up everywhere. Learn it once here, and you've learned it for the rest.

---

## How to choose

A rough decision tree:

1. **Already on GitHub's stack, want the path of least resistance?** Copilot.
2. **Want a polished IDE built around the agent, and happy to leave your editor?** Cursor (or Windsurf).
3. **Love your current editor and want to add an agent?** Cline or Continue.
4. **Prefer the terminal, want maximum control and transparency?** Claude Code, Codex CLI, opencode, or Aider.
5. **Want vendor neutrality and to bring your own model?** opencode (or Aider).
6. **Already deep on Anthropic / OpenAI / Google and want the tight integration?** Claude Code / Codex CLI / Gemini CLI respectively.
7. **Prototyping or doing one-off exploratory work?** The web-based tools are fine for that; just don't expect them to ship your codebase.

For most professionals, the practical answer in 2026 is to have one IDE-integrated tool (for in-editor edits and reviews) and one terminal agent (for multi-step work and tasks that benefit from the full loop). They're complementary, not exclusive.

---

## What to evaluate when you try one

The model is rarely the deciding factor — most tools let you pick from the same few frontier models. What actually differs:

- **The harness's context curation.** Does it evict the right things? Does it forget the task? Does it pollute the window with junk? (Chapter 6.)
- **The permissions model.** Can you set it to "ask before any shell command"? Can you allowlist specific commands? Can you sandbox? (Chapter 11.)
- **Rules file support.** Which format does it read? Does it support per-directory scoping? (Chapter 9.)
- **Slash commands and skills.** Can you define your own? Are there good bundled ones? Can you share them with a team? (Chapter 8, Chapter 9.)
- **MCP support.** Can it connect to MCP servers? How easy is it to add one? (Chapter 7.)
- **Subagent support.** Can you delegate noisy sub-tasks? (Chapter 9.)
- **Plan mode.** Does it have a real plan-then-execute workflow? (Chapter 9.)
- **Diff UX.** How does it show you what it wants to change? Can you accept selectively?
- **Model selection and cost controls.** Can you pick the model per task? Does it support prompt caching? Can you see what you're spending?
- **Speed and reliability.** Does it hang? Does it crash? Does it lose state?

Spend a week with a tool before forming an opinion. The first day is about the client; the rest of the week is about the harness. The harness is what you'll actually be living with.

---

## A prediction, offered cautiously

The tool landscape will keep churning, but a few things look stable:

- **The model layer will stay concentrated** — a few frontier providers, plus open-weights alternatives. You'll rarely choose a tool for its model alone.
- **MCP will become table stakes** — any tool without MCP support will be non-viable within a year or two.
- **AGENTS.md-style rules files will converge** — the cross-tool standard is winning; tool-specific formats will either read it directly or delegate to it.
- **Skills will become the main sharing unit** — communities will form around skill libraries, the way they formed around editor plugins before them.
- **The harness is where the differentiation lives.** Expect consolidation at the model layer and continuing innovation at the harness layer. The "best tool" question will keep being a "best harness" question.

The tools named in this chapter will come and go. The layers and patterns won't. Learn the layers; the tools are details.
