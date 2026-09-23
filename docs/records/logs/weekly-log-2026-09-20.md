---
title: 'Weekly Log (2026-09-20 to 2026-09-26)'
date: 2026-09-22
tags: [weekly-log, records, itdel, teaching, conversational-programming]
type: changelog
status: stable
liberal_art: Quadrivium-Music
---

# Weekly Log (2026-09-20 to 2026-09-26)

> Chronological record of agent operations during the week of 2026-09-20.

## [2026-09-22] ingest & ops | IT Del WhatsApp Project Submissions Pipeline

- **Trigger:** User at Institut Teknologi Del requested an incremental, lossless ingestion and showcase pipeline for ~50 students submitting project descriptions in a WhatsApp group chat (`Peserta Conversational Programming`).
- **Data Source:** Raw export zip `WhatsApp Chat - Peserta Conversational Programming.zip` in `Downloads`, archived immutably into `raw/transcripts/itdel_whatsapp/exports/export_2026-09-22_155610/`.
- **System Implemented:**
  - `src/sync_itdel_submissions.py`: Automated ingestion engine that locates the latest WhatsApp zip, unzips nested attachment archives (e.g. Nakula's 4 Markdown projects), normalizes headers, derives student NIM and Department (IF/SI/TE/MR), auto-categorizes projects into the 7 Liberal Arts per `AGENTS.md`, and merges follow-up links.
  - `docs/teaching/itdel_projects/projects/`: 12 verified project notes with full YAML frontmatter, objectives, and descriptions.
  - `docs/teaching/itdel_projects/students/`: 9 student profile pages grouping multi-project submissions.
  - `docs/teaching/itdel_projects/README.md`: Central Showcase Hub with live Dataview queries by category and delivery mode.
  - `docs/teaching/itdel_projects/chat_audit.md`: Lossless audit log evaluating all 34 chat messages to guarantee zero lost descriptions.
  - `docs/teaching/itdel_projects/missing_or_pending.md`: Action items and pre-formatted copy-paste WhatsApp reminder list for students pending GitHub/demo links.
- **Index Update:** Cataloged Showcase Hub in `index.md` under Teaching & curriculum.

## [2026-09-22] ingest & synthesis | IT Del & SUD Student Submissions Second Export Ingestion

- **Trigger:** Ingested new export `WhatsApp Chat - Peserta Conversational Programming (1).zip` (58 messages, 7 nested zip archives).
- **Achievements:**
  - Expanded catalog to **26 distinct students** across Institut Teknologi Del and SMA Unggul Del (SUD).
  - Cataloged **40 projects** spanning IoT & Hardware (ESP32/sensors), Interactive Games, Simulation & Telemetry, Educational Tools, and Productivity Tools.
  - Resolved multi-project nested archives with markdown indentation variations (Salsalina Enoli Ginting, Nakula Nathanael Gultom, Rahel Sendler Sianturi, Immanuel Siringoringo, Nathania Pelita Sitohang).
  - Updated Dataview dashboard at `docs/teaching/itdel_projects/README.md`, message audit log at `docs/teaching/itdel_projects/chat_audit.md`, and reminder list at `docs/teaching/itdel_projects/missing_or_pending.md`.

## [2026-09-22] ingest & synthesis | IT Del & SUD Third Export, English Translations & CSV Database

- **Trigger:** Ingested latest export `WhatsApp Chat - Peserta Conversational Programming (2).zip` (83 messages, historical cross-export retention).
- **Achievements:**
  - Implemented bilingual translation engine (`src/itdel_translations.py`) supplying authoritative English titles, descriptions, and objectives for all cataloged projects.
  - Implemented dual CSV exporters:
    - `docs/teaching/itdel_projects/student_projects.csv` (18 columns: Student Name, WhatsApp Handle, Phone Number, NIM, Department, School, Project Title ID/EN, Category, Liberal Art, Description ID/EN, Objective ID/EN, Demo URL, Repo URL, Status, Source Reference).
    - `docs/teaching/itdel_projects/student_summary.csv` (10 columns: Student Name, WhatsApp Handle, Phone Number, NIM, Department, School, Total Projects, Projects English Titles, Categories, Status).
  - Perfected multi-project splitting via uppercase title heading verification (`find_project_headings`), eliminating false positive splits on bulleted objectives (`Tujuan: 1. Melatih...`).
  - Successfully cataloged **29 verified students** and **57 distinct projects** (Briant Sinaga: 4, Wendy Simanjuntak: 7, Deddy Daniel Situmeang: 5, Nakula Nathanael Gultom: 4, Rahel Sendler Sianturi: 3, Salsalina Enoli Ginting: 2, Stephen Joy Marvel Simamora: 2, Mayrinkha Yosefine: 2, Claudia Calista Aprilliana Sinaga: 2, Grasela Siska Viktoria Samosir: 2, Honey Lumban Gaol: 2, Immanuel Siringoringo: 2, Nathania Pelita Sitohang: 2, Diva Aurel Anastacia Sirait: 2, Annisa Margareth Manalu: 2, etc.).
  - Re-generated central showcase hub (`docs/teaching/itdel_projects/README.md`), master matrix (`docs/teaching/itdel_projects/student_project_matrix.md`), lossless audit log (`docs/teaching/itdel_projects/chat_audit.md`), and WhatsApp reminders (`docs/teaching/itdel_projects/missing_or_pending.md`).
- **Follow-up Export Ingestion:** Ingested subsequent export `WhatsApp Chat - Peserta Conversational Programming (3).zip` archived to `raw/transcripts/itdel_whatsapp/exports/export_2026-09-22_174524/`; verified 100% data consistency across all 29 students and 57 projects.

## [2026-09-22] ops & synthesis | Consecutive Project Rows Matrix & Obsidian Pipe Escaping Fix

- **Trigger:** User reported Markdown table breakage in Obsidian (columns shifted due to unescaped `|` in wikilinks) and requested that same-person project rows appear consecutively next to each other with dual-language (ID/EN) descriptions.
- **Achievements:**
  - Implemented `format_table_cell()` in `src/sync_itdel_submissions.py` to escape all pipe characters (`\|`) in wikilinks (`[[target\|alias]]`) and convert multiline text to `<br>`.
  - Redesigned `docs/teaching/itdel_projects/student_project_matrix.md`:
    - **Section 1**: 57 consecutive individual project rows where multiple projects from the same student appear sequentially labeled `*(Project X/Total)*`, with both original Indonesian (`**ID**:`) and English (`**EN**:`) descriptions.
    - **Section 2**: 29 student summary rows providing high-level project counts and status.
  - Re-synchronized dual CSV files (`student_projects.csv` and `student_summary.csv`).
  - Created teamwork preview draft artifact (`prompt_draft.md`) for automated multi-agent workflow verification.

## [2026-09-23] synthesis | English Project Catalog & Comparative Topic Analysis

- **Trigger:** User requested a dedicated Markdown file compiling all 57 student projects one-by-one with English explanations and creator attribution, along with an overarching comparative analysis of topics, archetypes, and technologies created by the students.
- **Artifact Created:** `docs/teaching/itdel_projects/project_catalog_and_comparative_analysis.md` (63 KB).
- **Core Findings & Structural Breakdown:**
  - **Category Shares:** Interactive Games (32, 56.1%), Educational Tools (13, 22.8%), Web Applications (4, 7.0%), IoT & Hardware (4, 7.0%), Productivity Tools (2, 3.5%), Simulation & Telemetry (2, 3.5%).
  - **Six Functional Topic Clusters:** 3D WebGL / Canvas action games, Smart campus living & maintenance infrastructure, Syntax/language/medical EdTech, Math cognition & logic puzzles, Embedded IoT & Computer Vision, Macro/Micro ecological and national telemetry.
  - **Institutional Contrast:** IT Del students heavily focused on high-action 3D WebGL rendering, campus operational ticketing, and POS tools, while SMA Unggul Del students focused 100% on cognitive tools, developer utilities, and linguistic syntax engines.
  - **Departmental Flavor:** Informatika (IF) prioritized Three.js 3D graphics, OpenCV computer vision, and math puzzles; Sistem Informasi (SI) prioritized enterprise/campus workflows (FIDS, POS, dormitory ticketing, study desk booking, ride sharing).
- **Cross-References:** Cataloged in `index.md` and linked in `docs/teaching/itdel_projects/README.md`.


