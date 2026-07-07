---
title: "Workshop Plan — Second Brain, Marksman, Medallion"
date: 2026-07-07
audience: InaAI / Prabowo demo showcase
tags: [workshop, second-brain, marksman, medallion, inaai, plan]
---

# Workshop Plan — Second Brain, Marksman, Medallion

**Framing:** These are the three systems Ilham/InaAI built on top of opencode. The workshop doc walks each from zero to running — what to install, how to plan, what opencode executes vs. what the human verifies. The narrative spine for the demo: **PKC is the workshop, InaAI is the showroom.** These three systems are what the workshop *produces* — capability captured, structured, and compounding.

---

## Phase 0 — Prerequisites (the machine before any of the 3 systems exist)

### Install (in this order — dependencies matter)

1. **Docker Desktop** — runs the mem0 stack (Postgres+pgvector, mem0 FastAPI on :8888, dashboard on :3000)
2. **Ollama** → `ollama pull nomic-embed-text` (768-dim local embeddings for mem0; the `memories` table is `vector(768)` to match)
3. **opencode** — the agent runner. Has `opencode.jsonc` with the `mem0` MCP entry pointing at the custom wrapper
4. **Python 3.11+** with packages:
   - `pymupdf` — PDF → markdown (ground-truth ingestion)
   - `python-docx` — docx → markdown (Achievement Bank + alt resumes)
   - `httpx` — Himalayas/RemoteOK/Greenhouse JSON APIs
   - `feedparser` — WWR RSS
   - `openpyxl`, `xlrd<2.0`, `xlsxwriter`, `pandas` — Excel workflow (Masters/inbox + outbox)
   - `yt_dlp`, `faster-whisper`, `curl_cffi` — YouTube transcript fetcher with impersonation fallback
5. **pandoc + MiKTeX** (`lualatex`/`xelatex`) — for Marksman PDF rendering
6. **Microsoft Edge** — for headless daily-report PDFs

### Wire up (opencode does this)

- `docker compose up -d` from `mcp/mem0/server` — bring up the mem0 stack
- Custom MCP wrapper at `mcp/mem0-mcp/server.py` — bridges self-hosted mem0 to opencode (the official mem0 MCP plugin only supports mem0 Cloud, not self-hosted, so this wrapper is the bridge)
- Scheduled tasks:
  - `Mem0AutoStart` (at user logon) — starts Ollama → Docker Desktop → `docker compose up -d`, polling each layer
  - `MCPWatchdog` (every 2 min) — kills orphaned MCP processes, revives mem0 if down, kills opencode processes flagged "Not Responding" for >5 min
  - `VaultLint` (Sun 9am) — mechanical vault health scan
  - `WeeklySummary` (Sun 8am) — cadence report

---

## Phase 1 — Second Brain (foundation + brain)

The blueprint has 4 layers. The workshop walks each:

### Layer 1 — Foundation
The vault folder + `AGENTS.md` as root operating manual. opencode writes the folder skeleton:

```
Koo/
├── InaAI/              # AI YouTube summaries + Koo project conversations
├── ChatGPT/            # ChatGPT export archive (sanitized imports)
├── sessions/<topic>/   # dated convo summaries by topic
├── meta/               # vault-level notes (state, decisions, plans, audits)
├── .agents/skills/     # installed skills
├── .scripts/           # helper scripts (watchdog, lint, transcript fetcher)
├── Masters/inbox/      # Excel files for agent to read
├── Masters/outbox/    # Excel files agent creates
├── Medallion/          # market intelligence
└── Marksman/           # job search bot
```

Plus an `AGENTS.md` template covering: session-start rules, folder routing, memory architecture, skill map, watchdog/lint wiring, YouTube summary workflow, daily report workflow, Excel workflow, Medallion protocol.

