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

## [2026-06-26] synthesis | Document Relationship Map + MCard/VCard/PCard stubs

- **Trigger:** user asked to map the relation of each document to each other.
- **Method:** wrote `src/extract_link_graph.py` (re-runnable) to parse all `[[wikilinks]]` across 258 md files → 1,447 links. Dispatched 3 parallel subagents to read the 108 orphan files (no links in/out) and map conceptual relationships to the core.
- **Findings:**
  - The wiki is **1 connected core of 150 files** + **108 orphan islands** (42% of the wiki — teaching, shopper-analytics, hardware sub-pages, changelogs, chapter topic files, HoTT math course).
  - Top hubs by inbound: MCard (21), Cubical Logic Model (21), VCard (20), Flow State (19), PCard (17), PTR (11).
  - **848 dangling targets** (concepts referenced but no page). The MCard/VCard/PCard trio alone = 58 dangling links.
- **Files created:**
  - `docs/Document_Relationship_Map.md` (type: synthesis) — topology, hub table, 5 core clusters, 6 orphan-island tables with per-file reconnection guidance, top-30 dangling priorities, 6 recommended actions.
  - `docs/MCard.md`, `docs/PCard.md`, `docs/VCard.md` (type: entity) — stubs resolving the 58 highest-mention dangling links. Each defines the card type, its math (Σ/Π/Id-type), its Representation-Engine tier, and cross-links to the other two + [[MVP Cards Design Rationale]] + [[The_Representation_Engine]].
- **Cross-references added (high-value reconnections):**
  - `docs/docs_shopper_analytics/README.md` → linked to Ch 4, Ch 6, Local-First, edge_compute/ip_camera/lidar hubs (reconnects the 20-file orphan island entry point).
  - `chapters/02_The_Meaning_of_Shape/depth_sensing_kinect.md` → linked to Ch 2 README, hott_ssot_reference, Cubical Logic Model, GASing, deep_learning note, Ch 4, edge_compute.
  - `docs/deep_learning_and_physics_video_note.md` → upgraded frontmatter to full schema (type: source, sources: raw/transcripts/...); added connections to Universality, Science of Approximation, depth_sensing_kinect, MCard/PCard/VCard tiers.
- **Verification:** re-ran the graph script — MCard/VCard/PCard now RESOLVED (inbound counts rose to 25/24/21 via cross-links).
- **Pages touched:** docs/Document_Relationship_Map.md (new), docs/MCard.md (new), docs/PCard.md (new), docs/VCard.md (new), docs/docs_shopper_analytics/README.md (updated), chapters/02_The_Meaning_of_Shape/depth_sensing_kinect.md (updated), docs/deep_learning_and_physics_video_note.md (updated), index.md (updated), log.md.
- **Open items (lint backlog, in priority order):** reconnect remaining ~105 orphan files per the §4 tables in Document_Relationship_Map; create stubs for Computational Trinitarianism (9), Directionality (7), Representability (7), Conversational Programming (6), Epiplexity (6), Flow State (19, biggest); cross-link the ai_coding_guide ↔ teaching/handbook mirrors; mark PIPELINE_8080 status: stale; convert path-based markdown links to wikilinks in chapter topic files.
