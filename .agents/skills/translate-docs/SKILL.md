---
name: translate-docs
description: "Use when you need to translate OKF documentation into Indonesian, or when a participant asks 'translate to Indonesian', 'where is the Indonesian version', 'terjemahkan', '/translate', or 'buat versi Indonesia'. Creates Indonesian versions of OKF concept documents under ../../resources/okf/id/. Ensures every doc in ../../resources/okf/ has a corresponding id/ translation. Checks for stale translations when the English version is updated."
---

# Translate-Docs Skill — Indonesian Translation for OKF Bundle

## When to use

- "translate to Indonesian"
- "where is the Indonesian version?"
- "terjemahkan ke bahasa Indonesia"
- "buat versi Indonesia"
- "/translate"
- "translate docs"
- A new OKF document was created and needs an Indonesian version
- An English doc was updated and the Indonesian version may be stale

## What this skill does

Ensures every OKF concept document in `../../resources/okf/` has a corresponding Indonesian translation in `../../resources/okf/id/`. The skill:

1. **Scans** `../../resources/okf/` for all English concept documents
2. **Checks** which ones have (or are missing) an Indonesian version in `../../resources/okf/id/`
3. **Checks** which Indonesian versions are stale (English was updated after the Indonesian)
4. **Translates** missing or stale docs into Indonesian
5. **Commits** the translations

---

## Stage 1 — Scan for missing or stale translations

### Step 1.1 — List all English docs

```bash
find okf -name "*.md" -not -path "../../resources/okf/id/*" -not -name "index.md" -not -name "log.md" | sort
```

### Step 1.2 — List all Indonesian docs

```bash
find ../../resources/okf/id -name "*.md" 2>/dev/null | sort
```

### Step 1.3 — Find missing translations

For each English doc at `../../resources/okf/<category>/<file>.md`, check if `../../resources/okf/id/<category>/<file>.md` exists. If not, it's missing.

### Step 1.4 — Find stale translations

For each Indonesian doc, compare the `timestamp` in its frontmatter with the English version's `timestamp`. If the English timestamp is newer, the Indonesian version is stale.

### Step 1.5 — Report

Say:
> *"I found [N] English OKF documents.*
> *- [M] have Indonesian translations (up to date)*
> *- [X] are missing Indonesian translations*
> *- [Y] have stale Indonesian translations (English was updated)*
>
> *I'll translate the [X+Y] missing/stale docs now."*

---

## Stage 2 — Translate a document

### Step 2.1 — Read the English source

Read `../../resources/okf/<category>/<file>.md` fully.

### Step 2.2 — Translate to Indonesian

Translation rules:

| What to translate | What to keep in English |
|:---|:---|
| All prose (paragraphs, descriptions, explanations) | Code blocks and commands |
| Table headers (translate the header words) | File paths (e.g. `../../resources/okf/tools/git.md`) |
| Headings (translate the heading text) | Tool names (Git, Node.js, Python, Ollama, Docker, etc.) |
| Analogies and examples (translate the narrative) | YAML frontmatter keys (`type`, `title`, `tags`, etc.) |
| Citations text (translate the description) | URLs and links |
| Notes and warnings | Variable names and env vars (`LITELLM_API_KEY`, etc.) |

**Key terminology mapping:**

