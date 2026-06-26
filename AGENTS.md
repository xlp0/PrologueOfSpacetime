# AGENTS.md — LLM Wiki Schema for Prologue of Spacetime

> This file is the **schema**: it tells every LLM agent (OpenCode, Codex, Claude Code, etc.) how this wiki is structured, what the conventions are, and what workflows to follow. Co-evolve it with the user as conventions settle. **Read this before editing any wiki page.**

## 1. What this is

This repository is a **living wiki** for the *Prologue of Spacetime* project — a meta-game / curriculum / unifying namespace grounded in Homotopy Type Theory (HoTT), the D&D **Representation Engine**, and a 24/7 MLOps refinement loop. The wiki is a **persistent, compounding artifact**: knowledge is compiled once from sources and *kept current*, not re-derived on every query.

You (the LLM) **own the wiki layer entirely** — you create pages, update them when new sources arrive, maintain cross-references, flag contradictions, and keep everything consistent. The human owns **sourcing, direction, and questions**. You do the bookkeeping that humans abandon.

The human browses the result in **Obsidian** (this directory is an Obsidian vault). Obsidian is the IDE; you are the programmer; the wiki is the codebase. Lead with the outcome; never narrate maintenance steps.

## 2. The three layers

| Layer | Location | Who owns it | Mutability |
|:---|:---|:---|:---|
| **Raw sources** | `raw/` | Human curates; LLM reads | **Immutable.** Never modify, rename, or delete a source file. |
| **The wiki** | everything else (`README.md`, `chapters/`, `docs/`, `hardware/`, `index.md`, `log.md`) | **LLM owns** | LLM creates / updates / cross-references freely. |
| **The schema** | `AGENTS.md` (this file) | Co-evolved | Edit only when conventions change. |

`raw/` is the **source of truth**. The wiki is a derived, maintained synthesis. When a wiki claim is challenged, the raw source wins — update the wiki to match.

## 3. Directory layout

```
PrologueOfSpacetime/
├── AGENTS.md              # this schema (you are here)
├── README.md              # project overview / top-level synthesis (wiki)
├── index.md               # LLM-maintained catalog of every wiki page (§5)
├── log.md                 # append-only chronological record (§5)
├── raw/                   # IMMUTABLE source layer
│   ├── transcripts/       # video / audio transcripts (.txt, .json)
│   ├── articles/          # clipped articles, PDFs
│   └── assets/            # images, 3D models, and the Obsidian attachment folder
│       └── 3dmodels/
├── chapters/              # the 12-chapter matrix (wiki)
├── docs/                  # concept pages, entity pages, sub-vaults (wiki)
│   ├── people/  game_design/  narrative/  teaching/  workflows/
│   ├── changelog/  Update_History/  todos/  ...
│   └── mcard_studio/      # published / snapshot copies — keep in sync on path changes
├── hardware/              # hardware reference pages (wiki)
└── src/                   # code (MCard utils, OpenClaw loop, Titan Quorum)
```

The old `media/` directory was migrated into `raw/` on setup (2026-06-26). If you find source-like material loose in the tree (clipped articles, transcripts, PDFs), propose moving it into `raw/` and update path references — but never move files unilaterally without checking inbound links first (§7).

## 4. Page conventions

### 4.1 Frontmatter (required on new pages; backfill on edited pages)

Every wiki page starts with a YAML block. This is what Dataview queries against.

```yaml
---
title: 'The Representation Engine'        # human-readable title (quote if it contains a colon)
date: 2026-03-15                          # ISO date — creation or last major revision
tags: [Representation, D&D, Flow-State]    # match existing tags on the topic
type: concept                             # source | entity | concept | synthesis | overview | changelog | note
sources: [raw/articles/Foo.pdf]           # source files this page derives from (omit if none)
status: stable                            # draft | stable | stale  (set stale during lint if superseded)
---
```

- `type` drives the index categories and Dataview tables.
- `sources` gives **traceability** from a wiki claim back to its raw origin. Always populate for source-derived pages.
- `status: stale` is the lint signal that a page needs revision against newer sources.
- Legacy pages may carry only `modified:` or `title/date/tags` — when you edit them, bring them up to the full schema.

### 4.2 Links

- Use Obsidian **wikilinks**: `[[Target]]` or `[[Target|Alias]]`. This is the dominant convention — follow it; do not convert to markdown links.
- Path-based targets are allowed: `[[Hub/Theory/Category Theory/Directionality|Directionality]]`.
- **Every** new entity/concept you introduce should get its own page eventually; a red (dangling) link is a TODO, not a bug. Lint reports dangling links (§6.3).
- When you mention a source, cite its raw path inline: `` `raw/articles/Prologue_of_Spacetime_introduction.pdf` ``.

### 4.3 Structure and style

- Numbered top-level sections (`## 1.`, `## 2.`), `###` for subsections — match existing chapter/doc style.
- Open concept/entity pages with a blockquote epigraph or a one-sentence definition, as existing pages do.
- LaTeX for all math: `$inline$`, `$$display$$`.
- Markdown tables with alignment colons.
- One page = one concept/entity. Split when a page tries to be two things.

### 4.4 Naming

- Page filenames: `PascalCase_with_underscores_for_breaks.md` (e.g. `The_Representation_Engine.md`), matching current files.
- Place concept/entity pages under `docs/`; chapter content under `chapters/`; hardware under `hardware/`.
- Summary pages for sources go in `docs/` and are named `<SourceShortName>.md` with `type: source`.

## 5. The two special files

### index.md — content catalog (LLM updates on every ingest)

A catalog of every wiki page, grouped by `type`, each entry a link plus a one-line summary plus key metadata. Organized by category. **When answering a query, read `index.md` first** to find relevant pages, then drill in. This is the navigation layer that replaces embedding-RAG at moderate scale.

