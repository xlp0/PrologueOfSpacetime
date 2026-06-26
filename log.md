---
title: 'Wiki Log'
date: 2026-06-26
type: changelog
status: stable
---

# Wiki Log

> Append-only chronological record. Each entry starts with `## [YYYY-MM-DD] type | Title` so `grep -F '## [' log.md | tail -5` returns the last 5 entries.

## [2026-06-26] setup | LLM Wiki pattern instantiated (hybrid layering)

- **Trigger:** user requested setting up the LLM Wiki pattern (idea doc) on this existing Obsidian vault.
- **Decisions (co-designed with user):**
  - Layer mapping: **hybrid** — existing interlinked content (`chapters/`, `docs/`, `hardware/`, `README.md`) stays as the wiki; external/immutable source material moves into `raw/`.
  - Tooling wired: Dataview frontmatter schema, Marp slides, image handling (`raw/assets/`), qmd search (documented, not installed).
  - Ingestion style: one source at a time, human in the loop.
- **Files created:**
  - `AGENTS.md` — the schema (3 layers, page conventions, ingest/query/lint workflows, tooling, editing discipline).
  - `index.md` — first-pass catalog of ~170 wiki pages, grouped by category.
  - `log.md` — this file.
- **Files moved into `raw/` (immutable source layer):**
  - `transcript.txt` / `transcript.json` → `raw/transcripts/deep_learning_and_physics_transcript.{txt,json}` (descriptive rename; was the deep-learning-and-physics video).
  - 5 PDFs → `raw/articles/` (Prologue_of_Spacetime_introduction, Cognitive_Ascent_Mission_Guide, Engineering_Awe_A_Scale-Free_Architecture, Life_Mind_Machine_Stability, The_Mirror_and_the_Algorithm).
  - `BrainFactory_poweredByGASing.png` → `raw/assets/`.
  - `media/3DModels/scad/*` → `raw/assets/3dmodels/` (DigitalSundial.scad + README). The `media/` directory is now removed.
- **Inbound links updated (2) to reflect the PNG move:** `chapters/00_Structure_and_Vision.md` and `docs/mcard_studio/Public/Chapters_of_Prologue_of_Spacetime/00_Structure_and_Vision.md` (path mention `media/...` → `raw/assets/...`).
- **Obsidian config:** `.obsidian/app.json` → `attachmentFolderPath: raw/assets`. (Manual step remaining for user: bind 'Download attachments for current file' hotkey + confirm the attachment-location mode in Settings.)
- **Open items / lint backlog (for a future lint pass, not auto-fixed):**
  - Backfill full frontmatter (title/date/tags/type/sources/status) on legacy pages — most currently have only `modified:` or partial frontmatter.
  - Create `type: source` summary pages for the 5 PDFs now in `raw/articles/` (only the transcript currently has a note: `docs/deep_learning_and_physics_video_note.md`).
  - Many dangling `[[wikilinks]]` (e.g. `[[MCard]]`, `[[PCard]]`, `[[VCard]]`, `[[Directionality]]`, `[[Maxwell's Demon]]`, `[[Hub/...]]`) — Obsidian graph view tracks these; create stubs for the high-mention concepts.
  - Large binaries (~20 MB PDFs) in `raw/articles/` are Git-LFS candidates (flagged in AGENTS §9).
- **Notes:** No `raw/` source files were modified — only moved/renamed. All existing wiki pages preserved in place.

## [2026-06-26] synthesis | Pancasila and the Five-WH mapping
- Source: user query (no raw source)
- Pages touched: docs/Pancasila_and_the_Five_WH.md (created), index.md (updated), log.md
- Notes: Mapped 5-WH questions (Who/When/Where/Why/How) to Indonesian Pancasila's 5 sila. Key insight: 5-WH is the inquiry, Pancasila is the answer — both pentadic, both irreducible, both coordinated. Includes generative (生) and overcoming (克) cycles. Cross-referenced to Pentadic Threshold, Wuxing, Five Wise Guys, Five Dining Philosophers. Extended the pentadic convergence table to 7 traditions (added Pancasila as governance dimension).
