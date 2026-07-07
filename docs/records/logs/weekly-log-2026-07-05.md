---
title: 'Weekly Log (2026-07-05 to 2026-07-11)'
date: 2026-07-05
tags: [weekly-log, records]
type: changelog
status: stable
liberal_art: Quadrivium-Music
---

# Weekly Log (2026-07-05 to 2026-07-11)

> Chronological record of agent operations during the week of 2026-07-05.

## [2026-07-07] plan | AI Hackathon Plan v2 (Pre-Requisite Gated)

- **Trigger:** user requested a new version of the AI hackathon plan that gates entry on a verified install list, so participants who show up without anything installed do not slow down the cohort.
- **Files created/modified:**
  - `docs/plans/ai_hackathon_plan.md` (new)
- **Decisions locked with user:**
  - Verification mechanism = **self-report form** (Google Form, paste `--version` outputs, trainer sheet auto-flags red for missing items).
  - Required install set = **Tier 1 + Tier 2 + Tier 5** from `docs/teaching/pre_workshop_install_list.md` (13 items: OpenCode, Ollama, Docker, Git, GitHub; ChatGPT, Custom GPT, Claude, OpenRouter, skills.sh, mcp.so; mem0 MCP, @playwright/mcp).
- **Notes:** v2 makes the install list a hard pre-flight gate — no install, no entry to the AI coding guide. Added Pre-Flight Setup Session (T-1 day) as triage for participants with ≥3 red flags. The 12 Session guides in `docs/records/` are referenced by name but flagged for separate cleanup (wrong location, inconsistent frontmatter, drift from v2 install assumptions). `pitch_10_minute.md` and `presentation_plan.md` still say "no install required" — must be updated before student-facing comms go out (reconciliation note already in `pre_workshop_install_list.md`).

## [2026-07-02] reorg | Dissolve koo_project/ folder (Zettelkasten)

- **Trigger:** continuation of the docs/ reorg — distribute 38 `docs/records/koo_project/` files by type per Zettelkasten principle (folders by type, tags by topic).
- **Files moved:** 38
  - 17 → `docs/concepts/` (harness-vs-model, inaai, pkc, rlhf, architecture, etc.)
  - 7 → `docs/principles/` (one-master-note, anti-patterns, positioning, etc.)
  - 12 → `docs/records/` (cover letters, job apps, company research, etc.)
  - 2 → `docs/sources/` (catalog + highlights)
- **Notes:** `koo-project` tag stays on each file marking origin without trapping it in a topic folder. Commit `0175ccb` pushed to main. docs/ now has 12 content dirs (was 26 at start of session).
