---
name: sync-indonesian
description: "Use when the user says 'sync indonesian', 'sync translations', 'indonesian is out of date', 'check indonesian translations', 'terjemahan ketinggalan', 'sinkronkan indonesia', '/sync-id', or 'update indonesian versions'. Scans git history to find English OKF docs that were changed after their Indonesian translation was last updated, then automatically re-translates the stale Indonesian versions so they match the latest English content. Commits and pushes the updates."
---

# Sync-Indonesian Skill — Git-History-Driven Indonesian Translation Sync

## When to use

The user says any of:
- "sync indonesian"
- "sync translations"
- "indonesian is out of date"
- "check indonesian translations"
- "update indonesian versions"
- "terjemahan ketinggalan" (translations are behind)
- "sinkronkan indonesia"
- "/sync-id"
- "sync-id"

Also use proactively after editing English OKF docs — the Indonesian versions are now stale and should be re-synced.

## What this skill does

Keeps the Indonesian translations in `okf/id/` in sync with the English source docs in `okf/`. Unlike `translate-docs` (which uses frontmatter `timestamp` for staleness), this skill uses **git history** to detect staleness — which is more reliable because:

- Frontmatter `timestamp` is only updated when a human remembers to bump it.
- Git history captures every actual content change, even when frontmatter wasn't touched.
- Git history works even when the English doc was edited without any `status: stale` marker.

The skill:

1. **Scans** every English OKF doc in `okf/` (excluding `okf/id/`, `index.md`, `log.md`).
2. **Pairs** each English doc with its Indonesian counterpart at `okf/id/<same-relative-path>`.
3. **Compares git history** — last commit touching English vs. last commit touching Indonesian.
4. **Flags stale pairs** — English was committed after the Indonesian (or Indonesian is missing).
5. **Re-translates** each stale Indonesian doc using the latest English content.
6. **Commits and pushes** all updates in one batch.

> **Commander-Executor framing:** the AI (executor) detects and re-translates automatically, but the participant (commander) approves before the commit lands. Never push without showing the diff summary first.

---

## Stage 1 — Detect stale Indonesian translations via git history

### Step 1.1 — List all English OKF docs

```bash
find okf -type f -name "*.md" -not -path "okf/id/*" -not -name "index.md" -not -name "log.md" | sort
```

### Step 1.2 — For each English doc, find its last-modified commit timestamp

For an English doc at `okf/tools/git.md`:

```bash
git log -1 --format="%ct|%H|%ci" -- okf/tools/git.md
```

Output format: `<unix-timestamp>|<commit-hash>|<iso-date>`

- `%ct` — committer date, Unix timestamp (for numeric comparison)
- `%H` — full commit hash (for ancestry checks if needed)
- `%ci` — ISO 8601 date (for display)

### Step 1.3 — Find the Indonesian counterpart

The Indonesian version lives at `okf/id/<same-relative-path>`. So:
- `okf/tools/git.md` maps to `okf/id/tools/git.md`
- `okf/tech-stack/antigravity.md` maps to `okf/id/tech-stack/antigravity.md`
- `okf/concepts/mcard.md` maps to `okf/id/concepts/mcard.md`

To derive the Indonesian path from the English path, replace the leading `okf/` with `okf/id/`.

### Step 1.4 — Get the Indonesian doc's last-modified commit timestamp

```bash
git log -1 --format="%ct|%H|%ci" -- okf/id/tools/git.md
```

If the file doesn't exist in git history (or on disk), the Indonesian version is **missing** — that's a special case of staleness (handled the same way: create it).

### Step 1.5 — Compare timestamps to find stale pairs

For each English/Indonesian pair:

- `english_ts` = Unix timestamp of last commit touching English doc
- `indonesian_ts` = Unix timestamp of last commit touching Indonesian doc (0 if missing)

**Stale if:** `english_ts > indonesian_ts`

That is: the English doc was modified in a commit that came *after* the most recent commit that touched the Indonesian translation. The Indonesian is behind.

> **Note on same-commit edge case:** if `english_ts == indonesian_ts` (both last touched in the same commit, e.g. the initial translation commit), the Indonesian is **up to date** — not stale. Only flag when English is strictly newer.

### Step 1.6 — Batch script for detection

