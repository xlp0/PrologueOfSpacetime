---
marp: true
theme: default
paginate: true
title: 'Prologue of Spacetime — Wiki Overview'
date: 2026-07-07
tags: [Presentation, Marp, Seven-Liberal-Arts, Wiki, Overview]
type: note
sources: ['README.md', 'AGENTS.md', 'index.md']
status: draft
liberal_art: Trivium-Rhetoric
---

# Prologue of Spacetime

A living wiki for a Unifying Namespace grounded in **Homotopy Type Theory**, the D&D **Representation Engine**, and a 24/7 MLOps refinement loop.

2026-07-07

---

## What This Is

> *"Number is the ruler of forms and ideas, and the cause of gods and daemons."* — Iamblichus

Not a curriculum. Not a game. A **Demonstrative Example** of a Living System — proving that a Unifying Namespace can relate concepts, persist memory, and surface latent opportunities.

- **Mathematical foundation:** HoTT — "Equality" is a Path, not a boolean.
- **Engagement mechanic:** D&D as a word game about representation itself.
- **Operational substrate:** 24/7 MLOps, Git as membrane, Content-Addressable Storage.

---

## The Three Layers

| Layer | Location | Owner | Mutability |
|:---|:---|:---|:---|
| **Raw sources** | `raw/` | Human curates | **Immutable** — never edit, rename, or delete |
| **The wiki** | everything else | **LLM owns** | LLM creates / updates / cross-references freely |
| **The schema** | `AGENTS.md` | Co-evolved | Edit only when conventions change |

`raw/` is the **source of truth**. The wiki is a derived, maintained synthesis. When a wiki claim is challenged, the raw source wins.

---

## Directory Layout

```
PrologueOfSpacetime/
├── AGENTS.md              # the schema (read first)
├── README.md              # top-level synthesis
├── index.md               # LLM-maintained content catalog
├── raw/                   # IMMUTABLE source layer
│   ├── transcripts/ · articles/ · assets/
├── chapters/              # the 12-chapter matrix
├── docs/
│   ├── concepts/          # MCard, PCard, VCard, Representation Engine…
│   ├── principles/        # Local-First, SpacetimeDB, Observability…
│   ├── sources/           # source summaries (type: source)
│   ├── records/  + logs/  # minutes, changelogs, weekly agent logs
│   ├── plans/             # execution plans, k8s, demos
│   ├── teaching/          # curriculum, handbook, this slideshow
│   ├── templates/         # 11 page-type templates
│   └── …
├── hardware/              # reference pages per device
└── src/                   # MCard utils, OpenClaw, link-graph extractor
```

---

## The Unifying Namespace — CLM

Everything is indexed as a **Cubical Logic Model (CLM) triple**:

| Dimension | Handle | Captures |
|:---|:---|:---|
| **Spec** | MCard | The *What* — intent, requirement, rhetoric |
| **Impl** | PCard | The *How* — code, process, logic |
| **Exp**  | VCard | The *Proof* — tests, verification, grammar |

Worst-case fallback: the content's **SHA-3 hash**. Content can never be orphaned.

> **Guarantee:** we always have a Handle. The worst case is the content's default hash. This is the foundation of Universal Memory.

---

## HoTT in One Slide

A **Type** is a Space. A **Term** is a Point. An **Equality** is a **Path** between points.

- **Multiple Proofs** — many paths can show $x = y$; each carries structural info.
- **Propositions as Types** — to prove $P$, construct a term of type $P$.
- **Univalence** — equivalent types *are* identical. The foundation for content-addressable truth.

$$
\text{Effective Learning} = \text{Compression (Density)} \times \text{Kenosis (Capacity)}
$$

This is why Git works (directed commit graph → single source of history), why blockchain works (directed chain → single consensus), and why this wiki works.

---

## The Representation Engine

D&D is the oldest word game about representation: you speak a world into existence, and reality judges whether your words were faithful.

| Tier | Word Game | What Players Discover | Card |
|:---|:---|:---|:---|
| **1. Name** | "Cat" ≠ "Act" | Directionality creates distinction | MCard |
| **2. Describe** | "Cat on mat" ≠ "Mat on cat" | Non-commutativity determines truth | PCard |
| **3. Compose** | $5! = 120$ orderings | Permutation generates the namespace | VCard |
| **4. Prove** | Defend against reinterpretation | Representability collapses to truth | {P}C{Q} |

**The DM is Maxwell's Demon** — `DM` reversed is `MD`. Every adjudication costs $\geq k_B T \ln 2$ of entropy (Landauer).

---

## The 12-Chapter Matrix

**Trivium × Quadrivium** — a $3 \times 4$ grid where each chapter is a function:

|                           | **Arithmetic** | **Geometry** | **Music** | **Astrobiology** |
|:--------------------------|:---|:---|:---|:---|
| **Rhetoric** (Spec) | Ch 1: Counting Value | Ch 2: Deep Shape | Ch 3: Rhythm | Ch 4: Observation |
| **Logic** (Impl)    | Ch 5: Allocation | Ch 6: Pathfinding | Ch 7: Causality | Ch 8: Prediction |
| **Grammar** (Exp)   | Ch 9: Schema | Ch 10: Topology | Ch 11: Lifecycle | Ch 12: Coordination |

