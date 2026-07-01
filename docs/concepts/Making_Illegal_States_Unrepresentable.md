---
title: 'Making Illegal States Unrepresentable'
date: 2026-07-01
tags: [Trivium-Grammar, Seven-Liberal-Arts]
type: concept
sources: [raw/articles/Cognitive_Ascent_Mission_Guide.pdf]
status: draft
liberal_art: Trivium-Grammar
---

# Making Illegal States Unrepresentable

> The design principle of Type-Driven Design where a system's type signatures are engineered so that invalid or impossible configurations are mathematically impossible to express.

## 1. Definition

Coined by Yaron Minsky (CTO of Jane Street) in 2010 and popularized by Scott Wlaschin, the principle of **Making Illegal States Unrepresentable (MISU)** shifts verification from runtime checks to compile-time guarantees. 

Under the **Curry-Howard-Lambek Isomorphism**, this is equivalent to designing types such that invalid states correspond to uninhabited types (e.g., `Void` in Haskell/Scala, or empty types in Homotopy Type Theory):

| Logic / Proof Theory | Type Systems / ADTs | System Engineering |
| :--- | :--- | :--- |
| Impossible Proposition ($\bot$) | Uninhabited Type (`Void` / `never`) | Illegal System State |
| Implication ($A \Rightarrow B$) | Function Type ($A \to B$) | Valid State Transition |
| Disjunction ($A \lor B$) | Sum Type ($A + B$) | Mutually Exclusive Alternatives |
| Conjunction ($A \land B$) | Product Type ($A \times B$) | Compounded Dependencies |

### 1.1 Irreducibility as the Bedrock
MISU achieves correctness by constraining representable values to an **irreducible valid space**. Sum types ($A + B$) and Product types ($A \times B$) serve as the irreducible type constructors:
* **Sum Types**: Represent mutually exclusive, irreducible choices (e.g., an Order is *either* Pending *or* Shipped with tracking, preventing a "Shipped order with no tracking" state).
* **Product Types**: Represent irreducible combinations of dependencies.
Together, they form the algebraic primitives (along with Unit and Void) that compile domain logic into correct-by-construction code.

---

## 2. In the Prologue and the 3E Framework

In the **[[Prologue_of_Spacetime|Prologue of Spacetime]]**, MISU is the logical foundation of **Efficacy** (the first dimension of the **[[3E_Framework|3E Framework]]**):

* **Efficacy**: Measures whether the system has sufficient structural richness to span the solution space without leaking into failure states. By making illegal states unrepresentable, Efficacy is guaranteed because the compiler prevents the execution of invalid configurations.
* **The Plato-Orwell Galois Connection**: Under Abstract Interpretation, learning and verification are modeled as a Galois Connection between Plato's generalization ($\alpha$) and Orwell's verification ($\gamma$):
  $$\alpha(c) \sqsubseteq a \iff c \sqsubseteq \gamma(a)$$
  Without MISU, the Orwellian verification operator ($\gamma$) is manual, requiring developers to write runtime validations. With MISU, $\gamma$ is **automatic and type-enforced**, converging to a sound fixed point where no invalid state can be constructed:
  $$\boxed{\text{MISU} = \text{Making } \gamma \text{ (Orwellian Verification) Automatic}}$$

### 2.1 The CLM and VCard Sandwiches
In the **[[Cubical_Logic_Model|Cubical Logic Model (CLM)]]**, MISU is operationalized by the **[[VCard]] Sandwich** (`prep → exec → post`). The `prep` transition eliminates invalid inputs (Sum Elimination), and the `post` transition traps unexpected side-effects (Product Introduction), ensuring that only representable, verified terms reach the Single Source of Truth (SSOT).

---

## 3. Connections

- **[[Representability]]**: The mathematical limit of expression via the Yoneda Lemma.
- **[[Software_Lagrangian]]**: Minimizing computational action by eliminating high-entropy invalid states.
- **[[3E_Framework]]**: Guarantees the Efficacy of the system.
- **[[Awareness_of_Opportunities]]**: Enforces type safety on the ABC learning cycle.
- **[[Digital_Synesthesia]]**: Translates compiler constraints into structural resonance.

## See also

- [[Trivium]] x [[Quadrivium]]
- [[MCard]] · [[PCard]] · [[VCard]]
- [[Abstract_Interpretation]]
