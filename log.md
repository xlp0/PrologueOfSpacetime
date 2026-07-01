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

## [2026-06-26] reorg | docs/ directory sorted into typed subfolders

- **Trigger:** user noted docs/ was too messy (41 flat files + 20 dirs at root).
- **Method:** multi-agent workflow — 3 parallel subagents each handled one cluster of file moves (board_games, concepts, principles+records+plans+sources), while I handled cross-cutting path-ref fixes, the shopper_analytics rename, AGENTS.md update, and verification.
- **41 flat files sorted into 6 new typed subfolders:**
  - `docs/concepts/` (11 files: MCard, PCard, VCard, The_Representation_Engine, DM_as_Maxwells_Demon, Monadic Composition, hott_ssot_reference, Prologue_Conceptual_Digest, Pancasila_and_the_Five_WH, Document_Relationship_Map, Digital_Synesthesia)
  - `docs/principles/` (9 files: Local-First, Local-First Paradigm, Observability, Reliability, SpacetimeDB_*, PKC_ZITADEL, Five Dining Philosophers, Residential_Power)
  - `docs/board_games/` (13 files: all Board_Game_* + *_GAME_DOCUMENTATION + D&D docs + Monopoly story)
  - `docs/records/` (3 files: MoM files, WorkingNotes_Content_Summary)
  - `docs/plans/` (4 files: EXECUTION_PLAN, B200_24x7, duwei_workshop, presentation_plan)
  - `docs/sources/` (1 file: deep_learning_and_physics_video_note)
- **Directory renamed:** `docs/docs_shopper_analytics/` → `docs/shopper_analytics/` (21 files).
- **Path-based references fixed:** 13 total across index.md, Document_Relationship_Map.md, chapters/05/README, chapters/05/iot_motor_control, chapters/02/README, chapters/02/topology_printing, chapters/02/geometry_analytics, chapters/04/edge_observation_architecture, docs/inaai/prof-ben-koo-speeches, docs/plans/EXECUTION_PLAN, README.md. (Bare [[wikilinks]] resolve by basename in Obsidian — unaffected by moves.)
- **AGENTS.md updated:** §3 directory layout now reflects the new subfolder structure + an "organization convention" paragraph so future AI agents know where to file new pages by type.
- **Verification:** zero flat .md files remain at docs/ root. Link graph script confirms MCard/VCard/PCard still resolved (26/25/22 inbound). 68 renames staged in git.
- **Pages touched:** AGENTS.md, index.md, docs/concepts/Document_Relationship_Map.md, README.md, docs/plans/EXECUTION_PLAN.md, 5 chapter topic files, docs/inaai/prof-ben-koo-speeches.md, log.md. 68 files renamed via git mv (history preserved).

## [2026-06-26] templates | 8 page-type templates + Obsidian Templates plugin wired

- **Trigger:** user noted "we will have to have a lot of templates" — with 140+ pages and 7 page types, templates ensure consistency for future AI agents.
- **Files created (in `docs/templates/`):**
  - `README.md` — index of all templates + the seven liberal arts tag mapping table
  - `concept.md` — for foundational concept/entity pages
  - `principle.md` — for operational/architectural principles
  - `source.md` — for source summaries after ingest (§6.1)
  - `synthesis.md` — for query-that-became-a-page (§6.2)
  - `record.md` — for meeting minutes, working notes
  - `plan.md` — for execution/operational plans
  - `chapter_topic.md` — for chapter deep-dive topic files
  - `presentation_marp.md` — for Marp slide decks (§8.2)
- **Each template includes:**
  - Full YAML frontmatter per §4.1 schema (title, date, tags, type, sources, status, liberal_art)
  - Placeholder structure (UPPERCASE placeholders + `{{date}}` for Obsidian Templates plugin)
  - Section scaffolding matching existing page conventions (numbered sections, blockquote epigraphs, "See also" with cross-links)
  - The `liberal_art` field + `Seven-Liberal-Arts` tag — connecting every new page to the [[Trivium]] x [[Quadrivium]] narrative
- **Obsidian config:** `.obsidian/templates.json` → `{"folder": "docs/templates"}`. The Templates core plugin is enabled; bind "Insert template" to a hotkey (e.g. Cmd+T) to use.
- **AGENTS.md updated:** §4.4 naming now specifies the typed subfolders; new §4.5 "Templates" documents the 8 templates + the seven liberal arts tag mapping so future AI agents know to read the matching template before creating any new page.
- **Liberal arts distribution** (from the inaai/ files distributed earlier): Trivium-Logic (19), Trivium-Grammar (18), Quadrivium-Astronomy (11), Quadrivium-Geometry (9), Quadrivium-Arithmetic (8), Trivium-Rhetoric (7), Quadrivium-Music (5).

