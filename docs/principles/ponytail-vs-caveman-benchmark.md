---
title: 'ponytail-vs-caveman-benchmark'
date: 2026-06-26
tags: [Quadrivium-Arithmetic, Seven-Liberal-Arts, ponytail, caveman, benchmark, token-cost, head-to-head]
type: principle
sources: [YouTube — This Claude Code Plugin Writes 94% Less Code (Ponytail) (https://www.youtube.com/watch?v=2xuFcmUAQUc)]
status: stable
liberal_art: Quadrivium-Arithmetic
---

# Ponytail vs Caveman Benchmark

## Insight
The head-to-head: 3 methods (no skill / [[caveman-terse-output-skill]] / [[ponytail-yagni-ladder]]) × 3 models × 5 tasks × 10 runs. Ponytail reports 47–77% cheaper, with correctness checks (a broken one-liner fails on correctness, not just LoC).

The stacking experiment is the interesting data point: trying Caveman + Ponytail together on the same prompt produced similar output, *slightly more expensive* than Ponytail alone. The conclusion: **no benefit to combining**. Pick one. Ponytail wins on benchmarks.

Why doesn't stacking help? They optimize for different things and the second skill's input-token cost outweighs its marginal output savings once the first skill is already doing the heavy lifting. Caveman compresses *output*; Ponytail reduces the *amount of code written in the first place*. Ponytail's savings compound — less code means less to read, less to maintain, fewer dependencies — while Caveman's savings are linear per turn.

This is the same head-to-head pattern as [[catalog-vs-curator]] (OpenClaw vs Hermes) — pick-one, not use-both — and rhymes with [[static-vs-dynamic-context]] (one generalist agent + skills > zoo of specialists). Two skills targeting the same axis tend to fight each other on cost.

The fair critique from Colin Eberhart (see [[packaging-is-the-product]]): just saying "follow YAGNI principles" nearly matches Ponytail's score, and adding "and one-liner solutions" actually beats it. The counterargument is that packaging is the product — auto-injection + audit tools + debt ledger beat a system-prompt phrase.

## Context
From the "Ponytail" skill walkthrough; the stacking-with-Caveman benchmark section.

## Related
- [[ponytail-yagni-ladder]]
- [[caveman-terse-output-skill]]
- [[packaging-is-the-product]]
- [[InaAI]]
