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

## [2026-07-07] plan | Background Concepts section (harness, skills, OKF)

- **Trigger:** user requested basic information about skills, harness, and OKF added to the install list, plus push to remote.
- **Clarification:** user clarified "OKF" means **Open Knowledge Foundation** (UK nonprofit, open knowledge standards) — not a Google product. Documented accurately as the standards body above the technical install layer.
- **Files modified:**
  - `docs/teaching/pre_workshop_install_list.md` — added new "Background Concepts" section between the intro and Installation Order, covering:
    - **Harness** — what an AI coding harness is, comparison table (OpenCode / Claude Code / Cursor / Codex / Aider), workshop standardizes on OpenCode.
    - **Skills** — what a `SKILL.md` is, locations (`.agents/skills/`), marketplaces (skills.sh, mcp.so), examples (caveman, baoyu-youtube-transcript, youtube-video-analyst), and the distinction between skills (shape agent behavior) vs MCP servers (expose external capabilities).
    - **OKF** — Open Knowledge Foundation definition, Open Definition, CKAN, Frictionless Data, Open Knowledge Network; framed as the standards layer above the install choices. Noted that the PrologueOfSpacetime wiki is an open knowledge artifact under OKF's definition.
    - Added stub note: dedicated concept pages `[[Harness]]`, `[[Skills]]`, `[[Open_Knowledge_Foundation]]` should be filed under `docs/concepts/` when this section grows.

## [2026-07-07] plan | Restructure install list — OpenCode-first flow

- **Trigger:** user reframed the install philosophy — OpenCode is the foundation. Students install OpenCode first, grant it machine access, then OpenCode itself assists with installing everything else. Only a few items stay manual (browser OAuth, network joins, GUI app setup).
- **Files modified:**
  - `docs/teaching/pre_workshop_install_list.md`
    - Added new "Installation Order — OpenCode is the foundation" section at the top, with 6 phases:
      - Phase 0 — Manual prerequisites (admin access, shell, browser, git)
      - Phase 1 — Install OpenCode FIRST (the foundation)
      - Phase 2 — Grant OpenCode machine access (filesystem, bash, external directory)
      - Phase 3 — OpenCode assists with the rest (agent-driven install of Ollama, Docker, ZeroTier, Netbird, Hermes, MCP servers, skills, languages)
      - Phase 4 — Manual verification items (Google OAuth browser consent, ZeroTier network join, Netbird login, GitHub account, Obsidian vault/plugin)
      - Phase 5 — Smoke test (5 end-to-end checks the student asks OpenCode to run)
    - Updated "How to read this list" intro to point at the Installation Order section first.
  - `docs/teaching/local_model_demo_setup.md` §4 — restructured the pre-install checklist to match the same 6-phase flow (4.1 prerequisites → 4.2 OpenCode first → 4.3 grant machine access → 4.4 OpenCode-assisted → 4.5 manual verification → 4.6 smoke test).
- **Design principle:** OpenCode is the startup foundation. The student delegates the install to the agent they're installing, after explicitly granting it machine access. The doc is shaped so OpenCode itself can read it and drive the install for the student. Manual items are limited to: browser-based OAuth/account flows, GUI-app vault creation, and network-ID joins.

## [2026-07-07] plan | Pre-workshop install list revision (definitive checklist)

- **Trigger:** user wants the install list to be the definitive pre-workshop checklist — every student arrives with OpenCode + everything they need. Explicitly added ZeroTier, Netbird, and Hermes; removed nginx and similar heavy infra students won't touch.
- **Files modified:**
  - `docs/teaching/pre_workshop_install_list.md`
    - Tier 8 renamed "Networking & Container Runtime" — removed Kubernetes stack (kubeadm/kubelet/kubectl/containerd/etcd), ArgoCD/Argo Rollouts, GitHub Actions + ARC, nginx, UTM, MediaWiki, MariaDB, Matomo, Ansible, Tailscale, Cloudflare Tunnel. Kept Docker. Kept ZeroTier [INSTALL]. Added Netbird [INSTALL] (WireGuard mesh, self-hostable, peer-to-peer agent demos).
    - Tier 3: Hermes promoted from [DISCUSSED] → [INSTALL] (students will work with it as the 24/7 agent reference architecture).
    - Added "2026-07-07 revision" note at top: this is now the definitive pre-workshop install checklist.
    - Reconciliation note strengthened: pitch_10_minute.md + presentation_plan.md "no install required" claim is now **superseded** — must be updated before student-facing comms go out.
    - Added Related section cross-links to [[local_model_demo_setup]] and [[installing_google_workspace_mcp]].
  - `docs/teaching/local_model_demo_setup.md` §4 pre-install checklist — added ZeroTier, Netbird, Hermes rows + a pointer to the full [[pre_workshop_install_list]].
- **Notes:** the browser-based pitch still works as the *opening* pitch, but the hands-on day now has a real pre-install gate. The AI Hackathon Plan v2 (same week) already had a pre-requisite-gated design — this revision aligns the master install list with that gate. Removed infra (K8s/ArgoCD/nginx/etc.) is still documented in `docs/plans/utm-macstudio-kubernetes-setup.md` and related pages for the post-workshop advanced track.

## [2026-07-07] plan | Google Workspace MCP install + wiki overview slideshow

- **Trigger:** user installed `taylorwilsdon/google_workspace_mcp` as an OpenCode MCP server and asked for (a) a reproducible setup guide so others can replicate the install, and (b) a Marp slideshow overview of the wiki.
- **Setup performed (verified working):**
  - Created Google Cloud OAuth Desktop client `teachers`; enabled Gmail/Drive/Calendar/Docs/Sheets/Slides/Forms/Tasks/Contacts/Chat/Apps Script/Custom Search APIs; published the consent screen.
  - Exported `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, `OAUTHLIB_INSECURE_TRANSPORT=1` to `~/.zshrc`.
  - Added `google-workspace` MCP entry to `~/.config/opencode/opencode.json` (`uvx workspace-mcp --tool-tier core`, env via `{env:VAR}` interpolation).
  - Hardened repo `.gitignore` to block `.env*`, `client_secret*.json`, `credentials*.json`, `oauth*.json`, `*.pem`, `*.key`, `.google_workspace_mcp/`, `.workspace-mcp/` defensively (no secrets were ever tracked).
  - First authenticated tool call: `google-workspace_list_calendars` for `henrykoo1230@gmail.com` → returned 8 calendars. Tokens cached at `~/.google_workspace_mcp/credentials/`.
- **Files created:**
  - `docs/teaching/installing_google_workspace_mcp.md` (new, `type: note`, `liberal_art: Trivium-Grammar`) — 6-phase setup guide with prerequisites, troubleshooting, security notes, timeline.
  - `docs/teaching/prologue_of_spacetime_overview_slides.md` (new, Marp, `type: note`, `liberal_art: Trivium-Rhetoric`) — ~15-slide deck: three layers, directory layout, CLM, HoTT, Representation Engine, 12-chapter matrix, operations, tooling, liberal-arts mapping, how to contribute.
- **Files modified:**
  - `.gitignore` (added secrets block)
  - `index.md` (added both new pages to the Teaching & curriculum section)
- **Notes:** slideshow is `status: draft` pending user review/tweaks; setup guide is `status: stable` (verified procedure). Slides render via Marp (`run_presentation.sh` or any Marp CLI/preview). Slideshow cites [[README]], [[AGENTS]], [[index]] as primary sources.

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