### Layer 2 — Room (populated wiki)
Seed the vault. opencode runs `dispatching-parallel-agents` to:
- Import ChatGPT exports (proof-of-concept: 649 convs, 5 subagents, 15min wall time vs ~11hr serial)
- Summarize YouTube videos via `youtube-summary` skill into atomic notes (one concept per file, 200-500 words, with `## Related` wikilinks)

Backlinks reciprocated — when a new note relates to existing notes, edit those existing notes to backlink the new one.

### Layer 3 — Thermostat (cadence)
The scheduled skills. These are the reflexes — the vault heals itself:
- `vault-lint` weekly (broken wikilinks, orphan notes, missing-page opportunities, frontmatter issues, stubs, tag drift)
- `weekly-summary` weekly (notes created/modified in last 7 days, grouped by folder)
- `MCPWatchdog` every 2 min (kills orphaned MCP processes, revives mem0)
- `Mem0AutoStart` at logon (starts Ollama → Docker → mem0 stack)

### Layer 4 — Locks (guardrails)
- `ground-truth/` read-only by convention (enforced in skill prompts)
- No browser automation anywhere (Submit click structurally impossible)
- No email auto-send without approval
- Reviewer subagent always runs on fresh context before drafter shows output

### Memory architecture (two layers)

| Layer | What | Where | Use it when |
|---|---|---|---|
| **Markdown (canonical)** | YouTube notes, convo summaries, ChatGPT imports | `InaAI/`, `sessions/<topic>/`, `ChatGPT/` | Portable, any LLM reads it, Obsidian graph + grep |
| **mem0 (atomic facts)** | Atomic facts extracted from conversations — "user prefers X", "decision: use Y" | Docker Postgres+pgvector at `localhost:8888` | Cross-session semantic recall — "what did we discuss about X?" |

**Rule:** markdown is canonical. mem0 is an *index over* the markdown, not a separate silo. The `convo-summary` skill writes to both in one pass.

---

## Phase 2 — Marksman (career sniper)

**Codename:** Marksman. **Goal:** Find low-competition remote jobs (workable from Indonesia, or relocation-offering), surface top 10 daily, draft tailored resume + cover letter per pick, never edit existing files, never click Submit.

**One-liner architecture:** Bot scrapes → ranks → you pick N → bot drafts N fresh files → you paste + submit.

### Folder structure

```
Marksman/
├── ground-truth/                  # READ-ONLY to bot
│   ├── Master-Resume.md
│   ├── Achievement-Bank.md
│   ├── Profile.md
│   ├── Motivation-Letters/
│   ├── Writing-Samples/
│   ├── Alt-Resumes/
│   └── README.md                  # "DO NOT EDIT — bot reads only"
├── discovery/                     # bot writes here
│   ├── <board>-<date>.json
│   ├── ranked-<date>.md
│   └── to-apply.md                # your pick queue
├── output/<date>/<company>-<role>/  # bot writes here only — fresh per role
│   ├── 00-jd.md
│   ├── 01-fit-score.md
│   ├── 02-positioning.md
│   ├── drafts/{resume-draft, cover-letter, recruiter-notes, disclosure-block}.md
│   ├── 99-final.md
│   └── final.pdf                  # rendered by Pandoc, never AI-edited
├── tracker.csv
└── .scripts/                      # bot's own scripts
```

### Build phases

| # | What | Blocker |
|---|---|---|
| P0.5 | `extract-resume-text.py` on Master Resume.pdf + Achievement Bank.docx + Profile.pdf + motivation letters + alt resumes → markdown in `ground-truth/`. You verify. | None |
| P1 | Distill 9 profile files (`01-candidate-profile.md` through `08-disclosure-policy.md` + `09-positioning-options.md`) from ground-truth markdown | P0.5 |
| P2 | Port ApplyGPT custom instructions → `prompts/drafter.md`. Write `prompts/reviewer.md`. Write `SKILL.md` (single-line description — opencode loader requirement, multi-line YAML folded scalars silently fail to load). | P1 |
| P3 | Write 6 board scrapers + `rank-discovered-jobs.py`. Run `find-skills` first to discover existing web-scraping skill. | Independent of P1/P2 |
| P4 | Wire skill auto-trigger on "today's run" → table → "top N" → batch file creation. | P2 + P3 |
| P5 | Test end-to-end on real run. Iterate. | P4 |
| P6 (opt) | Proton IMAP reader for recruiter inbound. LaTeX pipeline if Pandoc PDFs insufficient. | If needed |

