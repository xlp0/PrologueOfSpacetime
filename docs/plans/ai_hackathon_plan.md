---
title: 'AI Hackathon Plan (v2 — Pre-Requisite Gated)'
date: 2026-07-07
tags: [Hackathon, AI-Coding-Guide, Pre-Requisites, Plan, Seven-Liberal-Arts]
type: note
sources: [docs/teaching/pre_workshop_install_list.md, docs/teaching/sprint_outline.md, docs/teaching/ai_coding_guide/README.md]
status: draft
liberal_art: Trivium-Rhetoric
---

# AI Hackathon Plan (v2 — Pre-Requisite Gated)

> A 12-session AI coding hackathon where entry is **gated on a verified install list** — participants who show up without the stack do not slow down the cohort.

## Why this version (v2)

The original sprint outline (`docs/teaching/sprint_outline.md`) and the 12 Session guides in `docs/records/` assume participants arrive with a working browser + ChatGPT. In practice, every cohort loses Day 1 to "I haven't installed anything." v2 makes the install list a **hard pre-flight gate**: no install, no entry to the AI coding guide. The cohort starts Day 1 already able to run `opencode`, hit an MCP server, and call an agent skill.

## Pre-Requisites (HARD GATE)

Every participant must complete the **Pre-Flight Install Checklist** (13 items below) and submit the **Pre-Flight Self-Report Form** at least 72 hours before Session 1. The form is reviewed by trainers; anyone with red flags is routed to the **Pre-Flight Setup Session** (see §Triage).

### Required install set (Tier 1 + Tier 2 + Tier 5)

Source: `docs/teaching/pre_workshop_install_list.md`. Henry has confirmed this scope (2026-07-07).

#### Tier 1 — Core install (5)

| # | Tool | Verification command | Account? |
|:--|:--|:--|:--|
| 1 | OpenCode | `opencode --version` | — |
| 2 | Ollama | `ollama --version` | — |
| 3 | Docker Desktop | `docker --version` | — |
| 4 | Git | `git --version` | — |
| 5 | GitHub account | paste profile URL | yes |

#### Tier 2 — Cloud AI services (6)

| # | Service | Verification | Account? |
|:--|:--|:--|:--|
| 6 | ChatGPT | paste profile URL | yes |
| 7 | Custom GPT (any one) | paste Custom GPT URL | yes |
| 8 | Claude (Anthropic) | paste profile URL | yes |
| 9 | OpenRouter | paste API key masked as `sk-or-***` | yes |
| 10 | skills.sh | paste profile URL | yes |
| 11 | mcp.so | paste profile URL | yes |

#### Tier 5 — MCP servers (2)

| # | MCP server | Verification |
|:--|:--|:--|
| 12 | mem0 MCP | `docker ps \| grep mem0` (running) |
| 13 | @playwright/mcp | `npx @playwright/mcp --version` |

### Pre-Flight Self-Report Form (Google Form)

One form per participant. Trainer-facing sheet auto-flags red for missing or malformed entries.

| Field | Type | Red flag if |
|:--|:--|:--|
| Full name | text | empty |
| Email | text | empty / not matching domain |
| Tool 1..5 `--version` output | paragraph | empty or "command not found" |
| GitHub profile URL | URL | 404 or no repositories |
| ChatGPT / Claude / OpenRouter / skills.sh / mcp.so URLs | URL | each not resolving |
| OpenRouter API key (masked) | text | not starting `sk-or-` |
| mem0 container running | boolean | false |
| `@playwright/mcp --version` output | paragraph | empty |
| Operating system | dropdown | — |
| Hardware specs (RAM, GPU) | text | <16GB RAM flagged for review |
| Self-rated confidence (1–5) | scale | 1 = no problem; we triage anyway |

### Trainer dashboard

- Google Sheet linked to the form.
- One row per participant. One column per item, colored green/red.
- **Cohort red count** = total red cells across all participants. Trainers review reds 48h before Session 1.
- Anyone with ≥3 red flags is auto-routed to Pre-Flight Setup Session.

## Triage: Pre-Flight Setup Session

A 2-hour session **the day before Session 1**, run in parallel to cohort onboarding.

