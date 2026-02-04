# 03. Propositions as Types

**Source:** [HoTT Math YouTube Channel](https://www.youtube.com/watch?v=RjBwYyrXnNw&list=PLFMMwXV6jh1QZhEgJE-LhlmHQWzyP0GPe&index=3)

## Video Summary
The third video in the series, titled **"Propositions as Types,"** explores how Homotopy Type Theory reconstructs the foundations of logic by treating types as mathematical statements.

### Key Concepts

*   **Types as Propositions**
    The video introduces the "Propositions as Types" principle, where a **proposition** (a statement that can be true or false) is represented as a **type**.
    *   **Proof as Inhabitant:** To prove that a proposition $P$ is true, one must construct a **term** within that type. If the type $P$ is inhabited by a term, the proposition is true; the term itself serves as the **proof**.
    *   **Multiple Proofs:** Unlike classical logic, where a statement is simply "true," HoTT allows for **multiple distinct inhabitants** (proofs) to exist for a single proposition. This aligns with the earlier concept that there can be multiple distinct paths (equalities) between terms.

*   **Falsehood and Negation**
    The sources explain how to represent the concept of "false" using the **empty type**, which is a type that contains no inhabitants.
    *   **Defining Negation:** A proposition is considered false if we can construct a **function** from that proposition to the empty type ($\neg P \iff P \to \bot$).
    *   **The Logic of Vacuity:** Such a function can only be defined if the starting proposition has no terms to map in the first place. Therefore, if a function to the empty type exists, the proposition must be uninhabited.

*   **Logical Implication**
    Standard **functions** serve as the mechanism for logical **implication**.
    *   **Constructing Proofs:** A function from proposition $P$ to proposition $Q$ ($P \to Q$) means that whenever we are provided with a term (proof) in $P$, we can systematically construct a term (proof) in $Q$.

## Prologue of Spacetime Integration

### 1. Logic as Context Transformation
In the context of the **Conversational Programming** model, logical implication ($P \to Q$) suggests that "Logic" is not a static set of rules but a **transformation of contexts**.
*   **Proof = Value / Proposition = Context:** If a 'Proof' is a 'Value' and a 'Proposition' is a 'Context,' then implication is the process of using a value in one context to generate a value in another.
*   **Constructive Logic:** A statement is only true if we can *construct* a value for it. This reinforces the **"Vibe Coding"** principle where code/narrative only proceeds if a valid state (term) can be passed forward.

### 2. Truth and Zero Trust
*   **Proof of Work:** The "Propositions as Types" principle aligns with **Zero Trust**. An MCard (Proposition) is not implicitly trusted or "True"; it is only valid if it contains a verifiable **payload** (Term/Proof).
*   **Multiple Truths:** The existence of "multiple distinct inhabitants" for a proposition supports the **plurality of narrative paths**. Different users might provide different "Proofs" (actions/terms) for the same "Proposition" (Quest/Context), all of which are valid but distinct.

### 3. Negation as Failed State
*   **The Empty Card:** The **Empty Type** models a **Failed Monadic State** (e.g., `Maybe Nothing` or `Either Left`).
*   **Constraint Checking:** A constraint is a function that demonstrates a specific state leads to a contradiction (the Empty Type). If a user's input maps to `Void`, the path is blocked (False).
