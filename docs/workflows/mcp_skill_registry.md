# MCP Skill Registry: OpenClaw Interface Specification

**Version:** 1.0
**Target Runtime:** OpenClaw v2.1
**Consumer:** Titan Quorum Agents

---

## 1. Overview
This registry defines the **Model Context Protocol (MCP)** tools exposed by OpenClaw. These tools allow the Titan Agents (Llama, DeepSeek, etc.) to interact with the database, the file system, and each other.

### 1.1 The MCard Data Layer

All skills operate on top of the **MCard Python library** (`mcard v0.1.46`), which provides the content-addressable storage backbone. Every document in the 10,000-file archive, every draft, critique, and published chapter is stored as an immutable **MCard** (content → SHA-256 hash + `g_time` timestamp).

| MCard Component | Skill Layer Role |
| :--- | :--- |
| **`CardCollection`** | Persistent store for all documents and artifacts (CRD-only: Create, Read, Delete) |
| **`MCard.hash`** | Cryptographic citation — agents reference sources by their exact content hash |
| **`MCard.g_time`** | Temporal ordering — the Planner knows *when* each fact was ingested |
| **`Handle`** | Stable name → current hash pointer (e.g., `chapter/gravity/latest`) |
| **`handle_history`** | Full version audit trail for every handle update |
| **`mcard.rag.MCardRAGEngine`** | Vector + FTS hybrid search engine powering `skill_qdrant_search` |
| **`mcard.rag.GraphRAGEngine`** | Entity extraction + knowledge graph traversal for multi-hop reasoning |

```python
from mcard import MCard, CardCollection
from mcard.rag import MCardRAGEngine, GraphRAGEngine

# The archive: all 10,000 files as MCards
archive = CardCollection(db_path="prologue.db")

# RAG engine for semantic retrieval (backs skill_qdrant_search)
rag = MCardRAGEngine(archive)
rag.index_all()  # Index all MCards with vector embeddings

# GraphRAG for entity-aware retrieval
graph_rag = GraphRAGEngine(vector_db_path="prologue_vectors.db")
```

---

## 2. Skill Registry

### 2.1 `skill_qdrant_search` (Retrieval)
Allows the agent to query the Memory-Resident Vector Lake using Hybrid Search (Dense + Sparse).

The retrieval layer is backed by the MCard RAG engine (`mcard.rag`), which provides:
*   **Vector Search:** Ollama embeddings (`nomic-embed-text`, 768 dimensions) stored in SQLite with `sqlite-vec` KNN
*   **Full-Text Search (FTS):** BM25 via SQLite FTS5 for keyword matching
*   **Hybrid Search:** Combined vector + FTS with configurable weighting (default: 0.7 vector / 0.3 FTS)
*   **GraphRAG:** Entity extraction and knowledge graph traversal for multi-hop reasoning across documents
*   **Chunking:** Long documents are split into overlapping chunks (default: 1000 chars, 200 overlap) for precise retrieval

Every search result includes the **source MCard hash** — a cryptographic proof of which document the fact came from. This is what makes the Fact-Checker's job possible: citations are verifiable, not hallucinated.

*   **Permission:** Read-Only
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_qdrant_search",
  "description": "Hybrid search (Vector + BM25) over the 10,000 document index.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The semantic search string (e.g., 'history of packet switching')."
      },
      "limit": {
        "type": "integer",
        "description": "Max results to return (Default: 5).",
        "maximum": 20
      },
      "mode": {
        "type": "string",
        "enum": ["hybrid", "dense", "sparse"],
        "description": "Retrieval mode. 'hybrid' uses RRF (Reciprocal Rank Fusion). Default: 'hybrid'"
      },
      "alpha": {
        "type": "number",
        "description": "Weighting for Dense vs Sparse (0.0 = BM25 only, 1.0 = Vector only). Default: 0.5"
      }
    },
    "required": ["query"]
  }
}
```

**MCard RAG Backing (Python):**
```python
from mcard.rag import MCardRAGEngine

rag = MCardRAGEngine(archive)

# Hybrid search: vector similarity + BM25 keyword matching
results = rag.search("history of packet switching", k=5, hybrid=True)
for r in results:
    print(f"Hash: {r.hash}, Score: {r.score:.4f}, Chunk: {r.chunk_text[:80]}")

# Full RAG query: search + LLM generation with cited sources
response = rag.query("Explain the history of packet switching")
print(response.answer)
print(f"Sources: {response.sources}")  # List of MCard hashes
print(f"Confidence: {response.confidence:.2f}")
```

### 2.2 `skill_submit_candidate` (Tournament Entry)
Allows an agent to submit a draft candidate to the Parallel Sprint.

*   **Permission:** Write (Staging)
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_submit_candidate",
  "description": "Submits a draft candidate to the Tournament Pool.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "topic_id": { "type": "string" },
      "markdown_content": { "type": "string" }
    },
    "required": ["topic_id", "markdown_content"]
  }
}
```

### 2.3 `skill_peer_review` (Critique)
Allows an agent to critique a peer's candidate.

*   **Permission:** Read/Write (Critique Ledger)
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_peer_review",
  "description": "Submits structured feedback on a peer's draft.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "target_candidate_id": { "type": "string" },
      "feedback": { "type": "string", "description": "Constructive criticism." }
    },
    "required": ["target_candidate_id", "feedback"]
  }
}
```

### 2.4 `skill_submit_fusion` (Tie-Breaker)
Allows 2 agents to submit a joint draft during a Runoff.

*   **Permission:** Write (Fusion Layer)
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_submit_fusion",
  "description": "Submits a co-authored draft from two agents.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "collaborator_ids": { "type": "array", "items": { "type": "string" } },
      "markdown_content": { "type": "string" }
    },
    "required": ["collaborator_ids", "markdown_content"]
  }
}
```

### 2.5 `skill_cast_vote` (Evaluation)
Allows an agent to grade a peer's Final Candidate.

*   **Permission:** Write (Consensus Ledger)
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_cast_vote",
  "description": "Submit a 0-10 scorecard for a pending draft.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "target_draft_id": { "type": "string" },
      "scores": {
        "type": "object",
        "properties": {
          "accuracy": { "type": "integer", "minimum": 1, "maximum": 10 },
          "depth": { "type": "integer", "minimum": 1, "maximum": 10 },
          "pedagogy": { "type": "integer", "minimum": 1, "maximum": 10 }
        },
        "required": ["accuracy", "depth", "pedagogy"]
      },
      "rationale": { "type": "string" }
    },
    "required": ["target_draft_id", "scores", "rationale"]
  }
}
```

### 2.6 `skill_synthesize_soul` (Evolution)
Allows the Council of Survivors to draft a new System Prompt.

**JSON Schema:**
```json
{
  "name": "skill_synthesize_soul",
  "description": "Collaboratively writes a new agent persona.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "goal": { "type": "string" },
      "system_prompt_content": { "type": "string" }
    },
    "required": ["system_prompt_content"]
  }
}
```

---

## 3. System Protocols

### 3.1 Error Handling
*   **`JSONDecodeError`**: If an agent output is malformed, OpenClaw returns a standardized error prompts: `Error: Invalid JSON. Please retry adhering strictly to the schema.`
*   **`Timeout`**: Tool execution time cap is **30 seconds**.

### 3.2 Security Policy
*   **Write Access**: Only `skill_broadcast_draft` can write content. This writes to a `staging` area.
*   **Publish Access**: NO agent has direct write access to the `completed` curriculum folder. Only the **OpenClaw System Actor** can move files from `staging` to `completed` upon verifying the Consensus State.
