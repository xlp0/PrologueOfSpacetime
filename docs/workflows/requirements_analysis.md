# Requirement Analysis: "Space Time" Simulatory Engine

**Version:** 3.0 (Parallel Axioms)
**Architect:** System Architect / Cosmologist
**Domain:** Computational History / Generative Publishing

---

## 1. System Overview & The "Parallel Evolution" Metaphor

The "Space Time" engine is a **Massively Parallel Historical Simulator**. It rejects the linear "Ring" of the Dining Philosophers in favor of a **"Many-Worlds" Tournament**.

Utilizing high-ram infrastructure (1.2TB), the system spawns all 5-7 agents simultaneously in each epoch. They do not wait to speak; they speak at once, and then **vote** to decide which timeline becomes canonical. We define this as a **Darwinian Epistemology Engine**.

---

## 2. Axiomatic Constraints (Immutable Laws)

These assertions are fundamental to the system's operation and cannot be overridden by agent prompts.

### Axiom I: The Law of Simultaneity (The Burst)
$$ \forall t \in T, P_{all} \to Generate(\Delta t) $$
*   **Constraint:** All agents MUST generate their output for Epoch $N$ concurrently.
*   **Rationale:** We do not want Agent B to be biased by Agent A's opening. We want 5 independent "takes" on history, which are then reconciled.

### Axiom II: The Law of Darwinian Consensus (The Vote)
$$ Winner_N = \max(Vote(P_i \to P_j)) $$
*   **Constraint:** At the end of every Burst, every agent MUST cast a scored vote (0-10) for every peer's output.
*   **Constraint:** The agent with the lowest aggregate score is **Deleted from Existence** (removed from memory) and replaced by a Reserve Agent.

### Axiom III: The Law of Finite Memory (Context Folding)
*   **Constraint:** Only the **Winning Persona's output** is written to the "Official History" (Context Window). The "Loser Timelines" are discarded (or archived in cold storage), preventing context pollution.

---

## 3. Functional Requirements (FR)

### 3.1 The Tournament Roster
The simulation supports up to 5-7 concurrent agents.

| Seat | Archetype | Domain Focus | Bias Vector |
| :--- | :--- | :--- | :--- |
| **P1** | **The Physicist** | Thermodynamic limits, semiconductors, vacuum tubes | *Materialist* |
| **P2** | **The Financier** | Capital allocation, ROI, market dominance | *Pragmatist* |
| **P3** | **The Politician** | Geopolitics, funding (ARPA), national security | *Statist* |
| **P4** | **The Mathematician** | Logic, complexity theory, algorithms | *Idealist* |
| **P5** | **The Technologist** | Architecture, packet switching, implementation | *Constructivist* |
| **P6** | **The Cyberneticist** | Feedback loops, control theory | *Systemic* |
| **P7** | **The Labor Historian**| Union dynamics, automation impact | *Humanist* |

### 3.2 Evolutionary Dynamics (The Elimination Round)
**FR-06:** The system triggers an **Elimination Event** after *every* Burst (not every 5 rounds).
**FR-07:** The **Peer Review Protocol** masks the identities of the authors.
    > *"Review these 4 drafts. Rate them on Insight and Novelty. Do not know who wrote them."*
**FR-08:** The lowest performing agent is replaced immediately. This creates extreme pressure to perform or perish.

### 3.3 The Semantic Harvester ("Consensus Events")
**FR-09:** A parallel daemon (The Harvester) monitors the **Voting Matrix**.
**FR-10:** It detects **"Unanimous Acclaim"**:
    > *Definition:* When >80% of agents vote for a single draft with a score >9/10.
**FR-11:** This triggers the "Canonization" workflow, minting that draft as a permanent Chapter in the Book.

---

## 4. Mathematical Logic Specifications

### 4.1 The Divergence-Convergence Loop
The flow follows a standard Map-Reduce pattern:

1.  **Diverge (Map):**
    $$ Output_i = LLM(Context, Persona_i) $$
    *(Run 7 times in parallel)*

2.  **Converge (Reduce):**
    $$ Score_i = \sum_{j \neq i} Vote(Agent_j, Output_i) $$

3.  **Selection:**
    $$ SurvivorSet = \{ A_i | Score_i > min(Scores) \} $$

---

## 5. System Sequence Diagram (The Burst)

1.  **Initialization:** The `TournamentDirector` loads 7 Agents.
2.  **The Burst (t=0):**
    *   Director sends `Task: "Explain the failure of the Babbage Engine"` to all 7 agents.
    *   **ASYNC WAIT:** 7 Streams generate text.
3.  **The Review (t=1):**
    *   Director anonymizes the paragraphs.
    *   Director sends `Task: "Vote on these 7 paragraphs"` to all agents.
4.  **The Judgment (t=2):**
    *   **The Financier** receives 3 votes (Winner).
    *   **The Cyberneticist** receives 0 votes (Loser).
    *   **Canonization:** The Financier's paragraph is written to the Book.
    *   **Elimination:** The Cyberneticist is unloaded. **The Artist** is loaded from Reserve.
5.  **Next Epoch:** The cycle repeats.