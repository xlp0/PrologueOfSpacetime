---
concept: token-economics-vibe-vs-agentic
tags: [agentic, token-cost, capex-opex, vibe-coding, harness, google]
source: YouTube — Google Just Dropped a Masterclass on Agentic Engineering (https://www.youtube.com/watch?v=zbmuiaPuiNM)
date: 2026-06-27
---

# Token Economics — Vibe vs Agentic

## Insight
The cost shape of vibe coding vs agentic engineering is structurally different:

- **Vibe coding** — low capex (no harness to build) but brutal opex (millions of tokens burned iterating on slop). Every iteration costs tokens; bad output → re-prompt → more tokens → still bad → re-prompt again. The token cost compounds with the mess.
- **Agentic engineering** — high capex (dedicate time / forward-deployed engineer team to build the harness) but low opex — 3–10× more reliable and cheaper, fast crossover. The harness is an engineered resource that lives in version control, just like code.

The crossover is the load-bearing number. Agentic engineering has high upfront cost; if the crossover takes years, it never pays back. If the crossover takes weeks (Google's claim), it pays back almost immediately for any team doing repeated work. Same logic as [[skill-injection-token-economics]] at the skill level — the skill has upfront cost; multi-turn caching amortizes it.

This is the financial framing of [[agentic-harness-90-percent]]. The harness is 90% of the system not as a moral point about engineering discipline — it's 90% because the harness is the part that compounds. Token cost per task drops as the harness absorbs more of the recurring work. The model is a per-token expense; the harness is a one-time investment that reduces the per-token expense on every future task.

Pair with [[ai-sdlc-spec-bottleneck]] for where the upfront capex actually gets spent (spec quality + validation infrastructure, not implementation). And with [[ponytail-vs-caveman-benchmark]] for the skill-level version of the same tradeoff.

The harness compounds; the model is replaceable. That's the entire financial thesis in one sentence.

## Context
From the Google Agentic Engineering masterclass; the capex/opex framing of harness investment.

## Related
- [[agentic-harness-90-percent]]
- [[ai-sdlc-spec-bottleneck]]
- [[skill-injection-token-economics]]
- [[InaAI]]