## [2026-06-26] reorg+templates | Root cleanup, teaching files upgraded, teaching template

- **Trigger:** user noted teaching files (like Ch4 Tokens and Context) had no links or frontmatter; asked for teaching template; questioned root directory professionalism.
- **Root directory cleanup:**
  - `ai_coding_guide/` → `docs/teaching/ai_coding_guide/` (13 chapters + README)
  - `abc_curriculum.md` → `docs/teaching/abc_curriculum.md`
  - `requirements.md` → `docs/plans/requirements.md`
  - `demos/` → `docs/demos/` (Python scripts + 2 markdown)
  - Deleted `Untitled.base`, `Untitled.canvas` (junk Obsidian files)
  - `skills-lock.json` added to .gitignore
  - Root now has only: AGENTS.md, README.md, index.md, log.md, Hub/ (71 refs, can't move), chapters/, docs/, hardware/, raw/, src/, requirements.txt, run_presentation.sh, skills-lock.json (gitignored)
- **Teaching template created:** `docs/templates/teaching_chapter.md` — for curriculum/lesson chapters with `course`, `chapter`, `audience` fields + liberal art tag. Total templates now: 11.
- **29 teaching files upgraded** via `src/upgrade_teaching_files.py`:
  - 14 files in `docs/teaching/ai_coding_guide/` (professional audience)
  - 15 files in `docs/teaching/handbook/` (beginner audience)
  - Each now has: full YAML frontmatter (title, date, tags, type, sources, status, course, chapter, liberal_art, audience) + wikilinks to core concepts (The_Representation_Engine, MCP, Trivium, abc_curriculum, Local-First, SpacetimeDB, second brain, Flow State, Dungeon Master, context engineering, prompt injection — first occurrence only)
  - Liberal arts distributed across chapters: Trivium-Grammar (ch 6,7,8,12), Trivium-Logic (ch 2,11), Trivium-Rhetoric (ch 1,5,10,13), Quadrivium-Arithmetic (ch 4), Quadrivium-Geometry (ch 3,14), Quadrivium-Music (ch 9)
- **AGENTS.md §4.5** updated with teaching_chapter template in the table.
- **Scripts:** `src/upgrade_teaching_files.py` (re-runnable), `src/distribute_inaai.py` (one-shot, done).

## [2026-07-01] synthesis | 3E Framework (Efficacy, Efficiency, Effectiveness) integration

- **Trigger:** user requested updating README.md and changelog, then pushing to Github.
- **Files created/modified:**
  - `docs/concepts/3E Framework.md` (new)
  - `docs/concepts/Efficacy.md` (new)
  - `docs/concepts/Efficiency.md` (new)
  - `docs/concepts/Effectiveness.md` (new)
  - `docs/records/weekly-2026-06-28.md` (new weekly changelog)
  - `README.md` (modified)
- **Notes:** integrated the 3E verification architecture. Aligned Efficacy with Logic/CLM Spec, Efficiency with Computation/CLM Impl, and Effectiveness with Category Theory/CLM Exp. Resolved rebase conflicts due to remote folder renaming (`docs/narrative/` -> `docs/concepts/` and `docs/changelog/` -> `docs/records/`).

## [2026-07-01] synthesis | Software Lagrangian, Least Action Principle, and Relational Metrics

- **Trigger:** user requested finding articles in StudyNotes relating to Software Lagrangian and Least Action Principle, creating similar content, and relating it to 3E Framework, Epiplexity, Entropy, Magnitude, Digital Synesthesia, and Awareness of Opportunities.
- **Files created/modified:**
  - `docs/concepts/Least_Action_Principle.md` (new)
  - `docs/concepts/Software_Lagrangian.md` (new)
  - `docs/concepts/Epiplexity.md` (new)
  - `docs/concepts/Entropy.md` (new)
  - `docs/concepts/Magnitude.md` (new)
  - `docs/concepts/Awareness_of_Opportunities.md` (new)
  - `docs/concepts/Digital_Synesthesia.md` (modified)
  - `index.md` (modified)
- **Notes:** formulated the Software Lagrangian ($L_{\text{software}} = S_T - H_T$) and the Least Action Principle as the thermodynamic and variational engines of adaptive systems. Integrated these with the 3E Framework (Efficacy/Epiplexity, Efficiency/Entropy, Effectiveness/Magnitude), Digital Synesthesia (resonance/roughness as conscious agent perception kernels), and the Awareness of Opportunities (ABC cycle as Kleene fixed-point iteration over abstract domains).

