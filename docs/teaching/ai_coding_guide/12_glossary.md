---
title: 'Chapter 12 — The Words You'll Hear'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Grammar]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 12
liberal_art: Trivium-Grammar
audience: professional
---

# Chapter 12 — The Words You'll Hear

## How to use this glossary

This is a glossary of the vocabulary people actually use in AI coding conversations, blog posts, and job listings in 2025–2026. Bookmark it. Every term is defined in plain English with a pointer to where in this guide (or beyond it) the concept is unpacked.

Terms are grouped by theme, not alphabetized — the grouping itself is information, because it shows which words belong together. Within each group, terms go from foundational to specialized.

---

## The eras and the shift

### Vibe coding
A style of AI-assisted development coined by Andrej Karpathy: you describe the *vibe* of what you want in natural language, accept whatever the model produces, iterate by feel. Defining trait: human-in-the-loop on every step; no real agentic autonomy; minimal verification. Useful for prototyping and exploration; risky for production. (Chapter 1.)

### Agentic coding / agentic engineering
The successor to vibe coding, also named by Karpathy. Instead of typing code, you *orchestrate agents* that plan, write, test, and ship code under your direction. You own the architecture, tests, and review. The defining difference from vibe coding is structure: agents run in a loop with memory, guardrails, and verification, rather than producing one-shot output you accept or reject. (Chapter 1, Chapter 9.)

### Prompt engineering (era)
The 2022–2024 practice of optimizing the *wording* of prompts to get better model output. Still relevant as a skill, but no longer the dominant frame. (Chapter 5.)

### Context engineering (era)
The mid-2025-onward successor: the deliberate curation of what the model *sees* (the context window) rather than just how the question is *worded*. The word the field has settled on for the actual skill that matters now. (Chapter 6.)

### Harness engineering (era)
The 2026-onward framing that takes [[static-vs-dynamic-context|context engineering]] further: designing the *whole runtime* around the LLM — memory, guardrails, orchestration, context pipelines, multi-agent coordination. The discipline of building reliable agents in production. (Chapter 2, Chapter 3.)

### Agent engineering
A broader synonym for harness engineering, sometimes used to emphasize the *system* (guides, sensors, context pipelines, orchestration) rather than the harness narrowly. Often used interchangeably with harness engineering.

---

## The model and the loop

### LLM (Large Language Model)
The text predictor at the center of everything. Stateless: it has no memory between calls. (Chapter 2.)

### Token
The unit the model reads and writes. Roughly ¾ of a word or 4 characters. (Chapter 4.)

### Context window
The maximum tokens the model can take in on a single call. Finite, costly to fill, and the central constraint of the whole stack. (Chapter 4.)

### The agentic loop
The cycle: gather context → prompt the model → model responds (possibly with tool calls) → harness executes tool calls → results go back into context → prompt again → repeat. The heartbeat of every modern AI coding tool. (Chapter 2.)

### Tool calling / function calling
The mechanism by which a model's text output is parsed into structured function calls the harness can execute ("read this file," "run this command"). Most modern models support this natively. (Chapter 2, Chapter 7.)

### Prompt caching
A feature where the stable prefix of a prompt is cached by the model provider and billed at a steep discount on subsequent calls. What makes agentic loops affordable. (Chapter 4.)

### Reasoning tokens / extended thinking
Hidden internal chain-of-thought tokens that some frontier models generate. You pay for them; you don't see them. Improve quality on hard tasks, increase cost. (Chapter 4.)

### Lost in the middle
A documented model weakness: attention is strongest at the start and end of a long context, weaker in the middle. Implication: bigger context windows don't solve everything. (Chapter 4, Chapter 6.)

---

## The stack

### Model
The LLM. The only layer that is genuinely "the AI." (Chapter 3.)

### Harness
The scaffolding around the model: the loop, the tool-call parsing, the execution, the context curation, the permissions, the memory, the orchestration. What turns a model into an agent. (Chapter 2, Chapter 3.)

### Client
The surface the user touches: the IDE extension, the terminal app, the web UI. Distinct from the harness. (Chapter 3.)

### Server (in the stack sense)
Anything the harness reaches out to: the model provider's API, the local filesystem, [[mcp-anthropic-standard|MCP]] servers, external services. (Chapter 3.)

---

## Context and retrieval

