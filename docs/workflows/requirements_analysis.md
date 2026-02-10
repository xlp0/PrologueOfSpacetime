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

### Axiom I: The Law of Parallel Competition
*   **Constraint:** For every topic, **ALL 5 AGENTS must generate a unique draft simultaneously.**
*   **The Iteration:** Agents must read each other's drafts, provide **Peer Feedback**, and then perform a second round of research ("The Refinement Loop") before the final vote.
*   **Rationale:** "Survival of the Fittest." We select the best draft from 5 options, rather than polishing one mediocre draft.

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

### 3.1 The Data Backbone (MCard Python Library)
The **MCard Python library** (`mcard v0.1.46`) provides the immutable, content-addressable storage layer that underpins the entire factory. Every file in the 10,000-document archive, every draft, every scorecard, and every published chapter is an **MCard**.

**FR-00 (Content-Addressable Storage):** All data artifacts must be stored as MCards.
*   **MCard:** Immutable container — `content` → SHA-256 `hash` + `g_time` (global timestamp).
*   **CardCollection:** CRD-only persistent store (Create, Read, Delete — no UPDATE). Content is immutable.
*   **Handles:** Stable names (e.g., `chapter/gravity/latest`) that point to the *current* MCard hash. Handles are mutable; content is not.
*   **Handle History:** Full audit trail `(handle, previous_hash, current_hash, changed_at)` for every version change.
*   **MCard RAG Engine:** Semantic vector search + FTS hybrid retrieval over the MCard collection, with Ollama embeddings (`nomic-embed-text`, 768d) and SQLite `sqlite-vec` KNN.
*   **GraphRAG Engine:** Automatic entity extraction and knowledge graph construction from MCard content, enabling multi-hop reasoning across the archive.
*   **Semantic Versioning:** Track how a handle's content evolves over time using embedding-based similarity deltas.

```python
from mcard import MCard, CardCollection
from mcard.rag import MCardRAGEngine, GraphRAGEngine

# Initialize the archive
archive = CardCollection(db_path="prologue.db")

# Ingest a source document
doc = MCard("The speed of light is 299,792,458 m/s.")
archive.add_with_handle(doc, "source/physics/speed_of_light")

# Semantic search over the archive
rag = MCardRAGEngine(archive)
rag.index_all()
results = rag.search("speed of light", k=5, hybrid=True)

# GraphRAG: entity-aware multi-hop retrieval
graph_rag = GraphRAGEngine(vector_db_path="prologue_vectors.db")
response = graph_rag.query("How does the speed of light relate to relativity?")
```

### 3.2 The Agentic Runtime (OpenClaw)
OpenClaw exposes the "Body" of the factory to the "Minds" of the Titans.

**FR-01 (Tool Exposure):** OpenClaw must expose high-level MCP Tools:
*   `skill_qdrant_search(query, mode="hybrid")`  // Hybrid = Vector/BM25 Fusion
*   `skill_submit_candidate(content)`
*   `skill_peer_review(target, feedback)`
*   `skill_submit_fusion(collaborators, content)`
*   `skill_cast_vote(target, verdict)`

**FR-02 (State Management):** OpenClaw maintains the `consensus_state` in PostgreSQL/Redis. It knows *who* has voted and *what* the current tally is.

### 3.3 The Titan Quorum (The High Council)
All agents must be **Open Weights** and capable of local inference.

| Seat | Model | Parameters | Role |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | **405B** | **Synthesis** |
| **Agent B** | **DeepSeek-V3** | **671B** | **Retrieval** |
| **Agent C** | **Nemotron-4 340B** | **340B** | **Verification** |
| **Agent D** | **Qwen-2.5 72B** | **72B** | **Nuance** |
| **Agent E** | **Mistral 8x22B** | **176B** | **Creativity** |

### 3.4 The Output Schema (The Product)
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
## 5. System Sequence Diagram (The OpenClaw Loop)

1.  **Event (t=0):** OpenClaw receives `MQTT: /factory/order {topic: "Gravity"}`.
2.  **Dispatch (t=1):** OpenClaw instantiates 5 Titans.
3.  **Sprint (t=2):**
    *   Titans call `skill_submit_candidate`.
    *   OpenClaw broadcasts drafts to all peers.
4.  **Critique (t=3):**
    *   Titans call `skill_peer_review`.
    *   Titans call `skill_qdrant_search` (Refinement).
5.  **Consensus (t=4):**
    *   Titans call `skill_cast_vote` on Final Candidates.
    *   OpenClaw tallies votes.
6.  **Resolution (t=5):**
    *   **Winner Selected:** Published to `curriculum/completed/`.
    *   **Tie Detected:** Trigger `skill_submit_fusion`.