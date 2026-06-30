---
concept: ai-sdlc-spec-quality-bottleneck
tags: [agentic, sdlc, spec-quality, google, agent-engineering]
source: YouTube — Google Just Dropped a Masterclass on Agentic Engineering (https://www.youtube.com/watch?v=zbmuiaPuiNM)
date: 2026-06-27
---

# AI-SDLC Spec Quality Bottleneck

## Insight
Traditional SDLC: days of requirements + design, weeks of implementation, week of test/deploy/maintain. AI-driven SDLC keeps the human-driven bookends (spec gathering, validation) but compresses implementation from 1–3 weeks to minutes or hours.

**Spec quality is the new bottleneck.** Google's claim — and the presenter agrees — is that the next $1B+ companies will be platforms that speed up requirements gathering and validation, since the middle is already solved.

This is a structural shift in where engineering time gets spent. Pre-AI SDLC: most of the cost was implementation (writing the code). Post-AI SDLC: most of the cost is upfront (writing a spec good enough that the agent can produce correct code) and end-stage (verifying the agent's output is actually correct). The middle collapses.

The spectrum, not a switch — pick the right level per job:

- **Vibe coding** — casual prompts, "does it seem to work?" validation, high risk, fine for MVPs and disposable code.
- **Structured AI-assisted** — more detailed prompts, manual spot-checking, still no formal specs.
- **Agentic engineering** — engineered specs, automated evals, CI/CD gates, LLM judges, separate code-review agent, systematic verification at every stage. Low risk, reliable output.

Agentic engineering is the default when code matters. The cost shape is also different (see [[token-economics-vibe-vs-agentic]]): vibe coding has low capex (no harness to build) but brutal opex (millions of tokens burned iterating on slop). Agentic engineering has high capex (dedicate time / forward-deployed engineer team to build the harness) but low opex — 3–10× more reliable and cheaper, fast crossover.

Pair this with [[plan-build-eval-review-split]] for the workflow that operationalizes spec quality — and with [[agentic-harness-90-percent]] for the harness that holds the spec.

## Context
From the Google Agentic Engineering masterclass; the bottleneck-shift framing is the SDLC section of the document.

## Related
- [[agentic-harness-90-percent]]
- [[plan-build-eval-review-split]]
- [[token-economics-vibe-vs-agentic]]
- [[InaAI]]
