# Chapter 10 — The Tools People Use

> There are several AI coding tools people use today. This chapter explains what each one is and what it is good at. The tools change fast; the categories do not.

---

## The Simple Version

All AI coding tools do the same fundamental thing: wrap a model, give it tools, and let you work on code with it. The differences are in style, defaults, and which models they support.

Here are the main ones people use.

---

## opencode

**What it is**: A terminal-native AI coding agent. You run it in your project directory; it has file and shell tools; it can use MCP servers and skills.

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

Continue to [Chapter 11 — Code of Conduct: Being Responsible](11_code_of_conduct.md).
