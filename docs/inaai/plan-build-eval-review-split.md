---
concept: plan-build-eval-review-split
tags: [agentic, plan-build-split, context-rot, agent-engineering, workflow]
source: YouTube — Google Just Dropped a Masterclass on Agentic Engineering (https://www.youtube.com/watch?v=zbmuiaPuiNM)
date: 2026-06-27
---

# Plan / Build / Eval / Review Split

## Insight
Google's factory: plan → build → eval → review → ship. The engineer designs the system; the agent produces code and docs. The two-session split is critical:

1. **Planning agent** loads specs/context, produces a plan as an artifact.
2. **Coding agent** receives the plan in a fresh session (avoids context rot + bias), builds, runs tests, iterates autonomously through quality gates.
3. Human reviews the pull request before ship — even in agentic engineering, you stay in the loop at the end.

The key move: **start a fresh session (or sub-agent) to execute. Avoid context rot + bias from the planning phase.** The planning agent has read all the context and made decisions; if the same session continues into build, those decisions bias the implementation. A fresh session with just the plan as input is cleaner.

This is the same pattern the AGENTS.md in this vault codifies for non-trivial tasks (>5 tool calls OR spans multiple files): run `writing-plans` first, emit the plan as an artifact (a markdown file or visible plan in chat), then start a fresh session to execute.

The companion move is **separate eval** — automated evals, CI/CD gates, LLM judges, a separate code-review agent. The reviewing agent shouldn't be the same context as the writing agent; the reviewer needs fresh eyes on the output, not the conversation that produced it.

**System evolution mindset:** when the agent fumbles, don't just patch the bug — have it retro on how to improve the workflows/rules so that failure mode is less likely to recur. The harness compounds in value over time.

Pair with [[agentic-harness-90-percent]] (why the harness matters) and [[static-vs-dynamic-context]] (how to keep each session's context lean). The plan/build/eval/review split is the workflow shape; the harness is what makes each stage reliable.

## Context
From the Google Agentic Engineering masterclass; the plan-build-eval-review workflow is the operationalization of the harness thesis.

## Related
- [[agentic-harness-90-percent]]
- [[ai-sdlc-spec-bottleneck]]
- [[static-vs-dynamic-context]]
- [[InaAI]]
