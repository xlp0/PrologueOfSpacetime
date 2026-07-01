---
title: 'Chapter 7 — MCP — Plugging Things In'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Grammar]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 7
liberal_art: Trivium-Grammar
audience: professional
---

# Chapter 7 — [[mcp-anthropic-standard|MCP]] — Plugging Things In

## The one-line answer

**MCP** ([[mcp-anthropic-standard|Model Context Protocol]]) is an open standard, introduced by Anthropic in late 2024 and adopted widely since, that lets an AI harness talk to external tools and data sources in a uniform way. The standard nickname is "the USB-C of AI" — one plug shape, many devices.

If you've ever wished your AI coding agent could just *query your database directly*, or *read the Linear ticket you're working on*, or *look something up in your company wiki* without you copy-pasting, MCP is the answer. It's the layer that lets a harness reach outside itself for capabilities.

---

## The problem MCP solves

Before MCP, every harness had its own ad-hoc way of adding tools. Cursor had one format, Claude Code had another, and if you wanted to teach your agent to talk to, say, Slack, you wrote a Slack integration specific to that harness. Switch harnesses and you threw the integration away.

Worse, the model itself had no standard way to *discover* what tools were available. Each harness would hand-roll its own tool descriptions in its own format, and the model would have to learn each one.

MCP fixes both problems by defining:

1. **A protocol** — how a harness and an external server speak to each other (JSON-RPC over stdio or HTTP).
2. **A shape** — how a tool is described (name, description, input schema) so any harness can read it and any model can call it.
3. **A discovery mechanism** — how a harness lists what tools a server offers, so the model can decide which to call.

The practical effect: write your Postgres MCP server once, and any MCP-capable harness can use it. Switch from Claude Code to Cursor to opencode and your same server keeps working. The ecosystem of "things your agent can do" becomes composable and shared, instead of fragmented per-tool.

---

## How it fits in the stack

Go back to Chapter 3's four layers: model, harness, client, server. MCP lives at the **server layer**. The model doesn't know about MCP. The client doesn't talk to MCP servers directly. Only the harness connects to them, exposes their tools to the model, and runs the tool calls when the model asks.

```
┌─────────────────┐
│     CLIENT      │  ← you type here
└────────┬────────┘
         │
┌────────▼────────┐
│     HARNESS     │  ← the loop, the context window, the permissions
└──┬──────────┬───┘
   │          │
   │ MCP      │ direct
   │          │ (filesystem,
   ▼          │  shell, etc.)
┌──────┐  ┌───▼────────┐
│ MCP  │  │ your laptop│
│server│  └────────────┘
└──────┘
```

When you read "MCP is a server," that's literal — an MCP server is a process (often local, sometimes remote) that speaks the MCP protocol. You start it (or your harness starts it on demand), the harness connects to it, and from then on the tools it exposes are part of what your agent can do.

---

## What an MCP server actually exposes

Three kinds of things:

1. **Tools** — functions the model can call. "Query the database," "search the wiki," "create a Linear issue," "take a screenshot," "place a trade." This is the main use. Tools have a name, a description, and a JSON schema for their arguments, and they return a result that goes back into the context window.
2. **Resources** — data the model can read, addressed by URI. "The contents of `file:///src/auth.ts`," "the schema of my `users` table," "the current weather in Tokyo." Resources are passive — the model asks for them by URI; they don't take arguments.
3. **Prompts** — pre-built prompt templates the server provides. Less common in practice, but useful for "run this exact analysis on the data I expose."

Most day-to-day MCP usage is tools. You'll see the word "tool" used interchangeably with "MCP tool" in conversation.

---

## Real examples (the kind people actually run)

The reason MCP took off is that the catalog of available servers got useful fast. A representative sample of what people plug into their AI coding agents in 2026:

