---
concept: Harness vs model concept
tags: [koo-project, harness, agent, architecture, mcp]
source: ChatGPT convs
---

# Harness vs Model — Agent = Model + Harness

## Insight
**Agent = model + harness.** The harness is the non-model runtime layer — the machinery wrapped around the LLM that makes it actually useful. The model is the brain; the harness is the rigging.

What the harness does: (1) **working memory** — not "remember facts about me" but operational memory (what the agent tried, which files it changed, what failed and why, what assumptions it made, current subtask state); (2) **tool orchestration** — routing work between scrapers, parsers, generators, validators, browsers, loggers, notifiers; (3) **stateful long-running tasks** — continue yesterday's job-search batch, resume half-finished code refactor, compare today's filings with last week's, keep a queue of already-processed companies; (4) **guardrails and trust boundaries** — separate safe-autopilot actions (scrape, summarize, draft, fill forms up to review step, create git branches / draft PRs) from human-approval-required actions (click "Submit", send emails, delete files, push to production, spend money, trade); (5) **logs, checkpoints, results, failure recovery**.

Three meanings of "harness" in AI jargon: **(a) evaluation harness** (most common in model work — run GPT/Claude/local on 500 benchmark tasks, compare scores); **(b) agent harness** (give the agent a repo, let it read files / edit code / run tests, see if it can fix a bug — manages sandbox, repo setup, task instructions, test execution, scoring); **(c) training harness** (infrastructure that runs training jobs: data loading, batching, GPU launching, checkpointing, distributed training).

A real harness upgrades you from "Here's a prompt and some files" to "Take a goal, inspect the environment, plan steps, call tools, store notes, retry failures, checkpoint progress, and ask me only when needed." Persistent local context + file access + control of the environment often beats a stronger raw model in a sterile chat box — which is why Ilham's OpenCode + GLM setup already felt much better than ChatGPT for some tasks.

## Context
Came up 2026-06-25 (Harness Explanation). Ilham asked: "succinctly, what is harness in the context of ai (memory related?)" — was confused whether harness was a concept or a tool, and where GitNexus fit.

## Related
- [[gitnexus-codebase-intelligence-tool]]
- [[obsidian-vs-sqlite-memory-split]]
- [[three-concrete-stacks-to-build]]
- [[safe-autopilot-vs-human-approval]]
- [[koo-project-highlights]]
- **Agentic Engineering Masterclass**
- **DeerFlow 2.0 harness**
- [[InaAI/mcp-anthropic-standard|MCP]]
