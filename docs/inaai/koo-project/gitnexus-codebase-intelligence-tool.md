---
concept: GitNexus codebase intelligence tool
tags: [koo-project, gitnexus, mcp, coding-agent, tool]
source: ChatGPT convs
---

# GitNexus — Codebase Intelligence Tool

## Insight
GitNexus is a **specific tool**, not a concept. It scans a repo and turns it into a **knowledge graph of the codebase** — files, symbols, dependencies, call chains, execution relationships — so an AI coding agent (Claude Code, Cursor, OpenCode) isn't stumbling around half-blind. Zero-server / local-first; builds a structural map; exposes that map through MCP/tools; has a browser UI for visual exploration.

Why it exists: normal LLM coding agents mostly see the current file, a few retrieved files, whatever fits in context. That's not the same as *understanding the architecture*. GitNexus gives the agent answers to: "What breaks if I change this function?" "Where is this symbol used?" "What is the call path from API route to DB layer?" "Which files belong to the same functional subsystem?"

The improvement is **not "more memory."** It's **better structural retrieval**. Mental model: vector memory = "I vaguely remember seeing this"; GitNexus = "Here is the dependency graph and call structure." Useful for refactoring, impact analysis, onboarding into a repo, tracing bugs across layers, generating architecture docs, large feature edits. Indexes the repo into a knowledge graph using AST/structural parsing and exposes that to agents via MCP so the agent can reason over relationships instead of just searching strings.

The clean distinction: **harness** = whole runtime/scaffolding around the model (concept/architectural layer); **GitNexus** = a specialized code-knowledge system the harness can call into (specific tool). "GitNexus is like giving Claude Code an x-ray + map of the repo instead of just a flashlight." For Ilham's use case (repos, notes, transcripts), GitNexus is basically irrelevant unless building/maintaining a serious codebase. It only matters for the AI-coding-operator stack.

## Context
Came up 2026-06-25 (Harness Explanation). Ilham asked "what is gitnexus?" after the harness explanation, and whether he needed the "full stack" of gitnexus + harness + other AI tools to do anything useful.

## Related
- [[harness-vs-model-concept]]
- [[three-concrete-stacks-to-build]]
- [[think-pipeline-not-plugin]]
- [[koo-project-highlights]]
- **Graphify**
- [[InaAI/mcp-anthropic-standard|MCP]]