### Context engineering
(See above, in "Eras and the shift.") The deliberate curation of what's in the context window: gathering, filtering, prioritizing, evicting, retrieving. (Chapter 6.)

### RAG (Retrieval-Augmented Generation)
The general idea of fetching relevant material and putting it in the context before the model answers. Classic RAG is one-shot retrieval; the model gets the top-K results and answers. (Chapter 6.)

### Agentic RAG
The loop version of RAG: the agent decides what to retrieve, retrieves it, evaluates it, retrieves more if needed, iterates. The smartest 2026 systems combine agentic RAG with a graph-backed knowledge base. (Chapter 6.)

### Knowledge graph (in the agent sense)
A pre-indexed graph of code symbols, relationships, and execution flows that an agent can query during the loop. Used for large or cross-repo work where grepping isn't enough. A common substrate for agentic RAG at scale.

### Subagent
A separate context window spawned for a sub-task, which does its work, returns a short answer, and is then discarded. Used to keep the main context clean when a sub-task would generate a lot of noise. (Chapter 6, Chapter 9.)

### Subagent orchestration
The practice of coordinating multiple subagents — typically for different roles (search, plan, implement, review) or different parts of a task. A core capability of a mature harness.

### Memory (agent)
Any mechanism by which an agent persists facts across turns or sessions — typically via a memory MCP server, a rules file, or a summary that's carried forward. The model is stateless; memory is a harness feature, not a model feature. (Chapter 6, Chapter 9.)

---

## MCP and tools

### MCP ([[mcp-anthropic-standard|Model Context Protocol]])
An open standard (Anthropic, late 2024) for how a harness talks to external tools and data sources. "The USB-C of AI." Defines a protocol, a tool-description shape, and a discovery mechanism. (Chapter 7.)

### MCP server
A process that speaks the MCP protocol and exposes tools, resources, and prompts to a harness. Can be local or remote. (Chapter 7.)

### MCP tool
A specific function exposed by an MCP server that the model can call. Has a name, description, and JSON-schema input. (Chapter 7.)

### Sandboxing
Running an agent, its tool calls, or specific MCP servers in a restricted environment (container, VM, network-isolated zone) so the blast radius is bounded. The strongest practical defense against agent-caused damage. (Chapter 7, Chapter 11.)

### Agentification
The pattern of taking an existing application or service and exposing it to agents via MCP or a similar interface — turning a video editor, a database, a CRM, or a design tool into something an agent can drive. (Chapter 7.)

---

## Know-how and procedures

### Skill (agent skill)
A packaged bundle of know-how that teaches an agent how to do a particular kind of task well: a manifest, instructions, optional resources, optional tool references. Loaded into context on demand. (Chapter 8.)

### Slash command / custom command
A pre-built prompt triggered on demand (e.g. `/review`, `/fix`, `/security-scan`). Stored as a Markdown file in a known directory (`/.cursor/commands/`, `/.claude/commands/`, etc.). The lightweight version of a skill. (Chapter 9.)

### Workflow file
A general term for a file (often Markdown or YAML) that defines a multi-step agent procedure — either a slash command, a skill, or a more elaborate workflow-as-code. Different tools use slightly different names for the same idea. (Chapter 9.)

### Rules file
A plain-text file at the project root (or scoped to a directory) that the harness loads into context automatically. Contains standing facts about the project: stack, conventions, what to avoid. The passive counterpart to skills' active procedures. (Chapter 9.)

### AGENTS.md
The emerging cross-tool standard for rules files. Read natively by Codex CLI, opencode, and an increasing list of tools; other tools can be pointed at it via a stub. (Chapter 9.)

### CLAUDE.md, GEMINI.md, .cursorrules, .cursor/rules/, .windsurfrules, .clinerules, copilot-instructions.md
Tool-specific rules file formats. Same pattern, different filenames. (Chapter 9.)

---

## Methodologies

### BMAD Method (Breakthrough Method for Agile AI-Driven Development)
An open-source AI-native development framework. Provides specialized agent roles, guided workflows, planning templates, and scale-adaptive ceremony. A packaged methodology for running whole projects with agents, the way Scrum packages human workflow. (Chapter 9.)

### Agent fleet / agent roles
A lighter-weight methodology pattern: define a small set of role-specific agents (reviewer, test-writer, planner, implementer) and orchestrate between them, without buying into a full framework like BMAD. (Chapter 9.)

