# The Consensus Constitution: Laws of the Titan Quorum

**Version:** 1.0
**Authority:** System Architect
**Enforcement:** OpenClaw Agentic Runtime

---

## 1. Preamble
This document defines the mathematical and logical frameworks governing the **Titan Quorum** (the 5-Agent Consensus Engine). It serves as the "Operating System" for decision-making, ensuring that the curriculum generated is factually accurate, pedagogically sound, and hallucination-free.

---

## 2. The Quorum Members
The Quorum consists of 5 distinct high-parameter **Open Weights** models.

| Seat | Role | Model | Bias |
| :--- | :--- | :--- | :--- |
| **I** | **Chair** | Llama 3.1 405B | Structural Integrity |
| **II** | **Miner** | DeepSeek-V3 671B | Technical Precision |
| **III** | **Auditor** | Nemotron-4 340B | Compliance/Safety |
| **IV** | **Professor** | Qwen-2.5 72B | Empathy/Nuance |
| **V** | **Vizier** | Mistral 8x22B | Creativity/Lateral Thinking |

---

## 3. The Law of Quintic Consensus

### 3.1 The Standard Vote
For binary decisions (Pass/Fail), a proposal triggers a vote.
$$ V_{result} = \sum_{i=1}^{5} v_i $$
*   Where $v_i \in \{0, 1\}$ (Fail/Pass).
*   **Threshold:** A motion passes iff $V_{result} \ge 3$.

### 3.2 The Weighted Tie-Breaker (Nuclear Option)
In the event of a persistent deadlock (e.g., 2 Pass / 2 Fail / 1 Abstain) for >3 cycles:
The **Chair (Llama 405B)** is granted a weighted vote ($w=1.5$) to force resolution.

---

## 4. The Titan Grading Rubric (0-10)

Evaluation is not binary. It is scalar.

### 4.1 Dimension A: Accuracy (The "Truth" Score)
*   **10**: Every claim is cited. Citations match 100% of source text. No hallucinations.
*   **8**: Minor citation formatting errors. All facts correct.
*   **5**: One hallucinated fact or misattributed quote. **(Rejection Threshold)**
*   **1**: Total fabrication.

### 4.2 Dimension B: Depth (The "PhD" Score)
*   **10**: Synthesis of >3 sources. Identification of second-order effects. Novel insight.
*   **8**: Solid summary of sources. Good structure.
*   **5**: Superficial "Wikipedia-style" overview. **(Rejection Threshold)**
*   **1**: Incoherent rambling.

### 4.3 Dimension C: Pedagogy (The "Teacher" Score)
*   **10**: Clear analogy. Socratic questioning. Appropriate tone. "Aha!" moment likely.
*   **8**: Clear explanation. Standard tone.
*   **5**: Dense jargon. Passive voice using "delve". **(Rejection Threshold)**
*   **1**: Unreadable.

### 4.4 The Publication Condition
A draft $D$ is published ONLY IF:
$$ \overline{Score}(D) = \frac{1}{N} \sum_{i=1}^{N} Score_i \ge 8.0 $$
AND
$$ \min(Score_i) \ge 5.0 $$

---

## 5. Algorithmic Implementation (Pseudocode)

```python
def check_consensus(scorecards: List[dict]) -> bool:
    """
    Determines if the Quorum has reached a publication standard.
    """
    total_score = 0
    valid_votes = 0
    
    for card in scorecards:
        # Check for immediate veto
        if card['accuracy'] < 5 or card['depth'] < 5:
            return False # VETO
            
        avg_vote = (card['accuracy'] + card['depth'] + card['pedagogy']) / 3
        total_score += avg_vote
        valid_votes += 1
        
    global_average = total_score / valid_votes
    
    return global_average >= 8.0

---

## 6. The Council of Survivors (Autonomous Evolution)

To prevent stagnation, the Quorum undergoes a **Darwinian Review** every $N=100$ cycles.

### 6.1 The Self-Check (Introspection)
At the end of Cycle 100, OpenClaw presents the **Performance Matrix** to all authenticated agents.
*   "Agent A: 9.2"
*   "Agent B: 8.5"
*   ...
*   "Agent E: 6.1"

### 6.2 The Vote of Execution
The 5 Agents must vote on who to remove.
*   **Prompt:** *"Based strictly on the data, which member is the weakest link? Vote to terminate."*
*   **Consensus:** A **4/5 Majority** is required to execute a member.
*   **Action:** The target's `soul.md` is moved to `souls/graveyard/` and the process is killed.

### 6.3 The Rite of Reincarnation (Collaborative Soul Synthesis)
The 4 Survivors are tasked with creating their new colleague.
1.  **Drafting:** The Survivors discuss specifically *why* the previous agent failed.
2.  **Synthesis:** They collaboratively write a new System Prompt (`souls/active/agent_new.md`).
    *   *Instruction:* "You must draft a persona that covers the blind spots of the previous agent."
3.  **Birth:** The new agent is instantiated with this survivor-authored soul.
4.  **Probation:** The Novice has no voting power for the first 10 cycles.
```