Save this as `scripts/check-id-sync.sh` and run it from the repo root (`abad/`). On Windows, run under Git Bash (ships with Git for Windows).

```bash
#!/usr/bin/env bash
# Prints: STATUS<TAB>english_path<TAB>indonesian_path<TAB>english_date<TAB>indonesian_date
# status = STALE | MISSING | OK

find okf -type f -name "*.md" -not -path "okf/id/*" -not -name "index.md" -not -name "log.md" | sort | while read -r en; do
  id="okf/id/${en#okf/}"
  en_ts=$(git log -1 --format="%ct" -- "$en" 2>/dev/null || echo 0)
  id_ts=$(git log -1 --format="%ct" -- "$id" 2>/dev/null || echo 0)
  en_date=$(git log -1 --format="%ci" -- "$en" 2>/dev/null || echo "never")
  id_date=$(git log -1 --format="%ci" -- "$id" 2>/dev/null || echo "never")
  if [ ! -f "$id" ]; then
    printf "MISSING\t%s\t%s\t%s\t%s\n" "$en" "$id" "$en_date" "$id_date"
  elif [ "$en_ts" -gt "$id_ts" ]; then
    printf "STALE\t%s\t%s\t%s\t%s\n" "$en" "$id" "$en_date" "$id_date"
  else
    printf "OK\t%s\t%s\t%s\t%s\n" "$en" "$id" "$en_date" "$id_date"
  fi
done
```

> The agent can also run this inline (without saving the script) by piping the `find` output through the `while read` loop directly in a single bash invocation.

---

## Stage 2 — Report findings to the commander

### Step 2.1 — Summarize the scan

Before touching anything, show the participant a clear report:

> *"I scanned [N] English OKF documents against their Indonesian translations using git history.*
>
> *- [M] are up to date*
> *- [X] Indonesian versions are STALE (English was updated after the translation)*
> *- [Y] Indonesian versions are MISSING (no translation exists yet)*
>
> *Stale docs:*
> - `okf/tools/git.md` — English updated 2026-07-13, Indonesian last touched 2026-07-12
> - `okf/tech-stack/antigravity.md` — English updated 2026-07-13, Indonesian last touched 2026-07-12
> *(... list all stale and missing)*
>
> *I'll re-translate the [X+Y] stale/missing docs now. Proceed? (yes/no)"*

### Step 2.2 — Get approval

Wait for explicit "yes" before proceeding. If the participant says "no" or wants to skip specific docs, respect that — they are the commander.

If approved, proceed to Stage 3.

---

## Stage 3 — Re-translate each stale/missing doc

For each stale or missing Indonesian doc, re-translate from the latest English content.

### Step 3.1 — Read the latest English source

Read `okf/<category>/<file>.md` fully. This is the source of truth.

### Step 3.2 — Read the existing Indonesian version (if it exists)

If `okf/id/<category>/<file>.md` already exists, read it too. Use it as a reference for:
- Terminology choices already made (keep them consistent)
- Frontmatter fields that should be preserved (`lang: id`, `status`)

### Step 3.3 — Translate to Indonesian

Follow the translation rules from the `translate-docs` skill (see [`../translate-docs/SKILL.md`](../translate-docs/SKILL.md) §2.2 for the full table). Summary:

| What to translate | What to keep in English |
|:---|:---|
| All prose (paragraphs, descriptions, explanations) | Code blocks and commands |
| Table headers (translate the header words) | File paths (e.g. `okf/tools/git.md`) |
| Headings (translate the heading text) | Tool names (Git, Node.js, Python, Ollama, Docker, etc.) |
| Analogies and examples (translate the narrative) | YAML frontmatter keys (`type`, `title`, `tags`, etc.) |
| Citations text (translate the description) | URLs and links |
| Notes and warnings | Variable names and env vars (`LITELLM_API_KEY`, etc.) |

**Key terminology mapping** (from `translate-docs` §2.2):

