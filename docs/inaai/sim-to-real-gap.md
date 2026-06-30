---
concept: sim-to-real-gap
tags: [physical-ai, nvidia, sim-to-real, omniverse, world-models, robotics]
source: YouTube — Physical AI — NVIDIA robotics interview (https://www.youtube.com/watch?v=kowlc-wywkI)
date: 2026-06-26
---

# Sim-to-Real Gap

## Insight
Two views on the sim-to-real gap — and the disagreement is constructive:

1. **Assume a sim-to-real gap always exists.** Reality isn't perfect, and conventional simulators (Omniverse) are *too* perfect (ground-truth). World models naturally introduce "slight imperfections," which actually help — they regularize the policy against overfitting to a clean simulation.

2. **We need ways to identify what to optimize for** to close the gap. LLMs had feature engineering → sparsity. Physical AI has none of that tooling yet — finding which data types have the most impact is open work. There's no feature-importance methodology for physical-AI training data.

Either way: always need some real-robot tuning. Every robot is calibrated slightly differently off the line. A policy trained purely in simulation will almost always fail on the first real-robot run; the question is how much real-world tuning closes the gap, not whether you need it.

This is the connective tissue between [[nvidia-cosmos-world-model]] (the simulator side) and [[physical-ai-chatgpt-moment]] (the goal). The compounding loop is: better sim → better data → better world model → better sim. But each loop iteration still ends with a real-robot calibration pass.

The analogy to LLMs is instructive: sparsity / feature engineering gave LLM researchers a knob to turn — "this data type matters more than that one." Physical AI doesn't have that knob yet. Until it does, sim-to-real is more art than science: train broadly in sim, then spend the expensive real-robot data on the parts where sim and reality diverge most.

The Isaac Groot platform (see [[isaac-groot-reference-platform]]) helps here too — if every lab is on the same hardware, sim-to-real calibrations can be shared rather than re-derived per robot. Standardization reduces the surface area where sim and reality diverge.

## Context
From the NVIDIA robotics interview; the sim-to-real discussion is the honest acknowledgment that simulation alone isn't enough.

## Related
- [[nvidia-cosmos-world-model]]
- [[physical-ai-chatgpt-moment]]
- [[isaac-groot-reference-platform]]
- [[InaAI]]