### Resume tailoring rules (non-negotiable)

1. **2 pages max.** If draft overflows, cut lowest-relevance bullets first (score each line by relevance to JD + uniqueness + cover-letter dependency). Never compress to fit; always cut.
2. **Do not change the structure.** Copy the Master Resume structure exactly — same section order, same heading style, same bullet format. Only swap content within that structure.
3. **No fabrication.** If evidence isn't in `ground-truth/`, leave it out or ask. Reviewer subagent explicitly checks for fabricated metrics, skills, employers, accomplishments.
4. **Positioning constrained to 9 options** (8 from ApplyGPT + AI Automation Engineer at InaAI). Bot picks one per JD, never invents a 10th.
5. **Internal recruiter review mandatory.** Drafter runs full 8-step → reviewer subagent critiques (fresh context) → drafter revises → only the revised final version is shown. Never show first draft.

### Job board tier list

**Tier 1 — auto-scraped (low friction, public API):**
- Himalayas (free JSON API, `country=ID` filter, `worldwide=true` filter)
- WeWorkRemotely (RSS feed with post-dates)
- RemoteOK (public JSON API)

**Tier 2 — auto-scraped with caveats:**
- YC Work at a Startup (internal JSON, founder-read indicators show popularity)
- Greenhouse / Lever / Ashby / Workable (per-company watchlist JSON)
- LinkedIn guest endpoint (ToS-gray, low volume)

**Manual — you push URLs to bot:**
- Wellfound (blocks bots with 403)

**Skip:**
- Otta (login-gated)
- LinkedIn logged-in (ToS violation at scale)
- Workday (high friction — the 516→0 graveyard)

### Daily cadence

1. You say "today's run" (or scheduled 9am via Windows Task Scheduler, mirroring Mem0AutoStart pattern)
2. Bot runs 6 scrapers in parallel via `dispatching-parallel-agents` skill
3. Bot filters + dedupes + ranks top 10
4. Bot presents table: title | company | pay | location | fit-score | link | friction-level
5. You pick: "all 10" / "top 3" / "5 and 7"
6. Bot creates `Marksman/output/<date>/<company>-<role>/` per pick
7. Drafter subagent runs ApplyGPT 8-step → reviewer subagent (fresh context) critiques → drafter revises → final markdown only
8. Pandoc renders `final.pdf` per role
9. You paste bullets into Master Resume DOCX template, click Submit yourself
10. Bot updates `tracker.csv` after you confirm submission

### Trust guardrails

Your exact failure mode: "didn't trust AI to auto-apply, AI messes up editing." The guardrails:

1. Bot writes only to `output/<date>/<company>-<role>/` — never edits existing files
2. `ground-truth/` read-only to bot (enforced in SKILL.md)
3. PDFs rendered by Pandoc mechanically — AI never touches PDF bytes
4. No browser automation anywhere — Submit click structurally impossible
5. Reviewer subagent explicitly checks for: fabricated content, wrong positioning, junk jobs surfaced, off-tone cover letters, editing-mistake class of bugs
6. Drafter never shows first draft — only post-review revised version

---

## Phase 3 — Medallion (market intelligence)

**Codename:** Jim Simons' Renaissance Technologies (RenTech) — the Medallion Fund is the most successful hedge fund in history. Folder name signals the project's intent: signal extraction from Indonesian market chatter.

### Folder structure

