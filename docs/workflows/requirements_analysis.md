# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 7.0 (The Quorum of Five)
**Architect:** System Architect / Educational Theorist
**Domain:** Automated Curriculum Design / Knowledge Synthesis

---

## 1. System Overview & The "Quorum" Metaphor

The system implements a **"Quorum of Truth"** protocol.
To ensure robustness and avoid "model monoculture" bias, every phase of generation is performed **simultaneously by 5 distinct SOTA models**.
They must achieve a super-majority (3/5) consensus before any artifact moves to the next stage.

---

## 2. Axiomatic Constraints (Immutable Laws)

### Axiom I: The Law of Quintic Consensus
$$ Truth(F) \iff \sum_{i=1}^{5} Verify(Agent_i, F) \ge 3 $$
*   **Constraint:** No fact is accepted unless verified by at least **3 independent agents** utilizing distinct model architectures.
*   **Rationale:** Preventing "echo chambers" where similar models hallucinate the same error.

### Axiom II: The Law of Cognitive Diversity
*   **Constraint:** The Quorum MUST consist of models with fundamentally different training distributions or architectures (e.g., MoE vs. Dense, Different Labs).

### Axiom III: The Law of Model Capability
*   **Constraint:** All agents must run on High-Parameter/High-Reasoning models.

---

## 3. Functional Requirements (FR)

### 3.1 The Quorum Roles (The Council)
All agents perform all tasks, but bring different "cognitive biases" to the table.

| Seat | Model | Parameter Count | Cognitive Bias |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | 405B | **Synthesis**. Grand unifying theory and structure. |
| **Agent B** | **DeepSeek-V3** | 671B (MoE) | **Retrieval**. Technical precision and code. |
| **Agent C** | **Qwen 2.5 72B** | 72B | **Logic**. Mathematical rigor and exactness. |
| **Agent D** | **Mixtral 8x22B** | 141B (MoE) | **Context**. Long-range dependency tracking. |
| **Agent E** | **Command R+** | 104B | **Citation**. RAG-optimized verification. |

### 3.2 Joint Execution Workflow
**FR-01 (Quorum Extraction):** All 5 agents query the vector database. The system computes the intersection of 5 sets of facts. Only facts found by $\ge 3$ agents are kept.
**FR-02 (Quorum Drafting):** All 5 agents draft the lesson text. The system selects the "Centroid" draft (closest to the average embedding of all 5).
**FR-03 (Quorum Review):** All 5 agents vote PASS/FAIL. Consensus threshold is 3/5.

### 3.3 The Output Schema (The Product)
**FR-04:** The final Verified Curriculum Artifact contains:
1.  **Module Title**
2.  **Consensus Metadata** (Vote tallies per section)
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
    *   Agents A-E run RAG queries.
    *   **Intersection:** System keeps facts found by {A,B,C}, {A,D,E}, etc.
3.  **Phase B: Structuring (5-Way):**
    *   Agents A-E propose outlines.
    *   **Vote:** Agents rank the 5 outlines. Winner is selected.
4.  **Phase C: Writing (5-Way):**
    *   Agents A-E write the content.
    *   **Synthesis:** Best sections are merged.
5.  **Phase D: Final Vote:**
    *   Agents cast `YES/NO` on final JSON.
    *   If 3/5 YES -> **Visualize**.