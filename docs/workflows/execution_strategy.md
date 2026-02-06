# Execution Strategy: "The Committee of Truth" (Consensus)

**Status:** Architecture v6.0 (Multi-Agent Consensus)
**Target Infrastructure:** Prologue of Spacetime / 1.2TB RAM Node
**Architecture Pattern:** Synchronous Consensus RAG (Triangulated Generation)

---

## 1. Technical Architecture & Stack

To ensure "PhD-level" accuracy from 10,000 documents, we replace the "handoff" model with a **"Unified Committee"** model.
Every operation is performed by the **Trinity** (Pedagogue, Technologist, Critic) simultaneously. The system acts as the **Chairman**, aggregating their outputs and demanding consensus.

### 1.1 The Committee (Shared Responsibility)

| Role | Core Model | Function in Consensus |
| :--- | :--- | :--- |
| **Role A** | **Llama 3.1 405B** | **Primary Synthesizer**. Adds structural depth and reasoning. |
| **Role B** | **DeepSeek-V3** | **Primary Retrieval**. Adds technical precision and "needle" finding. |
| **Role C** | **Claude 3.5 / GPT-4o** | **Primary Auditor**. Checks for logical fallacies and readability. |

*Crucially: ALL roles participate in ALL steps.*

### 1.2 System Architecture Diagram (The Conference Table)

```mermaid
graph TD
    subgraph "Step 1: Triangulated Extraction"
        Query[User Request] -->|Broadcast| Agents[Trinity: Llama + DeepSeek + GPT4]
        Agents -->|Parallel Search| QdrantRAM[(50GB Vector Lake)]
        QdrantRAM -->|Results A, B, C| ConvergenceEngine[Fact Intersector]
        ConvergenceEngine -->|Verified Facts| FactSheet[Consensus Fact Sheet]
    end

    subgraph "Step 2: Competitive Drafting"
        FactSheet -->|Prompt| Agents
        Agents -->|Draft A, Draft B, Draft C| RankingEngine[Blind Peer Review]
        RankingEngine -->|Select Best| Draft[Alpha Draft]
    end

    subgraph "Step 3: Unanimous Ratification"
        Draft -->|Review| Agents
        Agents -->|Vote| Decision{Is Consensus > 2/3?}
        Decision -- No -->|Feedback Loop| RankingEngine
        Decision -- Yes -->|Publish| JSON[Final Curriculum]
    end
```

---

## 2. Execution Workflows

### 2.1 The "Committee Meeting" Protocol
This loop runs for every single module generation.

#### Phase 1: The Fact Hunt (Extraction)
1.  **Chairman:** "Topic is 'Packet Switching'. Agents, search the library."
2.  **Trinity:** Each runs their own optimized RAG queries (approx 50 queries total).
3.  **Chairman:** Aggregates results.
    *   *Fact X found by 3/3 Agents* $\to$ **ACCEPTED**.
    *   *Fact Y found by 1/3 Agents* $\to$ **REJECTED** (Potential Hallucination).

#### Phase 2: The Outline Debate (Structuring)
1.  **Chairman:** "Propose a lesson outline based on ACCEPTED facts."
2.  **Trinity:** Generates 3 outlines.
3.  **Chairman:** Asks Trinity to vote on the best one (Blind Vote).
    *   *Result:* Llama 405B's outline wins. It becomes the **Governing Structure**.

#### Phase 3: The Write-a-thon (Drafting)
1.  **Chairman:** "Write Section 1 using Governing Structure and Accepted Facts."
2.  **Trinity:** Generates 3 versions of the text.
    *   *Technologist:* Too technical.
    *   *Pedagogue:* Good balance.
    *   *Critic:* Too simple.
3.  **Chairman:** Selects the "Pedagogue" version but injects "Technologist" citations where missing.

#### Phase 4: The Ratification (Review)
1.  **Chairman:** "Review the final JSON. Vote PASS/FAIL."
2.  **Trinity:**
    *   *Technologist:* PASS.
    *   *Pedagogue:* PASS.
    *   *Critic:* FAIL (Citations malformed).
3.  **Loop:** Chairman requests a fix for citations. Repeat Vote.
4.  **Success:** Unanimous PASS.

---

## 3. Data Schema: The Verified Artifact

The output includes metadata about the consensus process.

```json
{
  "module_id": "MOD-101",
  "title": "Origins of Network Theory",
  "consensus_metadata": {
    "participating_models": ["Llama-3.1-405B", "DeepSeek-V3", "GPT-4o"],
    "fact_agreement_rate": 0.92,
    "iterations_to_pass": 2
  },
  "content_blocks": [
    {
      "type": "concept_explanation",
      "text": "Packet switching decomposed messages...",
      "verified_by": ["Role A", "Role B", "Role C"]
    }
  ]
}
```

---

## 4. Development Roadmap

### Phase 1: The "Intersector" (Days 1-2)
*   **Goal:** Build the logic to find commonality between 3 JSON lists of facts.
*   **Deliverable:** Python script `intersect_facts(list_a, list_b, list_c) -> list_verified`.

### Phase 2: The "Voting Booth" (Days 3-4)
*   **Goal:** Allow agents to read text and output a score (0-10) reliably.
*   **Deliverable:** Scoring prompt engineering for Llama 405B.

### Phase 3: The Chairman (Days 5+)
*   **Goal:** Automate the full loop.
*   **Deliverable:** Main execution loop handling the State Machine of the meeting.