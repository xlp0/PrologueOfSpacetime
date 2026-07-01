---
title: 'Representability'
date: 2026-07-01
tags: [Trivium-Logic, Seven-Liberal-Arts]
type: concept
sources: [raw/articles/Engineering_Awe_A_Scale-Free_Architecture.pdf]
status: draft
liberal_art: Trivium-Logic
---

# Representability

> The mathematical and physical limit of expression, defining the capacity of a system to fully characterize abstract structures by their measurable interactions.

## 1. Definition

In Category Theory, a functor $F: \mathcal{C} \to \mathbf{Set}$ is **representable** if it is naturally isomorphic to a Hom-functor $\text{Hom}(X, -)$ for some object $X \in \mathcal{C}$:

$$F(-) \cong \text{Hom}(X, -)$$

* **The Representative ($X$)**: The concrete object (such as an **[[MCard]]**) that acts as a proxy for the abstract logic of $F$.
* **The Probes ($\text{Hom}(X, -)$)**: The set of all measurable interactions with $X$.
* **The Significance**: In the category of computation, *"To be is to be representable."* A system cannot process or govern any entity unless it can be represented by a concrete witness and probed via well-defined morphisms.

### 1.1 Representation-is-Explanation (Michael Leyton)
In cognitive science and design, a representation is not a static data structure, but a **causal recovery of history**. To represent an object is to recover the sequence of actions that brought it into existence. This matches the **[[The_Representation_Engine|Representation Engine]]**'s goal: using words to declare intent, Mealy transformations to execute, and type checks to confirm the causal history.

---

## 2. In the Prologue and the 3E Framework

Representability is the mathematical foundation of **Effectiveness** (the third dimension of the **[[3E_Framework|3E Framework]]**):

* **Effectiveness**: Verifies if the output matches the goal. This requires representability—the ability to perfectly encode interactive histories into concrete, verifiable objects.
* **The Four Planes of Representability (The 4 Ws)**: Building on the Yoneda Embedding, representability structures the four cognitive questions of system architecture:

| The 4 Ws | Category Theory | CLM / PKC Triad | Role in Representability |
| :--- | :--- | :--- | :--- |
| **Why** (Purpose) | Natural Transformation | **[[VCard]]** (Expectation) | The context and constraints validating the structure. |
| **How** (Action) | Morphism ($A \to B$) | **[[PCard]]** (Implementation) | The dynamic functions acting as probes. |
| **What** (Substance) | Object ($A$) | **[[MCard]]** (Specification) | The static content-addressed entity being represented. |
| **Whether** (Existence) | Identity Morphism ($\text{id}_A$) | **Root** | The foundation of existence; the identity operation. |

### 2.1 The Preconditions: Linearization and Invariance
To achieve representability, a system must be subjected to **Linearization**, mapping complex state transitions to the rules of **Linear Logic**. In a linearized state, variables act as physical resources ($A \multimap B$) that cannot be implicitly duplicated or discarded (respecting Landauer's Principle). This is enforced by:
1. **SSOT**: Providing the fixed, invariant hash target.
2. **Polynomial Functors**: Linearizing state machines into Spivakian dynamic interfaces.

### 2.2 The Empty Schema and Kan Extensions
To represent anything, the system must assume nothing. The **Empty Schema Principle** (Kenosis) provides the unopinionated polynomial canvas ($y^0$) upon which custom domains are mounted. Interoperability with external schemas is achieved via:
* **Right Kan Extensions ($\text{Ran}$)**: Inferring abstract laws and limits (Plato's problem / completion).
* **Left Kan Extensions ($\text{Lan}$)**: Integrating concrete features and colimits (Orwell's problem / filtering).

---

## 3. Connections

- **[[Making_Illegal_States_Unrepresentable]]**: The type-driven design pattern enforcing validity.
- **[[Least_Action_Principle]]**: Geodesic optimization over the representation space.
- **[[Software_Lagrangian]]**: The thermodynamic quality metric of representational abstraction.
- **[[Epiplexity]]**: The cost of extracting representations.
- **[[Magnitude]]**: Relational cardinality measuring representational size.

## See also

- [[3E_Framework]]
- [[MCard]] · [[PCard]] · [[VCard]]
- [[Yoneda_Lemma]]
