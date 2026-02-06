# Requirement Analysis: "The Brain Factory" Curriculum Engine

**Version:** 4.0 (Pedagogical Pivot)
**Architect:** System Architect / Educational Theorist
**Domain:** Automated Curriculum Design / Knowledge Synthesis

---

## 1. System Overview & The "Factory" Metaphor

The system is no longer a debate hall; it is a **High-Throughput Knowledge Factory**. Its purpose is to ingest vast unstructured data (2,000+ documents) and manufacture structured, pedagogically sound curriculum units.

We utilize a **Parallel RAG Architecture** managed by a "Pedagogical Trinity" of agents. The goal is not consensus, but **Clarity** and **Teachability**.

---

## 2. Axiomatic Constraints (Immutable Laws)

### Axiom I: The Law of Pedagogical Clarity
$$ Clarity(Lesson) > Threshold_{comprehension} $$
*   **Constraint:** All output MUST be formatted as structured learning materials (Learning Objectives, Core Concepts, Exercises).
*   **Constraint:** Abstract rambling is strictly forbidden. If an explanation is too dense, the **Critic Agent** MUST simplify it.

### Axiom II: The Law of Contextual Relevance (The Source)
$$ \forall Fact \in Lesson, \exists Source \in DocLake $$
*   **Constraint:** Every assertion made by the agents MUST be backed by a specific citation from the 2,000-document repository.
*   **Rationale:** We are building a curriculum based on *existing* knowledge, not hallucinating new physics.

---

## 3. Functional Requirements (FR)

### 3.1 The Pedagogical Trinity (The Workers)
To maximize efficiency, we strip away the "Legislative" branch (Politician, Financier) and focus purely on the "Executive" production of knowledge.

| Role | Agent Persona | Responsibilities | Bias Vector |
| :--- | :--- | :--- | :--- |
| **Extractor** | **The Technologist** | **Data Mining**. Scans the 2,000 docs. Identifies key entities, dates, and causal links. Ignores fluff. | *Recall-Focused* |
| **Architect** | **The Pedagogue** | **Lesson Planning**. Takes the raw facts from the Technologist and structures them into a Syllabus (Modules, Lessons, Quizzes). | *Structure-Focused* |
| **Inspector** | **The Critic** | **Quality Control**. Simulates a "Confused Student". Challenges the Architect if a concept is poorly explained. | *Clarity-Focused* |

### 3.2 The Factory Floor (Massive Ingestion)
**FR-01:** The system MUST support **Batch Ingestion** of directories containing up to 2,000 Markdown/PDF files.
**FR-02:** The system MUST utilize the host's **1.2TB RAM** to load the vector index into memory for near-instant retrieval (avoiding disk I/O bottlenecks).

### 3.3 The Output Schema (The Product)
**FR-03:** The final output is NOT a chat log. It is a **Curriculum Artifact** (JSON/Markdown) containing:
1.  **Module Title**
2.  **Learning Objectives** (Bloom's Taxonomy)
3.  **Core Content** (Synthesized from RAG)
4.  **Verification Exercises** (Quiz questions based on the content)

---

## 4. Mathematical Logic: The Comprehension Score

Instead of "Entropy," we optimize for "Comprehension":

```python
def calculate_teachability(lesson_draft):
    # 1. Flesch-Kincaid Grade Level (Target: 10-12)
    readability = analyze_readability(lesson_draft)
    
    # 2. Concept Density (Concepts per Paragraph)
    density = count_concepts(lesson_draft) / len(paragraphs)
    
    # 3. Citation Coverage (% of claims with [Source])
    integrity = count_citations(lesson_draft) / count_claims(lesson_draft)
    
    return weighted_average(readability, density, integrity)
```

*   **Goal:** Maximize Integrity, Optimize Density (not too high, not too low), Stabilize Readability.

---

## 5. System Sequence Diagram (The Assembly Line)

1.  **Ingest (t=0):**
    *   System loads `~2000 documents` into `VectorStore` (RAM).
2.  **Extraction (t=1):**
    *   **Technologist** runs 50 parallel queries: *"Extract all references to Packet Switching 1960-1969".*
    *   Retrieved chunks are aggregated into a "Fact Buffer".
3.  **Drafting (t=2):**
    *   **Pedagogue** reads Fact Buffer.
    *   Drafts `Lesson 1: The Birth of ARPANET`. Organizes facts into a narrative.
4.  **Inspection (t=3):**
    *   **Critic** reviews Lesson 1.
    *   *Flag:* "The explanation of TCP handshakes is too abstract."
5.  **Refinement (t=4):**
    *   **Pedagogue** rewrites section using an analogy (as requested by Critic).
6.  **Packaging (t=5):**
    *   Final Markdown is saved to `curriculum/module_01.md`.