- **Filesystem** — read/write files outside the harness's default workspace.
- **Git** — read history, create branches, make commits, open PRs.
- **Postgres / MySQL / SQLite** — schema introspection and read queries (writes are usually gated behind a permission).
- **GitHub / GitLab / Bitbucket** — read issues, open PRs, comment, search code across repos.
- **Linear / Jira** — read the ticket you're working on, update its status, create sub-tasks.
- **Notion / Confluence / Obsidian** — pull docs into context so the agent can read the spec.
- **Slack** — read a thread, post an update, search for a past decision.
- **Browser automation** (Playwright, Puppeteer) — drive a real browser, take screenshots, scrape a page, fill in a form.
- **Web search / web fetch** — let the agent look something up rather than guess.
- **Sentry / Datadog** — pull the error you're trying to fix directly into context.
- **Palmier** — the video editor used as an example elsewhere in this guide. A Palmier MCP server exposes the timeline as tools, so an agent can read the timeline, add clips, edit text overlays, and so on. This is a clean example of MCP turning an external application into an agent-accessible tool.
- **Memory / knowledge graph** — persist facts across sessions so the agent "remembers" your project.
- **Shell** — run arbitrary commands (with the usual permissions and sandboxing caveats — Chapter 11).

The list grows monthly. The point isn't any one server — it's that the moment a server exists for a thing, *every* MCP-capable agent gains that capability overnight, with no per-tool integration work.

---

## What changes about the agent when MCP servers are connected

Two things, both important:

1. **The model's toolset expands.** The agent's "what I can do" list is now `(harness-native tools) ∪ (every connected MCP server's tools)`. A coding agent connected to your database and your Linear is a meaningfully different thing from one that can only edit files and run shell.
2. **The context window fills differently.** MCP tool results are tokens like any other (Chapter 4). A big query result can blow the window. A good harness summarizes or truncates MCP results; a bad one dumps them raw. This is a context-engineering (Chapter 6) concern, not a protocol concern, but it matters in practice.

---

## Permissions and the trust question

This is where Chapter 11 starts to hover. An MCP server that can write to your database, push to git, or post to Slack on your behalf is an MCP server that can do real damage. The protocol itself doesn't enforce safety — it just moves bytes. Safety lives in:

- **The harness's permission system** — which tools require approval, which can run automatically, which are forbidden.
- **Sandboxing** — running MCP servers (and the agent's tool calls generally) in restricted environments: a container, a VM, a network-isolated zone. This is what people mean by "sandboxing" in the agent-architecture literature.
- **Your configuration** — you decide which servers to connect, which tools to enable, and what scope of access each has. The defaults matter; the override matters more.

A reasonable posture: **read-only by default, write with confirmation, destructive never (or only inside a sandbox).** An agent that can query your database freely is fine; an agent that can `DROP TABLE` is a question you should answer on purpose, not by accident.

---

## MCP vs. skills — the question people always ask

There's a closely related concept called **agent skills** (Chapter 8), and people get confused about the difference. The short version:

- **MCP** gives an agent new *tools* — things it can *do*. "Query the database," "post to Slack," "drive the browser."
- **Skills** give an agent new *know-how* — things it knows *how to do*. "How to do a code review in this codebase," "how to triage a bug in this product," "the right way to write a migration here."

A tool without the know-how is a wrench with no mechanic. Know-how without the tool is a mechanic with no wrench. Real agentic workflows need both, which is why Chapter 8 immediately follows this one. Skills tell the agent *what to do*; MCP gives it *the means to do it*.

---

## Why MCP matters even if you never write a server

You may never write an MCP server. Most developers won't. But you will *use* them, and the fact that they exist as a standard changes what you can expect from any tool:

- Any MCP-capable tool you pick up has access to the same growing library of integrations.
- Switching tools doesn't mean re-teaching your agent about your stack.
- A useful new server (someone wrote an MCP server for your favorite service yesterday) is available to your agent tomorrow, with no integration work on your end.
- The capabilities of your agent are no longer limited to what the tool vendor thought to build. They're limited by what the ecosystem has shipped and what you choose to connect.

That last point is the big one. Pre-MCP, your agent's reach was bounded by the vendor. Post-MCP, your agent's reach is bounded by the protocol's reach, which is much larger and growing. That's why MCP earned its own chapter.

---

## A note on the future

MCP is young. The protocol is still evolving, the server ecosystem is still figuring out conventions (especially around auth and security), and there's a long tail of rough edges — servers that crash, tools that hang, schemas that don't quite match reality. Treat it as a real and important standard, but verify each server you rely on rather than assuming it just works.

The trajectory is clear, though: the question "can my agent talk to X?" is increasingly being answered with "yes, via MCP, and here's the server." That's a fundamental shift in what an AI coding tool *is* — from a closed product to a composable one — and it's not going back.
