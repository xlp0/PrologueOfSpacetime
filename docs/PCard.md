---
title: 'PCard (Polynomial Functor Card)'
date: 2026-06-26
tags: [PCard, MVP-Cards, Polynomial-Functor, Pi-Type]
type: entity
sources: [docs/narrative/MVP Cards Design Rationale.md, docs/The_Representation_Engine.md]
status: stable
---

# PCard (Polynomial Functor Card)

> The **computation type** — encodes transformations as polynomial functors over [[MCard]] references. The $\Pi$-type (Dependent Product) of the MVP Cards triad; the algorithm half of *Programs = Algorithms + Data Structures*.

## Definition

**PCard** is the **Direction** component: the generative process, the logic. A PCard is a [[Polynomial functor|polynomial functor]] that transforms MCard references, functioning as the **Monadic Executor** — it handles dynamic control flow and dependent sequencing by implementing Reader, State, and Writer monadic patterns, structuring knowledge processing into composable Kleisli arrows without mutating underlying data.

| Dimension | PCard |
|:---|:---|
| Math | $\Pi$-type (Dependent Product) |
| Role | Transformation / algorithm; the "P" in [[PTR]] (Polynomial Type Runtime) |
| Pattern | Monadic Executor (Reader/State/Writer) |
| Composes via | Kleisli arrows, tensor products |

## In the Representation Engine

PCard is **Tier 2 — Describe** of the D&D word-game loop: *"Cat on mat" ≠ "Mat on cat"* — [[Commutativity|Non-Commutativity]] determines truth-value. The card that describes an arrangement is the PCard.

## See also

- [[MVP Cards Design Rationale]] — full rationale; PCard as polynomial functor and monadic executor.
- [[The_Representation_Engine]] — PCard is the "Describe" tier.
- [[MCard]] — the data type it transforms.
- [[VCard]] — the verification boundary that gates PCard execution.
- [[PTR]] — the Polynomial Type Runtime that evaluates PCards.
- [[Monadic Composition - The Algebra of Types]] — the monadic patterns PCard implements.
