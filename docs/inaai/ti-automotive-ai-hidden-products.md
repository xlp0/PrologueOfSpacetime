---
concept: ti-automotive-ai-hidden-products
tags: [physical-ai, automotive, ti, tda5, am62a, adas, driver-monitoring, functional-safety]
source: YouTube — AI (Texas Instruments — Physical AI & Embedded Processors) (https://www.youtube.com/watch?v=Uw64SYI3O0s)
date: 2026-06-26
---

# TI Automotive AI — Hidden Products

## Insight
Modern cars are supercomputers on 4 wheels, with a massive sensor-data explosion. The "hidden products" inside them — invisible to the user but always working — are where TI's automotive AI lives.

**TDA family** (TI Driver Assist): TDA5 is the latest generation, 15 years of evolution. Supports ADAS levels up to L3 (depending on OEM). The chip family that drives the active-safety stack on millions of vehicles.

**AM62A** — driver-monitoring chip with three behaviors worth pulling apart:

1. **Tracks hand position on wheel, eye position, pupil-size changes** to detect fatigue. (Pupil-size changes — not just gaze direction — as a drowsiness signal. That's a non-obvious biomarker.)
2. **Prompts the driver to pull over / take a break** when fatigue is detected.
3. **Monitors passengers** — seat belt compliance, and crucially, **detects children left in car seats** (anti-tragedy feature).

That last one is the design move worth flagging. The chip isn't just tracking the driver; it's tracking everyone in the cabin. The use case isn't "is the driver alert?" — it's "is everyone in this car safe?" Child-detection in car seats is a life-safety feature that quietly runs in the background, exactly the kind of thing physical AI is supposed to do.

**In-cabin audio** does double duty: acoustic enjoyment + safety guardian. Must filter noise while extracting safety-critical sounds (sirens, horns, emergency vehicles). Supports zone isolation (front vs rear passengers). TI has ~40 years of audio DSP experience — foundational for this AI-enhanced audio era.

**Industrial applications**: AM62A used for product quality / defect monitoring — e.g., inspecting test tube glass thickness in medical manufacturing, since glass thickness affects measurement accuracy. AI-based monitoring of these parameters is being deployed throughout China.

The pattern: same chip family, multiple verticals. Automotive safety, industrial QA, in-cabin experience — all running on TI's embedded AI silicon. This is the body-side of [[physical-ai-real-time-constraints]] made concrete.

## Context
From the Texas Instruments Physical AI interview; the automotive section near the end of the video.

## Related
- [[physical-ai-real-time-constraints]]
- [[pru-live-reprogramming]]
- [[InaAI]]