### Workflow-as-code
Defining multi-step agent workflows in a structured format (YAML, etc.), versioned with the repo, runnable on demand or in CI. The natural extension of slash commands to multi-step procedures. (Chapter 9.)

### Plan mode / plan-then-execute
A workflow pattern (and a feature in most harnesses) where the agent proposes a plan, the human approves or edits it, and only then does the agent execute. The single highest-leverage habit for non-trivial tasks. (Chapter 9.)

---

## Tools and surfaces

### Terminal agent
A CLI that runs the agentic loop in the terminal. Examples: Claude Code, Codex CLI, opencode, Gemini CLI, Aider, Goose. Where harness engineering is most visible. (Chapter 10.)

### IDE-integrated assistant
A plugin or fork of an editor with the agent inside it. Examples: GitHub Copilot, Cursor, Windsurf, Cline, Continue. (Chapter 10.)

### Background / CI agent
An agent that runs on a schedule or trigger (PR, commit, issue), doing work asynchronously. Where slot-4 autonomy earns its keep, gated behind review. (Chapter 10.)

### Plan mode, agent mode, ask mode
Common modes in modern tools: plan mode proposes without acting; agent mode edits and runs commands; ask mode answers questions read-only. Different tools use slightly different names. (Chapter 9, Chapter 10.)

---

## Responsibility

### Verification
The non-negotiable practice of confirming agent output before it ships: read the diff, run the tests, run the linter, actually run the feature. (Chapter 11.)

### Blast radius
The set of things an agent can actually affect — your filesystem, your git history, your database, your external services. Should be deliberately bounded by permissions and sandboxing. (Chapter 11.)

### Permissions model
The harness's rules for what the agent may do without asking, what requires confirmation, and what's forbidden. The main technical defense against agent-caused damage. (Chapter 11.)

---

## Adjacent terms you'll hear

### Hallucination
When the model states something false as if it were true — inventing an API that doesn't exist, citing a function that isn't there, fabricating a library name. Less common than in 2023 but not gone, especially in less-documented areas. Defense: verification (Chapter 11) and grounding in real context (Chapter 6).

### Grounding
Tying the model's output to real, verifiable sources — actual file contents, actual API docs, actual test results — rather than letting it reason in the abstract. The opposite of hallucination. (Chapter 6.)

### Fine-tuning
Training a model further on a specific dataset to specialize it. Distinct from prompt engineering and context engineering; rarely the right tool for individual developers in 2026, but relevant for organizations with specific domains.

### Distillation
Training a smaller model on the output of a larger one, to get a cheaper model that approximates the big one's quality on a specific task. How many "small but capable" models are made.

### Inference
Running a model to produce output. Distinct from training. When you use an AI tool, you're doing inference, not training.

### Embedding
A numerical vector representation of text (or other data) that captures semantic similarity. Used for retrieval (RAG), search, and clustering. The thing that makes "find code semantically similar to this" work.

### Vector database / vector store
A database optimized for storing and querying embeddings. The retrieval substrate for classic RAG. Less central in agentic RAG, where knowledge graphs often take its place.

### Eval (in the agent sense)
A test of an agent's behavior on a defined task, used to measure whether a change (to the model, the harness, the rules, the skills) made things better or worse. How serious teams track whether their agentic setup is improving. (Briefly, Chapter 11.)

---

## Terms that are fading

A few words you'll still see but that have mostly outlived their usefulness:

- **"Prompt engineering"** as a discipline — folded into context engineering.
- **"Copilot"** as a generic term for any AI coding assistant — GitHub has reclaimed the trademark; use "AI assistant" or "agent" instead.
- **"Llama/GPT/Claude wrapper"** as a dismissive term for a tool — every serious tool wraps a model; the wrapper is the whole point. (See: harness, Chapter 2.)

---

## A final note on drift

This glossary will be incomplete by the time you read it — new terms appear monthly. The way to stay current is to read the changelogs and docs of one terminal agent (Claude Code, opencode, or Codex CLI are the most active) and one IDE-integrated tool, plus the MCP spec. Everything else you need to know will show up in those channels within a few weeks of being coined.

The *concepts* in this glossary are much more stable than the *words*. If you understand the model, the harness, the loop, the context window, and the responsibility layer, you can re-derive any new term you encounter by figuring out which of those it relates to. The vocabulary is downstream of the mental model, not the other way around.
