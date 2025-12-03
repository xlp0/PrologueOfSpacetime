# Prologue of Spacetime: The Game of Continuation in Spacetime

> *"Number is the ruler of forms and ideas, and the cause of gods and daemons."* — Iamblichus

**Prologue of Spacetime** is a "Meta-Game" of continuation that fuses interactive storytelling, cultural philosophy, and advanced distributed systems engineering.

## 🤖 CodeWiki Workspace

This repository serves as a specialized **Project Workspace** designed for collaboration with **CodeWiki by Google**. It acts as an operational bridge between the user's personal knowledge base (DataVault) and the active development of the Prologue project.

## 📂 File Management Strategy

To maintain a **Single Source of Truth (SSOT)** while enabling active development, this project employs a **Hybrid Symbolic Link Strategy**:

1.  **Vault-Centric Truth**: The core narrative and theoretical documents reside permanently in the user's `DataVault/WorkingNotes`. We do not duplicate these files.
2.  **Symlink Synchronization**: Key documents are symbolically linked into the `docs/` directory of this repository.
    *   **Benefit**: Any edits made here (by the user or CodeWiki) are immediately reflected in the DataVault.
    *   **Benefit**: The repository remains lightweight, tracking only the project structure and code, not the heavy knowledge base assets.
3.  **Context Portal**: A symbolic link to the broader `WorkingNotes` is available in `docs/` to allow CodeWiki to search for related context (e.g., "Meta-Narrative" files) without needing to index the entire hard drive.
4.  **Git Configuration**: The `.gitignore` file is explicitly configured to ignore `docs/WorkingNotes` to prevent accidental commitment of the entire private knowledge base, while allowing specific project artifacts to be tracked.

## 📚 Active Context (in `docs/`)

The following core documents are currently linked for active work:

*   **[`Prologue of Spacetime.md`](docs/Prologue%20of%20Spacetime.md)**: The core "Game" document. It establishes the philosophical and mathematical axioms, introducing concepts like **Time as a Non-Commutative Medium** and the **Monadic Mental Model**.
*   **[`Meta-Narrative Framework for Prologue of Spacetime.md`](docs/Meta-Narrative%20Framework%20for%20Prologue%20of%20Spacetime.md)**: The "Dungeon Master's Guide" detailing the **12-Chapter Structure** and **Agentic Workflows**.

## 🗝 Key Concepts

### 1. The 12-Chapter Structure (Trivium × Quadrivium)
The framework is structured as a matrix of **Pedagogy (Reverse Trivium)** and **Content (Revived Quadrivium)**:

| | **Arithmetic** (Numbers) | **Geometry** (Space) | **Music** (Time) | **Astronomy** (Spacetime) |
|---|---|---|---|---|
| **Rhetoric** (Value/Why) | Ch 1: The Value of Counting | Ch 2: The Meaning of Shape | Ch 3: The Power of Rhythm | Ch 4: The Truth of Observation |
| **Logic** (Process/What) | Ch 5: Resource Allocation | Ch 6: Network Pathfinding | Ch 7: Temporal Causality | Ch 8: Orbit Prediction |
| **Grammar** (Structure/How) | Ch 9: Counting Water | Ch 10: Rice Terrace Topology | Ch 11: Ceremonial Beats | Ch 12: Calendar Coordination |

### 2. Conversational Programming (Vibe Coding)
The Prologue teaches **Monadic Thinking** without requiring knowledge of Haskell. By treating narrative prompts as typed functions, participants learn to manage context and side-effects:
*   **Maybe Monad**: Handling uncertainty.
*   **Either Monad**: Explicit failure paths.
*   **State Monad**: Evolving community conditions.
*   **IO Monad**: The boundary between decision and action.

### 3. Sovereign Operational Networks (SON)
The story demonstrates that true sovereignty comes from owning the "Maxwell's Demon"—the decision-making intelligence of the network.

---
*This project is part of the **PKC (Personal Knowledge Container)** ecosystem, dedicated to enabling **Computational Governance** and **Cultural Sovereignty** through open-source technology.*
