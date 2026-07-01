---
title: 'Chapter 10 — The Tools People Use'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 10
liberal_art: Trivium-Rhetoric
audience: beginner
---

# Chapter 10 — The Tools People Use

> There are several AI coding tools people use today. This chapter explains what each one is and what it is good at. The tools change fast; the categories do not.

---

## The Simple Version

All AI coding tools do the same fundamental thing: wrap a model, give it tools, and let you work on code with it. The differences are in style, defaults, and which models they support.

Here are the main ones people use.

---

## opencode

**What it is**: A terminal-native AI coding agent. You run it in your project directory; it has file and shell tools; it can use [[mcp-anthropic-standard|MCP]] servers and skills.

**What it is good at**: Multi-step agentic work in the terminal. Model-agnostic (you can use Claude, GPT, Gemini, local Llama). Supports MCP servers and skills out of the box.

**Style**: Terminal, multi-model, scriptable.

---

## Claude Code

**What it is**: Anthropic's terminal AI coding tool. Similar shape to opencode: terminal-native, file and shell tools, MCP support, agentic loop.

**What it is good at**: Using Claude models (Sonnet, Opus). Strong default safety — it asks for confirmation on file writes and shell commands until you grant broader permission.

**Style**: Terminal, Anthropic models, conservative-by-default safety.

---

## Cursor

**What it is**: A VS Code fork with AI tightly integrated. Less terminal-native than opencode or Claude Code; more editor-native.

**What it is good at**: Inline edits (select code, describe the change, accept or reject the diff). Tab autocomplete trained on your codebase. A "Composer" mode for multi-file agentic edits. MCP support via `.cursor/mcp.json`.

**Style**: GUI editor, VS Code-based, AI woven into editing.

---

## Aider

**What it is**: An open-source terminal coding agent. Older than the others; has its own conventions.

**What it is good at**: Git integration (it commits each change with a generated message by default). Scriptable. Mature.

**Style**: Terminal, git-first, open source.

---

## Claude Desktop (with MCP)

**What it is**: A chat application that supports MCP. Not a coding tool per se — it is a general chat app — but it is the easiest way to try MCP servers without a full coding agent.

**What it is good at**: Trying MCP servers. Install the filesystem server, point it at a project directory, and ask Claude to read files and explain them. Good for exploration and learning the protocol.

**Style**: GUI chat, MCP-capable, not for editing code.

---

## How to Choose

| Tool | Best for | Style |
| :--- | :--- | :--- |
| **opencode** | Terminal agentic work, any model | CLI, multi-model |
| **Claude Code** | Claude models, conservative safety | CLI, Anthropic models |
| **Cursor** | Editor-integrated AI, inline edits | GUI, VS Code-based |
| **Aider** | Git-first scripting, open source | CLI, scriptable |
| **Claude Desktop** | Trying MCP without a coding agent | GUI, chat |

The right answer is often "two of them." Many developers use a terminal agent (opencode or Claude Code) for multi-step agentic work and an editor (Cursor or VS Code + Copilot) for inline edits. They share the same MCP servers and the same project.

---

## A Concrete Session, Start to Finish

Here is what a real session looks like, end to end:

1. **Start in the project directory.** `cd my-project && opencode`.
2. **Scope the task.** "Audit the docs folder for broken links. Report what you find; do not change anything yet."
3. **AI explores.** Reads the docs folder, finds 38 broken links, reports.
4. **Approve a plan.** "Fix them all. Do not touch any other content."
5. **AI edits.** Rewrites the links, runs a grep to verify none remain.
6. **Verify.** "Run `grep -r 'file:///Users' docs/` and confirm zero matches."
7. **Commit.** `git add docs && git commit -m "fix: broken links in docs"`.
8. **Move on.** Next task, same session or a fresh one.

Notice the rhythm: **scope, plan, execute, verify, commit.** That rhythm is the professional workflow in miniature.

---

## The Big Picture

- The main tools are **opencode, Claude Code, Cursor, Aider, and Claude Desktop**.
- They all do the same fundamental thing (wrap a model, give it tools, let you work on code).
- They differ in **style** (terminal vs. editor), **models** (one vs. many), and **defaults** (conservative vs. permissive).
- Many people use **two** — a terminal agent for big agentic work, an editor for inline edits.
- The rhythm of a professional session: **scope, plan, execute, verify, commit.**

## 10.5 Other Tools Worth Knowing

The five tools above are the main ones professional developers reach for today. But the AI coding world is much bigger — new tools launch almost every week. Here are a few more worth knowing, grouped by what they are FOR.

**GitHub Copilot** — The original AI coding assistant, launched in 2021 by GitHub and OpenAI. It lives inside VS Code, JetBrains, Visual Studio, Neovim, and Xcode, suggesting code as you type and answering questions in a sidebar chat. It has a free tier (about 2,000 completions per month) and paid tiers for heavier use. ([github.com/features/copilot](https://github.com/features/copilot))

**Continue** — An open-source AI coding extension for VS Code and JetBrains that lets you plug in almost any model (Claude, GPT, local Llama, and more) and customize how it behaves. In 2025 Continue was acquired by Cursor, but its open-source codebase still exists and serves as a reference for how these tools are built. ([continue.dev](https://www.continue.dev))

**Codeium / Windsurf** — AI coding tools originally known for generous free tiers. Windsurf started as a Codeium-built VS Code fork (a full IDE with AI woven in) and in 2025 was acquired by Cognition and renamed Devin Desktop, adding multi-agent management. Codeium's free autocomplete is still widely used inside other editors. ([codeium.com](https://codeium.com))

**Tabnine** — One of the earliest AI code completion tools (it actually predates Copilot). It is best known for its privacy focus — it can run entirely on your own machines so your code never leaves your company — which makes it popular with banks and other enterprises that have strict data rules.

**Replit AI / Replit Agent** — AI coding that runs entirely in the browser. You describe an app, the agent writes the code, and Replit runs it for you in a cloud workspace — no setup, no installation, no local files. It is great for quick prototypes, learning, and sharing a project with a link.

**Bolt.new / Lovable / v0** — A newer category sometimes called "app generators." You type a prompt like "a habit tracker with a login page" and the tool builds a full, working app — frontend, styling, sometimes a backend — that you can use immediately. Bolt.new comes from StackBlitz, v0 from Vercel, and Lovable is an independent startup. They are less for editing existing code and more for spinning up something new fast.

---

### Categories matter more than names

New tools launch constantly and old ones merge, get acquired, or change names (Windsurf → Devin Desktop; Continue → part of Cursor). Instead of memorizing a list, learn the **categories**:

- **Chat** — talk to an AI about code (Claude Desktop, ChatGPT).
- **Inline completion** — AI suggests the next line as you type (Copilot, Tabnine, Codeium).
- **Agentic CLI** — a terminal agent that can edit files and run commands across many steps (opencode, Claude Code, Aider).
- **Editor-integrated** — AI woven into a full IDE (Cursor, Windsurf/Devin Desktop, Continue).
- **App generator** — type a prompt, get a whole app (Bolt.new, Lovable, v0, Replit Agent).

Once you know what a tool is FOR, picking it up — or switching to another one — becomes much easier. The models and the products change; the categories do not.

Continue to [Chapter 11 — Code of Conduct: Being Responsible](11_code_of_conduct.md).
