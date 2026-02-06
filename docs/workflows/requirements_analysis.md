# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 8.0 (Titan Class Quorum)
**Architect:** System Architect / Educational Theorist
**Domain:** Automated Curriculum Design / Knowledge Synthesis

---

## 1. System Overview & The "Titan" Metaphor

The system implements a **"Titan Quorum"**.
We reject the use of "toy" models (<100B parameters) for primary automated reasoning. Every phase of the curriculum generation is performed simultaneously by **5 Titan-Class Models (>300B Parameters)**.

This ensures that the "Teacher" agents possess the nuance, depth, and world-knowledge of a PhD-level instructor, rather than an undergraduate TA.

---

## 2. Axiomatic Constraints (Immutable Laws)

### Axiom I: The Law of Quintic Consensus
$$ Truth(F) \iff \sum_{i=1}^{5} Verify(Agent_i, F) \ge 3 $$
*   **Constraint:** No fact is accepted unless verified by at least **3 independent agents**.

### Axiom II: The Law of Titan Capability
*   **Constraint:** **NO PRIMARY AGENT MAY HAVE FEWER THAN 300 BILLION PARAMETERS.**
*   **Rationale:** Curriculum design requires deep synthesis. Smaller models optimize for speed/cost, which is irrelevant on our 1.2TB infrastructure. We prioritize **Maximum Reasoning Depth**.

### Axiom III: The Law of Cognitive Diversity
*   **Constraint:** The Quorum must mix architectures (Dense, MoE) and providers (Open Weights vs. API) to prevent "mode collapse."

---

## 3. Functional Requirements (FR)

### 3.1 The Titan Quorum (The High Council)
All agents perform all tasks, leveraging their specific massive-scale advantages.

| Seat | Model | Parameter Count | Strategy |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | **405 Billion** | **Synthesis**. The logic engine. Best at structuring complex arguments. |
| **Agent B** | **DeepSeek-V3** | **671 Billion** | **Technical**. Mixture-of-Experts giant. Best at retrieval/code. |
| **Agent C** | **Nemotron-4 340B** | **340 Billion** | **Reasoning**. NVIDIA's massive aligned model for strict verification. |
| **Agent D** | **Claude 3.5 Opus** | **>500B (Est)** | **Nuance**. Via API. Best at tone and pedagogical empathy. |
| **Agent E** | **GPT-4o** | **>1T (Est)** | **Creativity**. Via API. Best at lateral thinking and analogies. |

### 3.2 Joint Execution Workflow
**FR-01 (Titan Extraction):** All 5 Titans query the vector database.
**FR-02 (Titan Drafting):** All 5 Titans draft content.
**FR-03 (Titan Review):** All 5 Titans vote.
    *   *Note:* Running 5 Titans typically requires massive GPU clusters. We utilize the **1.2TB RAM Node** for the open models (via CPU/RAM offloading if needed) and parallel API calls for the closed models.

### 3.3 The Output Schema (The Product)
**FR-04:** The final Verified Curriculum Artifact contains:
1.  **Module Title**
2.  **Consensus Metadata** (Votes from Llama, DeepSeek, etc.)
3.  **Core Content** (Triangulated Facts)
4.  **Verification Exercises** (Peer-Reviewed Quizzes)

---

## 4. Mathematical Logic: The Super-Majority

```python
def check_quorum(votes):
    # votes = [True, True, False, True, False]
    yeas = sum(votes)
    return yeas >= 3
```

---

## 5. System Sequence Diagram (The Council Meeting)

1.  **Ingest (t=0):**
    *   Load 10k docs to RAM.
2.  **Phase A: Fact Hunt (5-Way):**
    *   Titans A-E run RAG queries.
    *   **Intersection:** System keeps facts found by {A,B,C}, {A,D,E}, etc.
3.  **Phase B: Structuring (5-Way):**
    *   Titans A-E propose outlines.
    *   **Vote:** Agents rank the 5 outlines. Winner is selected.
4.  **Phase C: Writing (5-Way):**
    *   Titans A-E write the content.
    *   **Synthesis:** Best sections are merged.
5.  **Phase D: Final Vote:**
    *   Agents cast `YES/NO` on final JSON.
    *   If 3/5 YES -> **Visualize**.