Each chapter produces an **MVP Card** indexed into the CLM: $12 \times 5 = 60 = |A_5|$ — the order of the smallest non-abelian simple group. The threshold of irreducible complexity.

---

## The Two Special Files

### `index.md` — content catalog
- Catalog of **every** wiki page, grouped by `type`.
- **Read this first** when answering a query, then drill in.
- Replaces embedding-RAG at moderate scale.

### `docs/records/logs/` — weekly agent operation logs
- Partitioned weekly: `weekly-log-YYYY-MM-DD.md`.
- Every entry starts with `## [YYYY-MM-DD] type | Title`.
- Append after every ingest, synthesis, reorg, or lint.

> The human owns sourcing and direction. The LLM owns the bookkeeping that humans abandon.

---

## Operations — Ingest, Query, Lint

### Ingest (one source at a time)
Read source → discuss 3–6 takeaways → write source summary (`type: source`) → update `index.md` → propagate to every related page → flag contradictions explicitly → append weekly log.

### Query
Read `index.md` → open 1–4 relevant pages → synthesize answer with citations → propose filing useful answers back as `type: synthesis` pages.

### Lint
Contradictions · stale claims · orphan pages · dangling links · missing pages · missing cross-references · data gaps.

---

## Page Conventions

Every page starts with YAML frontmatter — this is what Dataview queries against:

```yaml
---
title: 'The Representation Engine'
date: 2026-03-15
tags: [Representation, D&D, Flow-State]
type: concept          # source | entity | concept | synthesis | overview | changelog | note
sources: [raw/articles/Foo.pdf]
status: stable        # draft | stable | stale
liberal_art: Trivium-Rhetoric
---
```

- `type` drives Dataview tables and the index.
- `sources` gives traceability from claim → raw origin.
- `status: stale` is the lint signal.
- Every page carries one of the **Seven Liberal Arts** tags.

---

## Tooling

- **Obsidian** — the IDE; this directory is a vault. Wikilinks (`[[Target]]`) are the dominant convention.
- **`index.md`** — primary navigation; replaces RAG at moderate scale.
- **qmd** — local hybrid BM25 + vector search when the index can't resolve a query precisely.
- **Marp** — markdown → slides. This very deck is Marp.
- **Dataview** — frontmatter-driven queries inside Obsidian.
- **MCP servers** — external capabilities (GitNexus, Google Workspace, Playwright…) wired into OpenCode.

---

## The Seven Liberal Arts Mapping

Every page picks the art matching its primary mode:

| Art | Tag | Mode | Example |
|:---|:---|:---|:---|
| Trivium — Grammar | `Trivium-Grammar` | Structure, rules, specs | k8s components, CLM, this setup guide |
| Trivium — Logic | `Trivium-Logic` | Reasoning, verification | RAG vs wiki, security, harness thesis |
| Trivium — Rhetoric | `Trivium-Rhetoric` | Expression, persuasion | Plans, agency, **this slideshow** |
| Quadrivium — Arithmetic | `Quadrivium-Arithmetic` | Number, cost, FLOPs | Capex, token economics, benchmarks |
| Quadrivium — Geometry | `Quadrivium-Geometry` | Shape, space, graphs | Knowledge graphs, k8s architecture |
| Quadrivium — Music | `Quadrivium-Music` | Rhythm, pipelines, flow | CI/CD, business-OS wiring |
| Quadrivium — Astronomy | `Quadrivium-Astronomy` | Motion, time, worlds | World models, robotics, memory |

---

## How to Contribute

1. **Drop a source** into `raw/` (transcript, article, PDF) → ask the agent to ingest.
2. **Ask a question** → the agent reads `index.md`, drills in, answers with citations, files useful answers back.
3. **Request a lint** → the agent surfaces contradictions, stale claims, orphans, dangling links.
4. **Edit a page** → update frontmatter, preserve wikilinks, keep `sources:` traceable, append a weekly log entry.

> You (the human) own sourcing, direction, and questions. The LLM owns the wiki layer entirely — creation, updates, cross-references, contradiction flagging.

---

## Summary

- A **living wiki**, not a static doc site — knowledge is compiled once and *kept current*.
- Grounded in **HoTT** — equality as path, types as spaces.
- Indexed by the **CLM** — every concept is a `(Spec, Impl, Exp)` triple.
- Engaged through **D&D** — the Representation Engine.
- Operated as **24/7 MLOps** — Git as membrane, CAS as truth.
- **Obsidian** is the IDE; **AGENTS.md** is the schema; **you** are the programmer.

---

## References

- [[README|Prologue of Spacetime — README]] — top-level synthesis.
- [[AGENTS]] — the schema (read before editing any wiki page).
- [[index|Wiki Index]] — the content catalog.
- [[The_Representation_Engine|The Representation Engine]] — D&D as word game.
- [[Cubical Logic Model|Cubical Logic Model]] — the formal CLM definition.
- [[Trivium|Trivium]] · [[Quadrivium|Quadrivium]] — the classical frameworks.
- `docs/teaching/installing_google_workspace_mcp.md` — MCP setup guide (companion).
- [github.com/taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)
