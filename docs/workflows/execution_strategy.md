# Execution Strategy: OpenClaw & The Titan Quorum

**Status:** Architecture v10.0 (Titan Grading Rubric)
**Target Infrastructure:** Prologue of Spacetime / 1.2TB RAM Node
**Architecture Pattern:** Agentic Runtime (MCP Tools + Titan Models)

---

## 1. Technical Architecture & Stack

To ensure "PhD-level" accuracy, we utilize **Titan Rubric Scoring**.
The Titans do not just "vote"; they submit a detailed **Scorecard** via MCP.

### 1.1 The Titan Quorum (The Minds)

| Seat | Model | Parameters | Role |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | 405B | Synthesis |
| **Agent B** | **DeepSeek-V3** | 671B | Retrieval |
| **Agent C** | **Nemotron-4 340B** | 340B | Verification |
| **Agent D** | **Qwen-2.5 72B** | 72B | Nuance |
| **Agent E** | **Mistral 8x22B** | 176B | Creativity |

### 1.2 The Brain Stem (MCP Skill Definitions)

#### Skill 1: `skill_qdrant_search`
*   **Description:** "Retrieves verified facts from the 10k document lake."
*   **Input:** `{"query": "string", "limit": "integer"}`
*   **Output:** `[{"text": "...", "source": "doc_id.md"}]`

#### Skill 2: `skill_submit_candidate`
*   **Description:** "Submits a draft candidate to the Tournament Pool."
*   **Input:** `{"topic": "Gravity", "content": "markdown_string"}`
*   **Output:** `{"candidate_id": "uuid", "status": "awaiting_peer_review"}`

#### Skill 3: `skill_peer_review`
*   **Description:** "Critiques another agent's draft."
*   **Input:** `{"target_candidate_id": "uuid", "feedback": "Your analogy is weak..."}`
*   **Output:** `{"review_id": "uuid", "status": "sent"}`

#### Skill 4: `skill_submit_fusion` (Tie-Breaker)
*   **Description:** "Submits a co-authored draft from two agents."
*   **Input:** `{"collaborator_ids": ["Agent A", "Agent B"], "markdown_content": "..."}`
*   **Output:** `{"fusion_id": "uuid", "status": "pending_ratification"}`

#### Skill 5: `skill_cast_vote` (The Evaluation)
*   **Description:** "Submits a strict 0-10 scorecard on a specific draft."
*   **Input Schema:**
```json
{
  "target_draft_id": "uuid",
  "scorecard": {
    "accuracy": 9, // 1-10: Factual correctness
    "depth": 8,    // 1-10: Complexity of synthesis
    "pedagogy": 10 // 1-10: Teachability
  },
  "rationale": "Chain-of-Thought explanation for the score..."
}
```
*   **Output:** `{"current_average": 8.7, "consensus_met": true}`

---

## 2. Execution Workflows: The Automata

The entire loop is managed by the OpenClaw Event Bus.

### Phase 1: The Trigger
1.  **MQTT Event:** `factory/order` -> "Generate Module: Quantum Gravity".
2.  **OpenClaw:** Instantiates 5 Model Contexts.

### Phase 2: The Action
4.  **Agents A-E:** Call `skill_qdrant_search`.
5.  **OpenClaw:** Returns results.

### Phase 3: The Parallel Sprint (Tournament)
6.  **Agents A-E (Parallel):** Call `skill_submit_candidate`.
7.  **OpenClaw:** Distributes all 5 drafts to all 5 agents.

### Phase 4: The Peer Review & Iteration
8.  **Agents A-E:** Call `skill_peer_review` on 4 peers.
9.  **Agents A-E:** Read feedback, perform targeted research (`skill_qdrant_search`), and submit Final Candidate.

### Phase 5: The Final Vote
10. **Agents A-E:** Vote on the best Final Candidate.
    *   **Winner:** Highest score wins.
    *   **Publish:** The winning draft is written to `curriculum/completed/`.

### Phase 6: The Synthesis Round (Conditional)
*Triggered if Top 2 Scores < 0.5 delta.*
11. **OpenClaw:** Merges context from Draft A and Draft B.
12. **Authors A & B:** Call `skill_submit_fusion` to create a Joint Draft.
13. **Agents C-E:** Vote Up/Down on the Fusion Draft.

---

## 3. Data Schema: The Verified Artifact

