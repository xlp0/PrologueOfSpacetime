---
title: 'Chapter 13 — Where to Learn More'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 13
liberal_art: Trivium-Rhetoric
audience: beginner
---

# Chapter 13 — Where to Learn More

> This handbook is a starting point. The tools and the field change fast. Here are places to go deeper.

---

## Specifications and Official Docs

- **[[mcp-anthropic-standard|MCP]] specification** — https://modelcontextprotocol.io — the official protocol site, with the spec, SDKs, and a list of reference servers.
- **Anthropic MCP announcement** (November 2024) — the original blog post introducing the protocol.
- **opencode docs** — https://opencode.ai — configuration, MCP, skills, and the agentic loop.
- **Claude Code docs** — Anthropic's documentation for Claude Code.
- **Cursor docs** — https://cursor.com/docs — editor AI, Composer, MCP configuration.

---

## Reference MCP Servers to Study

- **`@modelcontextprotocol/server-filesystem`** — the simplest reference server. Read its source to learn the shape of an MCP server.
- **`@modelcontextprotocol/server-github`** — a real-world server with auth, pagination, and many tools.
- **`@modelcontextprotocol/server-postgres`** — a database-backed server; good model for read-only data exposure.

---

## Essays Worth Reading

- **"Tools, Not Prompts"** — the argument that tool configuration beats prompt engineering. A useful framing even if you disagree with the strong form.
- **"The Spec, Implement, Verify Loop"** — a write-up of the three-phase discipline applied to AI-assisted coding.
- **Anthropic's "Building Effective Agents"** — a short essay on when to use agents vs. workflows, and the patterns that work.

---

## Skills to Study

Look at the skills installed on your machine under `.agents/skills/` or `~/.agents/skills/`. Each one has a `SKILL.md` you can read. A few good starting points:

- Skills that wrap a CLI tool (like the gitnexus-* skills) — show how to expose an existing tool's workflow to an AI.
- Skills that define an analysis framework (like a video analyst skill) — show how to package a multi-step procedure.
- Skills that describe parallel execution — show how to coordinate multiple subagents.

Read a few `SKILL.md` files to get a feel for what a good skill looks like before authoring your own.

---

## Code of Conduct References

- Your employer's AI policy (if one exists; if not, propose one).
- The Open Source Initiative's guidance on AI-generated code in open source projects.
- Your model provider's data handling policy — read it, do not assume.

---

## A Note on Keeping Up

The field moves fast. Three habits that help:

1. **Read the changelogs** of the tools you use. Most publish weekly notes.
2. **Try one new thing per week** — a new MCP server, a new skill, a new prompting style. Small experiments keep you current without overwhelming you.
3. **Talk to other people using these tools.** The patterns that work are still being discovered; the best way to learn them is from someone who just figured one out.

---

## The End (For Now)

You have reached the end of the handbook. You now know:

- What AI coding tools are and how they work.
- How the AI sees text (tokens) and remembers (context window).
- How to talk to AI (prompting styles) and how to curate what it sees ([[static-vs-dynamic-context|context engineering]]).
- What MCP is and what people have plugged in.
- What skills are and why they save time and money.
- When to let AI run on its own (agentic workflows) and the patterns people use.
- The tools people use (opencode, Cursor, Claude Code, Aider, Claude Desktop).
- How to use AI responsibly (code of conduct).
- The words you will hear (glossary).

This handbook will go out of date. That is okay. The ideas — the model is the brain, the harness is the body, tools matter more than prompts, verify before you trust, you are responsible — those ideas will still be true even as the tools change.

Go build something.

---

*Back to [the handbook README](README.md).*
