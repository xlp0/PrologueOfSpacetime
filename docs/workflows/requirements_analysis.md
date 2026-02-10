# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 10.0 (Titan Grading Rubric)
**Architect:** System Architect / Educational Theorist
**Domain:** Automated Curriculum Design / Knowledge Synthesis

---

## 1. System Overview & The "Automata" Metaphor

The system operates as a **"Self-Driving Factory"**.
While the *Titan Quorum* provides the intelligence, **OpenClaw (The Brain Stem)** provides the nervous system. It orchestrates the flow of data, ensuring that the 5 massive models act in perfect synchronization without human "copy-pasting."

---

## 2. Axiomatic Constraints (Immutable Laws)

### Axiom I: The Law of Quintic Consensus
$$ Truth(F) \iff \sum_{i=1}^{5} Verify(Agent_i, F) \ge 3 $$

### Axiom II: The Law of Titan Capability
*   **Constraint:** **NO PRIMARY AGENT MAY HAVE FEWER THAN 300 BILLION PARAMETERS.**

### Axiom III: The Law of Cognitive Diversity
*   **Constraint:** The Quorum must mix architectures (Dense, MoE) and providers.

### Axiom IV: The Law of Automata
*   **Constraint:** The system must run **Headless** via OpenClaw.

### Axiom V: The Law of Evaluation
*   **Constraint:** No draft is published unless it achieves a **Titan Score > 8.0/10** from at least 3 peers.
*   **Rationale:** "Consensus" is too binary. We need "Excellence." High agreement on mediocrity is unacceptable.
*   **The Rubric:**
    1.  **Accuracy:** Factual verification against the Vector Lake.
    2.  **Depth:** Synthesis complexity (PhD-level vs. Wiki-summary).
    3.  **Pedagogy:** Teachability and clarity.

### Axiom VI: The Law of Evolution (Autonomous Peer Review)
*   **Constraint:** The Quorum manages its own membership. Every $N$ cycles, the agents **review their own performance scores**.
*   **The Execution:** The 4 top-performing agents vote to **Terminate** the lowest performer.
*   **The Reincarnation:** The "Council of Survivors" collaboratively drafts the **New Soul** (System Prompt) for the replacement agent, instructing it to avoid the failures of the deceased.
*   **Rationale:** True sovereignty requires the ability to self-correct and self-optimize without external intervention.

### Axiom VII: The Law of Sovereignty (Self-Hosting)
*   **Constraint:** **NO PROPRIETARY API MODELS.** All agents must be capable of running on local hardware (or self-hosted clouds).
*   **rationale:** If we cannot host it, we do not own the intelligence. We are building a "Brain Factory," not renting one.

---

## 3. Functional Requirements (FR)

### 3.1 The Agentic Runtime (OpenClaw)
OpenClaw exposes the "Body" of the factory to the "Minds" of the Titans.

**FR-01 (Tool Exposure):** OpenClaw must expose high-level MCP Tools:
*   `read_vector_lake(query)`
*   `propose_draft(content)`
*   `commit_vote(target_id, verdict)`

**FR-02 (State Management):** OpenClaw maintains the `consensus_state` in PostgreSQL/Redis. It knows *who* has voted and *what* the current tally is.

### 3.2 The Titan Quorum (The High Council)
All agents must be **Open Weights** and capable of local inference.

| Seat | Model | Parameters | Role |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | **405B** | **Synthesis** |
| **Agent B** | **DeepSeek-V3** | **671B** | **Retrieval** |
| **Agent C** | **Nemotron-4 340B** | **340B** | **Verification** |
| **Agent D** | **Qwen-2.5 72B** | **72B** | **Nuance** |
| **Agent E** | **Mistral 8x22B** | **176B** | **Creativity** |

### 3.3 The Output Schema (The Product)
**FR-04:** The final Artifact is a **Machine-Verified JSON** signed by the OpenClaw cryptographic key (attesting to the vote tally).

---

## 4. Mathematical Logic: The Automata Limit

```python
def orchestrate_cycle(max_retries=3):
    retries = 0
    while not check_quorum(current_votes):
        if retries > max_retries:
            OpenClaw.alert_human("DEADLOCK: Quorum cannot agree on 'Packet Switching'")
            return FAILURE
        
        # OpenClaw triggers debate
        OpenClaw.broadcast_feedback(reasons_for_rejection)
        retries += 1
    
    return SUCCESS
```

---

## 5. System Sequence Diagram (The OpenClaw Loop)

1.  **Event (t=0):** OpenClaw receives `MQTT: /factory/order {topic: "Gravity"}`.
2.  **Dispatch (t=1):** OpenClaw calls the 5 Titans via API.
3.  **Action (t=2):**
    *   Titans call `skill_qdrant_search`.
    *   OpenClaw executes search and returns JSON.
4.  **Consensus (t=3):**
    *   Titans call `skill_cast_vote`.
    *   OpenClaw tallies votes.
5.  **Publish (t=4):**
    *   If Pass: OpenClaw writes to `curriculum/completed/gravity.md`.