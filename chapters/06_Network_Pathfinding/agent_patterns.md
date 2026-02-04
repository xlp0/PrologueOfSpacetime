# Agent Design Patterns: The 12-Factor Approach

Based on the [HumanLayer Presentation](https://www.youtube.com/watch?v=8kMaTybvDUw), these patterns apply the rigor of "12-Factor Apps" to LLM Agents.

## 1. Tool Use as Code

> *There is no ethereal alien entity interacting with the world; it is just data processing.*

*   **The Myth**: Tools are magical extensions of an AI's will.
*   **The Reality**: "Tool Use" is simply the LLM outputting JSON.
*   **The Pattern**: Treat AI output as data input for deterministic code. Use `switch` statements, not magic.

## 2. Own Your Control Flow (DAGs)

*   **Anti-Pattern**: The Infinite Loop (`while(true) { run_agent() }`).
*   **Pattern**: Directed Acyclic Graphs (DAGs). Hardcode the steps where possible.
    *   If `step 1` succeeds -> go to `step 2`.
    *   If `step 1` fails -> go to `error_handler`.
*   **Benefit**: You can unit test a DAG. You cannot unit test a vibe.

## 3. Stateless Reducers

Agents should be **stateless functions**: $State_{n+1} = f(State_n, Event)$.

*   **Business State**: The data (e.g., "PR Approved").
*   **Execution State**: Where we are in the flow (e.g., "Waiting for User").
*   **Interruptibility**: By externalizing state (e.g., to a Postgres DB), an agent can "sleep" for days while waiting for a human, then resume exactly where it left off.

## 4. Context Hygiene

*   **No Stack Traces**: If a tool crashes, catch the error and feed a *sanitized* summary to the LLM. "The tool failed because file not found" is better than 50 lines of Python trace.
*   **Hand-Crafted Prompts**: Do not let a framework auto-generate your system prompt. You must control every token to guarantee reliability.

## 5. Micro-Agents

*   **Scope**: Limit "Loops" to 3-10 steps max.
*   **Composition**: A reliable application is a deterministic graph of small, encapsulated AI agents, not one Giant Brain.
*   **Deployment Bot Example**:
    1.  Deterministic CI code checks out repo.
    2.  Micro-Agent A analyzes diff.
    3.  Deterministic code posts to Slack.
    4.  Micro-Agent B waits for human reply.

## 6. First-Token Intent

When routing control flow (e.g., "Should I run a tool or ask the user?"), force the LLM to output its decision as the **First Token**.

*   *Prompt*: "Output 'TOOL' to run code or 'ASK' to message the user."
*   *Parsing*: Read token 0. Branch immediately.
