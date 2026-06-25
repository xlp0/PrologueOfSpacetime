---
created: 2026-06-25
modified: 2026-06-25
title: "The AI Coding Workflow Handbook: MCP, Skills, Agents, and Professional Practice"
audience: Intermediate developers who have used ChatGPT or Copilot but are new to MCP, skills, and agentic workflows
authors: Henry Koo
tags: [teaching, ai-coding, mcp, skills, agentic-workflow, code-of-conduct]
---

# The AI Coding Workflow Handbook

> A reference guide for intermediate developers moving from "I use ChatGPT to help me write code" to "I run a professional, verifiable, multi-tool agentic workflow."

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Mental Model: How AI Coding Tools Actually Work](#2-mental-model-how-ai-coding-tools-actually-work)
3. [Prompting Discipline for Code Work](#3-prompting-discipline-for-code-work)
4. [MCP (Model Context Protocol)](#4-mcp-model-context-protocol)
5. [Agent Skills](#5-agent-skills)
6. [Agentic Workflow Patterns](#6-agentic-workflow-patterns)
7. [Concrete Tooling Walkthrough](#7-concrete-tooling-walkthrough)
8. [Code of Conduct and Professional Practice](#8-code-of-conduct-and-professional-practice)
9. [The Reference Workflow](#9-the-reference-workflow)
10. [Glossary](#10-glossary)
11. [Further Reading](#11-further-reading)

---

## 1. Introduction

### 1.1 Who This Handbook Is For

You are a working developer. You have used ChatGPT, GitHub Copilot, or Claude to help write or explain code. You can prompt reasonably well for one-off tasks. But you have not yet adopted the things that distinguish a casual user from a professional one:

- **MCP** (Model Context Protocol) — the open standard for connecting AI tools to your actual systems.
- **Skills** — packaged workflow knowledge that an agent loads on demand.
- **Agentic workflows** — letting an AI plan, execute, and verify multi-step tasks with tool access.
- **A code of conduct** — the verification, security, and licensing discipline that keeps you and your employer safe.

This handbook teaches those four things, plus the concrete tooling that puts them into practice.

### 1.2 What Changed in 2024-2026

The shift from "AI as autocomplete" to "AI as a tool-using agent" happened in three steps:

1. **Tool use** (2023): Models could call functions you defined. You wrote the glue code.
2. **MCP** (late 2024): An open standard meant tools could be written once and used by any compatible client. The "USB-C for AI tools" moment.
3. **Agentic loops** (2025): Clients stopped waiting for you to drive every step. They began to plan, call tools, observe results, and continue until the task was done or they got stuck.

If your workflow is still "copy code into ChatGPT, paste answer back," you are operating at step zero. This handbook gets you to step three.

### 1.3 What You Will Learn

By the end of this handbook you should be able to:

- Explain what MCP is, install an MCP server, and read its tool definitions.
- Explain what a skill is, distinguish it from an MCP tool, and author a simple one.
- Recognize when a task benefits from an agentic workflow vs. direct chat.
- Run an agentic session safely: scope the task, manage context, verify output.
- Apply a code of conduct: verification, security, IP, attribution, and when not to use AI at all.

---

## 2. Mental Model: How AI Coding Tools Actually Work

Before tools, protocols, and workflows, you need an accurate mental model of what the model actually is. Most professional mistakes come from a wrong model.

### 2.1 What an LLM Actually Is

A large language model is a function that maps an input sequence of tokens to a probability distribution over the next token. That is the whole mechanism. Everything else — reasoning, coding, planning — is emergent behavior that arises from training on a very large corpus and from how the model is prompted and wrapped.

Two practical consequences:

1. **The model has no memory between sessions.** Every conversation starts fresh. Anything you want it to know must be in the context window for that session.
2. **The model cannot do anything.** It can only emit text. To read a file, run a test, or call an API, something outside the model must execute that action and feed the result back in.

### 2.2 The Context Window

The context window is the working memory of a session. It is measured in tokens (roughly 3-4 characters per token for English, less for code). When the window fills, older content is dropped or summarized. Everything the model "knows" about your task lives in this window.

Practical implications:

- **Loading the whole repo into context is usually wrong.** It burns tokens, costs money, and dilutes attention. Load only what is relevant.
- **Tool output is also context.** Every file read, every command output, every web page fetched consumes tokens. A 5000-line log dump can push useful context out of the window.
- **Longer is not better.** Models lose attention over very long contexts. A focused 5,000-token prompt often outperforms a sprawling 50,000-token one.

### 2.3 The Agentic Loop

The thing that makes modern AI coding tools feel different from a chatbot is the **agentic loop**:

```
1. Observe   - read the task, look at relevant files, run a search
2. Reason    - decide what to do next, possibly decompose into subtasks
3. Act       - call a tool: edit a file, run a command, search the web
4. Observe   - read the tool's output
5. Repeat    - until the task is done or the agent gets stuck
```

Without tools, the loop cannot act and step 3 is replaced by "emit text that the user must act on." With tools, the loop can run autonomously for many steps before needing human input.

The job of an AI coding tool (Cursor, opencode, Claude Code, Aider, etc.) is to wrap this loop: it gives the model tools, enforces safety checks, surfaces the loop's progress to you, and lets you intervene.

### 2.4 Why Tools Matter More Than Prompting

A common beginner mistake is to focus on prompt engineering while ignoring tools. But tools are the bottleneck, not the prompt. A mediocre prompt with the right tools (file search, grep, run tests, git diff) will outperform a brilliant prompt with no tools, because the model can verify its own work.

The professional shift is this: stop trying to write the perfect prompt, and start configuring the right tools. Then almost any reasonable prompt works.

### 2.5 The Harness: What Wraps the Model

A **harness** is the software that wraps a raw LLM and turns it into a usable coding agent. The model by itself is just a text-in, text-out function. The harness is everything around it: the tools, the file access, the shell, the safety checks, the chat UI, the git integration, the context management.

Think of it this way:

- The **model** is the engine.
- The **harness** is the car around the engine — steering wheel, brakes, dashboard, seatbelt.

opencode, Claude Code, Cursor, Aider — these are all harnesses. They use different models, expose different tools, and have different defaults, but they all do the same fundamental job: take a raw model and give it the parts it needs to actually work on your code.

Why this matters: when you pick a tool like opencode or Cursor, you are picking a **harness**, not a model. Most harnesses let you swap the model underneath (Claude, GPT, Gemini, local Llama). The harness is what determines the workflow, the tools, the safety posture, and the feel of the experience. The model determines the raw intelligence.

### 2.6 The Whole Stack: Model, Harness, Client, Server

Beginners often confuse these four layers. Here is what each one is **for**:

| Layer | What it is | What it is for | Examples |
| :--- | :--- | :--- | :--- |
| **Model** | The trained neural network. A text-in, text-out function. | Raw intelligence — the ability to reason, write, and plan. | GPT-4, Claude Sonnet, Gemini, Llama. |
| **Harness** | The software that wraps the model into a usable agent. | Tools, file access, safety, the agentic loop, the UI. | opencode, Claude Code, Cursor, Aider. |
| **MCP Client** | The part of the harness that talks to MCP servers. Often the harness itself. | Connecting the agent to external tools and data sources. | The MCP client inside opencode, Cursor, or Claude Desktop. |
| **MCP Server** | A separate program that exposes tools via the protocol. | Giving the agent access to a specific system (GitHub, Postgres, filesystem). | `server-github`, `server-filesystem`, `server-postgres`. |

The flow: **you** talk to a **harness**, which runs a **model**, which calls **tools** provided by **MCP servers** connected through the harness's **MCP client**. Each layer has a job. When something goes wrong, knowing which layer is responsible tells you where to look.

### 2.7 System Prompt vs User Prompt

Every message sent to the model has two parts:

- **System prompt**: instructions the harness sets that the user does not usually see. It tells the model who it is, what tools it has, what it should and should not do, how to format output. This is set by the harness developers and by your configuration (e.g. an `AGENTS.md` file or a project-level system prompt).
- **User prompt**: what you type. The actual task.

This matters because the system prompt shapes behavior heavily. Two people using the same model can get very different results because their harnesses ship different system prompts. This is also why the same model behaves differently in ChatGPT vs. Claude Desktop vs. opencode — same engine, different car.

When you write a project-level `AGENTS.md` or `CLAUDE.md` or `.cursorrules` file, you are adding to the system prompt. You are telling the model "this is how we work here." That is a powerful lever and most beginners do not realize they have it.

### 2.8 Tokens and Why They Matter

A **token** is the unit the model processes text in. Roughly:

- 1 token ≈ 4 characters of English
- 1 token ≈ 0.75 words
- Code is denser — a line of Python is often 5-15 tokens

Tokens matter for three reasons:

1. **Cost**: providers bill per token, both for input (what you send) and output (what the model generates).
2. **Context limit**: every model has a maximum context window in tokens. When it fills, older content drops out.
3. **Speed**: more tokens in means more time before the model starts responding.

Beginner mistake: pasting a 2,000-line file into chat "for context." That is roughly 15,000-20,000 tokens — a chunk of your window, a chunk of your budget, and possibly more than the model can usefully attend to. Load what you need, not everything.

### 2.9 Embeddings and Vector Search (RAG)

**RAG** (Retrieval-Augmented Generation) is how tools give a model access to a large body of text without pasting it all into the prompt. It has two parts:

1. **Embeddings**: convert each document (or chunk of one) into a vector — a list of numbers that captures the meaning of the text. Similar text has similar vectors.
2. **Vector search**: when the model needs information, the harness converts the question into a vector, finds the closest document vectors, and pastes only those into the prompt.

This is what lets an agent "search your codebase" or "search the docs" without loading everything into context. The agent's `grep` or `search` tool often uses a variant of this under the hood.

You do not need to build a RAG system to use AI coding tools — the harness handles it. But knowing it exists explains why the agent sometimes finds the wrong file: the search is by meaning similarity, not exact match. A function named `getUser` and a doc talking about "fetching user profiles" will match even if the words are different. That is usually what you want, but it can surprise you.

### 2.10 Sampling: Temperature and Friends

When the model picks the next token, it does not pick the single most likely one every time. It samples from a probability distribution. Two knobs that control this:

- **Temperature** (0 to ~2): higher means more random, lower means more deterministic. Temperature 0 always picks the most likely next token; temperature 1 allows more variety.
- **Top-p** (0 to 1): only consider the most likely tokens whose cumulative probability reaches p. A common setting.

For code work, low temperature (0 to 0.3) is usually right — you want the model to be careful and predictable, not creative. For brainstorming or naming, higher temperature can help. Most harnesses pick a sensible default; you rarely need to touch this.

### 2.11 Fine-Tuning vs Prompting vs RAG

Three ways to make a model better at a specific task, in increasing order of cost:

1. **Prompting**: put the instructions and examples in the prompt. Cheap, fast to iterate, works for almost everything. This is what you do 95% of the time.
2. **RAG**: give the model access to a searchable knowledge base at inference time. Good when the knowledge is large, changes often, or is proprietary. The harness or MCP server does the search; the model just reads the results.
3. **Fine-tuning**: train the model further on examples of the task. Expensive, slow, and only worth it when prompting and RAG are not enough — usually for a consistent style or format that prompting cannot reliably produce.

Beginners often jump to fine-tuning because it sounds impressive. Almost always, better prompting or better tools (RAG, MCP) is the right answer. Fine-tune last, if ever.

### 2.12 Prompting Styles and Patterns

There are many named prompting techniques floating around. You do not need to memorize them all — most are just shorthand for "be clear about what you want." But you will hear the names, so here is what each one means and what it is for.

**Caveman prompting** — Writing very short, direct, no-fluff prompts. Like a caveman: "fix bug login.ts line 42" instead of "Could you please help me figure out why the login endpoint is returning a 500 error when I submit the form?" The point is not to be rude — it is to strip away politeness and filler that the model does not need. Long polite sentences can actually dilute the task signal. Caveman style works great when the task is mechanical and the model has the context. It fails when the task is subtle and the model needs the extra explanation. Use it when you know exactly what you want; switch to full sentences when you need to explain the "why."

**Zero-shot prompting** — Asking the model to do something without giving any examples. "Write a function to reverse a string." Most modern models are good enough at common tasks that zero-shot just works. This is the default.

**Few-shot prompting** — Giving the model 2-5 examples of the input/output you want, then asking it to produce the next one. Useful when the format is unusual or the task is specific to your domain. Example: show the model three examples of "user complaint → categorized ticket" then give it a fourth complaint. The pattern teaches the model what you want better than a description would.

**Chain-of-thought (CoT)** — Asking the model to think step by step before giving the answer. "Think step by step" is the classic trigger phrase. This helps with math, logic, and multi-step reasoning because the model uses the intermediate tokens to "show its work." Some models now do this automatically; for others you still need to ask.

**Role prompting** — Telling the model who to be. "You are a senior security engineer reviewing this code." This sets the model's perspective and what knowledge to draw on. It is not magic — a model cannot actually be a security engineer — but it does bias the output toward the right lens. Use sparingly; overdone role prompts waste tokens and can make the model play-act instead of think.

**Step-back prompting** — Before answering, ask the model to state the broader principle or context. "What are the general principles of input validation? Now apply them to this code." This helps when the model is about to dive into details and miss the bigger picture.

**Self-consistency** — Run the same prompt a few times (with temperature > 0) and take the majority answer. Useful for reasoning questions where one run might go wrong. Expensive in tokens; use only when correctness matters more than cost.

**Tree of thoughts** — A more elaborate version of chain-of-thought where the model explores multiple branches of reasoning and picks the best. Mostly research-grade; most production tools do not use it directly, but you may see the name.

**Instruction-style vs. conversation-style** — Two broad flavors of prompt. Instruction style: "Do X, then Y, then Z." Conversation style: "Hey, I was thinking about X, what do you think?" Both work. Instruction style is more reliable for code tasks; conversation style is better for brainstorming and exploration. Most beginners default to conversation style when instruction style would serve them better.

The common thread: all of these are ways to give the model a clearer signal about what you want. There is no "best" technique — there is only the technique that fits the task. If you remember nothing else, remember that clarity beats cleverness. A plain, clear prompt beats a fancy-named technique applied wrong.

### 2.13 Context Engineering

A newer term you may hear: **context engineering**. It is the idea that the real skill in AI coding is not writing a clever prompt — it is curating what goes into the context window.

This means:

- Which files to load (not the whole repo — the relevant ones).
- Which tool outputs to keep (not the 5000-line log — a summary).
- When to start a fresh session (when the current one is polluted with failed attempts).
- What system prompt rules to set in `AGENTS.md` or equivalent.
- Which MCP servers to enable (so the model has the right tools without being overwhelmed).

Prompt engineering asks: "what words do I type?" Context engineering asks: "what does the model see, in total, before it generates?" The second question matters more. A perfect prompt in a polluted context still produces bad output. A mediocre prompt in a clean, well-curated context often produces great output.

This is why professionals spend more time on tools, file selection, and context management than on prompt wording. The wording is the tip of the iceberg; the context is the rest.

### 2.14 Newest Terms You Will Hear (2025-2026)

The vocabulary around AI coding is still being invented. Here is a plain-language glossary of terms that have become common in the last year. You do not need to use these words to use the tools — but you will see them in docs, in changelogs, and in conversations, so it helps to know what they mean.

**Harness** — (covered in §2.5) The software that wraps a raw model into a usable coding agent. opencode, Cursor, Claude Code, and Aider are all harnesses. The model is the engine; the harness is the car.

**Agent** — An AI system that runs the observe-reason-act loop on its own, possibly for many steps, using tools. "Agent" is used loosely; sometimes it means the whole harness, sometimes just one run of the loop. Context usually disambiguates.

**Subagent** — A secondary agent spawned by a main agent to handle an independent subtask. The subagent gets its own fresh context window, does its work, and returns a result. This keeps the main context clean and allows parallel work. See §6.4.

**Skill** — (covered in §5) A packaged unit of workflow knowledge (a `SKILL.md` plus supporting files) an agent loads on demand. The skill tells the agent what to do; the agent's tools do the actual work.

**MCP (Model Context Protocol)** — (covered in §4) The open standard for connecting AI tools to external systems. "USB-C for AI tools."

**Tool** — Any callable capability the model can invoke: read a file, run a shell command, search the web. MCP tools are one kind; harnesses also have built-in tools.

**Resource (MCP)** — A read-only data source an MCP server exposes to the model. The model can read it but not change it. Examples: a file tree, a database schema, a list of open PRs.

**Prompt** — The text you send to the model. Includes the task, the context, and any tool output fed back in.

**System prompt** — Instructions the harness sets (that you usually do not see) telling the model who it is, what tools it has, and how to behave. When you write an `AGENTS.md` or `.cursorrules` file, you are adding to the system prompt.

**Context window** — The working memory of a session, in tokens. Everything the model "knows" about your task lives here. When it fills, older content drops out.

**Context engineering** — (covered in §2.13) The practice of curating what goes into the context window, instead of just polishing the prompt wording.

**Token** — The unit the model processes text in. Roughly 4 characters of English. Context windows, model pricing, and speed are all measured in tokens.

**Embedding** — A vector (a list of numbers) that captures the meaning of a piece of text. Similar text has similar vectors. Used for semantic search.

**RAG (Retrieval-Augmented Generation)** — (covered in §2.9) Giving the model access to a searchable knowledge base at inference time, instead of pasting everything into the prompt.

**Vector database** — A store that lets you find vectors "closest" to a query vector. Used by RAG to find the most relevant documents.

**Fine-tuning** — Training a model further on examples of a specific task. Almost always the wrong answer for beginners; prefer prompting and RAG.

**Sampling** — How the model picks the next token: not always the most likely one. Controlled by knobs like temperature and top-p. (See §2.10.)

**Temperature** — A sampling knob (0 to ~2). Lower means more predictable; higher means more random. Code work usually wants low temperature.

**Chain-of-thought (CoT)** — (covered in §2.12) Asking the model to "think step by step" so it uses intermediate tokens to reason. Some models now do this automatically.

**Few-shot** — (covered in §2.12) Giving the model 2-5 examples in the prompt to teach it the pattern you want.

**Zero-shot** — Asking the model to do something without giving any examples. The default for most prompts.

**Prompt injection** — An attack where untrusted content the agent reads (a file, a web page) contains instructions that hijack its behavior. Critical to understand if your agent reads untrusted input.

**Tool call / Function call** — A structured call the model emits, asking the harness to run a specific function and feed the result back. The mechanism that lets the model "do" things.

**JSON Schema** — A standard for describing the shape of JSON data. MCP tool parameters are defined as JSON Schemas, which lets the harness validate tool calls before they reach the server.

**Stdio (transport)** — The most common way MCP servers run: as a local process communicating over standard input/output. The alternative is HTTP/SSE for remote servers.

**Skills CLI** — A package manager for the open agent skills ecosystem. `npx skills find <query>` searches for skills; `npx skills add <package>` installs one.

**Lock file** (`skills-lock.json`, `pnpm-lock.yaml`, etc.) — A file that pins the exact versions of installed packages. Makes installs reproducible across machines.

**AGENTS.md / CLAUDE.md / .cursorrules** — Project-level files that add to the model's system prompt. They tell the model "this is how we work here" — naming conventions, lint commands, what not to touch. A powerful lever most beginners do not realize they have.

**Knowledge graph** — A structured representation of a codebase (nodes = files, functions, classes; edges = calls, imports, contains). Some tools build one to let the agent answer "how does X work?" without reading every file. See §5.6 examples.

**Eval** — A test for an AI workflow: a set of inputs and expected outputs used to measure whether a prompt or tool change made things better or worse. Professionals run evals before adopting a change; beginners trust their gut.

**Guardrails** — Safety rules the harness enforces, like "ask before running shell commands" or "never edit files outside the project directory." Most harnesses ship with sensible defaults; you can tighten or loosen them.

---

_Handbook continues in subsequent sections. See Table of Contents._

---

## 3. Prompting Discipline for Code Work

Even with great tools, the prompt sets the task. Bad prompts waste tokens, produce wrong output, and cause cascading errors in agentic loops.

### 3.1 The Four-Part Prompt

A good code prompt has four parts, in this order:

1. **Goal**: what you want, stated concretely.
2. **Context**: the relevant files, the error, the test that fails, the design constraint.
3. **Constraints**: style guide, library choices, what NOT to touch, performance budget.
4. **Done condition**: how you will know the task is complete.

Bad example:

> fix the login bug

Good example:

> **Goal**: The login endpoint returns 500 instead of 401 when the password is wrong.
>
> **Context**: `src/auth/login.ts:42` calls `verifyPassword`, which throws when the hash does not match. The handler at `src/auth/login.ts:88` catches the wrong exception type.
>
> **Constraints**: do not change the public API. Use the existing `AuthError` class. Do not add new dependencies.
>
> **Done**: `npm test auth` passes, and `curl -X POST /login` with a wrong password returns 401 with the `AuthError` JSON body.

The second prompt is longer to write but saves a round trip and prevents the model from "fixing" things you did not ask it to touch.

### 3.2 The Spec, Implement, Verify Loop

For anything non-trivial, structure the work as three explicit phases:

- **Spec**: write down what the code should do, in the prompt or a file the agent reads.
- **Implement**: let the agent write the code.
- **Verify**: run the tests, read the diff, check edge cases. If wrong, feed the failure back into the spec and loop.

When the agent writes code without a spec, it will guess. Guesses are usually reasonable and often subtly wrong in ways that compound. The spec forces you to think before the agent writes.

### 3.3 Anti-Patterns

**Prompt-as-task-dump**: pasting a Jira ticket with 800 words of business context and asking the agent to "just do it." The agent will get lost. Translate business language into engineering language first.

**Trust-without-verify**: accepting the first response because it looks plausible. The model is fluent even when it is wrong. Fluency is not correctness.

**"Do it again but better"**: a prompt that gives the model no signal about what was wrong. Always tell it specifically what failed and what would be better.

**Vague scope**: "refactor this module" with no constraints. The model will rewrite everything, including things you wanted kept. Always say what is in scope and what is out.

**Premature decomposition**: breaking a small task into many sub-prompts when one good prompt would do. Each handoff loses context. Decompose when context is genuinely too large or when subtasks are truly independent.

---

## 4. MCP (Model Context Protocol)

### 4.1 What MCP Is

The Model Context Protocol is an open standard, introduced by Anthropic in November 2024, for connecting AI applications to external data sources and tools. Before MCP, every integration between an LLM and an external system was bespoke: a custom function, a custom prompt, a custom client. MCP standardizes that integration so that a tool written once works with any MCP-compatible client.

The analogy that stuck is "USB-C for AI tools." A more precise analogy: MCP is to AI tools what LSP (Language Server Protocol) is to editors. One server, many clients.

### 4.2 Why MCP Matters

Three concrete benefits:

1. **Tool reuse.** A community-written `mcp-server-github` works with Claude Desktop, Cursor, opencode, Continue, and any other MCP client. You do not write a separate integration for each.
2. **Local-first by default.** Most MCP servers run as a local stdio process on your machine. Your data does not leave your machine unless you choose a remote server. This matters for security and for latency.
3. **Composability.** You can run many MCP servers at once. The client surfaces all their tools to the model. The model picks which to call.

### 4.3 Anatomy of MCP

Four concepts:

| Concept | What it is | Example |
| :--- | :--- | :--- |
| **Server** | A program that exposes capabilities via the protocol. Can be local (stdio) or remote (HTTP/SSE). | `mcp-server-filesystem` exposing your project directory. |
| **Client** | The AI application that connects to servers and surfaces their tools to the model. | Claude Desktop, Cursor, opencode. |
| **Tools** | Callable functions the server exposes. Each has a name, a description, and a JSON Schema for its parameters. | `read_file(path)`, `search_repo(query)`, `create_issue(title, body)`. |
| **Resources** | Read-only data sources the server exposes. The model can read but not modify. | A file tree, a database schema, a list of open PRs. |

The model never talks to the server directly. The client mediates: it lists the tools to the model, the model emits a tool call, the client forwards it to the server, the server returns a result, the client feeds it back to the model. The model only sees text in, text out.

### 4.4 Installing an MCP Server

The exact command varies by client, but the pattern is the same: you tell the client how to launch the server process, and the client does the rest.

In opencode, MCP servers are declared in `opencode.json`:

```json
{
  "mcp": {
    "github": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx" }
    },
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "/Users/me/project"]
    }
  }
}
```

In Claude Desktop, the same servers go into `claude_desktop_config.json`. In Cursor, into `.cursor/mcp.json`. The server definitions are portable; only the config file location differs.

### 4.5 Anatomy of a Tool Definition

When the client connects to a server, it asks: "what tools do you have?" The server replies with a list. Each tool definition has three parts:

```json
{
  "name": "search_repo",
  "description": "Search a GitHub repository for code matching a query. Returns matching file paths and line numbers.",
  "inputSchema": {
    "type": "object",
    " properties": {
      "query": { "type": "string", "description": "Code or text to search for." },
      "repo": { "type": "string", "description": "Full repo name, e.g. owner/name." }
    },
    "required": ["query", "repo"]
  }
}
```

- **`name`**: the identifier the model uses to call the tool.
- **`description`**: the most important field. The model uses this to decide when to call the tool. A vague description ("search") means the model will guess wrong; a specific one ("search a GitHub repo for code matching a query") means the model calls it at the right time.
- **`inputSchema`**: a JSON Schema. This is how the model knows what arguments to pass. The schema also validates the model's call before it reaches the server.

### 4.6 Finding MCP Servers

Two good starting points:

- **Official reference servers**: `@modelcontextprotocol/server-*` on npm. Covers filesystem, GitHub, GitLab, Google Drive, Slack, Postgres, SQLite, Fetch, Puppeteer, and more.
- **Community registries**: `mcp.so` and the `awesome-mcp-servers` GitHub list aggregate hundreds of third-party servers.

Before installing a community server, check: who maintains it, does it have tests, when was it last updated, what does it do with your data? A malicious or buggy MCP server has whatever file and network access you grant the process. Treat it like any other dependency: review before trust.

### 4.7 Writing Your Own MCP Server

If no existing server does what you need, write one. The protocol is simple and SDKs exist for TypeScript, Python, Go, and Rust. A typical server is 50-200 lines: define a few tools, wire them to your existing functions, return the results as text or structured data.

The most common mistake in authoring servers is writing tool descriptions that are too short. The model only has the description to go on. If you write `name: "get_issue", description: "get an issue"`, the model will call it for any issue-shaped request and pass wrong arguments. Spend as much care on the description as on the implementation.

### 4.8 MCP vs. Custom Function Calling

If you have used OpenAI function calling or Claude tool use, you may ask: "Why do I need MCP?" The answer: you do not, for a single client. But the moment you want to share the tool across clients, or swap clients, or let a teammate use the same integration, MCP saves you from rewriting the same glue for each one. It is a portability and reuse standard, not a capability the model did not have before.

---

## 5. Agent Skills

### 5.1 What a Skill Is

A skill is a packaged unit of workflow knowledge that an agent loads on demand. Concretely: a folder containing a `SKILL.md` file (the instructions the agent reads) plus whatever scripts, references, and templates the skill needs to do its job.

Think of it this way:

- A **tool** (MCP or otherwise) is a single capability: "read a file," "run a test," "search the web."
- A **skill** is a procedure that uses tools: "review a pull request by reading the diff, checking the style guide, running the tests, and writing a structured report."

The tool is a verb. The skill is a recipe.

### 5.2 Skills vs. MCP Tools

| Aspect | MCP Tool | Skill |
| :--- | :--- | :--- |
| Granularity | One capability | One workflow (uses many tools) |
| Format | JSON Schema over the protocol | A markdown file plus supporting files |
| Lives where | In a running server process | On the filesystem, loaded when needed |
| Authored by | Server developer | Anyone, often the team itself |
| Loaded when | Always (while server runs) | On demand, when the task matches |
| Example | `grep_search(pattern, path)` | "Review a PR against our code style guide" |

Skills and MCP tools compose: a skill's instructions tell the agent which tools to call, and the tools do the actual work.

### 5.3 The SKILL.md Format

A skill is a folder with a `SKILL.md`. The file has a short description that the agent matches against the user's task, and a longer body of instructions that the agent reads when the skill is activated.

```
.agents/skills/
  pr-review/
    SKILL.md
    checklist.md
    style_guide.md
    scripts/
      diff_stat.sh
```

A minimal `SKILL.md`:

```markdown
# Skill: Pull Request Review

**When to use**: The user asks to "review a PR", "check this pull request",
or otherwise wants a structured review of a GitHub pull request.

## Workflow

1. Run `gh pr diff <PR_NUMBER>` to get the diff.
2. Read the changed files for context (not just the diff).
3. Check each change against `checklist.md`.
4. Check style against `style_guide.md`.
5. Run `scripts/diff_stat.sh <PR_NUMBER>` for a summary.
6. Write a structured review with sections: Summary, Risks, Suggestions, Approval.
```

That is the whole format. The skill tells the agent what to do; the agent already knows how to read files, run shell commands, and write text.

### 5.4 When to Author a Skill

Author a skill when you find yourself giving the same multi-step instructions repeatedly. If you have typed "review this PR by checking the diff, the style guide, and the tests" three times, write the skill once.

Do NOT author a skill for:

- A single tool call (just use the tool).
- A one-off task (just do it).
- Something the model already does well without instructions (the skill adds nothing).

### 5.5 Skill Discovery

Different clients handle skill discovery differently. The common patterns:

- **Directory convention**: the client scans `.agents/skills/` or `~/.agents/skills/` for `SKILL.md` files. Each skill's short description becomes a match candidate.
- **Explicit registration**: the client config lists skill paths.
- **Lock file**: a `skills-lock.json` records which skills are installed and from where.

In opencode, skills live under `.agents/skills/<name>/SKILL.md` in the project or `~/.agents/skills/` globally. The skill tool loads them by name when a task matches.

### 5.6 Sharing Skills

Because a skill is just files, sharing is straightforward: commit it to the repo, or publish it as a Git repo that others clone into their own `.agents/skills/`. A `skills-lock.json` pins versions for reproducibility, the same way `package-lock.json` does for npm.

The same review discipline applies as for MCP servers: review a skill's instructions and scripts before running them, especially if a skill runs shell commands or makes network calls.

### 5.7 Worked Examples: Real Skills and Why They Save Tokens

The best way to understand skills is to look at real ones. Below are six skills (five from the global `~/.agents/skills/` directory, one from this project's `.agents/skills/`). For each: what it does, what it replaces, and roughly how many tokens it saves per session.

The math is approximate — 1 line of markdown is roughly 10-15 tokens — but the shape of the saving is what matters.

#### Example 1: `gitnexus-exploring` (78 lines)

**What it does**: Tells the agent how to answer "how does X work in this codebase?" using the GitNexus knowledge graph — instead of reading every file.

**What it replaces**: Without the skill, you would have to say: "Read the README, then look at the directory structure, then open src/, then grep for X, then read the files that mention X, then trace the calls, then summarize." Every file read is 200-2000 tokens into the context window. For a real codebase, exploring one question can burn 20,000-50,000 tokens.

**Why it saves tokens**: The skill points the agent at a pre-built knowledge graph (a single JSON file with nodes and edges). The agent greps the graph for the keyword instead of reading source files. A grep result is 100-500 tokens; reading 10 source files is 10,000+ tokens. **Typical saving: 15,000-40,000 tokens per exploration task.**

#### Example 2: `understand-chat` (55 lines)

**What it does**: Same idea as above, for the `understand-anything` knowledge graph. Tells the agent to grep the graph JSON instead of dumping the whole file into context.

**What it replaces**: Without the skill, a common beginner move is "load the whole knowledge graph into context" — but a real graph can be 50,000-500,000 tokens. That instantly fills the window.

**Why it saves tokens**: The skill's instructions explicitly say "Search the file with Grep BEFORE reading it. Only read sections you need." This is the difference between 500 tokens (a grep result) and 50,000 tokens (the whole graph). **Typical saving: 40,000+ tokens per session.** Without this discipline, the session fails outright — the window cannot hold the graph.

#### Example 3: `parallel-execution` (241 lines)

**What it does**: Tells the agent how to spawn multiple subagents in parallel — and crucially, that all `Task` calls must be in ONE assistant message for true parallelism.

**What it replaces**: Without the skill, the agent might spawn subagents one at a time, each waiting for the previous to finish. Or it might inline all the work into the main context, burning tokens on every file read.

**Why it saves tokens**: Two ways. (1) Parallelism: 5 subagents running at once finish in roughly the time of 1, not 5. (2) Context isolation: each subagent does its reads in its OWN context window, then returns a short summary. The main context only sees the summaries, not the 10,000 tokens of files each subagent read. **Typical saving: 30,000-60,000 tokens in the main context** for a 5-way parallel task.

#### Example 4: `youtube-video-analyst` (253 lines)

**What it does**: A multi-step forensic analysis of a YouTube transcript — extract hooks, retention mechanics, emotional beats, viral patterns, and produce a structured blueprint.

**What it replaces**: Without the skill, you would type out the entire analysis framework every time: "Read this transcript. Find the hooks. Identify the retention mechanics. Map the emotional journey. Extract reusable patterns. Score each element. Format as a blueprint." That is ~300 words of instructions you would repeat for every video.

**Why it saves tokens**: The skill loads once (253 lines ≈ 3,000 tokens) and then applies to every video. Without it, you retype the framework each session (~3,000 tokens each time) AND risk the model forgetting a step. Over 10 videos, the skill saves 10 × 3,000 = 30,000 tokens of repeated instructions — and more importantly, gives consistent results. **Typical saving: 3,000 tokens per session after the first.**

#### Example 5: `find-skills` (142 lines)

**What it does**: When a user asks "how do I do X?", the skill tells the agent to search the skills registry (skills.sh) before writing custom instructions from scratch.

**What it replaces**: Without the skill, the agent tries to solve the problem from scratch — often badly, reinventing a workflow that already exists as a maintained skill.

**Why it saves tokens**: Two ways. (1) Reuse: an existing skill is already battle-tested; using it avoids the model's first 3-5 failed attempts (each a few thousand tokens). (2) Quality: the right skill produces correct output the first time, avoiding the retry loop entirely. **Typical saving: 10,000-30,000 tokens** by avoiding failed attempts and rework.

#### Example 6: `agent-swarm` (80 lines)

**What it does**: Tells the agent how to orchestrate multi-agent swarms via the Flow Nexus MCP server — initialize a swarm, spawn agents, assign tasks, monitor, scale, destroy.

**What it replaces**: Without the skill, the agent has to figure out the MCP tool names (`mcp__flow-nexus__swarm_init`, `mcp__flow-nexus__agent_spawn`, etc.) by listing the server's tools and guessing the parameters. Each tool listing is 500-1,000 tokens, and wrong guesses cost a round trip.

**Why it saves tokens**: The skill gives the exact tool names and parameter shapes as worked examples in markdown. The agent reads 80 lines (~1,000 tokens) and calls the tools correctly the first time, instead of listing tools, guessing, failing, and retrying. **Typical saving: 3,000-8,000 tokens** per orchestration task.

### 5.8 The Pattern: Why Skills Reduce Tokens

Looking at the six examples above, the token savings come from four mechanisms. This is the underlying reason skills work — understand the mechanism and you can predict when a skill will help.

| Mechanism | What it does | Example skill | Saving |
| :--- | :--- | :--- | :--- |
| **Avoid reading the whole thing** | Point the agent at a searchable index (graph, grep, vector DB) instead of loading files | `gitnexus-exploring`, `understand-chat` | 15,000-50,000 tokens |
| **Context isolation via subagents** | Spawn subagents with their own context; main context only sees the summary | `parallel-execution` | 30,000-60,000 tokens |
| **Reuse a workflow instead of retyping it** | Load the framework once; apply to every future task | `youtube-video-analyst` | 3,000 tokens/session after first |
| **Avoid failed attempts and retries** | Give exact tool names and parameter shapes as examples, so the agent gets it right first try | `find-skills`, `agent-swarm` | 3,000-30,000 tokens |

The unifying principle: **a skill is a way to spend 1,000-3,000 tokens of instructions once, to save 10,000-50,000 tokens of reading, retrying, and re-typing on every session afterward.** That is why professionals author skills for any workflow they run more than twice.

If you remember nothing else from this section, remember the shape of the trade:

- **Without a skill**: the model reads files, guesses tool parameters, retries on failure, and you retype the workflow every time. Token cost: high and repeated.
- **With a skill**: the model reads a short instruction file once, follows the workflow, calls tools correctly the first time. Token cost: low and one-time.

That gap — often 10x or more per session — is why skills exist.

---

## 6. Agentic Workflow Patterns

### 6.1 When to Use an Agentic Workflow (and When Not To)

An agentic workflow is the right choice when the task has three properties:

1. **Multi-step**: the task cannot be done in one shot. It requires reading, editing, testing, and iterating.
2. **Verifiable**: there is a concrete signal the agent can check — a test passing, a build succeeding, a diff looking right.
3. **Bounded**: you can describe the done condition clearly enough that the agent knows when to stop.

If any of these is missing, use direct chat instead:

- **Single-shot question** (what does this function do?): direct chat is faster.
- **Unverifiable creative task** (write a marketing email): direct chat gives you the output to edit yourself.
- **Unbounded task** ("improve the codebase"): the agent will thrash. Narrow the scope first.

### 6.2 Pattern: Direct Edit

The simplest pattern. You ask the agent to make a change, it edits the file directly, you review the diff.

```
User: rename `getUserData` to `fetchUserProfile` everywhere
Agent: [runs grep, edits 7 files, runs the test suite, reports]
```

Use this for mechanical, well-scoped changes. The agent does the boring part, you verify.

### 6.3 Pattern: Plan Then Execute

For non-trivial tasks, ask the agent to plan first, then execute only after you approve the plan.

```
User: add pagination to the users list endpoint. Show me a plan first.
Agent: [reads the code, writes a plan]
  1. Add `page` and `pageSize` query params to the route schema.
  2. Modify the query in `userRepo.list()` to accept offset/limit.
  3. Update the response shape to include `total` and `page`.
  4. Add tests in `users.test.ts`.
  5. Update the API doc.
User: looks good, go.
Agent: [executes each step, runs tests, reports]
```

This catches scope creep early. It is much cheaper to reject a plan than to undo 12 file edits.

### 6.4 Pattern: Subagent Delegation

When a task has independent parts, the main agent can spawn subagents to work in parallel. Each subagent gets its own context window, does its piece, and returns a result. The main agent then assembles.

Example: "refactor the auth module and update the docs."

- Subagent A: refactor `src/auth/` (reads code, edits, runs auth tests).
- Subagent B: update `docs/auth.md` (reads the new code, rewrites the docs).
- Main agent: verifies both are consistent and the build passes.

Use subagents when:

- The parts are truly independent (otherwise they will conflict on the same files).
- Each part needs a lot of context (subagents keep the main context clean).
- You want parallelism (multiple subagents can run at once).

Avoid subagents when the work is sequential and tightly coupled — the overhead of splitting outweighs the benefit.

### 6.5 Pattern: Explore-Then-Edit

For unfamiliar codebases, the first phase is exploration (read-only), the second is editing. Splitting them prevents the agent from making changes based on a misunderstanding.

```
Phase 1 (Explore):
  Agent: [reads package.json, README, directory tree, key files]
  Agent: "I now understand the structure. The auth module is here, the DB layer is here. Where would you like me to start?"

Phase 2 (Edit):
  User: start with the auth module.
  Agent: [makes changes, runs tests]
```

This pattern is especially valuable when joining an existing project. It mirrors what a human engineer does on day one.

### 6.6 Pattern: Verify-and-Loop

The agent makes a change, runs the verification (tests, build, lint), reads the failure if any, and iterates until green.

```
Agent: [edits code]
Agent: [runs `npm test`] -> 2 failures
Agent: [reads failures, edits code]
Agent: [runs `npm test`] -> 1 failure
Agent: [reads failure, edits code]
Agent: [runs `npm test`] -> all pass
Agent: done.
```

This is where the agentic loop shines: the agent can catch its own mistakes without a round trip to you. Set a cap on iterations (3-5) to avoid infinite loops on problems that need human judgment.

### 6.7 Context Management

The most common failure mode of a long agentic session is context exhaustion: the window fills, important early context drops, and the agent starts repeating itself or losing track.

Tactics:

- **Re-scope mid-session**: if the task drifts, stop the agent, write a fresh prompt with the current state, and continue.
- **Use subagents for big reads**: instead of reading a 10,000-line log into the main context, have a subagent read it and return a summary.
- **Checkpoint with git**: commit after each meaningful step. If the agent goes off the rails, you can reset to the last good state without losing work.
- **Watch the token counter**: most clients show context usage. When you cross 60-70%, start wrapping up or spawning a fresh session.

### 6.8 When to Intervene

Intervene immediately when:

- The agent edits files you did not ask it to touch.
- The agent runs commands with side effects (deploys, emails, payments) without confirmation.
- The agent is stuck in a loop (same failed action twice).
- The agent's plan diverges from the task.

Do NOT intervene every step. The point of an agentic workflow is to let the agent run. If you micromanage every action, you lose the benefit and you may as well drive each tool call yourself.

---

## 7. Concrete Tooling Walkthrough

This section walks through how the concepts above look in real tools. The tools change fast; the patterns do not.

### 7.1 opencode (Terminal-Native Agentic CLI)

opencode is a terminal-native AI coding agent. You run it in your project directory, it has file and shell tools, and it can use MCP servers and skills.

**Starting a session:**

```bash
cd my-project
opencode
```

**Typical workflow for a bug fix:**

1. Describe the bug in a prompt: "The login endpoint returns 500 when the password is wrong. The handler is in `src/auth/login.ts`."
2. opencode reads the file, finds the bug, proposes a fix.
3. You approve the edit (or opencode applies it directly, depending on config).
4. opencode runs `npm test auth`. If it fails, it reads the failure and iterates.
5. When tests pass, opencode stops and reports.

**Adding an MCP server** (e.g. GitHub):

Edit `opencode.json` in the project root:

```json
{
  "mcp": {
    "github": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx" }
    }
  }
}
```

Restart opencode. Now the agent can call `create_issue`, `search_repo`, `get_pr_diff`, and so on — you did not write any glue code.

**Adding a skill:**

Drop a folder under `.agents/skills/`:

```
.agents/skills/pr-review/SKILL.md
```

The next time you ask opencode to "review PR 42," it loads the skill and follows the workflow you wrote.

### 7.2 Claude Code

Claude Code is Anthropic's terminal agentic tool. Similar shape to opencode: terminal-native, file and shell tools, MCP support, agentic loop.

Key differences from opencode:

- Bundled with Claude models (Sonnet, Opus).
- MCP config lives in `claude_desktop_config.json` (shared with Claude Desktop).
- Strong default safety: it asks for confirmation on file writes and shell commands until you grant broader permission.

When to choose Claude Code: when you want the Claude models specifically, or when you value its conservative-by-default safety posture.

### 7.3 Cursor

Cursor is a VS Code fork with AI tightly integrated. Less terminal-native than opencode or Claude Code, more editor-native.

**What Cursor does well:**

- Inline edits with `Cmd+K` (select code, describe the change, accept or reject the diff).
- Tab autocomplete trained on your codebase (faster than generic Copilot).
- "Composer" mode: a multi-file agentic edit that can span many files at once.
- MCP support via `.cursor/mcp.json` (same server definitions as everywhere else).

**When to choose Cursor:** when you prefer a GUI editor and want AI woven into editing rather than driving from the terminal.

### 7.4 Aider

Aider is an open-source terminal coding agent, older than the others. It has its own conventions (a `.aider.conf.yml` config, a `REPO.md` project summary it maintains automatically).

Strengths: mature, scriptable, git-integrated (it commits each change with a generated message by default).

When to choose Aider: when you want a scriptable, git-first agent and are happy with its model routing.

### 7.5 Claude Desktop (with MCP)

Claude Desktop is not a coding tool per se — it is a chat application that supports MCP. But it is the easiest way to try MCP servers without a coding agent.

Typical use: install the filesystem server, point it at a project directory, and ask Claude to read files and explain them. Good for exploration and learning the protocol; less good for actual edits because Claude Desktop does not have the agentic editing loop of opencode or Claude Code.

### 7.6 Choosing Among Them

| Tool | Best for | Style |
| :--- | :--- | :--- |
| **opencode** | Terminal-native agentic work, model-agnostic | CLI, multi-model |
| **Claude Code** | Claude models, conservative safety | CLI, Anthropic models |
| **Cursor** | Editor-integrated AI, inline edits | GUI, VS Code-based |
| **Aider** | Git-first scripting, open source | CLI, scriptable |
| **Claude Desktop** | Trying MCP without a coding agent | GUI, chat-based |

The right answer is often "two of them." Many developers use a terminal agent (opencode or Claude Code) for multi-step agentic work and an editor (Cursor or VS Code + Copilot) for inline edits. They share the same MCP servers and the same project.

### 7.7 A Concrete Session, Start to Finish

Here is what a real session looks like, end to end, using opencode on this very repo:

1. **Start in the project directory.** `cd PrologueOfSpacetime && opencode`.
2. **Scope the task.** "Audit the changelog directory for broken links and hardcoded paths. Report what you find; don't change anything yet."
3. **Agent explores.** Reads `docs/changelog/`, finds 38 hardcoded `file:///` paths, reports.
4. **Approve a plan.** "Fix them all to repo-relative paths. Don't touch any other content."
5. **Agent edits.** Rewrites the paths, runs a grep to verify none remain.
6. **Verify.** "Run `grep -r 'file:///Users' docs/changelog/` and confirm zero matches."
7. **Commit.** `git add docs/changelog && git commit -m "fix: replace hardcoded paths with repo-relative in changelog"`.
8. **Move on.** Next task, same session or a fresh one.

Notice the rhythm: scope, plan, execute, verify, commit. That rhythm is the professional workflow in miniature.

---

## 8. Code of Conduct and Professional Practice

This is the section that separates the professional from the casual user. Everything before this point was about how to use the tools. This section is about how to use them responsibly.

### 8.1 The First Rule: You Are Responsible

Code you commit is your code. A bug the AI introduced is still your bug. A license the AI violated is still your violation. A security hole the AI left is still your hole. "The AI did it" is not a defense in a code review, an audit, or a courtroom.

This means: you read every line the AI writes before you commit it. You run the tests. You check the licenses. You own the result.

### 8.2 Verification Discipline

**Never trust the first output.** The model is fluent even when it is wrong. Fluency is not correctness. Three concrete verification habits:

1. **Read the diff.** Not the summary the agent gives you — the actual `git diff`. Summaries hide mistakes.
2. **Run the tests.** If there are no tests, write one. If you cannot write a test, do the change manually to confirm it works.
3. **Check the edge cases.** The AI handles the happy path well. It misses null inputs, empty lists, concurrent access, Unicode, timezones, and off-by-one. Probe those yourself.

If you skip verification because "it looks right," you will eventually commit a confidently wrong change. The confidence is the model's, not yours.

### 8.3 Security

AI coding tools have file and shell access on your machine, and they can make network calls. Treat them like any other privileged process.

- **Read the MCP server code before you trust it.** A malicious server can exfiltrate your files, run arbitrary shell, or plant backdoors. Prefer official servers and well-reviewed community ones.
- **Read the skill scripts before you run them.** A `SKILL.md` is just instructions, but the scripts in the skill folder run with your privileges.
- **Do not put secrets in prompts.** Anything in the prompt can end up in logs, in the model's training data (depending on the provider), or in a context that another tool reads. Use environment variables and secret managers; let tools read those, not the prompt.
- **Watch for prompt injection.** If the agent reads a file or a web page, that content becomes part of the prompt. A malicious file can instruct the agent to do something you did not ask for. Be especially careful with agents that have shell access and read untrusted files (e.g. a skill that reviews PRs from strangers).
- **Principle of least privilege.** Give the agent the minimum tools it needs. Do not enable the GitHub MCP server if the task only needs the filesystem. Do not grant shell access if the task only needs file reads.

### 8.4 Intellectual Property and Licensing

Three concerns:

1. **Model training data.** Some providers train on your prompts; some do not. Know which is which for the model you use, and choose a "no training" mode (often a paid plan or an API flag) for work where this matters.
2. **Output licensing.** Code the model produces may resemble code it was trained on. In practice this is rarely a problem for short snippets, but for substantial blocks of code you should check the license of any obvious source. Some enterprises ban AI-generated code in certain modules for this reason; respect the ban.
3. **Open source compliance.** If the AI suggests code from a GPL-licensed project and you paste it into a proprietary codebase, you have created a license violation. The AI will not warn you. You must check.

Rule of thumb: if the AI's output is substantial (more than a few lines) and looks like it came from a specific project, find the source and check its license.

### 8.5 Attribution

When you commit AI-assisted code, the question is not "did the AI write this?" but "can a reviewer understand the provenance?" Three habits:

- **Commit messages**: mention AI assistance when substantial. `feat: add pagination (AI-assisted, reviewed)` is honest. `feat: add pagination` is fine for small mechanical changes.
- **Code review**: when you open a PR, be ready to explain any line the AI wrote. If you cannot explain it, you do not understand it, and you should not merge it.
- **Co-author trailers**: some teams use `Co-Authored-By: Claude <noreply@anthropic.com>` trailers. This is a style choice; the important thing is that the human author takes responsibility.

### 8.6 When NOT to Use AI

There are tasks where AI makes things worse. Recognize them:

- **Untested critical paths**: if a bug in this code would cause data loss, financial harm, or safety risk, do not let the AI write it unsupervised. Use it as a pair programmer, not an autopilot.
- **Compliance-regulated code**: HIPAA, PCI, SOX, FDA, automotive ISO 26262 — these regimes require traceability that AI-assisted code can complicate. Check with your compliance team first.
- **Code you do not understand**: if you cannot tell whether the AI's output is correct, you are not ready to use it for this task. Learn the domain first, then use the AI to speed up what you already understand.
- **Trivial mechanical changes**: if a sed one-liner does the job, do not spin up an agent. It is slower and less reliable for one-liners.
- **Sensitive conversations**: performance reviews, security disclosures, HR matters. The model has no judgement; you do.

### 8.7 Team Norms

If you work on a team, agree on:

- Which tools are allowed (some enterprises ban specific providers).
- Which models are allowed (cost and data-handling differ).
- How AI-assisted commits are marked.
- Which MCP servers and skills are pre-approved.
- A review policy for new MCP servers and skills (treat them like new dependencies).

Write these down. A norm that is not written down is a norm that does not exist.

### 8.8 Cost Awareness

AI coding tools cost money. The model bills per token, and an agentic session can easily burn through tens of thousands of tokens reading files and running tools. Three habits:

- **Watch the spend dashboard** for your provider. Surprises are unpleasant.
- **Prefer cheaper models for mechanical work.** A fast, cheap model (Haiku, Flash, Mini) is often enough for renames, format fixes, and grep-style tasks. Save the expensive models for hard reasoning.
- **Scope the task.** A vague prompt leads to a long agentic loop. A scoped prompt ends fast and costs less.

### 8.9 Honesty About What You Did

The most important code of conduct rule is also the simplest: be honest. If the AI wrote 90% of a PR and you reviewed it, say so. If you do not understand a line, say so. If the AI broke something and you caught it in review, say so.

The goal of AI coding tools is not to outsource your judgement. It is to let you apply your judgement to more work. Keep your judgement engaged and everything else follows.

---

## 9. The Reference Workflow

A single-page summary you can pin above your desk. This is the professional agentic workflow, end to end.

### 9.1 Before the Session

1. **State the goal.** Write it down. One sentence.
2. **List the context.** Which files, which error, which test. Do not dump everything; list what is relevant.
3. **Set the constraints.** What is in scope, what is out, what must not change.
4. **Define done.** A test that passes, a build that succeeds, a diff that looks right.

### 9.2 During the Session

1. **Plan first.** Ask the agent for a plan. Reject or adjust before it edits.
2. **Verify at each step.** Read the diff after each edit. Run the tests after each change.
3. **Commit checkpoints.** Commit after each meaningful step. Reset if the agent drifts.
4. **Watch context usage.** Re-scope or split when usage crosses ~70%.

### 9.3 After the Session

1. **Read the full diff** one more time, not the agent's summary.
2. **Run the full test suite**, not just the tests the agent ran.
3. **Check the licenses** of any new dependencies the agent introduced.
4. **Mark the commit** honestly if AI-assisted.
5. **Open the PR** with a description a reviewer can understand.

### 9.4 Quick Reference: Tool Selection

| Task | Tool |
| :--- | :--- |
| Rename a symbol across the repo | agentic CLI (opencode, Claude Code) |
| Explain an unfamiliar function | direct chat (Claude Desktop, ChatGPT) |
| Inline edit in a file you have open | editor AI (Cursor Cmd+K, Copilot) |
| Multi-step refactor with tests | agentic CLI with plan-first pattern |
| Review a PR | agentic CLI with a `pr-review` skill |
| Search a large codebase | agent with grep/search tools (not loading all files into context) |
| One-off shell one-liner | just run the shell command |
| Hard architectural decision | direct chat with a strong model, then implement yourself |

### 9.5 Quick Reference: When to Stop

Stop the agent and take over manually when:

- It edits files outside the agreed scope.
- It runs the same failing command twice in a row.
- It asks for confirmation on the same kind of action repeatedly (scope the permission or stop).
- Its plan has diverged from the task.
- You cannot explain the last diff it produced.

Stopping is not failure. It is the professional move when the agent has hit the limit of what it can do safely.

---

## 10. Glossary

**Agent** — An AI system that runs the agentic loop (observe, reason, act) using tools, possibly for many steps before needing human input.

**Agentic loop** — The observe-reason-act cycle that an agent runs repeatedly until the task is done or it gets stuck.

**Context window** — The working memory of a model session, measured in tokens. Everything the model knows about the current task lives here.

**Function calling / Tool use** — The model's ability to emit a structured call to a function, which an external system executes and feeds back. Predates MCP.

**JSON Schema** — A standard for describing the shape of JSON data. MCP tool parameters are defined as JSON Schemas.

**LSP (Language Server Protocol)** — An open standard for editors to talk to language tools. Useful analogy for MCP: same shape of problem (one server, many clients), different domain.

**MCP (Model Context Protocol)** — An open standard for connecting AI applications to external data sources and tools. "USB-C for AI tools."

**MCP client** — The AI application (Claude Desktop, Cursor, opencode) that connects to MCP servers and surfaces their tools to the model.

**MCP server** — A program that exposes tools and resources via the MCP protocol. Can be local (stdio) or remote (HTTP/SSE).

**MCP tool** — A callable function exposed by an MCP server. Has a name, a description, and a JSON Schema for parameters.

**Prompt** — The text the user (and the client, on the user's behalf) sends to the model. Includes the task, the context, and any tool output fed back in.

**Prompt injection** — An attack where untrusted content (a file, a web page) read by the agent contains instructions that hijack its behavior.

**Resource (MCP)** — A read-only data source an MCP server exposes. The model can read but not modify.

**Skill** — A packaged unit of workflow knowledge (a `SKILL.md` plus supporting files) that an agent loads on demand.

**Subagent** — A secondary agent spawned by a main agent to work on an independent subtask, with its own context window.

**Token** — The unit the model processes text in. Roughly 3-4 characters of English, less for code. Context windows are measured in tokens.

**Tool** — Any callable capability the model can invoke: read a file, run a shell command, search the web, call an API. MCP tools are one way to expose tools; not the only way.

---

## 11. Further Reading

### 11.1 Specifications and Docs

- **MCP specification**: https://modelcontextprotocol.io — the official protocol site, with the spec, SDKs, and a list of reference servers.
- **Anthropic MCP announcement** (November 2024): the original blog post introducing the protocol.
- **opencode docs**: https://opencode.ai — configuration, MCP, skills, and the agentic loop.
- **Claude Code docs**: Anthropic's documentation for Claude Code.
- **Cursor docs**: https://cursor.com/docs — editor AI, Composer, MCP configuration.

### 11.2 Reference Servers to Study

- `@modelcontextprotocol/server-filesystem` — the simplest reference server. Read its source to learn the shape of an MCP server.
- `@modelcontextprotocol/server-github` — a real-world server with auth, pagination, and many tools.
- `@modelcontextprotocol/server-postgres` — a database-backed server; good model for read-only data exposure.

### 11.3 Essays Worth Reading

- **"Tools, Not Prompts"** — the argument that tool configuration beats prompt engineering. A useful framing even if you disagree with the strong form.
- **"The Spec, Implement, Verify Loop"** — a write-up of the three-phase discipline applied to AI-assisted coding.
- **Anthropic's "Building Effective Agents"** — a short essay on when to use agents vs. workflows, and the patterns that work.

### 11.4 Skills to Study

This very repo contains skills under `.agents/skills/` that are good examples of the format:

- `youtube-video-analyst` — a multi-step workflow skill with scripts and references.
- `gitnexus-*` skills — skills that wrap a CLI tool and expose its workflow to an agent.

Read a few `SKILL.md` files to get a feel for what a good skill looks like before authoring your own.

### 11.5 Code of Conduct References

- Your employer's AI policy (if one exists; if not, propose one).
- The Open Source Initiative's guidance on AI-generated code in open source projects.
- Your model provider's data handling policy — read it, do not assume.

---

*End of handbook. Last updated 2026-06-25. Suggestions and corrections welcome; this document is meant to be revised as the tools and conventions evolve.*