```
Medallion/
├── influencers/
│   ├── stockbit/
│   │   ├── <handle>/          # one folder per named influencer
│   │   ├── others/            # everyone else, bucketed
│   │   ├── news/              # StockbitNews + StockbitReports + Stockbit admin, FILTERED to ticker-mentioning posts only
│   │   └── trending/          # daily overall sentiment summary (one md per day)
│   ├── instagram/
│   │   └── <handle>/          # IG stories, OCR'd — incl. vacation/lifestyle signals (those matter too)
│   └── youtube/
│       └── Astronacci/        # only market-analysis videos, drop mindset/inspirational/non-him content
├── companies/                 # FLAT — one .md per ticker, no subfolders. Updated on CA/RI/earnings/UBO/shareholder news.
└── raw/                       # source jsonl files (one per scrape batch)
```

### Named influencers (Stockbit)
8 named: `teddyed`, `Hauw2x`, `dojjun`, `r4wr`, `HannisaFaradillah`, `agasmhndr`, `itokireng`, `Mirzal` — each gets own subfolder. Everyone else → `others/`. Official Stockbit accounts (`StockbitNews`, `StockbitReports`, `Stockbit`) → `news/` folder, filtered to posts that mention at least one ticker (drop ADMIN posts + generic open/close chatter).

### Named influencers (Instagram stories)
`hengkyadinata21`, `_michaelyeoh`, `andryhakim`, `davidnoahl`, `dojjun` (same person as Stockbit dojjun, different platform — kept separate). OCR the story image. If they're on vacation / at a non-market event, that's still relevant — note it.

### YouTube — Astronacci relevance rule
**Only transcribe videos where Astronacci is doing market analysis.** Drop:
- Mindset / self-improvement / inspirational content (e.g. "Master Gema" type videos)
- Videos where he's not the speaker
- Pure vlogs with no market thesis
- agold-style content if it's just gold price updates with no thesis (borderline — keep if user is trading XAUUSD that week)

When in doubt, surface the title and ask.

### Build steps (opencode executes)

1. Create folder structure
2. Write `_organize.py` — splits `YYYY-MM-DD.jsonl` by author → per-influencer per-day .md files
   - StockbitNews/Reports/admin → `news/` filtered to posts mentioning tickers (`\$[A-Z]{2,5}` regex or non-empty `tickers_mentioned`)
   - YouTube → Astronacci filtered to market analysis
   - Dedupe by `video_url`
3. Write trending digest generator — 6 sections: Briefing → Market pulse → Key voices → Trending tickers → Corporate actions → Watchlist signals → Related (wikilinks to prior + next day)
4. Write ticker file template — sections in order: Profile, UBO (dated history append-only), Shareholders (dated history append-only), Key stats (refreshed each scrape), Analyst consensus (refreshed), Financials quarterly (markdown table, append-only, newest first), Corporate actions (Dividends/RUPS/Stock Split/Right Issue/Warrant/Bonus Shares/Tender Offer/Pubex/Other — append-only), Group (wikilinks to siblings)
5. Write company-update script:
   - Refresh `updated:` frontmatter
   - Append new CA events (never duplicate, never overwrite)
   - Refresh Key stats + Analyst consensus (overwrite — snapshot data)
   - Append new quarter row to Financials table (never overwrite)
   - Update Profile/UBO/Shareholders only when scrape contains a change — keep prior state as dated bullet for history
6. Set watchlist: BBCA, BBRI, BMRI, TPIA, MDKA, UNTR (6). Surfaced tickers in digest as promotion candidates — user reviews periodically, bot never auto-adds.

### Morning scrape cadence (every day new JSONL arrives)

1. **Posts** — Run `_organize.py` → splits posts by author into per-influencer .md files
2. **Company updates** — for each ticker in `companies-*.jsonl`, update `companies/<TICKER>.md`
3. **Trending digest** — generate `trending/<date>.md` with all 6 sections
4. **Watchlist signals** — surfaced tickers (mentioned today but not on watchlist), zero-mention watchlist tickers, watchlist tickers with active catalysts (dividents cum-date, RUPS, right issues happening today or this week)

