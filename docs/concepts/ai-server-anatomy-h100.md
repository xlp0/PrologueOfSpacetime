---
title: 'ai-server-anatomy-h100'
date: 2026-06-26
tags: [Quadrivium-Arithmetic, Seven-Liberal-Arts, ai-infrastructure, nvidia, h100, dgx, hardware, supply-chain, shovel-sellers]
type: concept
sources: [YouTube — AI大基建时代的产业现状与发展趋势 (https://www.youtube.com/watch?v=cGPBfQHir7s)]
status: stable
liberal_art: Quadrivium-Arithmetic
---

# AI Server Anatomy — DGX H100

## Insight
Anatomy of an AI server (Nvidia DGX H100, ~¥200k+):

- 8× H100 GPUs.
- 6× SK Hynix HBM modules per GPU (TSMC packaging).
- 4× Nvidia NVSwitch chips on motherboard for zero-latency inter-GPU comms.
- Plus: optical modules, switches, PCB, liquid cooling, power.

Goldman Sachs: **75–80% of the $1T+ AI capex goes to compute hardware + network gear.** These hardware vendors are the real shovel sellers — they win no matter which model wins.

**Two-layer compute stack:**

1. **Compute chip system** (GPU + CPU + HBM) ≈ 70% of hardware spend.
2. **Network gear** (800G/1.6T switches, optical modules at ~1:2 ratio to GPUs, 6M+ optical cables) ≈ 15–20% of hardware spend.
3. **Power + cooling** (1.2 GW+ per 400k-GPU center ≈ a mid-sized city's draw) ≈ 10% of hardware spend.

**Stargate Phase 1 ledger (illustrative):**

- Oracle placed ~$40B order with Nvidia for GB200 GPUs. At Nvidia's ~55% net margin → **>$20B net profit from one order.**
- 400k-GPU center: tens of thousands of 800G/1.6T switches, 800k–1.2M 1.6T optical modules, 6M+ optical cables, 1.2 GW+ power.

The framework: target the essential physical links (compute, network, cooling, PCB, power) that the industry is *forced* to keep upgrading no matter who wins the model war. Compute vendors (Nvidia, AMD, Intel), network vendors (Broadcom, Cisco, Arista), optical module vendors, PCB makers, power/cooling providers — all of them are the shovel sellers.

This is the supply-chain complement to [[ai-capex-not-bubble]] — the demand-side numbers explain why the buildout is happening; this anatomy explains where the money actually flows. And it's the substrate under [[physical-ai-chatgpt-moment]] — physical AI needs the compute, network, and cooling to actually deploy.

## Context
From the AI Infrastructure Buildout (AI大基建) deep-dive; the AI-server anatomy is the shovel-seller framework.

## Related
- [[ai-capex-not-bubble]]
- [[nvidia-tax-vs-ualink-alliance]]
- [[physical-ai-chatgpt-moment]]
- [[InaAI]]
