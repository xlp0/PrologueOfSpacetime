---
title: 'Chapter 3 — The Stack: Model, Harness, Client, Server'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Quadrivium-Geometry]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 3
liberal_art: Quadrivium-Geometry
audience: professional
---

# Chapter 3 — The Stack: Model, Harness, Client, Server

## Four layers, not one

When people say "AI coding tool" they are usually collapsing four distinct things into a single mental blob. The blob is wrong. The stack has layers, and each layer is a place where someone made decisions that affect your experience, your bill, and your security posture. Knowing the layers means you can ask the right questions about any tool you pick up.

From the inside out:

1. **The model** — the LLM.
2. **The harness** — the loop, the tools, the context management.
3. **The client** — the thing you actually touch: the editor extension, the terminal app, the web UI.
4. **The server** — anything the harness talks to that isn't the model: [[mcp-anthropic-standard|MCP]] servers, your filesystem, your CI, external APIs.

Let's take them one at a time.

---

## Layer 1 — The model

We covered this in Chapter 2. The model is the stateless text predictor. It is the only layer that is genuinely "the AI." Examples: Claude Sonnet/Opus, GPT-4/5-class models, Gemini, and open-weights models like Llama, DeepSeek, Qwen.

Things that live at this layer:

- The weights.
- The context window size (a property of the model, even though the harness decides how to fill it).
- The pricing per token (in/out).
- The base capabilities: how good it is at code, how long it can reason, whether it supports **tool calling** natively, whether it supports **prompt caching**.

Things that do *not* live at this layer, even though people often assume they do:

