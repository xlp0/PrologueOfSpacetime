# MCP Skill Registry: OpenClaw Interface Specification

**Version:** 1.0
**Target Runtime:** OpenClaw v2.1
**Consumer:** Titan Quorum Agents

---

## 1. Overview
This registry defines the **Model Context Protocol (MCP)** tools exposed by OpenClaw. These tools allow the Titan Agents (Llama, DeepSeek, etc.) to interact with the database, the file system, and each other.

---

## 2. Skill Registry

### 2.1 `skill_qdrant_search` (Retrieval)
Allows the agent to query the Memory-Resident Vector Lake.

*   **Permission:** Read-Only
*   **Authorized Agents:** All (I-V)

**JSON Schema:**
```json
{
  "name": "skill_qdrant_search",
  "description": "Semantic search over the 10,000 document vector index.",
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
      "threshold": {
        "type": "number",
        "description": "Minimum similarity score (0.0 - 1.0). Default: 0.75"
      }
    },
    "required": ["query"]
  }
}
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
