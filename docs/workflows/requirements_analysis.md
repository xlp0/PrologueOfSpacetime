# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 6.0 (Committee of Truth Consensus)
**Architect:** System Architect / Educational Theorist
**Domain:** Automated Curriculum Design / Knowledge Synthesis

---

## 1. System Overview & The "Committee" Metaphor

The system rejects the "Assembly Line" where work is handed off. Instead, we implement a **"Committee of Truth"**.
Every distinct phase of generation (Extraction, Structuring, Writing, Reviewing) is performed **simultaneously by all 3 agents**. They must achieve consensus before the artifact moves to the next stage.

**Why?** To eliminate hallucinations. If the *Technologist* hallucinates a fact, the *Pedagogue* and *Critic* will catch it during the consensus check.

---

## 2. Axiomatic Constraints (Immutable Laws)

### Axiom I: The Law of Triangulation
$$ Truth(F) \iff \exists \{A_1, A_2\} \in Agents : Verify(A_1, F) \land Verify(A_2, F) $$
*   **Constraint:** No fact ($F$) is accepted into the curriculum unless at least **two independent agents** verify its existence in the source text.
*   **Rationale:** Single-agent hallucinations are common. Multi-agent hallucinations are statistically rare.

### Axiom II: The Law of Pedagogical Clarity
$$ Clarity(Lesson) > Threshold_{comprehension} $$
*   **Constraint:** All output MUST be formatted as structured learning materials. Complex topics must be approved by the **Critic** as "Teachable".

### Axiom III: The Law of Model Capability
*   **Constraint:** The Committee MUST utilize **High-Parameter Models** (Llama 3.1 405B, DeepSeek-V3) for all consensus steps.
*   **Constraint:** Agents must share the 1.2TB RAM context to validate each other's work without re-ingesting data.

---

## 3. Functional Requirements (FR)

### 3.1 The Committee Roles (The Peers)
Roles utilize specific models but share the workload.

| Role | Responsibility | Target Model |
| :--- | :--- | :--- |
| **The Technologist** | **Proposal Generator**. Suggests facts, structures, and quiz questions. | **DeepSeek-V3** |
| **The Pedagogue** | **Proposal Generator**. Suggests facts, structures, and quiz questions. | **Llama 3.1 405B** |
| **The Critic** | **Proposal Generator**. Suggests facts, structures, and quiz questions. | **Claude 3.5 / GPT-4o** |

*> Note: All agents perform ALL tasks. The 'Role' mainly defines their personality/prompt bias during the debate.*

### 3.2 Joint Execution Workflow
**FR-01 (Joint Extraction):** All 3 agents query the vector database independently. The system computes the **Intersection Set** of their findings.
**FR-02 (Joint Drafting):** All 3 agents draft the lesson text. The system selects the version with the highest **Comprehension Score** (or merges them).
**FR-03 (Joint Review):** All 3 agents review the final artifact. It is only released if `Unanimous_Vote == True`.

### 3.3 The Output Schema (The Product)
**FR-04:** The final output is NOT a chat log. It is a **Verified Curriculum Artifact** (JSON/Markdown) containing:
1.  **Module Title**
2.  **Learning Objectives** (Consensus-Approved)
3.  **Core Content** (Triangulated Facts)
4.  **Verification Exercises** (Peer-Reviewed Quizzes)

---

## 4. Mathematical Logic: The Consensus Threshold

```python
def check_consensus(proposals):
    # Cluster proposals by semantic similarity
    clusters = cluster_vectors(proposals)
    
    # Identify the 'Majority View'
    dominant_cluster = max(clusters, key=len)
    
    # If majority < 66% (2/3 agents), Trigger Debate Loop
    if len(dominant_cluster) < 2:
        return trigger_debate(proposals)
    
    return synthesis(dominant_cluster)
```

---

## 5. System Sequence Diagram (The Committee Meeting)

1.  **Ingest (t=0):**
    *   Load 10k docs to RAM.
2.  **Phase A: Fact Finding (Parallel):**
    *   **Technologist:** Finds 50 facts.
    *   **Pedagogue:** Finds 45 facts.
    *   **Critic:** Finds 48 facts.
    *   **System:** Merges to keep the 42 facts found by everyone.
3.  **Phase B: Structuring (Parallel):**
    *   All 3 agents propose an outline.
    *   **Vote:** Agents vote on the best outline. (Winner: Pedagogue's Outline).
4.  **Phase C: Writing (Parallel):**
    *   All 3 agents write the content for "Section 1" using the verified facts.
    *   **Synthesis:** The best paragraph from each is combined.
5.  **Phase D: Final Sign-off:**
    *   Agents cast a simple `YES/NO` vote on the final JSON.
    *   If 3/3 YES -> **Visualize**.