# HoTT SSoT Reference: The Secret Sauce
> **Source**: Notebook LM (https://notebooklm.google.com/notebook/97846aca-b3c2-417e-85ad-4fa95ffc0b9f)
> **Last Updated**: 2026-03-03

This document is the **Single Source of Truth** reference for all theoretical grounding in the Prologue of Spacetime project. All design, code, and narrative must align to the cue words and structures below.

---

## 1. The Three Pillars: Sum, Product, Exponent

These are the **Algebraic Data Types (ADTs)** — the absolute minimum required to capture any formal language. Think of them as middle-school arithmetic elevated to type theory.

| ADT | Arithmetic | Category | Operational Role | Maps To | Cue Words |
|---|---|---|---|---|---|
| **Sum Type** | A + B | Coproduct | Handle Registry (pointers) | **Identity** — The "Who" | Choice, OR, Disjoint Union, Coproduct, Addition (+) |
| **Product Type** | A × B | Conjunction | Handle History (State×Time) | **Evolution** — The "When" | Combination, AND, Cartesian Product, Multiplication (×) |
| **Exponent Type** | B^A | Hom-set | The Card (immutable content) | **Reality** — The "What" | Function, Mapping, Implication (A→B), Hom-set, Exponential Object |

### Beginner Analogies
- **Sum Type**: A `Boolean` = `True + False`. Choose one or the other. Also: the "Yes/No" gate.
- **Product Type**: A 2D coordinate = `X × Y`. Combine two things together. Also: `State × Time` = an audit trail.
- **Exponent Type**: An array of 5 integers = `Integer^5` — a function from index to value. Also: `Content^Hash` = a "Card" that stores immutable reality.

### Combined Example (Polynomial Functor)
```
Tree(X) = 1 + X²
         ↑     ↑
       Leaf   Node (2 branches)
```
Sum = choice to be a Leaf or Node. Exponent = the dual positions of the Node.

---

## 2. Computational Trinitarianism

The **unifying meta-structure** — Logic, Computation, and Category Theory are **one relational entity** viewed from three angles.

| Dimension | Domain | Role | Analogy |
|---|---|---|---|
| **Type** | Logic | Abstract Specification | Currency Denomination — *What we claim is true* |
| **Algorithm** | Computation | Concrete Implementation | Currency Transaction — *How we compute it* |
| **Proof / Witness** | Category Theory | Accountability Verification | Balanced Expectations — *Why it is valid* |

> **Key Insight**: You cannot pass the "Checkpoint of Reality" with fewer than three dimensions. The third (Proof/Witness) is mathematically necessary to break symmetry and provide the recursive space to measure and correct systems.

---

## 3. HoTT: Perception, Action, Reasoning as Paths

Based on Robert Harper's Cubical Type Theory, intelligent behavior is modeled geometrically:

- **Perception** → A **1D Path** in the space of sensory data (tracking continuous sensory input over time).
- **Action** → A **Higher-Dimensional Path** built upon perception (sequence of responses).
- **Reasoning** → A **Homotopy** — the continuous deformation/refinement of possible action paths into one another.

> The system *reasons* by finding paths between paths — this is the HoTT structure giving computation its geometry.

---

## 4. Entropy, Diversity & Magnitude

The mathematical spine connecting biology, information theory, and AI:

- **Tom Leinster's diversity axioms**: Hill numbers and Rényi entropies are the **only logically consistent** ways to quantify variety and similarity.
- **Enriched category theory + LLMs**: The geometric concept of **magnitude** can recover semantic information and entropy from text processed by AI.
- **Signal-to-Noise / Entropy-Based Alignment**: The degree of alignment of our work is measurable as entropy; high alignment = low noise = strong signal to the target audience.

---

## 5. Cue Word Vocabulary (Signal Words)

Use these exact terms to "send the signal" to the target audience:

**Sum Types**: Choice · OR · Disjoint Union · Coproduct · Addition (+)

**Product Types**: Combination · Conjunction · AND · Cartesian Product · Multiplication (×)

**Exponents**: Function · Mapping · Implication (A→B) · Hom-set · Internal Hom-set · Exponential Object

**Polynomial Functors (the assembly)**: Shape · Constructor · Arity · Holes · Positions · Directions

**The Meta-Level**: Trinity · Computational Trinitarianism · SSoT · Homotopy · Path · Witness · Entropy

---

## 6. Languages (Functional Programming Stack)

| Language | Level | Best For |
|---|---|---|
| **Clojure** | Beginner | First FP language — dynamic types, low friction |
| **Haskell** | Intermediate | Explaining concepts, Monads, Kleisli composition |
| **Agda** | Advanced | Poly category, dependent types, writing proofs as code |
| **Idris** | Advanced | Dependently typed alternative to Agda |
| **PureScript** | Web | Front-end components (Halogen), Polynomial Functor modeling |

> Note: Haskell lacks native dependent types, limiting its use for Polynomial Functors. **Agda is the primary language for the Poly category** — described as "super Haskell".

---

## 7. The PKC Container Role

> "Even if all technologies are totally free for everyone, integrating them with individual person's physical and social environments will still have many hurdles."

PKC (Personal Knowledge Container) is the **container** whose purpose is to reduce this integration complexity — it is the pragmatic vehicle that delivers the theoretical SSoT/HoTT framework into the hands of real people.

---

## 8. The MCard Schema (SSoT In Practice)

The three ADTs directly map to the MCard database architecture:

- **Sum Type** → Handle Registry: stores pointers, managing mutable identity (`Pointer + Pointer`)
- **Product Type** → Handle History: tracks causal time and audit trails (`State × Time`)
- **Exponent Type** → The Card: stores immutable content (`Content^Hash`) — the archetypal representable functor grounding the system in reality.