### log.md — chronological record (append-only)

Every ingest, query-that-became-a-page, and lint pass gets a dated entry. Use the exact prefix format so the log is parseable with simple unix tools:

```
## [2026-06-26] ingest | Deep Learning and Physics (video transcript)
- Source: raw/transcripts/deep_learning_and_physics_transcript.txt
- Pages touched: docs/deep_learning_and_physics_video_note.md (updated), index.md
- Notes: linked renormalization to MERA; flagged tension with §3 of chapters/09
```

`grep -F '## [' log.md | tail -5` returns the last 5 entries. Keep this property.

## 6. Operations

### 6.1 Ingest (default: one source at a time, human in the loop)

When the user drops a source into `raw/` (or points you at one already there) and says to process it:

1. **Read** the source fully. For long media, work coarse-to-fine: overview / transcript segments first, then zoom into windows. For PDFs, read text; view referenced images separately when relevant.
2. **Discuss** the 3–6 key takeaways with the user before writing. Ask what to emphasize.
3. **Write/update a source summary page** under `docs/` with `type: source`, `sources: [...]`, frontmatter per §4.1.
4. **Update the index** (`index.md`) — add the new page and any new entity/concept pages.
5. **Propagate**: update every entity/concept page the source bears on (a single source may touch 10–15 pages). Add or strengthen cross-references. **Flag contradictions explicitly** — do not silently overwrite an older claim; add a `> Contradicts:` note citing both sources and let the user resolve.
6. **Append a `log.md` entry** with the prefix format above.

Never modify the source file itself. If a source needs renaming or relocating, ask the user.

### 6.2 Query

When the user asks a question:

1. Read `index.md`, then open the 1–4 most relevant pages.
2. Synthesize an answer **with citations** (wikilinks to the pages, and the source path for claims of fact).
3. If the answer is a useful artifact (a comparison, analysis, discovered connection), **propose filing it back into the wiki** as a new `type: synthesis` page. Good answers should compound, not evaporate into chat.
4. For presentation requests, output **Marp** markdown (§8.2). For data, prefer a markdown table or a chart spec the user can render.
5. Log significant queries-that-became-pages in `log.md`.

### 6.3 Lint

Run when the user asks for a health check (periodically, or before a milestone):

1. **Contradictions** between pages — surface each with both citations.
2. **Stale claims** superseded by newer sources → mark `status: stale`.
3. **Orphan pages** with no inbound links.
4. **Dangling links** (wikilinks with no target page) — create stubs for important ones.
5. **Missing pages** for concepts mentioned often but lacking a page.
6. **Missing cross-references** — two pages that should link but don't.
7. **Data gaps** that a web search or new source could fill — suggest specific questions to investigate.
8. Report findings as a checklist; append a `log.md` lint entry. Fix only what the user approves.

## 7. Cross-reference and orphan hygiene

- Before moving or renaming any wiki page, **grep for inbound links** (`[[OldName` and `[[OldName|`) and update them. The `docs/mcard_studio/Public/` tree holds published copies — update those path references too when you move shared assets.
- Dangling links are tracked by Obsidian's graph view and by lint. A concept mentioned 3+ times across the wiki without a page is a lint finding.

## 8. Tooling

### 8.1 Search — qmd

`index.md` is the primary navigation. When the wiki outgrows the index, use **qmd** (github.com/tobi/qmd) — a local hybrid BM25 + vector search over markdown with LLM re-ranking, on-device. It has a CLI (shell out) and an MCP server (native tool). Use it for queries the index cannot resolve precisely.

```bash
qmd search 'renormalization MERA multiscale'   # shell out for ad-hoc search
```

If qmd is installed and exposed as an MCP tool, prefer the MCP interface.

### 8.2 Slides — Marp

For presentations, emit **Marp** markdown (the project already has `docs/presentation_plan.md` and `run_presentation.sh`). Front-matter directive plus `---` slide separators:

```markdown
---
marp: true
theme: default
---
# Slide title
- bullet
---
## Next slide
```

File under `docs/visuals/` or alongside `presentation_plan.md`. Keep slide generation wiki-driven: pull structure from the cited wiki pages.

### 8.3 Dataview

Frontmatter (§4.1) is shaped for Dataview. Example queries the user can drop into a page:

```dataview
TABLE date, status FROM 'docs' WHERE type = 'concept' SORT date DESC
```

```dataview
LIST FROM #D&D WHERE status != 'stable'
```

Keep frontmatter consistent so these queries stay useful.

### 8.4 Images

- Obsidian's **attachment folder** is set to `raw/assets/` (`.obsidian/app.json`). New pasted/downloaded images land there automatically.
- **One-time manual setup** (cannot be done by file edit): Obsidian → Settings → Files and links → set 'Default location for new attachments' = *In the folder specified below* = `raw/assets`. Then bind 'Download attachments for current file' to a hotkey (e.g. Ctrl+Shift+D) under Settings → Hotkeys.
- LLMs cannot read markdown plus inline images in one pass. When an image matters, read the text first, then view the referenced image file separately for additional context.

## 9. Editing discipline

- **You own the wiki; the human owns raw sources and direction.** Make edits directly — do not ask permission for individual cross-reference updates.
- **Raw is immutable.** Never edit, rename, or delete anything under `raw/`.
- **Trace every claim to a source** via the page's `sources:` field or an inline path. If you cannot, mark the claim as `[unverified]`.
- **Contradictions are explicit**, never silently resolved.
- **Re-read `index.md` before answering; append `log.md` after every ingest or lint.**
- Large binary assets in `raw/` (the ~20 MB PDFs) are candidates for Git LFS — flag this to the user rather than committing more.
- This is a git repo. You get version history, branching, and collaboration for free.