Every artifact produced by the Titan Quorum is persisted as an **MCard** — an immutable, content-addressable data container from the `mcard` Python library (`v0.1.46`). MCard provides the cryptographic backbone that makes citations verifiable and tamper-proof.

### 3.1 MCard Python Library: Core Primitives

| Primitive | Description | Prologue Role |
| :--- | :--- | :--- |
| **`MCard`** | Immutable container: `content` → SHA-256 `hash` + `g_time` | Every draft, critique, scorecard, and published chapter is an MCard |
| **`CardCollection`** | CRD-only store (Create, Read, Delete — no UPDATE) | The 10,000-file archive + all generated artifacts |
| **`Handle`** | Stable name → mutable pointer to the *current* MCard hash | `chapter/gravity/latest` always resolves to the winning draft |
| **`handle_history`** | Version log: `(handle, previous_hash, current_hash, changed_at)` | Full audit trail of every chapter revision |

**Key Properties:**
*   **Content-Addressable:** Same content always produces the same hash. The Librarian can cite *exactly* which source it used.
*   **Collision-Safe:** If two different contents produce the same hash, MCard auto-upgrades the hash algorithm.
*   **Temporal Ordering:** `g_time` provides a global timestamp, so the Planner knows *when* each fact was ingested.

```python
from mcard import MCard, CardCollection

# Store a verified chapter as an MCard
collection = CardCollection(db_path="prologue.db")
chapter = MCard("Loop quantum gravity proposes that spacetime is discrete...")
hash_value = collection.add(chapter)

# Retrieve by cryptographic hash (the verifiable citation)
retrieved = collection.get(hash_value)
print(retrieved.get_content(as_text=True))

# Use handles for stable references
collection.add_with_handle(chapter, "chapter/gravity/latest")
current = collection.get_by_handle("chapter/gravity/latest")

# Version history: track how a chapter evolves
history = collection.get_handle_history("chapter/gravity/latest")
```

### 3.2 The Verified Artifact Schema

```json
{
  "module_id": "MOD-101",
  "title": "Quantum Gravity",
  "orchestrator": "OpenClaw v2.1",
  "mcard_hash": "sha256-a1b2c3d4e5f6...",
  "mcard_handle": "chapter/quantum_gravity/latest",
  "consensus_metadata": {
    "average_score": 9.2,
    "scores": {"Llama-405B": 9, "DeepSeek-671B": 10, "Nemotron-340B": 8, "Qwen-72B": 9}
  },
  "content_blocks": [
    {
      "type": "concept_explanation",
      "text": "Loop quantum gravity proposes...",
      "verified_by": ["Llama-405B", "DeepSeek-671B", "Qwen-72B"],
      "source_hashes": ["sha256-f7e8d9c0...", "sha256-b1a2c3d4..."]
    }
  ]
}
```

---

## 4. Development Roadmap

### Phase 1: The "Skill Forge" (Days 1-2)
*   **Goal:** Update `skills/consensus.py` to parse JSON Scorecards.

### Phase 2: The "Bus Driver" (Days 3-4)
*   **Goal:** Configure OpenClaw to reject drafts with score < 8.0.

### Phase 3: The "Titan Link" (Days 5+)
*   **Goal:** End-to-end generation with grading.

### Phase 4: The "Council of Survivors" (Evolution)
*   **Goal:** Implement `skill_synthesize_soul` for collaborative prompt engineering.

---

## 5. The Soul Layer (Prompt Engineering)

The "Soul" of an agent is its System Prompt + Few-Shot Examples. We treat Souls as **Code Artifacts**.

### 5.1 Soul Directory Structure
```text
/souls
  /active
    agent_a_v4.md # Current Llama 3.1 Soul
    agent_b_v2.md
  /graveyard
    agent_a_v1.md # Fired for hallucinations
    agent_a_v2.md # Fired for low creativity
  /templates
    base_synthesis.md
    base_critic.md
```

### 5.2 Skill: `skill_synthesize_soul`
*   **Description:** "Allows the 4 Survivors to collaboratively draft a new System Prompt."
*   **Input:** `{"collaborators": ["Agent A", ...], "goal": "Fix failures of Agent E"}`
*   **Process:**
    1.  OpenClaw opens a shared context (The "Soul Forge").
    2.  Agents discuss defects of the previous agent.
    3.  Survivors vote on the final text of `souls/active/agent_new.md`.
*   **Output:** `{"new_soul_path": "souls/active/agent_e_v2.md", "status": "born"}`