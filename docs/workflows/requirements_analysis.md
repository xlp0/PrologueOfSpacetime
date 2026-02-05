# Requirement Analysis: "Space Time" Simulatory Engine

**Version:** 2.0 (Axiomatic Revision)
**Architect:** System Architect / Cosmologist
**Domain:** Computational History / Generative Publishing

---

## 1. System Overview & The "Dining Philosophers" Metaphor

The "Space Time" engine is not merely a chat bot; it is a **closed-loop historical simulator**. It utilizes a **"Dining Philosophers" topology** where the scarce resource is not food, but the **Context Window (Token Budget)**.

To prevent "intellectual stagnation" (deadlock), the system employs an evolutionary mechanism (The Swapping Gate) to rotate agent personas, ensuring the output is a divergent synthesis of ideas rather than a linear summary. We define this as a **Generative Adversarial Collaboration (GAC)** system.

---

## 2. Axiomatic Constraints (Immutable Laws)

These assertions are fundamental to the system's operation and cannot be overridden by agent prompts.

### Axiom I: The Law of Sequentiality (Round-Robin)
$$ \forall t \in T, Speaker(t) = P_{(t \pmod 5)} $$
*   The conversation MUST proceed in a strict ring: $P_0 \to P_1 \to P_2 \to P_3 \to P_4 \to P_0$.
*   No agent may speak out of turn. "Interrupting" is architecturally impossible.

### Axiom II: The Law of Entropy (Abel-Ruffini)
$$ E(Turn) = \sum_{i=0}^{n} p_i \log_b p_i $$
*   The system acknowledges that a 5-agent debate cannot be "solved" (converged) by simple linear summarization.
*   **Constraint:** If `Entropy < Threshold` (Agents are agreeing too much), the system **MUST** inject a perturbation (e.g., a "Black Swan Event" prompt) to destabilize the equilibrium.

### Axiom III: The Law of Finite Memory (Context Folding)
*   The Universe (Context Window) is finite.
*   **Constraint:** At the end of every Cycle (5 turns), the oldest Cycle MUST be compressed into a "Holographic Summary" (Vector Embedding) and removed from the active context.

---

## 3. Functional Requirements (FR)

### 3.1 The Pentagonal Persona Configuration
The Table shall always be seated with 5 archetypes, initially defined as:

| Seat | Archetype | Domain Focus | Bias Vector |
| :--- | :--- | :--- | :--- |
| **P1** | **The Physicist** | Thermodynamic limits, semiconductors, vacuum tubes | *Materialist* |
| **P2** | **The Financier** | Capital allocation, ROI, market dominance | *Pragmatist* |
| **P3** | **The Politician** | Geopolitics, funding (ARPA), national security | *Statist* |
| **P4** | **The Mathematician** | Logic, complexity theory, algorithms | *Idealist* |
| **P5** | **The Technologist** | Architecture, packet switching, implementation | *Constructivist* |

### 3.2 Evolutionary Dynamics (The Swapping Gate)
**FR-06:** The system MUST implement a **"Swapping Gate"** that triggers exactly every **5 rounds** (the "Quintic Threshold").

At this Gate:
1.  **Evaluate:** An external "Evaluator" scores each agent on **Information Gain (IG)**.
    > *"Did this agent introduce new facts, or merely restate existing ones?"*
2.  **Eliminate:** The agent with the lowest IG score is evited.
3.  **Inject:** A new agent is drawn from the **Reserve Pool** (e.g., `LaborHistorian`, `Cyberneticist`, `Artist`) and seated in the empty slot.
4.  **Rationale:** This ensures the conversation evolves from "How to build a computer" (Tech/Physics focus) to "How to live with a computer" (Society/Labor focus) over time.

### 3.3 The Semantic Harvester ("Consensus Events")
**FR-09:** A parallel daemon (The Harvester) MUST monitor the event stream.
**FR-10:** It detects **"Consensus Events"**:
> *Definition:* A Consensus Event occurs when $Agent_A$ (Thesis) and $Agent_B$ (Antithesis) are followed by $Agent_C$ providing a Synthesis that references both prior agents with positive sentiment.
**FR-11:** Upon detection, the Harvester triggers the `generate_chapter_artifact` workflow.

---

## 4. Mathematical Logic Specifications

### 4.1 The Combination Index (CI)
To determine if a turn is "harvestable," we calculate the Combination Index:

```python
def calculate_combination_index(turn, history):
    # 1. Semantic Distance from previous turn (Novelty)
    novelty = cosine_distance(turn.embedding, history[-1].embedding)
    
    # 2. Reference Density (Connection)
    references = count_references(turn.content, history)
    
    # 3. Sentiment Alignment (Consensus)
    sentiment = analyze_sentiment(turn.content)
    
    # CI = (Novelty * Connection) / Friction
    ci = (novelty * references) / (1 + abs(sentiment.friction))
    return ci
```

*   If $CI < 0.5$: **Stagnation.** Trigger "Objection" prompt.
*   If $CI > 1.5$: **Chaos.** Trigger "Socratic" stabilization.
*   If $0.8 < CI < 1.2$: **Synergy.** Harvest immediately.

---

## 5. System Sequence Diagram (The Cycle)

1.  **Initialization:** The `DiningTableManager` seats P1-P5.
2.  **Debate Loop (Turns 1-5):**
    *   P1 holds token $\rightarrow$ Generates thought.
    *   `Harvester` calculates CI.
    *   Token passes to P2.
3.  **The Quintic Gate (Turn 5):**
    *   `Evaluator` runs `rank_agents()`.
    *   *Result:* "The Mathematician is too abstract." $\rightarrow$ **EVICT**.
    *   `ReservePool` selects "The Labor Unionist".
    *   **INJECT** Labor Unionist into Seat P4.
4.  **Context Folding:**
    *   Turns 1-5 represent the "Vacuum Tube Era".
    *   `Summarizer` compresses them into a single node: *"The physical limits of vacuum tubes (P1) forced a capital crisis (P2), resolved by government intervention (P3)."*
    *   Raw turns are flushed from active memory.
5.  **Next Epoch:** The cycle repeats with the new agent mix.