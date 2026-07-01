---
title: 'skill-injection-token-economics'
date: 2026-06-26
tags: [Quadrivium-Arithmetic, Seven-Liberal-Arts, token-cost, prompt-caching, skills, claude-code, multi-turn]
type: principle
sources: [YouTube — This Claude Skill Cuts Your Token Costs In HALF (Caveman) (https://www.youtube.com/watch?v=RuH3uiJy84A)]
status: stable
liberal_art: Quadrivium-Arithmetic
---

# Skill Injection Token Economics

## Insight
The Caveman benchmark reports 45% fewer output tokens vs baseline, 39% fewer than just saying "be concise." But there's a catch that doesn't show up in the headline number: **the skill markdown itself costs input tokens.** On single-shot short prompts, Caveman is actually ~10% *more* expensive than baseline once you factor in input cost.

The crossover happens with **follow-up questions**, because prompt caching kicks in: the skill is injected once, then the cached prefix is reused across turns. With caching, Caveman wins again — about 39% cheaper than baseline on multi-turn sessions.

This is a general pattern for any skill or system-prompt-based optimization, not just Caveman:

- **Single-shot / one-off prompt** — the skill's input-token cost dominates. The optimization can backfire.
- **Multi-turn session** — caching amortizes the skill's input cost across the conversation. The optimization wins.
- **Single-word prompts** — skip the skill entirely; the injection overhead isn't worth it.

The implication for harness design: don't measure a skill in isolation. Measure it in the deployment shape it'll actually run in. A skill that loses money on shot-one but saves money across a 20-turn session is the right trade for an agent that lives in long conversations — and the wrong trade for a one-shot CLI tool.

This rhymes with the broader capex/opex framing of [[token-economics-vibe-vs-agentic]] and [[agentic-harness-90-percent]]: the harness is upfront cost, the savings compound over time. Same logic at the skill level — see also [[caveman-terse-output-skill]] and [[ponytail-yagni-ladder]].

## Context
From the "Caveman" skill walkthrough; the benchmark caveat that doesn't make the headline.

## Related
- [[caveman-terse-output-skill]]
- [[token-economics-vibe-vs-agentic]]
- [[agentic-harness-90-percent]]
- [[InaAI]]