| English | Indonesian |
|:---|:---|
| Required | Wajib |
| Optional | Opsional |
| Install | Instal / Pasang |
| Verify | Verifikasi / Periksa |
| Setup | Pengaturan / Persiapan |
| Configuration | Konfigurasi |
| Repository (repo) | Repositori (repo) |
| Commit / Push / Pull / Branch / Stage | Keep in English (git terms) |
| Skill | Skill (keep — concept name) |
| Participant | Peserta |
| Instructor | Instruktur |
| Training | Pelatihan |
| Sovereign | Berdaulat |
| Offline / Online | Luring / Daring |
| Gateway / Embedding / Frontmatter / Dashboard / VPN | Keep in English (tech terms) |

### Step 3.4 — Write the Indonesian version

Write to `okf/id/<category>/<file>.md`. Create parent directories if needed:

```bash
mkdir -p okf/id/tools okf/id/tech-stack okf/id/concepts okf/id/skills okf/id/sources
```

### Step 3.5 — Update frontmatter

**Preserve from English:** `type`, `tags`, `timestamp` — keep the same values as the English source (so future syncs can compare).

**Translate:** `title` and `description` — translate to Indonesian.

**Add/set Indonesian-specific fields:**
- `lang: id`
- `status: stable` (we just re-translated, so it's now in sync)
- `synced_from: <english-commit-hash>` — the commit hash of the English version this translation is based on (for traceability; optional but recommended)

Example Indonesian frontmatter:

```yaml
---
type: Tool
title: Git
description: Sistem kontrol versi terdistribusi — lacak dan bagikan pekerjaan.
tags: [version-control, foundation]
timestamp: 2026-07-13T00:00:00Z
lang: id
status: stable
synced_from: d628ead
---
```

### Step 3.6 — Cross-links

In Indonesian docs, cross-links should point to the Indonesian versions. Since Indonesian docs live at `okf/id/<category>/`, a link to another Indonesian doc uses the same relative path as in English (because the directory structure is mirrored under `okf/id/`).

Example: in `okf/id/tools/git.md`, a link to the Obsidian doc is `[Obsidian](../tech-stack/obsidian.md)` — same relative path as the English version, but it resolves to the Indonesian Obsidian doc.

### Step 3.7 — Repeat for every stale/missing doc (use parallel subagents)

Process each stale/missing doc. The PRIMARY workflow is to launch multiple `general` subagents via the Task tool in parallel — each subagent handles a batch of docs. This is not optional; it is how the skill is designed to be run.

**How to batch:**
- Group stale/missing docs by category (`okf/concepts/`, `okf/tools/`, `okf/tech-stack/`, `okf/sources/youtube/`, etc.).
- If a category has more than ~20 docs, split it into multiple batches of ~10-20 docs each.
- Launch one subagent per batch, all in parallel (single message, multiple Task tool calls).
- Each subagent gets: the list of English paths to translate, the target Indonesian paths, and the translation rules (§3.3-3.6).
- Each subagent reads English, translates, writes the Indonesian file. Subagents do NOT commit — the parent agent commits at the end (Stage 4).

**Example:** if there are 77 stale/missing docs across 4 categories, launch 4-5 subagents in parallel:
- Subagent 1: `okf/tech-stack/*` (8 docs)
- Subagent 2: `okf/tools/*` (13 docs)
- Subagent 3: `okf/concepts/*` batch 1 (19 docs)
- Subagent 4: `okf/concepts/*` batch 2 (18 docs)
- Subagent 5: `okf/sources/youtube/*` (19 docs)

**After all subagents complete:** verify all files were written (count Indonesian docs vs English docs), then proceed to Stage 4 to commit everything in one batch.

> **Why parallel:** 77 docs translated serially would take hours. In parallel, it takes minutes. This is the whole point of the skill — make it practical to keep 100+ Indonesian docs in sync.

---

## Stage 4 — Commit and push

### Step 4.1 — Show the diff summary

Before committing, show the participant what changed:

```bash
git status --short okf/id/
git diff --stat okf/id/
```

Show:

> *"Here's what I'm about to commit:*
> - *Updated [X] stale Indonesian translations*
> - *Added [Y] missing Indonesian translations*
> - *Files: (list)*
>
> *Commit message will be: `sync-id: re-translate [N] stale Indonesian OKF docs`*
>
> *Proceed? (yes/no)"*

### Step 4.2 — Stage all Indonesian docs

```bash
git add okf/id/
```

### Step 4.3 — Commit

```bash
git commit -m "sync-id: re-translate N stale Indonesian OKF docs

Synced via git-history detection (sync-indonesian skill):
- X stale docs re-translated from latest English
- Y missing docs created

Stale docs (English updated after Indonesian):
- okf/id/tools/git.md
- okf/id/tech-stack/antigravity.md
(... list all)

Per AGENTS.md R16: every OKF document must have an Indonesian version,
and the Indonesian version must stay in sync with the English source."
```

### Step 4.4 — Push

```bash
git push origin main
```

If push fails (offline, auth), tell the participant and stop — don't force anything.

### Step 4.5 — Confirm

> *"Done. Synced [N] Indonesian translations.*
>
> *Commit: `<commit-hash>`*
> *View on GitHub: [link to the commit]*
>
> *All Indonesian OKF docs are now up to date with the English source."*

---

## Stage 5 — Verify

### Step 5.1 — Re-run the detection scan

Run the Stage 1.6 script again. Every pair should now report `OK` (no stale, no missing).

### Step 5.2 — Report

> *"Verification complete. [N] English OKF docs, [N] Indonesian translations — all in sync."*

If any are still stale or missing, list them and offer to re-run.

---

## Edge cases

### English doc has no Indonesian counterpart directory

If `okf/id/<category>/` doesn't exist, create it:

```bash
mkdir -p okf/id/<category>
```

### Indonesian doc exists but is untracked in git

If `git log -1` returns nothing for the Indonesian path but the file exists on disk, treat it as `MISSING` (the on-disk version may be stale or a draft). Re-translate from English and `git add` it.

### Same commit touched both English and Indonesian

If `english_ts == indonesian_ts`, the pair is in sync (both last touched in the same commit, e.g. the initial translation commit). Don't flag as stale.

### English doc was renamed

Git rename detection may cause `git log` to follow history across the rename. If the English path was renamed but the Indonesian wasn't, the Indonesian will show as stale. Re-translate to the new English content and (optionally) rename the Indonesian file to match:

```bash
git mv okf/id/<old-path> okf/id/<new-path>
```

Then re-translate the content.

### Participant wants to skip a specific doc

If the participant says "skip `okf/id/tools/git.md`", honor it. Record it in the report as "skipped by participant" and don't touch the file.

### Participant wants to review each translation before commit

If the participant wants to review each translation one-by-one instead of batch-committing:
1. Translate one doc.
2. Show the participant the diff: `git diff okf/id/<path>`.
3. Wait for "ok" or "edit".
4. If "edit", ask what to change, make the edit, re-show.
5. Move to the next doc.
6. Commit all approved docs at the end.

### Push fails (offline or auth)

If `git push` fails:

> *"Commit saved locally, but push failed: [error]. You're offline or not authenticated. Run `git push` later when ready."*

Don't force-push. Don't amend. Just stop and report.

### Frontmatter `timestamp` disagrees with git history

If the English frontmatter `timestamp:` is older than the git commit date, trust **git history** (the commit date). The frontmatter timestamp may not have been bumped. Git history reflects actual file changes.

### No internet / no remote

If `git push` isn't possible (no remote, no internet), still commit locally and tell the participant. The sync work is preserved in the local commit.

---

## What this skill does NOT do

- **Does not translate non-OKF docs.** Only `okf/` docs have Indonesian versions per AGENTS.md R16. If the user asks to sync docs in `docs/`, `curriculum/`, or `participants/`, point them to R16 — those aren't required to have Indonesian versions. (They can ask for a one-off translation via the `translate-docs` skill if needed.)
- **Does not modify the English source.** The English docs are the source of truth. This skill only writes to `okf/id/`.
- **Does not delete Indonesian docs** that have no English counterpart (orphaned translations). If found, report them to the participant and ask whether to delete — don't delete automatically.
- **Does not bypass the commander.** Always show what's about to be committed and get explicit approval before pushing.

---

## Reference

- [AGENTS.md R16](../../AGENTS.md) — rule: every OKF document must have an Indonesian version, kept in sync
- [translate-docs skill](../translate-docs/SKILL.md) — one-off translation skill (uses frontmatter `timestamp` for staleness); this skill complements it by using git history for more reliable detection
- [OKF bundle](../../okf/) — the English source
- [OKF spec](../../docs/okf.md) — Open Knowledge Format reference