- Whether the tool can read your files. (That's the harness.)
- Whether it remembers your project across sessions. (That's the harness + your rules files.)
- Whether it's safe to let it run `rm -rf`. (That's the harness's permissions layer.)

A common mistake is to evaluate a tool by asking "which model does it use?" It matters, but it's maybe a third of the story. Two tools using the identical model can feel completely different because of the other three layers.

---

## Layer 2 — The harness

This is the layer from Chapter 2: the loop, the tool-call parsing, the execution, the context curation, the permissions, the memory, the orchestration. The harness is what turns a model into an agent.

In 2025–2026, "harness engineering" emerged as a recognized discipline — the practice of designing the runtime around an LLM so the agent is reliable in production. The short version of what a good harness gives you:

- **Tool definitions** — a clear schema of what the model is allowed to call (read_file, edit_file, run_shell_command, etc.) and the arguments each takes.
- **Reliable tool-call parsing** — turning the model's text output into actual function calls without choking on edge cases.
- **Permission and sandboxing** — deciding what the agent may do without asking, what it must ask about, and what it can never do.
- **Context management** — what goes into the window, what gets evicted when it's full, what gets summarized.
- **Prompt caching** — reusing the stable prefix of a prompt across calls so you pay less and wait less. (More in Chapter 4.)
- **Subagent orchestration** — spawning focused sub-agents for sub-tasks (e.g. a separate context for "search the codebase" vs "write the fix") so the main context doesn't fill with noise.
- **Memory and rules** — loading your project's rules files (Chapter 9), remembering facts across turns, deciding what to persist across sessions.

Open-source harnesses you'll hear about: the engines inside opencode, Claude Code, Codex CLI, Cursor's agent runtime, Aider, Goose, and others. They differ in philosophy — some optimize for tight human control, some for maximum autonomy — but they're all solving the same set of problems at this layer.

**Harness vs. client.** A subtle point: the harness is not the same as the client. The harness is the runtime; the client is the surface you drive it from. Claude Code ships a terminal client *and* an IDE integration; both talk to the same harness. opencode's harness can be driven from its own TUI or from editor plugins. Keep the layers separate in your head and you'll understand how tools can share a harness while feeling totally different to use.

---

## Layer 3 — The client

The client is the surface *you* touch. This is where a tool lives or dies for most users, because it's the part you actually experience.

Examples of clients:

- An IDE extension (GitHub Copilot's VS Code extension, Cursor's editor, the Continue plugin).
- A terminal TUI (Claude Code's CLI, opencode's terminal interface, Aider's REPL, Codex CLI).
- A web app (ChatGPT's web UI, Claude.ai, the various web-based agents).
- An editor built from scratch around the agent (Cursor is the canonical example — it's a fork of VS Code reorganized around the agent).

What lives at the client layer:

- The editor surface — where the diff shows up, how you accept or reject edits, whether you can see the agent's plan before it acts.
- The chat panel — where your conversation lives.
- Slash commands and custom commands (Chapter 9) — the `/fix`, `/review`, `/refactor` shortcuts the client exposes.
- Inline UX — ghost text completions, inline diffs, the "accept / reject" buttons on a proposed edit.
- Keyboard shortcuts, theming, all the usual editor stuff.
- How multi-file edits are presented — side-by-side, streaming, queued for approval, etc.

A great client on top of a mediocre harness can still feel good for small tasks. A great harness behind a clunky client will frustrate you before you ever discover how good the harness is. When you're evaluating a tool, the client is what you'll have an opinion about in the first five minutes; the harness is what you'll have an opinion about after a week.

---

## Layer 4 — The server(s)

"Server" is the fuzziest layer name because it covers a grab-bag of things the harness reaches out to. Three flavors:

### a) The model provider's API

The harness sends prompts to an HTTP endpoint run by Anthropic, OpenAI, Google, or whoever hosts the open-weights model you're using. This is the most fundamental "server" in the stack. When the model feels slow, it's usually this hop. When the bill shows up, it's measured against this server's token pricing.

### b) Your own machine

When the harness reads `src/auth.ts`, it's reading a file on your local filesystem. When it runs `npm test`, it's a process on your machine. This is "serverless" in the sense that there's no remote box, but it's still a place where actions have consequences — including deleting files or pushing to git. This is why Chapter 11 is so focused on permissions and sandboxing. Your laptop *is* a server the harness can act against.

### c) MCP servers and external services

This is the newest and most interesting category. **MCP** ([[mcp-anthropic-standard|Model Context Protocol]], Chapter 7) is a standard way for a harness to talk to external tools and data sources: a database, a Slack workspace, a Jira board, the Palmier video editor, a browser, a stock-photo library. Each of those runs as an MCP server that the harness connects to, and the model can then call the tools that server exposes as if they were local.

A 2026 AI coding tool is rarely just "model + harness + editor." It's "model + harness + editor + a small constellation of MCP servers," each of which gives the agent a new capability. The list of what your agent can actually do is the union of (what the harness can do) + (what each connected MCP server can do). This is why Chapter 7 is its own chapter and not a footnote.

---

## How the layers combine in real tools

A few concrete examples, to make the layers tangible:

| Tool | Model | Harness | Client | Notable servers |
|---|---|---|---|---|
| Claude Code | Claude (Anthropic API) | Anthropic's own | Terminal CLI + IDE plugins | Whatever MCP servers you configure |
| Cursor | Multiple (you pick) | Cursor's agent runtime | Cursor's own editor (VS Code fork) | Cursor's backend services, MCP servers |
| opencode | Multiple (you pick) | opencode's open harness | TUI + editor plugins | MCP servers |
| GitHub Copilot | GPT-class models | GitHub's harness | VS Code / JetBrains extension | GitHub's backend, MCP servers |
| Codex CLI | OpenAI models | OpenAI's harness | Terminal CLI | MCP servers |
| ChatGPT web (no harness) | GPT-class | Minimal (no real agentic loop) | Web UI | None by default |

Read that table carefully and you'll see why, for example, "I asked ChatGPT and it couldn't fix my test" is not a meaningful statement about the model — ChatGPT's web client has no harness that can see your files or run your tests. The same model inside Claude Code would behave completely differently.

You can also see why **MCP is layer-agnostic in practice but logically sits at the server layer**: it's how the harness reaches outside itself for capabilities. A model doesn't know about MCP. A client doesn't talk to MCP servers directly. The harness is the only layer that connects to them.

---

## Why the layers matter

Three reasons:

1. **You can swap layers independently.** Don't like the model your tool ships with? Many tools let you pick. Don't like the client? Some harnesses have multiple clients. Don't like the harness? That's the hardest layer to swap, but it's also the one that most defines the tool.
2. **It tells you where a problem lives.** "It's slow" — probably the model API. "It edits the wrong file" — harness, specifically context curation. "The diff view is ugly" — client. "It can't query my database" — missing MCP server. Knowing the layers turns debugging from vibes into a checklist.
3. **It tells you what you're responsible for.** The model provider is responsible for the model. The tool vendor is responsible for the harness and (usually) the client. *You* are responsible for which MCP servers you connect, what permissions you grant, what rules files you write, and what you accept into your codebase. That last sentence is the entire subject of Chapter 11.

---

## A useful self-test

Next time you sit down with an AI coding tool, try to name each layer out loud before you start:

- "Today I'm using **Claude Sonnet** (model) inside **Claude Code's harness** (harness), driven from its **terminal client** (client), with an **MCP server connected to my Postgres** (server)."

If you can do that, you understand the stack. The rest of this guide is about getting good at each layer — starting with the one that constrains everything else: the context window and its tokens.
