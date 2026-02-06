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
| **Agent D** | **Claude 3.5 Opus** | >500B | Nuance |
| **Agent E** | **GPT-4o** | >1T | Creativity |

### 1.2 The Brain Stem (MCP Skill Definitions)

#### Skill 1: `skill_qdrant_search`
*   **Description:** "Retrieves verified facts from the 10k document lake."
*   **Input:** `{"query": "string", "limit": "integer"}`
*   **Output:** `[{"text": "...", "source": "doc_id.md"}]`

#### Skill 2: `skill_broadcast_draft`
*   **Description:** "Publishes a structural outline or text draft to the Council."
*   **Input:** `{"section_id": "string", "content": "markdown_string"}`
*   **Output:** `{"draft_id": "uuid", "status": "pending_vote"}`

#### Skill 3: `skill_cast_vote` (The Evaluation)
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

### Phase 3: The Consensus
6.  **Agents A-E:** call `skill_broadcast_draft`.
7.  **OpenClaw:** Aggregates drafts. Asks for Judgement.

### Phase 4: The Ratification (Titan Judge)
9.  **Agents A-E:** Call `skill_cast_vote` with Scorecards.
10. **OpenClaw:** Calculates Weighted Average.
    *   **Threshold:** Average > 8.0 AND Min 3 Votes.
    *   If Pass: **PUBLISH**.
    *   If Fail: **RETRY** with feedback from rationale.

---

## 3. Data Schema: The Verified Artifact

```json
{
  "module_id": "MOD-101",
  "title": "Quantum Gravity",
  "orchestrator": "OpenClaw v2.1",
  "consensus_metadata": {
    "average_score": 9.2,
    "scores": {"Llama-405B": 9, "DeepSeek-671B": 10, "Nemotron-340B": 8, "Claude-Opus": 9}
  },
  "content_blocks": [
    {
      "type": "concept_explanation",
      "text": "Loop quantum gravity proposes...",
      "verified_by": ["Llama-405B", "DeepSeek-671B", "Claude-Opus"]
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