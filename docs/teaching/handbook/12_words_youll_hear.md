---
title: 'Chapter 12 — The Words You'll Hear'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Grammar]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 12
liberal_art: Trivium-Grammar
audience: beginner
---

# Chapter 12 — The Words You'll Hear

> A plain-language glossary of the terms you will see in docs, chats, and changelogs. If a word is new to you, look it up here.

---

## The Simple Version

The vocabulary around AI coding is still being invented. Here is a glossary of terms that have become common. You do not need to use these words to use the tools — but you will see them, so it helps to know what they mean.

---

## A–Z Glossary

### Agent
An AI system that runs the observe-reason-act loop on its own, possibly for many steps, using tools. "Agent" is used loosely; sometimes it means the whole tool, sometimes just one run of the loop.

### AGENTS.md / CLAUDE.md / .cursorrules
Project-level files that add to the AI's system prompt. They tell the AI "this is how we work here" — naming conventions, lint commands, what not to touch. A powerful lever most beginners do not realize they have.

### Chain-of-Thought (CoT)
Asking the AI to "think step by step" so it uses intermediate tokens to reason. Some models now do this automatically.

### Context Engineering
The practice of curating what goes into the context window, instead of just polishing the prompt wording. See [Chapter 6](06_context_engineering.md).

### Context Window
The working memory of a session, in tokens. Everything the AI "knows" about your task lives here. When it fills, older content drops out. See [Chapter 4](04_tokens_and_context.md).

### Embedding
A vector (a list of numbers) that captures the meaning of a piece of text. Similar text has similar vectors. Used for semantic search.

### Eval
A test for an AI workflow: a set of inputs and expected outputs used to measure whether a change made things better or worse. Professionals run evals before adopting a change; beginners trust their gut.

### Few-Shot
Giving the AI 2-5 examples in the prompt to teach it the pattern you want. See [Chapter 5](05_prompting_styles.md).

### Fine-Tuning
Training a model further on examples of a specific task. Almost always the wrong answer for beginners; prefer prompting and RAG.

### Guardrails
Safety rules the harness enforces, like "ask before running shell commands" or "never edit files outside the project directory."

### Hallucination
When the AI confidently states something that is not true. The AI is fluent even when it is wrong; fluency is not correctness.

### Harness
The software that wraps a raw model and turns it into a usable coding agent. opencode, Cursor, Claude Code, and Aider are all harnesses. See [Chapter 2](02_how_ai_tools_work.md).

### JSON Schema
A standard for describing the shape of JSON data. [[mcp-anthropic-standard|MCP]] tool parameters are defined as JSON Schemas, which lets the harness validate tool calls before they reach the server.

### Knowledge Graph
A structured representation of a codebase (nodes = files, functions, classes; edges = calls, imports, contains). Some tools build one to let the AI answer "how does X work?" without reading every file.

### Lock File (skills-lock.json, pnpm-lock.yaml)
A file that pins the exact versions of installed packages. Makes installs reproducible across machines.

### MCP ([[mcp-anthropic-standard|Model Context Protocol]])
The open standard for connecting AI tools to external systems. "USB-C for AI tools." See [Chapter 7](07_mcp.md).

### MCP Client
The part of the harness that talks to MCP servers. Often the harness itself.

### MCP Server
A program that exposes tools and resources via the MCP protocol. Can be local (stdio) or remote (HTTP/SSE).

### MCP Tool
A callable function exposed by an MCP server. Has a name, a description, and a JSON Schema for parameters.

### Model
The trained AI. A text-in, text-out function. Examples: GPT-4, Claude, Gemini, Llama.

### Prompt
The text you send to the AI. Includes the task, the context, and any tool output fed back in.

### Prompt Injection
An attack where untrusted content the AI reads (a file, a web page) contains instructions that hijack its behavior. Critical to understand if your AI reads untrusted input.

### RAG (Retrieval-Augmented Generation)
Giving the AI access to a searchable knowledge base at inference time, instead of pasting everything into the prompt.

### Resource (MCP)
A read-only data source an MCP server exposes to the AI. The AI can read it but not change it. Examples: a file tree, a database schema.

### Sampling
How the AI picks the next token: not always the most likely one. Controlled by knobs like temperature and top-p.

### Skill
A packaged unit of workflow knowledge (a `SKILL.md` plus supporting files) an AI loads on demand. See [Chapter 8](08_agent_skills.md).

### Skills CLI
A package manager for the open agent skills ecosystem. `npx skills find <query>` searches; `npx skills add <package>` installs.

### Stdio (transport)
The most common way MCP servers run: as a local process communicating over standard input/output. The alternative is HTTP/SSE for remote servers.

### Subagent
A secondary AI spawned by a main AI to handle an independent subtask. The subagent gets its own fresh context window, does its work, and returns a result.

### System Prompt
Instructions the harness sets (that you usually do not see) telling the AI who it is, what tools it has, and how to behave. When you write an `AGENTS.md` file, you are adding to the system prompt.

### Temperature
A sampling knob (0 to ~2). Lower means more predictable; higher means more random. Code work usually wants low temperature.

### Token
The unit the AI processes text in. Roughly 4 characters of English. Context windows, pricing, and speed are all measured in tokens. See [Chapter 4](04_tokens_and_context.md).

### Tool
Any callable capability the AI can invoke: read a file, run a shell command, search the web. MCP tools are one kind; harnesses also have built-in tools.

### Tool Call / Function Call
A structured call the AI emits, asking the harness to run a specific function and feed the result back. The mechanism that lets the AI "do" things.

### Tree of Thoughts
A fancier version of chain-of-thought where the AI explores multiple branches of reasoning and picks the best. Mostly research-grade.

### Vector Database
A store that lets you find vectors "closest" to a query vector. Used by RAG to find the most relevant documents.

### Zero-Shot
Asking the AI to do something without giving any examples. The default for most prompts.

---

## The Big Picture

You do not need to memorize these. You just need to know they exist, so when someone says "the temperature is too high" or "we should run an eval" or "this is a [[prompt-injection-anatomy|prompt injection]] risk," you know what they mean.

Continue to [Chapter 13 — Where to Learn More](13_where_to_learn_more.md).
