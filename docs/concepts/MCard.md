---
title: 'MCard (Monadic Card)'
date: 2026-06-26
tags: [MCard, MVP-Cards, Monad, Content-Addressing, Sigma-Type]
type: entity
sources: [docs/narrative/MVP Cards Design Rationale.md, docs/The_Representation_Engine.md]
status: stable
---

# MCard (Monadic Card)

> The **root type** — the irreducible, content-addressed, windowless unit of data. The $\Sigma$-type (Dependent Sum) of the MVP Cards triad; every other card is ultimately stored *as* an MCard.

## Definition

**MCard** is the **Magnitude** component of the MVP Cards triad: the immutable raw data, the fact-as-truth. It corresponds to the data-structure half of Wirth's *Programs = Algorithms + Data Structures*, realized as a content-addressed unit in a Merkle-DAG collection that serves as the [[Single-source of Truth|Single Source of Truth]].

| Dimension | MCard |
|:---|:---|
| Math | $\Sigma$-type (Dependent Sum), the existential witness |
| Named after | [[Monadology|Leibniz's Monad]] + [[Monadic Composition - The Algebra of Types|Wadler's monads]] |
| Role | Irreducible data unit; "One Object" mandate |
| Property | Windowless, immutable, hash-indexed |

## In the Representation Engine

MCard is **Tier 1 — Name** of the D&D word-game loop: *"Cat" ≠ "Act"* — [[Directionality]] creates distinction from identical parts. The card that names a thing is the MCard.

## See also

- [[MVP Cards Design Rationale]] — the full architectural rationale and mathematical foundations.
- [[The_Representation_Engine]] — the D&D engagement loop where MCard is the "Name" tier.
- [[PCard]] — the computation type ($\Pi$-type) that transforms MCard references.
- [[VCard]] — the verification boundary (Id-type) that gates MCard state transitions.
- [[Cubical Logic Model]] — the specification surface that addresses MCards.
- [[hott_ssot_reference]] — the HoTT grounding ($\Sigma$-types as dependent sums).
