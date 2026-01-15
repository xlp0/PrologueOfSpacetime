# 06. Coproducts

**Source:** [HoTT Math YouTube Channel](https://www.youtube.com/watch?list=PLFMMwXV6jh1QZhEgJE-LhlmHQWzyP0GPe&index=6)

## Video Summary
The sixth video in the series, titled **"Coproducts,"** introduces the **coproduct type ($A + B$)**, which serves as the mathematical foundation for "choice" and "branching," acting as the counterpart to the product type.

### Key Concepts

*   **Disjunction: The "OR" Relationship**
    In set theory known as a disjoint union, the **coproduct type** represents a logical "OR".
    *   **Inhabitants:** Unlike a product (which needs both $x$ AND $y$), a coproduct $A + B$ is inhabited if you have a term from $A$ **OR** a term from $B$.

*   **Injections**
    Terms are constructed via **injection**:
    *   **Left Injection:** Maps a term $x:A$ into $A + B$.
    *   **Right Injection:** Maps a term $y:B$ into $A + B$.
    *   This preserves the "history" of where the term came from (Left or Right path).

*   **Logic Completeness**
    With coproducts, HoTT now has a full suite of logical operations: Proofs, Negations ($\neg$), Implications ($\to$), Universal Quantifiers ($\forall$), Conjunctions ($\times$), and Disjunctions ($+$).

## Prologue of Spacetime Integration

### 1. Branching Narratives in "Vibe Coding"
The **coproduct type** is the formal model for **branching paths** in an interactive narrative.
*   **The Fork:** If a user faces "Choice A" or "Choice B," the resulting state is type $A + B$.
*   **Narrative Flow:** "Left Injection" transitions the system context to A; "Right Injection" transitions to B. The "Conversation" remains mathematically valid regardless of the path taken.

### 2. Choice-Based MCards (Monadic Containers)
While Product MCards are fixed pairs, a **Coproduct MCard** represents a **"Choice Container."**
*   **Polymorphic Content:** Used when an MCard might contain one of two distinct data types (e.g., $Image + Text$).
*   **Handling:** The system handles the general type $Image + Text$, only "unpacking" the specific content (via pattern matching on the injection) when processed.

### 3. Resilience in "Distributed Verification"
Coproducts model **Redundancy Logic** in Zero Trust systems.
*   **Robust Access:** Unlike the "AND" logic of MFA (Product Type), a "Disjunction" ($Biometric + Key$) acts as a fail-safe.
*   **Proof Validity:** "Access" is granted if *either* proof is provided. This models systems where multiple valid paths lead to the same successful state, increasing resilience.
