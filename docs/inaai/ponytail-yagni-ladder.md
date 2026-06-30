---
concept: ponytail-yagni-ladder
tags: [ponytail, claude-code, skill, yagni, lean-code]
source: YouTube — This Claude Code Plugin Writes 94% Less Code (Ponytail) (https://www.youtube.com/watch?v=2xuFcmUAQUc)
date: 2026-06-26
---

# Ponytail YAGNI Ladder

## Insight
Ponytail is a Claude Code skill that makes your AI coding agent think like "the laziest senior dev in the room" — embracing YAGNI (You Ain't Gonna Need It) to ship the leanest possible solution. Before writing any code, the agent must climb a five-rung decision ladder:

1. Does this need to exist at all?
2. Can a standard library handle it?
3. Is there a native platform feature for this?
4. Is there already an installed dependency that does this?
5. Can it be a one-liner?

Only if every answer is "no" does it write new code — and even then, the minimum required.

The modal-dialogue example makes it concrete. A normal agent installs Radix UI React Dialog to show two buttons: portal + overlay + root + trigger + content wrapper, 30 lines + a new dependency. Ponytail uses the browser's native `<dialog>` element — focus trap, escape-to-close, CSS backdrop, supported since 2022. 8 lines, zero dependencies. A `// ponytail:` comment notes what it skipped and why, so upgrading later is easy.

The benchmark reports 47–77% cheaper than baseline, with correctness checks (a broken one-liner fails on correctness, not just LoC). The caveat: the benchmark cost reflects single-shot calls that resend the skill every time. In real sessions the skill injects once and is cached — so real-world savings are larger.

Demo vs default Claude Code on a weather dashboard prompt: Ponytail finished in <1 min, single HTML file, detected geolocation, ~50% cheaper. Default: 2:30 runtime, 3 files, Python server, prettier UI but didn't detect location (showed London as default). More overengineered.

Stacking with [[caveman-terse-output-skill]]? Slightly more expensive than Ponytail alone — see [[ponytail-vs-caveman-benchmark]].

## Context
From the "Ponytail" skill walkthrough; benchmarks favorably vs no-skill and vs Caveman.

## Related
- [[ponytail-vs-caveman-benchmark]]
- [[packaging-is-the-product]]
- [[caveman-terse-output-skill]]
- [[InaAI]]
