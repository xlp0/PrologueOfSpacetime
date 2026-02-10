# Local-First: Data Sovereignty as Ground Truth

**Architectural Focus**: Local-First Software (The Sovereign Observer)
**Curriculum Column**: Astrobiology (Spacetime)

## 1. The Philosophy of Ownership

In **Observation**, there is a hidden assumption: *Who controls the instrument controls the truth.* If your telescope is rented from a landlord who can revoke access, you do not truly observe—you are permitted to observe. Your truth is contingent on another's will.

**Local-first** is the architectural principle that eliminates this dependency. It states:

> *The primary copy of data resides on the user's local device. Servers exist, but they hold secondary copies.*

This is not merely a technical optimization. It is the **Copernican Revolution of data architecture**—moving the center of gravity from the cloud (someone else's computer) back to the user's own device. In the language of the Prologue:

*   **Cloud-First**: The Server is the Single Source of Truth. The user is a client—a supplicant requesting access.
*   **Local-First**: The Device is the Single Source of Truth. The server is a mirror—a convenience for synchronization.

The difference is **Sovereignty**. The Observer who owns their own instrument owns their own truth.

### Universal Grammar

In the polynomial $f = \sum c_k \phi_k$, local-first defines where the **coefficients** ($c_k$) are stored and who controls them:

*   **Cloud-first**: $c_k$ lives on the server. The user sees a projection.
*   **Local-first**: $c_k$ lives on the device. The server sees a replica.

This is the difference between **observing a shadow** and **holding the object**.

### GASing Perspective

*   **Menyenangkan (Rhetoric)**: "It's MY data." The primal feeling of **Ownership**. When the internet goes down, your work is still there. No spinners. No waiting. No permission needed.
*   **Asyik (Logic)**: The "Game" of **Offline Survival**. Can you keep working when the network dies? Local-first turns network failure from a crisis into a non-event—the system simply syncs later.
*   **Gampang (Grammar)**: The axioms of **CRDTs** (Conflict-free Replicated Data Types). Mathematical structures that guarantee: any two devices editing the same data independently will always converge to the same result when they reconnect. No central authority needed.

## 2. The Seven Ideals: A Verification Checklist

The Ink & Switch research lab (Martin Kleppmann, Adam Wiggins, Peter van Hardenberg, Mark McGranaghan) published the original local-first manifesto in 2019. They defined seven ideals—a **specification** against which any system can be verified:

| # | Ideal | Verification Question | Prologue Mapping |
| :--- | :--- | :--- | :--- |
| 1 | **Fast** | Does the UI respond instantly, without network round-trips? | Observation without latency |
| 2 | **Multi-Device** | Can data sync across all the user's devices? | Multiple Observers, one Truth |
| 3 | **Offline** | Does the app work without internet? | The Observer survives isolation |
| 4 | **Collaboration** | Can multiple users edit simultaneously? | Consensus among Observers |
| 5 | **Longevity** | Will data outlive the vendor? | Truth outlives the Instrument |
| 6 | **Privacy** | Is data end-to-end encrypted? | The Observer's journal is sealed |
| 7 | **User Control** | Can the user export, migrate, and modify freely? | **Data Sovereignty** |

These seven ideals map directly to the **Observer's requirements** in the Prologue: an Observer who cannot act independently (offline), who cannot retain their own records (longevity), or who cannot verify without permission (user control) is not a true Observer—they are a **dependent**.

### The Kleppmann Definition (2024)

At Local-First Conf 2024, Kleppmann proposed a refined definition:

> *"In local-first software, the availability of another computer should never prevent you from working."*

This is the **Zero Trust** principle applied to infrastructure itself: trust no server to be available. Trust only your own device. Sync when you can; work always.

## 3. The Three Eras: A Causal History

The evolution of software architecture mirrors the evolution of observation itself:

### Era 1: The Desktop (The Solitary Observer)
Software ran locally. Files lived on disk. The user had **full ownership** but was isolated—no collaboration, no cross-device access. Like Tycho Brahe alone in his observatory, accumulating data that only he could see.

### Era 2: The Cloud (The Institutional Observatory)
Software moved to servers. Google Docs, Figma, Slack—collaboration became effortless. But ownership was surrendered. The server became the **Single Source of Truth**, and the user became a tenant. Like astronomers who must book time on a shared telescope: powerful, but contingent.

*   **The Trap**: "There is no cloud. It's just someone else's computer." If the service shuts down, your data may vanish. If the company changes terms, your access may be revoked. The Observer does not own the instrument.

### Era 3: Local-First (The Sovereign Observatory)
A synthesis. The user's device is primary; the cloud is secondary. Collaboration happens through **synchronization**, not through a central server. Like each astronomer having their own telescope, but sharing observations through a common protocol.

*   **The PKC Connection**: The **Personal Knowledge Container (PKC)** is a local-first system by design. Your knowledge lives on your device. It syncs with others when you choose. No central authority decides what you can know or remember.

## 4. The Technical Anatomy

### 4.1 CRDTs: The Mathematics of Consensus Without Authority

**Conflict-free Replicated Data Types** are the foundational technology of local-first. They solve the problem that has plagued distributed systems since Lamport's Byzantine Generals:

> *How can multiple independent agents modify shared state and always converge to agreement—without a central coordinator?*

A CRDT guarantees **Strong Eventual Consistency**: if two devices have received the same set of updates (in any order), they will be in the same state. This is a mathematical invariant, not a protocol—it holds regardless of network topology, timing, or failures.

```
Device A: Insert "Hello" at position 0
Device B: Insert "World" at position 0
                    ↓
        (Both devices go offline)
                    ↓
        (Both devices reconnect)
                    ↓
CRDT Merge: Deterministic ordering → "HelloWorld" or "WorldHello"
            (Same result on BOTH devices, guaranteed)
```

**The Geometry of CRDTs**: In the Universal Grammar, a CRDT is a **Lattice**—a partially ordered set where every pair of elements has a unique least upper bound (join). The merge operation is the join. This guarantees:

$$ \text{merge}(A, B) = \text{merge}(B, A) \quad \text{(Commutativity)} $$
$$ \text{merge}(A, \text{merge}(B, C)) = \text{merge}(\text{merge}(A, B), C) \quad \text{(Associativity)} $$
$$ \text{merge}(A, A) = A \quad \text{(Idempotency)} $$

These three properties guarantee convergence. They are the **axioms of distributed truth**—the algebraic structure that makes consensus possible without a dictator.

### 4.2 The Sync Engine: The Nervous System

The sync engine is the middleware that connects local databases to remote replicas. It handles:

*   **Change Detection**: What has changed locally since the last sync?
*   **Conflict Resolution**: When two devices modified the same record, which version wins? (CRDTs answer this automatically.)
*   **Patch Transmission**: Sending only the delta (difference), not the entire state.
*   **Reconnection**: Gracefully resuming after network interruption.

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Device A   │         │  Sync Layer │         │  Device B   │
│  (Primary)  │◄───────►│  (Optional) │◄───────►│  (Primary)  │
│  SQLite/IDB │         │  Server/P2P │         │  SQLite/IDB │
└─────────────┘         └─────────────┘         └─────────────┘
       ▲                                               ▲
       │              Both are PRIMARY.                 │
       │         The server is a RELAY, not             │
       │              an AUTHORITY.                     │
       └───────────────────────────────────────────────┘
```

### 4.3 Key Technologies

| Technology | Role | Analogy |
| :--- | :--- | :--- |
| **Automerge** | CRDT library (JSON documents) | The mathematical proof engine |
| **Yjs** | CRDT library (real-time collaboration) | The shared whiteboard |
| **SQLite (Wasm)** | Local relational database in browser | The personal filing cabinet |
| **IndexedDB** | Browser-native key-value storage | The desk drawer |
| **PowerSync** | Sync engine (Postgres ↔ SQLite) | The postal service |
| **Replicache** | Sync engine (optimistic mutations) | The telegraph |
| **ElectricSQL** | Sync engine (Postgres-native) | The railway |

## 5. Local-First in the Brain Factory

### 5.1 PKC as Local-First Architecture

The **Personal Knowledge Container** is the Brain Factory's implementation of local-first principles:

| PKC Feature | Local-First Ideal | Implementation |
| :--- | :--- | :--- |
| Local MediaWiki instance | **Offline Capability** | Knowledge accessible without internet |
| Git-based version control | **Longevity** | Data survives any single server failure |
| User-owned data directory | **User Control** | Export, migrate, fork at will |
| MinIO object storage | **Multi-Device Sync** | Replicate across nodes |
| ZITADEL authentication | **Privacy/Security** | Identity is self-sovereign |
| Markdown-first content | **Longevity** | Readable as plain text, forever |

### 5.2 The Retail Lab Scenario

In the **Convenience Store** scenario (see `abc_curriculum.md` §4.1), local-first ensures operational continuity:

*   **Point-of-Sale**: The register works offline. Transactions sync when connectivity returns. No internet outage stops a sale.
*   **Inventory Tracking**: Local database on each device tracks stock. CRDTs merge updates from multiple clerks without conflicts.
*   **Kinect Data**: Depth maps and skeleton data from the [Kinect sensors](../02_The_Meaning_of_Shape/depth_sensing_kinect.md) are processed and stored locally. The cloud receives summaries, not raw streams—preserving bandwidth and privacy.

### 5.3 Cross-Curriculum Connections

Local-first is not confined to a single column of the Quadrivium. It touches every dimension:

| Quadrivium Column | Local-First Aspect | Chapter Connection |
| :--- | :--- | :--- |
| **Arithmetic** (Number) | Token economy: local computation reduces cloud cost | **[Ch 05: Resource Allocation](../05_Resource_Allocation/README.md)** |
| **Geometry** (Space) | Data lives HERE (on device), not THERE (on server) | **[Ch 02: The Meaning of Shape](../02_The_Meaning_of_Shape/README.md)** |
| **Music** (Time) | Sync is temporal: changes propagate over time, not instantly | **[Ch 03: The Power of Rhythm](../03_The_Power_of_Rhythm/README.md)** |
| **Astronomy** (Spacetime) | Sovereignty: the Observer owns the instrument | **Ch 04** (This chapter) |

## 6. Observability Exercises

### Exercise A: The Offline Test
*   **Concept**: Sovereignty through Independence.
*   **Task**: Open the PKC wiki. Disconnect from the internet. Edit a page. Reconnect. Verify the edit syncs.
*   **Lesson**: If your system cannot survive disconnection, you do not own your data—you are renting access to it. The Observer who depends on the network is not observing; they are requesting permission to observe.

### Exercise B: The Conflict Resolution Game
*   **Concept**: Consensus without Authority.
*   **Task**: Two students edit the same document simultaneously on separate devices (both offline). Reconnect both. Observe how the CRDT merges their changes without data loss.
*   **Lesson**: Distributed truth does not require a dictator. CRDTs prove that **mathematical structure** can replace **institutional authority**. This is the algebraic foundation of the Byzantine Generals solution.

### Exercise C: The Longevity Audit
*   **Concept**: Truth outlives the Instrument.
*   **Task**: Export all PKC data to a USB drive. Delete the server. Restore from the USB drive on a fresh machine. Verify completeness.
*   **Lesson**: If your data cannot survive the death of its host, it is not yours. Local-first demands that **data is portable, format-independent, and self-contained**. This is the Tycho Brahe test: can your observations survive the destruction of your observatory?

### Exercise D: The Cost Comparison
*   **Concept**: Thermodynamic Efficiency.
*   **Task**: Measure the latency of a cloud API call vs. a local SQLite query. Compare the energy cost (network round-trip vs. local disk read).
*   **Lesson**: Every network round-trip is a thermodynamic cost ($E = k_B T \ln 2$ per bit erased). Local-first minimizes the **verification tax**—the energy spent asking "Is the server still there?" instead of doing actual work.

## 7. The Duality: Cloud and Local

Cloud-first and local-first are not enemies. They are **dual architectures**, each optimizing for a different constraint:

| | **Cloud-First** | **Local-First** |
| :--- | :--- | :--- |
| **Primary Copy** | Server | Device |
| **Optimizes For** | Collaboration | Sovereignty |
| **Failure Mode** | Server down → all users blocked | Server down → users continue locally |
| **Trust Model** | Trust the provider | Trust the device (Zero Trust) |
| **Latency** | Network round-trip | Near-zero (local disk) |
| **Cost Model** | Pay per request/storage | Pay once for device storage |
| **Philosophical Role** | **Institutional Truth** (the server decides) | **Sovereign Truth** (the user decides) |

The Brain Factory uses **both**: PKC runs local-first for sovereignty; it syncs to MinIO for redundancy. The local copy is the truth; the cloud copy is the backup. This is the **Hoare Triple of Data Sovereignty**:

$$ \{P: \text{Data on Device}\} \ C: \text{Sync to Cloud} \ \{Q: \text{Data on Device AND Cloud}\} $$

The postcondition preserves the precondition. The local copy is never destroyed by the sync—only replicated. This is the **non-destructive** property of local-first: syncing adds redundancy without surrendering control.

## 8. Why Local-First Matters for Indonesia

The Brain Factory's choice of local-first is not accidental. It is a **strategic necessity** for the Indonesian context:

1.  **Network Unreliability**: Rural Indonesia (including the Lake Toba region around IT Del) has intermittent connectivity. A cloud-dependent system would be unusable for significant portions of the day. Local-first turns this constraint into a non-issue.
2.  **Digital Sovereignty**: Indonesia's national interest requires that critical knowledge infrastructure not depend on foreign cloud providers. Local-first ensures that if AWS, Azure, or GCP become unavailable (by policy, pricing, or politics), the Brain Factory continues operating.
3.  **Cost Efficiency**: Cloud compute is priced in USD. Local compute is priced in device hardware (one-time cost). For a developing nation, local-first dramatically reduces the recurring cost of knowledge infrastructure.
4.  **The GASing Principle**: **Gampang** (Easy). A system that works without internet is simpler to deploy, simpler to maintain, and simpler to teach. Complexity is the enemy of adoption.

> For the strategic implementation details, see **[Brain Factory Implementation Case Study](../Brain_Factory_Implementation_Case_Study.md)** §2 (Sovereignty: PKC-OS + Local-first).

## 9. Reverse Mathematics Proof

*   **Theorem**: "Distributed agents can maintain consistent shared state without a central authority."
*   **Weakest Subsystem**: **RCA₀** (Recursive Comprehension Axiom). CRDTs require only computable join operations on a lattice—basic arithmetic on partially ordered sets. No set-theoretic machinery is needed. The convergence guarantee is **constructive**: given the same set of operations, any device can compute the same result. This is consensus reduced to pure computation.

> **"Sovereignty is not isolation. It is the ability to collaborate without dependency. The Sovereign Observer syncs with the world but answers to no server. Local-first is the architecture of freedom."**
