---
title: 'Wiki Index'
date: 2026-06-26
type: overview
status: stable
---

# Wiki Index

> Catalog of every wiki page, grouped by category. The LLM updates this on every ingest (see [[AGENTS]] §5). Read this first when answering a query, then drill in. *First-pass index — summaries inferred from titles; refine during future ingests/lints.*

## Overview

- [[README|Prologue of Spacetime — README]] — top-level synthesis: the Unifying Namespace, HoTT grounding, D&D Representation Engine, 24/7 MLOps continuum. Start here.
- [[Document_Relationship_Map|Document Relationship Map]] — graph-theoretic + conceptual map of how every page relates: topology, hubs, orphan islands, dangling-link priorities, recommended reconnection actions.
- [[templates/README|Page Templates]] — 8 templates (concept, principle, source, synthesis, record, plan, chapter_topic, presentation_marp) for creating new wiki pages. Each enforces the AGENTS.md frontmatter schema + the seven liberal arts tag.
- [[CHANGELOG|Project Changelog]] — milestone releases, active sprint suite history, and architectural revisions.

## Foundational concepts (`docs/` root)
- [[docs/principles/Cordis_Spatiotemporal_Composability|Cordis: The Meta-Framework for Spatiotemporal Composability]] — architectural principle unifying spatial isolation (ctx.isolate, fiber tree) and temporal reversibility (LIFO DisposableList, HMR effect migration).
- [[docs/concepts/Perspective_and_Referential_Coordinates_in_Spacetime_Compositionality|Perspective and Referential Coordinates in Spacetime Compositionality]] — why multi-agent systems compose over tensorial invariants rather than frame chauvinism; 3+1 CLM decomposition ([L] space vs [T] time).
- [[docs/concepts/Knowledge_Is_Free_Judgment_Is_Not|Knowledge Is Free, But Judgment Is Not]] — player axiom and ethical mechanic: free commons knowledge ([L] space) vs. costly judgment ([V] → [T] space) revealing character color through Landauer dissipation and dynamic synesthetic aura.
- [[docs/concepts/Vibration_Perturbation_and_the_Energy_Cost_of_Coherence|Vibration, Perturbation, and the Energy Cost of Coherence]] — physical proto-agency (free will to jump between alternate realities) and the thermodynamic cost collective particles pay in energy to re-establish an order-preserving entry.

