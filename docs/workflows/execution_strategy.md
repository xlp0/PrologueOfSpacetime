# Execution Strategy: "Space Time" Generative Engine

**Status:** Draft v2.0
**Target Infrastructure:** Prologue of Spacetime / Kinetic Node Ecosystem
**Architecture Pattern:** Event-Driven Multi-Agent Systems (ED-MAS)

---

## 1. Technical Architecture & Stack

To support the "Dining Philosophers" topology with evolutionary harvesting, we recommend a hybrid stack that balances strict state enforcement with fluid agentic dialogue.

### 1.1 Core Components

| Component | Technology | Role in "Space Time" Cosmology |
| :--- | :--- | :--- |
| **Orchestrator** | **Microsoft AutoGen** (Extended) | **The Dining Table**. Specifically uses `RoundRobinGroupChat` to strictly enforce the sequential $A \to B \to C \to D \to E$ topology. AutoGen handles the heavy lifting of message broadcasting and speaker selection better than raw LangChain. |
| **State Fabric** | **PostgreSQL + pgvector** | **The Akasjic Record**. Stores structured relational data (Current Agents, Turn Order) alongside unstructured embeddings (Debate Vector History, MVP Documents). |
| **Observability** | **Streamlit** | **The Epistemic Deck**. A lightweight, reactive dashboard that visualizes the "Entropy" of the conversation in real-time, allowing human observers to "watch the table turn." |
| **Harvester** | **Python Asyncio Daemon** | **The Semantic Harvester**. A background service that "fishes" for consensus intervals and commits them to the permanent "Book" structure. |

### 1.2 System Architecture Diagram

```mermaid
graph TD
    subgraph "The Closed Room (Simulation)"
        Orchestrator[AutoGen Orchestrator] -->|Token Passing| P1[Physicist]
        P1 -->|Token Passing| P2[Financier]
        P2 -->|Token Passing| P3[Politician]
        P3 -->|Token Passing| P4[Mathematician]
        P4 -->|Token Passing| P5[Technologist]
        P5 -->|Token Passing| P1
    end

    subgraph "State Fabric (Postgres)"
        EventLog[(Event Log Table)]
        VectorStore[(Vector Embeddings)]
        AgentConfig[(Agent Config Table)]
    end

    subgraph "The Harvester"
        Daemon[Semantic Harvester Daemon] -->|Polling| EventLog
        Daemon -->|Analysis (CI Score)| VectorStore
        Daemon -->|Extract| BookChapter[JSON Chapter Artifact]
    end

    Orchestrator -->|Commit Turn| EventLog
    Daemon -->|Update| AgentConfig
```

---

## 2. Data Schema Specification

The "Space Time" system requires a rigorous schema to track not just *what* was said, but the *meta-data* of the conversation (entropy, consensus, friction).

### 2.1 The Event Log (`debate_turns`)
This is the raw stream of consciousness from the Table.
```sql
CREATE TABLE debate_turns (
    turn_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES debate_sessions(id),
    round_number INT NOT NULL,
    agent_persona VARCHAR(50) NOT NULL, -- e.g., 'Physicist_v1'
    content TEXT NOT NULL,
    
    -- Meta-Analysis Fields
    token_count INT,
    sentiment_score FLOAT, -- -1.0 (Hostile) to 1.0 (Friendly)
    complexity_index FLOAT, -- Abel-Ruffini Score
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 2.2 Consensus Artifacts (`book_chapters`)
The output of the Harvester.
```sql
CREATE TABLE book_chapters (
    chapter_id UUID PRIMARY KEY,
    title VARCHAR(255),
    
    -- The JSON payload ready for PDF generation
    content_json JSONB, 
    
    -- Provenance
    source_turn_range INT8RANGE, -- e.g., [150, 200]
    participating_agents TEXT[],
    consensus_strength FLOAT
);
```

---

## 3. Risk Mitigation & Resilience Protocols

Operating a 5-agent infinite loop carries specific algorithmic risks. We apply **"Pre-Mortem Engineering"** to prevent these states.

### 3.1 The "Politeness Loop" (Infinite Agreement)
*   **Symptom:** Agents devolve into "I agree with [Previous Agent], that is a profound insight."
*   **Protection:** **Semantic Entropy Guard**.
*   **Implementation:** The Orchestrator calculates the cosine similarity between the current turn and the previous turn. If `similarity > 0.85`, the turn is **rejected**, and the agent is prompted with: *"You are echoing the previous speaker. Introduce a Counter-Factual or a Constraint."*

### 3.2 The "Consensus Trap" (Expertise Dilution)
*   **Symptom:** The Politician overrules the Physicist on a matter of quantum tunneling.
*   **Protection:** **Epistemic Weighting**.
*   **Implementation:**
    1.  Classify current topic (e.g., `Topic: Semiconductor Physics`).
    2.  Lookup Agent Weight for Topic (Physicist: 0.9, Politician: 0.2).
    3.  If a low-weight agent attempts to contradict a high-weight agent without a citation, the system injects a `[CITATION NEEDED]` system message.

### 3.3 The "Deadlock" (Resource Contention)
*   **Symptom:** Dining Philosophers problem where the system hangs waiting for an API response.
*   **Protection:** **Async Timeouts & Token Revocation**.
*   **Implementation:** The `RoundRobinManager` has a `turn_timeout=45s`. If an agent fails to generate, the Manager:
    1.  Logs a `TURN_FAILURE` event.
    2.  Passes the token to the next agent with the context: *"The previous speaker remained silent. Please continue."*

---

## 4. Development Roadmap

### Phase 1: The Zero-Topology (Days 1-2)
*   **Goal:** 5 Agents passing a token in strict order.
*   **Deliverable:** Python script running `autogen.GroupChat` with `allow_repeat_speaker=False` and `speaker_selection_method="round_robin"`.

### Phase 2: The Memory Substrate (Days 3-4)
*   **Goal:** Postgres persistence.
*   **Deliverable:** Dockerized Postgres + pgvector. AutoGen hooks customized to write every message to the DB before broadcasting.

### Phase 3: The Harvester (Days 5-7)
*   **Goal:** Extraction of coherent thoughts.
*   **Deliverable:** Background daemon scanning the DB. Implementation of the "Consensus Detection" algorithm (detecting sequences of `Thesis -> Antithesis -> Synthesis`).

### Phase 4: Viz & Polish (Day 8+)
*   **Goal:** The "Space Time" Experience.
*   **Deliverable:** Streamlit app connecting to the DB, showing live scrolling text and "Entropy Charts."