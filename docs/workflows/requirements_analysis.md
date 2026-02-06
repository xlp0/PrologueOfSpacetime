# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 9.0 (OpenClaw Orchestration)
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
*   **Constraint:** The system must run **Headless**.
*   **Rationale:** Managing 5 Titans manually is impossible. **OpenClaw** acts as the runtime, triggering the standard MCP tools (`search`, `draft`, `vote`) automatically based on the consensus state machine.
*   **Threshold:** Human intervention is ONLY permitted if Consensus drops below 3/5 for >3 consecutive cycles (Deadlock).

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
All agents perform all tasks via the OpenClaw Tools.

| Seat | Model | Parameters | Role |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | **405B** | **Synthesis** |
| **Agent B** | **DeepSeek-V3** | **671B** | **Retrieval** |
| **Agent C** | **Nemotron-4 340B** | **340B** | **Verification** |
| **Agent D** | **Claude 3.5 Opus** | **>500B** | **Nuance** |
| **Agent E** | **GPT-4o** | **>1T** | **Creativity** |

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