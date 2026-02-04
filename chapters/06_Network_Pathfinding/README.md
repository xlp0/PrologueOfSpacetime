# Chapter 6: Network Pathfinding (The 12-Factor Agent)
**Phase**: Logic (Process/Reliability)
**Subject**: Geometry (Structure/Graphs)

> *"Agents are just software."* — Dex Horthy

> This chapter serves as the "Logic" phase of the Geometry column. It deals with the structure of execution, specifically navigating the state space of an agentic workflow reliably.

## 📂 Chapter Contents

| Document | Description |
| :--- | :--- |
| **[README.md](README.md)** | This file. Overview of 12-Factor Agents and Network Pathfinding. |
| **[Agent Design Patterns](agent_patterns.md)** | Technical deep-dive into DAGs, Stateless Reducers, and Context Hygiene. |
| **[VPN & Mesh Networking](vpn_mesh_network.md)** | **Project Phase 3**: Connecting the Kinetic Node to the swarm via Tailscale/NetBird. |

## The Problem of the Loop


## The Problem of the Loop

The naive approach to finding a path through a problem space is an infinite loop: `Prompt -> Tool -> Context -> Repeat`. This is fragile. As the context window fills, reliability degrades.

> **Video Resource:** [12-Factor Agents: Patterns of reliable LLM applications](https://www.youtube.com/watch?v=8kMaTybvDUw)

## The Solution: Explicit Control Flow

To build reliable systems, we must abandon the idea of the "Magical Agent" and return to software engineering principles.

### Why It Matters

1.  **Reliability vs. Autonomy**: Infinite loops are unpredictable. Explicit Directed Acyclic Graphs (DAGs) are testable.
2.  **State Management**: Treating agents as "Stateless Reducers" allows them to be paused, resumed, and integrated with human timescales (e.g., waiting 3 days for an email approval).
3.  **The "Anti-Framework"**: We must own the "Hard Parts" (Context & Prompts) rather than outsourcing them to heavy libraries.

### 2. Project: Kinetic Node (Phase 3)
We apply pathfinding to **Network Routing**.
*   **[VPN & Mesh Networking](vpn_mesh_network.md)**: Connecting the isolated Ch 05 Node to the Swarm.


## Technical Patterns

For a detailed breakdown of the 12-Factor Agent patterns, specifically designed for TypeScript/Software Engineers, see:

*   [**Agent Design Patterns**](agent_patterns.md)