- [[The_Representation_Engine|The Representation Engine]] — D&D as iterative word-game loop; the Permutation Thesis (MCard → PCard → VCard → {P}C{Q} tiers).
- [[Representability|Representability]] — the mathematical limit of expression, characterizing objects by their measurable interactions (Yoneda Lemma).
- [[Making_Illegal_States_Unrepresentable|Making Illegal States Unrepresentable]] — type-driven design principle enforcing compile-time correctness by preventing invalid states.
- [[MCard]] · [[PCard]] · [[VCard]] — the MVP Cards triad: Monadic Card (data, Σ-type) · Polynomial Functor Card (computation, Π-type) · Verification Card (boundary, Id-type). See [[MVP Cards Design Rationale]] for the full foundation.
- [[DM_as_Maxwells_Demon|DM as Maxwell's Demon]] — structural isomorphism between the Dungeon Master and Maxwell's Demon (Landauer, Szilard, entropy, Epiplexity).
- [[Monadic Composition - The Algebra of Types|Monadic Composition]] — monads as the algebra of composable types.
- [[hott_ssot_reference|HoTT SSOT Reference]] — Homotopy Type Theory as the single-source-of-truth grounding.
- [[Prologue_Conceptual_Digest|Prologue Conceptual Digest]] — compact digest of core concepts.
- [[Digital_Synesthesia|Digital Synesthesia]] — cross-sensory representation.
- [[Least_Action_Principle|Least Action Principle]] — optimization rule selecting paths (geodesics) that minimize computational action.
- [[Software_Lagrangian|Software Lagrangian]] — real-time thermodynamic metric ($L_{\text{software}} = S_T - H_T$) governing software abstraction quality.
- [[Epiplexity|Epiplexity]] — metric of the structural, learnable information ($S_T$) extractable by a bounded observer.
- [[Entropy|Entropy]] — metric of expressive freedom, alternative states, and uncompressed noise ($H_T$).
- [[Magnitude|Magnitude]] — numerical invariant of enriched categories measuring relational size and diversity ($|X| = \mathbf{1}^{\top} Z^{-1} \mathbf{1}$).
- [[Awareness_of_Opportunities|Awareness of Opportunities]] — continuous learning loop governed by the ABC cycle in response to entropic space expansion.
- [[Godel_Machine|Gödel Machine]] — theoretical self-referential computer architecture capable of mathematically proving beneficial code modifications.
- [[Red_Queen_Godel_Machine|Red Queen Gödel Machine]] — co-evolutionary framework for recursive self-improvement where agents and evaluators adapt in lockstep.
- [[Local-First|Local-First]] and [[The Local-First Software Paradigm Architecture, Developer Experience, and User Agency|Local-First Paradigm (full)]] — data sovereignty and user agency.
- [[SpacetimeDB_Overview|SpacetimeDB Overview]] and [[SpacetimeDB_Integrations|SpacetimeDB Integrations]] — SpacetimeDB as the reactive DB substrate.
- [[PKC_ZITADEL_Game_Board_Planning|PKC ZITADEL Game Board]] — identity/game-board planning.
- [[The Five Dining Philosophers|Five Dining Philosophers]] — concurrency parable mapped to the system.
- [[Observability - Living Spaces|Observability: Living Spaces]] and [[Reliability - Continuous Presence Practices|Reliability: Continuous Presence]] — ops principles.
- [[Residential_Power_Setup_Budget|Residential Power Setup Budget]] — power budget for the hardware footprint.

### Board games (representation microcosms)

- [[Board_Games_Compendium|Compendium]] — [[Board_Game_Chess|Chess]] · [[Board_Game_Go|Go]] · [[Board_Game_Catan|Catan]] · [[Board_Game_Risk|Risk]] · [[Board_Game_Pandemic|Pandemic]] · [[Board_Game_Backgammon|Backgammon]]
- Long-form docs: [[CHESS_GAME_DOCUMENTATION|Chess]] · [[GO_GAME_DOCUMENTATION|Go]] · [[MONOPOLY_GAME_DOCUMENTATION|Monopoly]] · [[Monopoly Game Board PKC story|Monopoly PKC story]]

## Source summaries (`type: source`)
- [[docs/sources/Dialect_Relativity_Unification_Electricity_Magnetism|Dialect — Relativity's Unification of Electricity and Magnetism is Pure Mathematical Fiction]] — deconstructs Purcell/Feynman reduction of magnetism to electrostatics; proves tensorial invariants and perspective define relativistic fields.

- [[deep_learning_and_physics_video_note|Deep Learning & Physics — video note]] — source: `raw/transcripts/deep_learning_and_physics_transcript.txt`. Renormalization ↔ MERA ↔ deep nets; multiscale compression as the shared strategy of physics and AI.
- *Pending source pages for the 5 PDFs in `raw/articles/` (Prologue_of_Spacetime_introduction, Cognitive_Ascent_Mission_Guide, Engineering_Awe_A_Scale-Free_Architecture, Life_Mind_Machine_Stability, The_Mirror_and_the_Algorithm).*

## The 12-chapter matrix (`chapters/`)

Each chapter has a `README` (overview) and an `MVP_The_*` (minimum viable prototype), plus topic files. Chapter 1 also hosts a HoTT math course.

- [[00_Structure_and_Vision|Ch 0 — Structure and Vision]] — the Brain Factory, HoTT, Cubical Logic Model, Reverse Trivium. The architectural keystone.
- [[chapters/01_The_Value_of_Counting/README|Ch 1 — The Value of Counting]] · [[chapters/01_The_Value_of_Counting/MVP_The_Counter|MVP: The Counter]] · HoTT math course (6 lessons under `HoTT_Math_Course/`: Universes & Functions, Propositions as Types, Universal Quantifiers, Products, Coproducts).
- [[chapters/02_The_Meaning_of_Shape/README|Ch 2 — Meaning of Shape]] · [[chapters/02_The_Meaning_of_Shape/MVP_The_Shape|MVP: The Shape]] · depth_sensing_kinect, geometry_analytics, topology_printing.
- [[chapters/03_The_Power_of_Rhythm/README|Ch 3 — Power of Rhythm]] · [[chapters/03_The_Power_of_Rhythm/MVP_The_Rhythm|MVP: The Rhythm]] · sonic_synchronization.
- [[chapters/04_The_Truth_of_Observation/README|Ch 4 — Truth of Observation]] · [[chapters/04_The_Truth_of_Observation/MVP_The_Observer|MVP: The Observer]] · drone_explorer, automated_collection, continuous_monitoring, edge_observation_architecture, grafana_dashboard, local_first_sovereignty.
- [[chapters/05_Resource_Allocation/README|Ch 5 — Resource Allocation]] · [[chapters/05_Resource_Allocation/MVP_The_Allocator|MVP: The Allocator]] · token_mechanics, engram_memory, iot_motor_control, nitinol_vr_goggles.
- [[chapters/06_Network_Pathfinding/README|Ch 6 — Network Pathfinding]] · [[chapters/06_Network_Pathfinding/MVP_The_Navigator|MVP: The Navigator]] · vpn_mesh_network, agent_patterns.
- [[chapters/07_Temporal_Causality/README|Ch 7 — Temporal Causality]] · [[chapters/07_Temporal_Causality/MVP_The_Historian|MVP: The Historian]] · mqtt_event_bus, high_availability, backup_recovery.
- [[chapters/08_Orbit_Prediction/README|Ch 8 — Orbit Prediction]] · [[chapters/08_Orbit_Prediction/MVP_The_Predictor|MVP: The Predictor]] · openclaw_skills.
- [[chapters/09_Counting_Water/README|Ch 9 — Counting Water]] · [[chapters/09_Counting_Water/MVP_The_Water_Count|MVP: The Water Count]].
- [[chapters/10_Rice_Terrace_Topology/README|Ch 10 — Rice Terrace Topology]] · [[chapters/10_Rice_Terrace_Topology/MVP_The_Topology|MVP: The Topology]].
- [[chapters/11_Ceremonial_Beats/README|Ch 11 — Ceremonial Beats]] · [[chapters/11_Ceremonial_Beats/MVP_The_Ceremony|MVP: The Ceremony]].
- [[chapters/12_Calendar_Coordination/README|Ch 12 — Calendar Coordination]] · [[chapters/12_Calendar_Coordination/MVP_The_Calendar|MVP: The Calendar]] · digital_sundial (see also `raw/assets/3dmodels/DigitalSundial.scad`).
- [[Brain_Factory_Implementation_Case_Study|Brain Factory Case Study]] and [[Strategic_Validation_Reverse_Mathematics_of_the_Brain_Factory|Strategic Validation (reverse math)]] — cross-chapter syntheses.

## Improvement concepts (`docs/prologue_of_spacetime_improvement/`)

- [[Trivium|Trivium]] and [[Quadrivium|Quadrivium]] — the classical frameworks; [[Trivium x Quadrivium Framework for ABC Curriculum|their cross product]] structures the 12-chapter matrix.
- [[Type Theory|Type Theory]] · [[Homotopy Type Theory Explained|HoTT Explained]] · [[Cubical Logic Model|Cubical Logic Model]] · [[Universality|Universality]] · [[Modularity|Modularity]].
- [[Single-source of Truth|Single-source of Truth]] · [[Local-first Principle|Local-first Principle]].
- [[GASing|GASing]] · [[EEAO|EEAO]] · [[Agentic Trinitarianism|Agentic Trinitarianism]] · [[Science of Governance|Science of Governance]].
- [[Pentadic Improvement Plan for Prologue of Spacetime|Pentadic Improvement Plan]] — overall roadmap.
- [[Pancasila_and_the_Five_WH|Pancasila and the Five-WH]] — mapping the 5-WH inquiry questions to Indonesian Pancasila; both as instances of the Pentadic Threshold.

## Narrative (`docs/narrative/`)
- [[docs/narrative/Prologue_of_Spacetime_Master_Document|Prologue of Spacetime Master Document]] — comprehensive master narrative of the meta-game, Tri Hita Karana causal networks, and the 12-chapter matrix.
- [[docs/narrative/Prologue_of_Spacetime_Ludic_Architecture_and_Synesthetic_Game_Sprints|Prologue of Spacetime: Ludic Architecture and Synesthetic Game Sprints]] — grand strategy game design, four civilizational epochs, dual-type skill lattice, and synesthetic type hierarchy.

- [[Combinatorial Species|Combinatorial Species]] and [[Combinatorial Species Catalog|Species Catalog]] — the combinatorial bestiary.
- [[Function-Number Duality|Function-Number Duality]] · [[Lambda Calculus and the Three Foundational Metrics of Representables|Lambda Calculus & 3 Metrics]] · [[Symmetry|Symmetry]] · [[Judgment|Judgment]] · [[Why Three|Why Three]] · [[TAME|TAME]].
- [[Digital Scope|Digital Scope]] · [[digital_synesthesia|digital synesthesia (narrative)]] · [[digital_synesthesia_convergence|synesthesia convergence]].
- [[Science of Approximation|Science of Approximation]] · [[Sovereign Truth and Sustainable Swarms|Sovereign Truth & Sustainable Swarms]].
- [[PKC as an Autonomous Mesh Network|PKC as Autonomous Mesh]] · [[PTR|PTR]] · [[REPL|REPL]] · [[MVP Cards Design Rationale|MVP Cards Rationale]].
- [[why_linguists|why linguists]] · [[xiao_yao_you|xiao yao you]].

## Active Sprints (`docs/sprints/_active/`)

- [[docs/sprints/_active/README|Active Sprints Workspace Overview]] — cockpit and status matrix for the civilizational strategy game sprint suite.
- [[docs/sprints/_active/SPRINT-00-MASTER-ORCHESTRATION|Sprint 00: Master Orchestration Plan]] — civilizational strategy game, synesthetic type lattice, and Tri Hita Karana synthesis.
- **Epoch I: The Primordial Sensorium (Why / Rhetoric Era)**
  - [[docs/sprints/_active/SPRINT-01-GRANULAR-TIDEPOOL|Sprint 01: The Granular Tidepool]] — discrete bitstream sieving, Shannon entropy, auditory pulse train.
  - [[docs/sprints/_active/SPRINT-02-TOPOGRAPHIC-CELL-WALL|Sprint 02: The Topographic Cell Wall]] — geometric membrane enclosure, Gauss-Bonnet curvature, topological parallax.
  - [[docs/sprints/_active/SPRINT-03-HARMONIC-SWARM|Sprint 03: The Harmonic Swarm]] — rhythmic cadence locking, Kuramoto phase order, harmonic dissonance perception.
  - [[docs/sprints/_active/SPRINT-04-HORIZON-OF-CONSENSUS|Sprint 04: The Horizon of Consensus]] — multi-observer parallax triangulation, Huber loss, spectral coherence.
- **Epoch II: The Sovereign Tribal Mesh (What / Logic Era)**
  - [[docs/sprints/_active/SPRINT-05-YONEDA-BAZAAR|Sprint 05: The Yoneda Bazaar]] — dual-category resource allocation, Yoneda test probes, thermal haptic feedback.
  - [[docs/sprints/_active/SPRINT-06-SUBAK-MESHWAY|Sprint 06: The Subak Meshway]] — topological Reticulum routing, max-flow min-cut, fluidic vector streams.
  - [[docs/sprints/_active/SPRINT-07-CAUSAL-MONAD-FORGE|Sprint 07: The Causal Monad Forge]] — Petri net place-transitions, non-commutative causality, phosphorescent causal trails.
  - [[docs/sprints/_active/SPRINT-08-ASTRODYNAMIC-NEXUS|Sprint 08: The Astrodynamic Nexus]] — Socratic forward simulation, Lyapunov exponents, attractor manifold holography.
- **Epoch III: The Sheaf Metamaterial (How / Grammar Era)**
  - [[docs/sprints/_active/SPRINT-09-HYDRAULIC-VAULT|Sprint 09: The Hydraulic Vault]] — typed micro-measurement, algebraic sum/product types, crystalline lattice sight.
  - [[docs/sprints/_active/SPRINT-10-RICE-TERRACE-SHEAF|Sprint 10: The Rice Terrace Sheaf]] — topographic sheaf gluing, vanishing Čech cohomology H¹ = 0, zero-shear manifold vision.
  - [[docs/sprints/_active/SPRINT-11-ZERO-QUEUE-CEREMONY|Sprint 11: The Zero-Queue Ceremony]] — Kotekan interlocking rhythms, Little's Law collapse W_q ≡ 0, acoustic strobe resonance.
- **Epoch IV: The Planetary Noosphere (Transcendent Era / Synthesis)**
  - [[docs/sprints/_active/SPRINT-12-IMPLEDICATIVE-CALENDAR|Sprint 12: The Impredicative Calendar]] — Tri Hita Karana planetary synthesis, Software Lagrangian, universal noospheric synesthesia.
- **Algebra of Systems (AoS) Reorganization Suite**
  - [[docs/sprints/_active/SPRINT-AOS-01-CONTENT-INVENTORY|Sprint AoS-01: Content Inventory & Topic Taxonomy]]
  - [[docs/sprints/_active/SPRINT-AOS-02-MATHEMATICAL-FORMALIZATION|Sprint AoS-02: Mathematical Formalization & Rank-Nullity]]
  - [[docs/sprints/_active/SPRINT-AOS-03-MODULARITY-AND-DECOUPLING|Sprint AoS-03: Modularity, Decoupling & Independence Axiom]]
  - [[docs/sprints/_active/SPRINT-AOS-04-CROSS-DOMAIN-SYNTHESIS|Sprint AoS-04: Cross-Domain Synthesis & Real Options]]
  - [[docs/sprints/_active/SPRINT-AOS-05-VERIFICATION-AND-QA|Sprint AoS-05: Verification & Zero-Loss QA]]
  - [[docs/sprints/_active/SPRINT-AOS-06-CONTINUOUS-FILTRATION|Sprint AoS-06: Continuous Filtration & Loopback Mechanics]]

## Game design (`docs/game_design/`, `docs/gameboard/`)

- [[game_board_concept_and_story|Game board concept & story]] · [[story_chapters_overview|Story chapters overview]] · [[game_board_based_learning|Game-board-based learning]] · [[blindsight_integration|Blindsight integration]] · [[presentation_he_mengxin|Presentation: He Mengxin]].
- [[Board_Games_as_Pedagogical_Engines|Board Games as Pedagogical Engines]].

## People (`docs/people/`)

- [[felix_mesak|Felix Mesak]] — contributor profile.

## Workflows (`docs/workflows/`)

- [[consensus_constitution|Consensus Constitution]] · [[execution_strategy|Execution Strategy]] · [[requirements_analysis|Requirements Analysis]] · [[inventory_management|Inventory Management]] · [[mcp_skill_registry|MCP Skill Registry]] · [[openclaw_local_memory_setup|OpenClaw Local Memory Setup]].

## Teaching & curriculum

- [[abc_curriculum|ABC Curriculum]] and [[requirements|Requirements]] — top-level curriculum + requirements.
- [[ai_coding_guide/README|AI Coding Guide]] (13 lessons: what AI coding is → how tools work → the stack → tokens/context → prompting → context engineering → MCP → agent skills → agentic workflows → the tools → code of conduct → glossary → further reading). Mirrored at [[docs/teaching/handbook/README|docs/teaching/handbook]] (14 lessons, adds concrete examples).
- [[docs/teaching/sprint_outline|Teaching sprint outline]] · [[docs/teaching/presentation_plan|Teaching presentation plan]].
- [[docs/teaching/installing_google_workspace_mcp|Installing the Google Workspace MCP Server]] — reproducible setup guide for wiring `taylorwilsdon/google_workspace_mcp` into OpenCode (OAuth client, API enablement, env vars, opencode.json, first-call consent).
- [[docs/teaching/prologue_of_spacetime_overview_slides|Prologue of Spacetime — Wiki Overview (Marp)]] — slide deck tour: three layers, directory layout, CLM, HoTT, Representation Engine, 12-chapter matrix, operations, tooling.
- [[docs/teaching/observations/not_aware_of_opportunities|Not Aware of Opportunities]] — teaching observation: students consistently fail to recognize and act on imminent, trivially accessible opportunities (buying paper/tape, using calendars, organizing Lego components). Root-cause analysis traces this to conventional education suppressing agency and local resourcefulness.
- [[docs/teaching/itdel_projects/README|IT Del & SUD Student Projects Showcase Hub]] — live catalog and Dataview matrix of 57 student projects from 29 students across Institut Teknologi Del and SMA Unggul Del (Conversational Programming & AI Systems Workshop), tracking simulations, games, IoT/hardware, and educational tools with bilingual (ID/EN) metadata, dual CSV database exports, lossless chat audit, and reminder tracking.
- [[docs/teaching/itdel_projects/student_project_matrix|IT Del & SUD Student Project Matrix]] — comprehensive student-centric matrix categorizing 57 projects across 29 students by Creator, WhatsApp Handle/Phone, NIM/School, Project Type, and Title (Indonesian & English).
- [[docs/teaching/itdel_projects/project_catalog_and_comparative_analysis|IT Del & SUD Project Catalog & Topic Analysis]] — comprehensive one-by-one English project descriptions, architectural profiles, and comparative domain analysis across 6 topic clusters, schools, departments, and 7 Liberal Arts.
- [[docs/teaching/itdel_projects/games_and_educational_tools_catalogs|IT Del & SUD Games & Educational Catalogs]] — specialized two-part catalog grouping all 34 interactive games (across 7 genres) and 27 educational platforms (across 6 learning domains) with English mechanics, pedagogy, and creator attribution.
- [[docs/records/Session 1 Team Formation Activity Guide|BBS Activities]] — 12-session Bootcamp/Build/Showcase guides (Sessions 1–12).
- [[docs/records/TODO_story_chapters|TODO: story chapters]] · [[docs/records/TODO_strategy|TODO: strategy]].
- [[docs/plans/clm_problem_model|CLM problem model]] (visual).

## Hardware (`hardware/`)

Reference pages per device: [[hardware/drone/README|drone]] · [[hardware/edge_compute/README|edge_compute]] · [[hardware/ip_camera/README|ip_camera]] · [[hardware/oscilloscope/README|oscilloscope]] · [[hardware/telescope/README|telescope]] · [[hardware/vr_lenses/README|vr_lenses]] · [[hardware/turbine/README|turbine]] (+ site_inspection_*, existing_plant_knowledge) · [[hardware/toycar/planning|toycar]] (+ solar_rc_toy_car_chassis) · [[hardware/microscope/medical_device_spec|microscope]] · [[hardware/lidar/hardware_explanation|lidar]] (+ esp32_lidar_wiring_guide, shopper_analytics_lidar).

### Edge / shopper-analytics subsystem (`docs/shopper_analytics/`)

~20 pages on the shopper-analytics edge pipeline: hardware specs (hikvision_ds2CD2021g1, spc_bc1_3mp), kinect/lidar compute, NVIDIA Jetson AGX cost, docker setup, edge_compute_strategy, pipeline 8080, system operations, network access, toy-car build. Start at [[docs/shopper_analytics/README|its README]].

## Operations & records

- **Changelog + Update history** (`docs/records/`) — weekly entries 2025-11-30 → 2026-06-28 plus update history. Latest weekly: [[docs/records/weekly-2026-06-28|weekly-2026-06-28]].
- [[docs/records/logs/README|Wiki Log Index]] — index of weekly agent operation logs (setup, syntheses, reorgs, lints).
- [[docs/records/WorkingNotes_Content_Summary_2026-02-07|Working notes summary 2026-02-07]].
- [[docs/records/MoM - 17 March 2026|MoM 17 Mar 2026]] · [[docs/records/MoM PKC - 17 March 2026|MoM PKC 17 Mar 2026]] — meeting minutes.
- [[docs/plans/EXECUTION_PLAN|EXECUTION_PLAN]] · [[docs/plans/B200_24x7_OPERATIONAL_PLAN|B200 24x7 Operational Plan]] · [[docs/plans/duwei_workshop_plan|Duwei workshop plan]].
- [[docs/plans/ai_hackathon_plan|AI Hackathon Plan v2]] — pre-requisite-gated (Tier 1+2+5 install list, self-report form, Pre-Flight triage session).
- Kubernetes: [[docs/plans/github_actions_migration_strategy|GitHub Actions migration]] · [[docs/plans/minipc_network_flapping_resolution|minipc network flapping]].
- [[docs/plans/utm-macstudio-installation|Mac Studio UTM install]] · [[docs/plans/utm-macstudio-kubernetes-setup|Mac Studio k8s setup]].

## Demos & presentations

- [[docs/plans/presentation_plan|Presentation plan]] + `run_presentation.sh` (Marp).
- [[docs/demos/slide6_astrobiology_manifest|Slide 6: Astrobiology Manifest]] · [[docs/demos/slide7_grafana_heartbeat|Slide 7: Grafana Heartbeat]].
- [[docs/plans/rubik_3x3_program|Rubik 3x3 challenge]] · [[docs/plans/plan|Arduino Micro Quadruped]].

---

*Not catalogued above (intentionally): the `docs/mcard_studio/Public/` tree holds published snapshot copies of chapter content — do not edit as primary; keep in sync on path changes. `docs/Fleeting/` holds transient notes. See [[AGENTS]] §7 for cross-reference hygiene.*
