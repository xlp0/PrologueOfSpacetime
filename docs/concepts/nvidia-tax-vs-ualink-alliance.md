---
title: 'nvidia-tax-vs-ualink-alliance'
date: 2026-06-26
tags: [Trivium-Logic, Seven-Liberal-Arts, ai-infrastructure, nvidia, nvlink, ualink, asic, hyperscaler, supply-chain]
type: concept
sources: [YouTube — AI大基建时代的产业现状与发展趋势 (https://www.youtube.com/watch?v=cGPBfQHir7s)]
status: stable
liberal_art: Trivium-Logic
---

# Nvidia Tax vs UALink Alliance

## Insight
**The "Nvidia tax"**: buying GPUs forces hyperscalers into Nvidia's whole network stack — NVLink in-cabinet, InfiniBand out-of-cabinet, DPUs, liquid-cooling standards. Deep ecosystem lock-in → capex flows into Nvidia's pocket → cloud margins squeezed.

Two counterattack vectors from Microsoft / Google / Meta:

1. **Self-developed ASICs** (Google TPU, Microsoft Maya, etc.) — drop general compute, focus on AI matrix ops; cheaper + lower power. Used to offload inference and some training.

2. **Open communication-standard alliance** — 2024: AMD + Intel + Broadcom + Microsoft + Meta formed the "Avengers" alliance → **UALink** open protocol, to break NVLink's monopoly on intra-node interconnect and let chips from different vendors mix via Broadcom/Cisco.

Outcome unknown, but **both paths still require** higher-bandwidth interconnects, better liquid cooling, higher-end PCB, more stable power → those "essential links" are the shovel sellers forced to upgrade regardless.

The structural insight: even if UALink succeeds and breaks Nvidia's interconnect monopoly, the shovel sellers (optical modules, switches, PCB, cooling, power) win either way. The protocol layer is contested; the physical layer is not.

This is the supply-chain-politics complement to [[ai-capex-not-bubble]] (why the buildout is happening) and [[ai-server-anatomy-h100]] (where the money flows). The Nvidia tax explains why hyperscalers are motivated to find alternatives; the UALink alliance is the actual counterattack; the shovel-seller framework is the answer to "OK, but who wins?"

The lesson for thinking about AI infrastructure: don't bet on the protocol layer (NVLink vs UALink vs something else), bet on the physical layer that all protocols require. The protocol layer is contested and the winner is uncertain; the physical layer is forced to upgrade regardless of who wins.

## Context
From the AI Infrastructure Buildout (AI大基建) deep-dive; the Nvidia tax + counterattack section.

## Related
- [[ai-capex-not-bubble]]
- [[ai-server-anatomy-h100]]
- [[InaAI]]
