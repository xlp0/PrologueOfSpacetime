---
aliases:
  - Type Theory
  - type theory
title: "Type Theory: a universal framework for namespace management"
subject: Type, Category Theory, CT for Programmers, Type Systems, Proof Vocabulary, DDL, DML, Curry-Howard, Proposition, Axiom, Theorem, Empty Schema Principle
authors: Ben Koo, Bard, ChatGPT, Antigravity
modified: 2025-12-24T10:45:00+08:00
---
[Type theory](https://www.wikiwand.com/en/Type_theory) or [[intuitionistic type theory]] is a formal system used in computer science, mathematics, and philosophy to study the properties of mathematical objects and their relationships. It provides a foundation for constructing and reasoning about programs, proving theorems, and understanding the structure of mathematical concepts. It is particularly useful in [[Namespace Management]].

In type theory, every expression has a type associated with it, which defines the set of values that expression can take. Types can be simple (e.g., numbers or booleans) or complex (e.g., functions or sets). The type system ensures that expressions are used in a consistent manner, preventing errors such as adding a number to a string.

One key aspect of type theory is the concept of [[dependent types]]. Dependent types allow types to depend on values, enabling more precise specifications and more expressive programming languages. This allows for advanced features like dependent function types and dependent pattern matching.

Type theory also includes notions such as type inference, which automatically deduces the types of expressions based on their context, and parametric polymorphism, which allows functions to be applied to arguments of different types.

Type theory also includes notions such as type inference, which automatically deduces the types of expressions based on their context, and parametric polymorphism, which allows functions to be applied to arguments of different types.

# Girard's Paradox and the Universe Hierarchy

A critical insight in the development of modern Type Theory comes from **[[Literature/People/Jean-Yves Girard|Jean-Yves Girard]]**, who discovered **Girard's Paradox**.
*   **The Paradox**: In early systems (like System U), it was possible to define a "Type of all Types" (`Type : Type`). Girard showed that this leads to logical inconsistency, similar to Russell's Paradox.
*   **The Implication**: A system cannot be both **expressive enough to describe itself** and **flat**.
*   **The Resolution**: **Stratification**. Valid Type Theories must implement a **Universe Hierarchy** ($U_0 \in U_1 \in U_2 \dots$). This ensures that any meta-reasoning happens at a strictly higher level than the object being reasoned about.
*   **Connection to GoI**: This stratification is the static counterpart to the dynamic stability ensured by **[[Hub/Theory/Category Theory/Logic/Geometry of Interaction|Geometry of Interaction]]**.

# What are the main branches of Type Theory

The main branches of Type Theory are:

1. [[Martin-Löf Type Theory]] ([[MLTT]]): Developed by Per Martin-Löf, MLTT is one of the most widely studied and used branches of Type Theory. It is a constructive type theory that provides a foundation for both mathematics and computer science.

2. [[Homotopy Type Theory]] ([[HoTT]]): Homotopy Type Theory combines concepts from homotopy theory and type theory. It explores the relationship between spaces and types, with the aim of providing a foundation for mathematics based on higher-dimensional structures.

3. [[Extensional Type Theory]] ([[ETT]]): Extensional Type Theory focuses on equality between types or terms, allowing for more flexible reasoning about equality compared to intensional type theories.

4. [[Intensional Type Theory]] ([[ITT]]): Intensional Type Theory emphasizes computational aspects and proofs-as-programs interpretation, where types are seen as sets or collections of values.

5. [[Dependent type theory]]: Dependent Type Theory extends traditional type systems by allowing types to depend on values, enabling more expressive and precise specifications of programs or mathematical structures.

6. [[Categorical Type Theory]]: Categorical Type Theory bridges the gap between [[category theory]] and type theory by using category-theoretic concepts to study the structure and properties of types.

1. [[Constructive Set Theory]]: Constructive Set Theory is an alternative to classical set theory that is based on constructive logic principles, where sets are defined in terms of their elements and the operations that can be performed on them.
2. [[Naïve Type Theory]] ([[NTT]]) is a foundational theory in the field of mathematics and computer science. It is based on the concept of types, which classify mathematical objects and expressions. NTT treats types as first-class citizens, meaning that they can be manipulated and used as objects themselves.
3. [[@YonedaEmbeddingExpresses2023|The Yoneda Embedding Expresses Whether, What, How, Why]]: The [[WH questions]] can be expressed in Category Theory, and provides a natural language interpretation of [[Type Theory]].

These branches of Type Theory often overlap and influence each other, leading to further developments in the field.

## Comparison with Number Theory for Namespace Management

Type Theory and [[Number Theory in Namespace Management|Number Theory for Namespace Management]] address complementary aspects of structure and correctness:

| Aspect | Type Theory | NSM / Number Theory |
|--------|------------|---------------------|
| **Primary focus** | Formal specification and verification of programs, proofs, and mathematical objects | Efficient, scalable naming, addressing, and partitioning using arithmetic |
| **Core objects** | Types, terms, typing judgments, inference rules, dependent types | Integers, residues, primes, ideals, quotient structures, number-theoretic functions |
| **View of errors** | Ill-typed terms are rejected; illegal states become unrepresentable | Bad namespaces show up as collisions, poor distribution, or leaking invariants |
| **Role of functions** | Functions are typed morphisms; function types and dependent function types central to express behavior | Hash functions, modular maps, and key-derivation functions shape the identifier space and its security/performance properties |
| **Foundational story** | Curry–Howard: propositions-as-types, proofs-as-programs; basis for proof assistants (e.g. [[Lean]]) | [[Fundamental theorem of arithmetic]], modular arithmetic, and [[quotient structures]] supply a compact, domain-independent vocabulary for namespaces |
| **Verification** | Proofs (possibly machine-checked) show that terms satisfy specifications | Number-theoretic [[invariants]] can be expressed as types/propositions in a type theory and mechanically verified for concrete NSM designs |
| **Namespace interpretation** | Namespaces arise as type-level classifications and module/namespace constructs in languages | Namespaces arise as quotient/decomposition of arithmetic spaces with number-theoretic operations providing the mechanics |

For a concrete, infrastructure-level application of number theory that Type Theory can formalize and verify, see [[Number Theory in Namespace Management|Number Theory for Namespace Management]].

---

## Type Theory, Proof Vocabulary, and the DDL/DML Duality

A critical connection exists between **Type Theory**, the **[[Literature/PKM/Tools/DataSecurity/Proof|Proof Vocabulary]]**, and the **[[Hub/Tech/DDL and DML - The Structure-Content Duality|DDL/DML duality]]**. This section explains how Type Theory deals with **foundational** and **expanded vocabulary** in its formalized language.

### The Curry-Howard-Lambek Isomorphism: The Triadic Foundation

The **[[Curry-Howard-Lambek isomorphism]]** establishes a **Triadic Foundation** for understanding:

| Logic (**Proof**) | Type Theory (**Meaning**) | Category Theory (**Structure**) |
|-------------------|--------------------------|--------------------------------|
| **[[Hub/Theory/Category Theory/Logic/Proposition\|Proposition]]** | Type | Object |
| **[[Literature/PKM/Tools/DataSecurity/Proof\|Proof]]** | Term (inhabitant) | Morphism |
| **Implication (A → B)** | Function type (A → B) | Arrow (Hom(A, B)) |
| **Conjunction (A ∧ B)** | Product type (A × B) | Product |
| **Disjunction (A ∨ B)** | Sum type (A + B) | Coproduct |
| **True (⊤)** | Unit type `()` | Terminal Object |
| **False (⊥)** | Empty type `Void` | Initial Object |

> **The Triadic Slogan**: $\boxed{\text{Proof} \cong \text{Meaning} \cong \text{Structure}}$

| Pillar | Domain | Role |
|--------|--------|------|
| **Proof** | Logic | **Justification** — Why is it true? |
| **Meaning** | Semantics/Type Theory | **Interpretation** — What does it signify? |
| **Structure** | Grammar/Category Theory | **Organization** — How is it composed? |

**Key Insight**: In Type Theory, **propositions ARE types** and **proofs ARE programs** (terms that inhabit types). This means the [[Literature/PKM/Tools/DataSecurity/Proof|proof vocabulary]] (Axiom, Proposition, Lemma, Theorem, etc.) maps directly to type-theoretic concepts.

> For the complete synthesis, see **[[Hub/Theory/Integration/Proof and Meaning - The Curry-Howard Foundation of Understanding|Proof, Meaning, and Structure: The Triadic Foundation]]**.


### Proof Vocabulary as Type-Theoretic Constructs

The mathematical vocabulary used in proofs corresponds to different **roles** in the type system:

| Proof Term | Type-Theoretic Role | Description |
|------------|---------------------|-------------|
| **[[Hub/Theory/Category Theory/Logic/Axiom\|Axiom]]** | **Postulated Type** (assumed inhabited) | A type we assume has an inhabitant without constructing one. In [[Hub/Theory/Category Theory/Logic/Proof/Lean 4\|Lean]]: `axiom A : Type`. |
| **[[Hub/Theory/Category Theory/Logic/Definition\|Definition]]** | **Type Alias** (abbreviation) | A new name for an existing type. In Lean: `def A := B`. |
| **[[Hub/Theory/Category Theory/Logic/Proposition\|Proposition]]** | **Type** (to be inhabited) | A type whose inhabitant (proof) we seek. In Lean: `theorem A : P`. |
| **[[Hub/Theory/Category Theory/Logic/Lemma\|Lemma]]** | **Helper Function Type** | A smaller function (proof) used to build larger ones. In Lean: `lemma A : P := ...`. |
| **[[Hub/Theory/Category Theory/Logic/Theorem\|Theorem]]** | **Target Function Type** | The main result—a type we successfully inhabit. In Lean: `theorem A : P := ...`. |
| **[[Hub/Theory/Category Theory/Logic/Corollary\|Corollary]]** | **Composed Function Type** | A type trivially inhabited by composing theorem with simple functions. |
| **[[Literature/PKM/Tools/DataSecurity/Proof\|Proof]]** | **Term (Inhabitant)** | The actual term that has type Proposition. |

### Foundational vs. Expanded Vocabulary in Type Theory

Type Theory distinguishes between **foundational types** (built-in primitives) and **expanded vocabulary** (user-defined types):

| Category | Foundational (DDL-like) | Expanded (DML-like) |
|----------|------------------------|---------------------|
| **In Type Theory** | Primitive types ($\mathbb{N}$, `Bool`, `→`, `×`, `+`) | User-defined types (`User`, `Order`, `MyTheorem`) |
| **In Logic** | [[Hub/Theory/Category Theory/Logic/Axiom\|Axioms]], basic connectives ($\land, \lor, \to$) | [[Hub/Theory/Category Theory/Logic/Proposition\|Propositions]], [[Hub/Theory/Category Theory/Logic/Theorem\|Theorems]] |
| **In Databases** | [[Hub/Tech/DDL and DML - The Structure-Content Duality\|DDL]] (schema) | [[Hub/Tech/Data Manipulation Language\|DML]] (data) |
| **Role** | **Defines what CAN exist** | **Defines what DOES exist** |
| **Temporal** | Fixed at language/theory design time | Evolves as users add content |

### The DDL/DML Duality in Type Theory

The **[[Hub/Theory/Integration/The Empty Schema Principle - Domain-Independent Knowledge Through Zero Assumptions|Empty Schema Principle]]** applied to Type Theory:

```
┌───────────────────────────────────────────────────────────────┐
│                TYPE THEORY AS EMPTY SCHEMA                    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  DDL (Foundational Types):                                    │
│    • Primitive types: ℕ, Bool, Unit, Void                     │
│    • Type constructors: →, ×, +, Σ, Π                         │
│    • Inference rules: function application, abstraction       │
│    • Universe hierarchy: U₀ : U₁ : U₂ : ...                   │
│                                                               │
│  DML (User-Defined Content):                                  │
│    • New type definitions: `inductive MyList (A : Type)`      │
│    • New theorems: `theorem my_theorem : P → Q`               │
│    • New axioms (postulates): `axiom funext : ...`            │
│    • Library content: Mathlib, Stdlib, etc.                   │
│                                                               │
│  At t₀: DDL exists, DML = ∅ (empty theory)                    │
│  At tₙ: DDL unchanged, DML = rich library                     │
└───────────────────────────────────────────────────────────────┘
```

### How Type Theory Handles Vocabulary Expansion

Type Theory provides mechanisms for **safely extending** the vocabulary:

| Mechanism | Type-Theoretic Tool | Safety Guarantee |
|-----------|---------------------|------------------|
| **Inductive Types** | `inductive`, `data` | Ensures well-foundedness; no infinite regress. |
| **Type Aliases** | `def`, `abbrev` | Conservative; doesn't add proof power. |
| **Axioms** | `axiom`, `postulate` | User's responsibility; may break consistency. |
| **Universe Polymorphism** | `Type u` | Avoids Girard's Paradox via stratification. |
| **Modules/Namespaces** | `namespace`, `section` | Organizes vocabulary; controls scope. |

**Example in Lean 4**:

```lean
-- DDL-like: Foundational primitives (built into Lean)
-- Π, Σ, →, ×, +, ℕ, Bool, etc.

-- DML-like: User-defined content
inductive MyList (A : Type) where
  | nil : MyList A
  | cons : A → MyList A → MyList A

-- Axiom (postulated, must be used carefully)
axiom myAxiom : ∀ (A : Type), A → A

-- Definition (conservative extension)
def id (A : Type) (a : A) : A := a

-- Theorem (inhabited type via proof)
theorem id_applied : ∀ (n : ℕ), id ℕ n = n := by
  intro n
  rfl
```

### Type Theory and CLM

The **[[Hub/Tech/Cubical Logic Model|Cubical Logic Model]]** implements Type Theory's DDL/DML duality:

| CLM Component | Type-Theoretic Analog | DDL/DML Role |
|---------------|----------------------|--------------|
| **Three Dimensions (A/C/B)** | Core type constructors | **DDL** (fixed structure) |
| **Abstract Specification** | Type declaration | **DDL** (what we want) |
| **Concrete Implementation** | Term construction | **DML** (program/proof) |
| **Balanced Expectations** | Type checking + tests | **Verification** |
| **MCard** | Proof witness (term) | **DML** (artifact) |

> **Key Insight**: CLM is a **typed DML**—it applies Type Theory's type-safety to data manipulation. See **[[Hub/Tech/CLM and the Empty Schema - How Proof Vocabulary Enables Soundness and Completeness|CLM and the Empty Schema]]** for how this achieves Soundness and Completeness.

---

# Conclusion

Overall, type theory provides a rigorous framework for specifying and verifying the behavior of programs and mathematical proofs. It has influenced the development of programming languages like [[Haskell]], [[Coq]], and [[Agda]], as well as various branches of mathematics and philosophy.

# References

```dataview
Table title as Title, authors as Authors
where contains(subject, "Type Theory") or contains(title, "Type Theory") or
contains(subject, "type theory") or contains(title, "type theory") 
```