- **Audience:** anyone with ≥3 red flags on the self-report form, OR anyone who did not submit the form.
- **Format:** bring-your-own-laptop clinic. Trainers walk the room with the install checklist. Each participant leaves green on all 13 items, or is moved to **audit mode** (see below).
- **Hard rule:** participants who cannot complete the install by end of Pre-Flight Session do **not** join a hackathon team. They audit the sessions (watch + take notes) and may join the next cohort. Rationale: a single unprepared teammate derails a 5-person team for the entire week.

## The 12 Sessions (structure preserved from v1)

The existing Session guides in `docs/records/` (`Session 1` through `Session 12`) define the curriculum. They are **slated for cleanup** (the user has flagged this as a follow-up task — wrong location, inconsistent frontmatter, drift from v2 install assumptions). For now, v2 references them by name and notes what changes.

| Session | Title | v2 delta |
|:--|:--|:--|
| 1 | Team Formation | Install verification moved OUT to Pre-Flight. Session 1 can start at full strength. |
| 2 | PKC Deployment | Now possible Day 1 — Docker is pre-installed. |
| 3 | BMAD Method | No change. |
| 4 | GitHub & Project Planning | GitHub account already exists. |
| 5 | IoT Conversational Interfaces | @playwright/mcp pre-installed. |
| 6 | IoT-PKC Integration | mem0 stack already running. |
| 7–9 | Team Development | No change. |
| 10 | Showcase Prep | No change. |
| 11 | Final Showcase | No change. |
| 12 | Graduation | No change. |

See also: `docs/teaching/sprint_outline.md` for the 5-day surprise-first alternative framing.

## Timeline

| Phase | Date | Owner | Deliverable |
|:--|:--|:--|:--|
| Install list locked | 2026-07-07 | @henry | This plan + Tier 1/2/5 frozen |
| Self-report form live | T-14 days | @henry | Google Form + sheet wired |
| Form submissions due | T-3 days (72h before S1) | participants | all forms in |
| Trainer review | T-2 days | @henry | red list compiled |
| Pre-Flight Setup Session | T-1 day | @henry + 1 TA | all reds cleared or moved to audit |
| Session 1 | Day 0 | cohort | teams formed at full strength |
| Sessions 2–12 | Days 1–11 | cohort | per Session guides |

## Dependencies

- [[pre_workshop_install_list]] — source of truth for the 13-item install list
- [[ai_coding_guide/README]] — the 13-chapter handbook the hackathon teaches
- [[sprint_outline]] — alternative 5-day framing
- [[pitch_10_minute]] — student-facing pitch (currently says "no install required"; must be updated to reflect the v2 gate)
- [[presentation_plan]] — same; reconciliation note in `pre_workshop_install_list.md §Reconciliation`

## Risks

- **Install friction on Windows** → mitigation: Pre-Flight Session provides WSL2 + Docker Desktop walkthrough; mac/Linux are smooth.
- **OpenRouter key cost** → mitigation: trainer provides a shared key for the hackathon week with $5 cap per participant.
- **Cohort red count too high** → mitigation: if >30% red at T-2 days, push Session 1 by one day and extend Pre-Flight to a full day.
- **Audit-mode morale** → mitigation: audit participants get first-priority slot in next cohort + access to all session recordings.
- **Pitch deck out of sync** → mitigation: update `pitch_10_minute.md` and `presentation_plan.md` before any student-facing comms go out (reconciliation note in `pre_workshop_install_list.md`).

## Open items for Henry

- [ ] Confirm hackathon date (T-0)
- [ ] Lock the 13-item list or trim further (currently Tier 1 + 2 + 5)
- [ ] Build the Google Form + linked Sheet
- [ ] Decide shared OpenRouter key budget
- [ ] Update `pitch_10_minute.md` + `presentation_plan.md` to reflect v2 install gate
- [ ] Schedule Pre-Flight Setup Session (T-1 day)
- [ ] Clean up the 12 Session guide files (location, frontmatter, v2 alignment) — separate task

## Related

- [[pre_workshop_install_list]]
- [[sprint_outline]]
- [[ai_coding_guide/README]]
- [[pitch_10_minute]]
- [[presentation_plan]]
