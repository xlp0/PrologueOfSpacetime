---
title: 'Wiki Page Templates'
date: 2026-06-26
tags: [Templates, Seven-Liberal-Arts]
type: overview
status: stable
liberal_art: Trivium-Grammar
---

# Wiki Page Templates

> Obsidian template files for each page type. Use the Templates plugin (hotkey: insert template) or copy manually. Each template enforces the [[AGENTS]] §4 frontmatter schema.

## Available templates

| Template | `type` | Use for | File |
|:---|:---|:---|:---|
| concept | `concept` | Foundational concept/entity pages | [[concept]] |
| principle | `principle` | Operational/architectural principles | [[principle]] |
| source | `source` | Generic source summary after ingest (§6.1) | [[source]] |
| video | `source` | YouTube video note (transcript + chapters + cover) | [[video]] |
| synthesis | `synthesis` | Query-that-became-a-page (§6.2) | [[synthesis]] |
| record | `changelog` | Meeting minutes, working notes | [[record]] |
| plan | `note` | Execution/operational plans | [[plan]] |
| chapter_topic | `concept` | Chapter deep-dive topic files | [[chapter_topic]] |
| teaching_chapter | `note` | Teaching/curriculum lesson chapters | [[teaching_chapter]] |
| presentation_marp | `note` | Marp slide decks (§8.2) | [[presentation_marp]] |

## Seven Liberal Arts tag mapping

Every page gets a `liberal_art` frontmatter field + matching tag. Pick the art that best fits the page's primary mode:

| Liberal Art | Tag | Mode | Example pages |
|:---|:---|:---|:---|
| Trivium — Grammar | `Trivium-Grammar` | Structure, rules, specs | k8s components, skills spec, CLM |
| Trivium — Logic | `Trivium-Logic` | Reasoning, verification, comparison | RAG vs wiki, prompt injection, harness thesis |
| Trivium — Rhetoric | `Trivium-Rhetoric` | Expression, persuasion, presentation | Presentation plans, agency product, packaging |
| Quadrivium — Arithmetic | `Quadrivium-Arithmetic` | Number, counting, cost, FLOPs | AI capex, token economics, benchmarks |
| Quadrivium — Geometry | `Quadrivium-Geometry` | Shape, space, architecture, graphs | Knowledge graphs, k8s architecture, vector retrieval |
| Quadrivium — Music | `Quadrivium-Music` | Rhythm, harmony, pipelines, flow | CI/CD pipelines, business-OS wiring, canary shifts |
| Quadrivium — Astronomy | `Quadrivium-Astronomy` | Motion, time, worlds, physical AI | World models, robotics, persistent memory, SSD streaming |

## How to use

1. **In Obsidian:** Settings → Templates → Template folder location = `docs/templates`. Bind "Insert template" to a hotkey (e.g. Cmd+T). Create a new note, hit the hotkey, pick a template.
2. **As the LLM:** when creating a new page, read the matching template first, then fill it in. Replace all `UPPERCASE` placeholders. Set `status: draft` initially; flip to `stable` after review.
3. **The `{{date}}` placeholder** is filled by Obsidian's Templates plugin automatically (uses the date format from Settings).