### Ticker file structure (target state)

```markdown
---
ticker: BBRI
added: 2026-07-01
updated: 2026-07-04
tags: [medallion, company, ledger]
---

# BBRI

_Bank Rakyat Indonesia (Persero) Tbk._

## Profile
_(company name, sector, listing date, employees, business description)_

## UBO
- 2026-07-01: [name] — [path] — [percentage]

## Shareholders
- 2026-07-01: [name] — [percentage]

## Key stats
_(refreshed each scrape)_
- Market cap: ...
- P/E: ...
- PBV: ...
- as of: YYYY-MM-DD

## Analyst consensus
_(refreshed each scrape)_
- Target price: ...
- Recommendation: Buy/Hold/Sell
- # analysts: ...
- as of: YYYY-MM-DD

## Financials (quarterly)
_(appended each quarter — never overwritten)_

| Quarter | Revenue | Net income | EPS | YoY % |
|---|---|---|---|---|
| 2026Q1 | ... | ... | ... | ... |
| 2025Q4 | ... | ... | ... | ... |

## Corporate actions

### Dividends
- dividen Rp X | ex YYYY-MM-DD | bayar YYYY-MM-DD

### RUPS
### Stock Split
### Right Issue
### Warrant
### Bonus Shares
### Tender Offer
### Pubex
### Other

## Group
- **<group-name>** — [[<sibling1>]], [[<sibling2>]]
```

### What the morning scrape does NOT do

- **Does not auto-add or auto-delete watchlist tickers.** Surfaced tickers go in the digest as promotion candidates — user adds/removes.
- **Does not invent data.** Unpopulated sections stay as `_(pending population)_` placeholders until the scrape provides data. Verify with Wikipedia/IDX filings before populating, and note source + date.
- **Does not edit the original scrape JSONL.** Raw data is immutable. All processing writes to `.md` files only.

---

## Tie-together (the "so what" for the demo)

The 3 systems aren't parallel — they stack:

- **Second Brain is the OS** (vault + memory + skills + cadence + guardrails). Marksman and Medallion both run on top of it.
- **Marksman uses**: `dispatching-parallel-agents` (6 scrapers in parallel), `subagent-driven-development` (drafter/reviewer split), `verification-before-completion` (before bot says "your 5 resumes are ready"), `cavecrew` (compressed subagent output, ~60% smaller tool-results for 10-job batches), `find-skills` (discover existing scraping skill before writing 6 from scratch).
- **Medallion uses**: morning scrape protocol on top of the scheduled-task infrastructure from Second Brain's thermostat layer. Ticker files as time-series ledger — "past 3 quarters positive returns" = read top 3 rows of quarterly table. UBO/Shareholders keep dated bullets so "when did UBO change last?" = read the section, find the most recent dated bullet.
- **Shared substrate**: opencode as engine, mem0 for cross-session recall, AGENTS.md as operating manual, parallel subagents as the default execution mode for batch work.

The narrative for the demo: **PKC is the workshop, InaAI is the showroom.** These three systems are what the workshop *produces* — capability captured, structured, and compounding. The brain-building workflow (raw capture → AI-processed → linked wiki notes) is the same pattern whether you're processing ChatGPT exports (Second Brain), job postings (Marksman), or Stockbit chatter (Medallion).

---

## Source references

- `sessions/vault/second-brain-blueprint-layers.md` — Second Brain 4-layer blueprint (foundation/room/thermostat/locks)
- `meta/plans/2026-07-02-marksman.md` — Marksman full plan
- `Medallion/PROTOCOL.md` — Medallion morning scrape protocol
- `InaAI/koo-project/july-8-prabowo-demo.md` — PKC = workshop, InaAI = showroom framing
- `InaAI/koo-project/pkc-personal-knowledge-container.md` — PKC definition