| English | Indonesian |
|:---|:---|
| Required | Wajib |
| Optional | Opsional |
| Install | Instal / Pasang |
| Verify | Verifikasi / Periksa |
| Setup | Pengaturan / Persiapan |
| Configuration | Konfigurasi |
| Repository (repo) | Repositori (repo) |
| Commit | Commit (keep in English — it's a git command) |
| Push | Push (keep in English — it's a git command) |
| Pull | Pull (keep in English — it's a git command) |
| Branch | Branch (keep in English — it's a git term) |
| Stage | Stage (keep in English — it's a git term) |
| Skill | Skill (keep in English — it's a concept name) |
| Participant | Peserta |
| Instructor | Instruktur |
| Training | Pelatihan |
| Sovereign | Berdaulat |
| Offline | Offline / Luring |
| Online | Online / Daring |
| Gateway | Gateway (keep in English — it's a tech term) |
| Embedding | Embedding (keep in English — it's a tech term) |
| Frontmatter | Frontmatter (keep in English — it's a tech term) |
| Dashboard | Dashboard (keep in English — it's a UI term) |
| VPN | VPN (keep in English) |

### Step 2.3 — Write the Indonesian version

Write to `../../resources/okf/id/<category>/<file>.md`.

**Frontmatter changes:**
- Keep `type`, `tags`, `timestamp`, `resource` the same
- Translate `title` and `description` to Indonesian
- Add `lang: id` field
- Add `status: stable` (or `draft` if uncertain)

Example:
```yaml
---
type: Tool
title: Git
description: Sistem kontrol versi terdistribusi — lacak dan bagikan pekerjaan.
tags: [version-control, foundation]
timestamp: 2026-07-13T00:00:00Z
lang: id
status: stable
resource: https://git-scm.com
---
```

**Body changes:**
- Translate all prose to Indonesian
- Keep code blocks, commands, file paths unchanged
- Translate table headers but keep tool names in English
- Translate analogies and explanations
- Keep cross-links pointing to the same relative path (since both English and Indonesian are under `../../resources/okf/`, the relative paths work the same way — but for Indonesian docs, links should point to `../../resources/okf/id/<category>/<file>.md` versions)

> **Cross-link rule:** In Indonesian docs, cross-links should point to the Indonesian versions. Since Indonesian docs are at `../../resources/okf/id/<category>/`, a link to another Indonesian doc is `../<category>/<file>.md` (same relative path as in English, because the directory structure is mirrored).

### Step 2.4 — Create directories if needed

```bash
mkdir -p ../../resources/okf/id/tools ../../resources/okf/id/tech-stack ../../resources/okf/id/skills
```

---

## Stage 3 — Translate index.md and log.md

### index.md

Translate `../../resources/okf/index.md` to `../../resources/okf/id/index.md`:
- Translate the intro text
- Translate the category descriptions
- Keep the link targets pointing to the Indonesian versions (e.g. `[Git](tools/git.md)`)

### log.md

Translate `../../resources/okf/log.md` to `../../resources/okf/id/log.md`:
- Translate the log entries to Indonesian
- Add an entry for the translation itself

---

## Stage 4 — Commit and push

### Step 4.1 — Stage all new/updated Indonesian docs

```bash
git add ../../resources/okf/id/
```

### Step 4.2 — Commit

```bash
git commit -m "translate: add Indonesian versions of OKF docs

Translated [N] documents to Bahasa Indonesia:
- ../../resources/okf/id/index.md
- ../../resources/okf/id/log.md
- ../../resources/okf/id/tools/[list]
- ../../resources/okf/id/tech-stack/[list]
- ../../resources/okf/id/skills/[list]

Per AGENTS.md R16: every OKF document must have an Indonesian version."
```

### Step 4.3 — Push

```bash
git push origin main
```

---

## Stage 5 — Verify completeness

### Step 5.1 — Re-scan

After translation, re-run the scan from Stage 1 to verify every English doc now has an Indonesian version.

### Step 5.2 — Report

> *"Translation complete. All [N] OKF documents now have Indonesian versions at `../../resources/okf/id/`."*

---

## Edge cases

### Participant asks for a specific doc to be translated

If the participant says "translate the Git guide to Indonesian":
1. Find the English doc: `../../resources/okf/tools/git.md`
2. Check if `../../resources/okf/id/tools/git.md` exists
3. If not, translate it
4. If yes, check if it's stale and re-translate if needed
5. Commit and push

### English doc is updated

When an English doc is updated:
1. Set the Indonesian version's `status: stale` in frontmatter
2. Re-translate on the next `translate-docs` run
3. Set `status: stable` when done

### New doc is created

When a new OKF concept document is created:
1. The `translate-docs` skill should be run to create the Indonesian version
2. If the skill isn't run immediately, the lint will catch it (R16 violation)

---

## Reference

- [AGENTS.md R16](../../AGENTS.md) — rule: every OKF document must have an Indonesian version
- [OKF bundle](../) — the English source
- [OKF spec](../../resources/okf-spec.md) — Open Knowledge Format reference
