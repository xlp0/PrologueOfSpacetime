# HoTT Math Course Notes

This directory contains notes and resources for the **Homotopy Type Theory (HoTT)** video series by the [HoTT Math YouTube channel](https://www.youtube.com/@HoTTMath).

## Course Overview

### **Foundations and Basic Concepts**
*   **#1 Homotopy Type Theory Explained: A New Foundation for Mathematics:** This video introduces Homotopy Type Theory (HoTT) as a single language for algebra, topology, and logic. It defines **types as spaces** and **terms as points**. It distinguishes types from sets by how they handle equality: equality is viewed as a **path** with shape and structure, and multiple paths can exist between terms. These "paths of paths" are called **homotopies**, which can extend to infinity.
*   **#2 Universes, Functions, and Π-types:** This entry introduces **universes**, which are types whose terms are themselves types, existing in an infinite nested hierarchy. It explains function types ($A \to B$) and **type families**, which are functions mapping to a universe. It also details **$\Pi$-types**, which allow for **dependent functions** where the output type depends on the input term.
*   **#10 Path Induction:** Returning to the spatial view of types, this video introduces the **principle of path induction**. It explains that to prove a property for any path, one only needs to prove it for the reflexivity path ($refl_x$) from a term to itself. This principle is used to prove that equalities are **symmetrical**.

### **Logic and Propositions**
*   **#3 Propositions as Types:** This video explores how types can represent propositions, where an inhabitant of a type serves as a **proof**. It defines **falsehood (negation)** as a function from a proposition to an empty type and **implication** as a standard function between types.
*   **#4 Universal Quantifiers:** Building on the previous logic video, this explains how **dependent functions** ($\Pi$-types) serve as the type-theoretic analogue for the **universal quantifier** ("for all $x$").
*   **#5 Products:** This video covers **product types** ($A \times B$), which represent pairs of terms and use **projections** ($\pi_1, \pi_2$) to extract them. In logic, product types represent **conjunctions** (the "AND" operator).
*   **#6 Coproducts:** This details **coproduct types** ($A + B$), which use left and right injections to construct terms. Logically, they represent **disjunctions** (the "OR" operator).
*   **#7 Σ-types:** This introduces **$\Sigma$-types**, which generalize product types into **dependent pairs**. While a standard product type uses fixed types, a $\Sigma$-type's second term's type depends on the first term.
*   **#8 Existential Quantifiers:** This explains that applying $\Sigma$-types to propositions creates the type-theoretic equivalent of the **existential quantifier** ("there exists").
*   **#9 Law of Excluded Middle, Lambda Calculus:** This video argues that the **Law of Excluded Middle (LEM)** does not hold in HoTT because not all propositions are provably true or false. However, it uses **$\lambda$-calculus** to prove that LEM is "not not true" ($\neg\neg (A + \neg A)$).

### **Inductive Types and Arithmetic**
*   **#11 Inductive Types, Finite Sets, Natural Numbers:** This video teaches how to build types from scratch. It covers **finite sets** like the unit type (one term) and **infinite sets** like **natural numbers**, which use constructors for zero and the successor function.
*   **#12 Addition, Currying, Functions from Inductive Types:** This entry explains how to construct functions from inductive types and introduces **currying** to handle multiple arguments. These methods are used to define **addition** in type theory.
*   **#13 Recursors, Multiplication, Factorial:** This video introduces **recursors** as a systematic way to define functions by mapping constructors to sequences. It demonstrates defining multiplication and **factorial** using recursors and **pattern matching**.
*   **#14 Inductors:** This explains **inductors** as a generalization of recursors for dependent functions. It highlights that applying inductors to propositions is the type-theoretic analogue of **mathematical induction**.

### **Advanced Topology and Fibrations**
*   **#15 Higher Inductive Types, Circle, Sphere:** This video moves beyond ordinary sets to **Higher Inductive Types (HITs)**, which include **path constructors**. It explains the **circle type ($S^1$)** with a loop constructor and the **sphere ($S^n$)** using higher-dimensional path constructors like "surf".
*   **#16 Torus, Transitivity of equality:** This video uses path induction to prove that equality is **transitive** and explores path composition. It then uses these compositions to define the **torus** with two base paths and a path of paths between their compositions.
*   **#17 Fibrations, Transport:** This entry introduces the **transport function**, which moves terms between types in a type family along a path. It defines **fibrations** as a "total space" ($ \Sigma $-type) lying over a "base space," where each point in the base maps to a **fibre**.
*   **#18 Path-lifting:** Building on fibrations, this video explains how to construct paths between pairs. It specifically details **path-lifting**, where a path in the base space is "lifted" to a path in the total space using the transport function.
*   **#19 Mapping out of S¹, functoriality:** This final video explains **functoriality**, the principle that functions respect equality by mapping paths to paths. It concludes by showing how to construct functions out of the **circle type** using its recursion principle.
