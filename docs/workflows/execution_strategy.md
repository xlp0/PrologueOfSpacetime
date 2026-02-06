# Execution Strategy: OpenClaw & The Titan Quorum

**Status:** Architecture v9.0 (OpenClaw Orchestration)
**Target Infrastructure:** Prologue of Spacetime / 1.2TB RAM Node
**Architecture Pattern:** Agentic Runtime (MCP Tools + Titan Models)

---

## 1. Technical Architecture & Stack

To ensure "PhD-level" accuracy and "Self-Driving" automation, we integrate **OpenClaw** as the Event Bus and Tool Provider.
The Titans (models) do not run scripts; they satisfy requests from OpenClaw by calling MCP Tools.

### 1.1 The Titan Quorum (The Minds)

| Seat | Model | Parameters | Role |
| :--- | :--- | :--- | :--- |
| **Agent A** | **Llama 3.1 405B** | 405B | Synthesis |
| **Agent B** | **DeepSeek-V3** | 671B | Retrieval |
| **Agent C** | **Nemotron-4 340B** | 340B | Verification |
| **Agent D** | **Claude 3.5 Opus** | >500B | Nuance |
| **Agent E** | **GPT-4o** | >1T | Creativity |

### 1.2 The Brain Stem (OpenClaw Skills)

Instead of vague "actions," the system defines rigorous JSON-Schema Skills (MCP).

#### Skill 1: `skill_qdrant_search`
*   **Description:** "Retrieves verified facts from the 10k document lake."
*   **Input:** `{"query": "string", "limit": "integer"}`
*   **Output:** `[{"text": "...", "source": "doc_id.md"}]`

#### Skill 2: `skill_broadcast_draft`
*   **Description:** "Publishes a structural outline or text draft to the Council."
*   **Input:** `{"section_id": "string", "content": "markdown_string"}`
*   **Output:** `{"draft_id": "uuid", "status": "pending_vote"}`

#### Skill 3: `skill_cast_vote`
*   **Description:** "Submits a pass/fail judgment on a specific draft."
*   **Input:** `{"target_draft_id": "uuid", "verdict": "PASS|FAIL", "rationale": "string"}`
*   **Output:** `{"current_tally": "3/5"}`

---

## 2. Execution Workflows: The Automata

The entire loop is managed by the OpenClaw Event Bus.

### Phase 1: The Trigger
1.  **MQTT Event:** `factory/order` -> "Generate Module: Quantum Gravity".
2.  **OpenClaw:** Instantiates 5 Model Contexts (Agents A-E).
3.  **OpenClaw:** Injects System Prompt: *"You are Agent X. Use `skill_qdrant_search` to find facts about Quantum Gravity."*

### Phase 2: The Action
4.  **Agents A-E:** (Simultaneously) Call `skill_qdrant_search`.
5.  **OpenClaw:** Executes valid queries against Qdrant(RAM). Returns results.

### Phase 3: The Consensus
6.  **OpenClaw:** Updates System Prompt: *"Facts retrieved. Use `skill_broadcast_draft` to propose an outline."*
7.  **Agents A-E:** call `skill_broadcast_draft`.
8.  **OpenClaw:** Aggregates drafts. Asks for Votes.

### Phase 4: The Ratification
9.  **Agents A-E:** Call `skill_cast_vote`.
10. **OpenClaw:** Checks Tally.
    *   If `YES >= 3`: **PUBLISH** to `fs/curriculum/quantum_gravity.md`.
    *   If `YES < 3`: **RETRY** (Loop back to Phase 2 with feedback).

---

## 3. Data Schema: The Verified Artifact

```json
{
  "module_id": "MOD-101",
  "title": "Quantum Gravity",
  "orchestrator": "OpenClaw v2.1",
  "consensus_metadata": {
    "quorum_agreement": 0.80,
    "votes": {"Llama-405B": true, "DeepSeek-671B": true, "Nemotron-340B": false, "Claude-Opus": true, "GPT-4o": true}
  },
  "content_blocks": [
    {
      "type": "concept_explanation",
      "text": "Loop quantum gravity proposes...",
      "verified_by": ["Llama-405B", "DeepSeek-671B", "Claude-Opus", "GPT-4o"]
    }
  ]
}
```

---

## 4. Development Roadmap

### Phase 1: The "Skill Forge" (Days 1-2)
*   **Goal:** Write the 3 OpenClaw Skills in Python/TypeScript (MCP compliant).
*   **Deliverable:** `skills/qdrant.py`, `skills/consensus.py`.

### Phase 2: The "Bus Driver" (Days 3-4)
*   **Goal:** Configure OpenClaw to listen to MQTT and trigger the skills.
*   **Deliverable:** `openclaw_config.yaml`.

### Phase 3: The "Titan Link" (Days 5+)
*   **Goal:** Connect the vLLM/API endpoints to OpenClaw.
*   **Deliverable:** End-to-end generation.