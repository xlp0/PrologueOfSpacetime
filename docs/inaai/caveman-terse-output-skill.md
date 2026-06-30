---
concept: caveman-terse-output-skill
tags: [caveman, claude-code, skill, token-cost, yagni, terse-output]
source: YouTube — This Claude Skill Cuts Your Token Costs In HALF (Caveman) (https://www.youtube.com/watch?v=RuH3uiJy84A)
date: 2026-06-26
---

# Caveman — Terse Output Skill

## Insight
Caveman is a trending Claude Code skill (inspired by The Office's Kevin) that makes AI coding agents answer in terse, filler-free "caveman" style. The skill enforces four rules:

- Drop articles (a/an/the), filler words, pleasantries, hedging.
- Use short synonyms ("big" not "extensive", "fix" not "implement a solution for").
- Keep technical terms, code blocks, errors verbatim.
- Structure output as **thing → action → reason → next step**.

Demo: same auth question, baseline Claude rambles with m-dashes and qualifications; Caveman replies "demo only, client-side auth, no real security, built for Better Stack RUM tracking demos."

Intensity modes scale from light → full (default) → ultra (abbreviates everything, strips conjunctions, uses arrows for causality, one word when one word's enough). A Wenyan mode uses classical Chinese characters — most token-efficient, but unreadable to most.

Companion skills extend the pattern: **Caveman commit** writes terse conventional-commit messages, **Caveman review** gives one-line-per-finding code review comments, and **Compressed** takes natural-language files and "Cavemanifies" them for reuse with fewer input tokens.

The benchmark result is real but qualified: ~45% fewer output tokens vs baseline, ~39% fewer than just saying "be concise." A separate study this year showed constraining large models to brief responses improved accuracy by 26% on certain benchmarks — terseness isn't just cheaper, it can be more correct.

The catch is in [[skill-injection-token-economics]] — on single-shot short prompts the skill markdown itself costs more input tokens than it saves, but multi-turn prompt caching flips the math back in Caveman's favor. Stack with [[ponytail-yagni-ladder]]? Head-to-head benchmark says no — see [[ponytail-vs-caveman-benchmark]].

## Context
From the "Caveman" skill walkthrough; one of two token-saving skills benchmarked together (the other is [[ponytail-yagni-ladder]]).

## Related
- [[skill-injection-token-economics]]
- [[ponytail-yagni-ladder]]
- [[ponytail-vs-caveman-benchmark]]
- [[InaAI]]
