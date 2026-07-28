---
name: feedback
description: "Use when a participant says /feedback, /question, I have feedback, I have a question, let me give feedback, or ask a question. Collects the participant's feedback or question, appends it to a single OKF-conformant markdown file at participants/<github-username>/feedback.md or participants/<github-username>/question.md, then commits ONLY that participant's folder and pushes. Entries are appended with date + sequence headers."
---

# Feedback and Question Skill — 5-Day AI Builder Training

## When to use

The participant says any of:

**Feedback triggers:**
- `/feedback`
- 'I have feedback'
- 'let me give feedback'
- 'I want to give feedback'
- 'feedback for the instructors'

**Question triggers:**
- `/question`
- 'I have a question'
- 'ask a question'
- 'let me ask something'
- 'quick question'

If the trigger is ambiguous (participant just says 'feedback' or 'question' without context), ask: *'Are you submitting feedback, or asking a question?'*

## What this skill does

1. **Identifies the participant** — gets their GitHub username (auto-detected from git config + remote URL).
2. **Determines entry type** — `feedback` or `question` (from the trigger phrase, or by asking).
3. **Creates the participant folder** — `participants/<github-username>/` if it does not exist.
4. **Collects the entry** — asks the participant for the content (one open prompt, plus optional context).
5. **Appends to a single file** — appends to `participants/<github-username>/feedback.md` or `participants/<github-username>/question.md`. Creates the file with OKF frontmatter on first use. Each entry is a dated, sequenced `##` section appended at the bottom.
6. **Isolated commit + push** — stages ONLY `participants/<github-username>/`, commits, pushes. Other changes in the repo stay uncommitted.

> **Commander-Executor framing:** the participant is the commander — they decide what to say. The AI is the executor — it asks for the content, formats it, writes the file, commits, and pushes. The AI never edits the participant's words beyond light formatting (line breaks, bullet points).

> **Isolated push rule:** only stage `participants/<github-username>/`. Never `git add -A` or `git add .`. This lets participants push their own folder even when other files in their working tree are dirty.

---

## Stage 1 — Identify the participant

### Step 1.1 — Auto-detect GitHub username from git

Run:

```powershell
git config user.name
git config user.email
git remote get-url origin
```

### Step 1.2 — Extract GitHub username

Parse the username from the remote URL:

- `git@github.com:<github-username>/<repo>.git` → username is between `:` and `/`
- `https://github.com/<github-username>/<repo>.git` → username is between `github.com/` and `/`

PowerShell extraction:

```powershell
$url = git remote get-url origin
if ($url -match 'github\.com[:/]([^/]+)/') { $githubUsername = $Matches[1] }
```

### Step 1.3 — Sanitize the folder name

Per AGENTS.md R17 + participants/README.md:
- **lowercase** — convert to lowercase
- **no spaces** — replace spaces with hyphens
- **kebab-case only** — letters, numbers, hyphens, dots

```powershell
$folderName = $githubUsername.ToLower() -replace '\s+', '-'
$folderName = $folderName -replace '[^a-z0-9.-]', ''
```

### Step 1.4 — Verify with the participant

> *"I detected your GitHub username: `<github-username>` (folder: `participants/<folder-name>/`)."*
>
> *"Is this correct? If different, tell me your GitHub username."*

If git config is empty or remote URL does not reveal a username, ask directly:
> *"I could not auto-detect your GitHub username. What is it? (This becomes your folder name under `participants/`.)"*

### Step 1.5 — Record identity for this session

- **full_name** — from `git config user.name`
- **github_username** — extracted from remote URL (sanitized to kebab-case for folder name)
- **folder_path** — `participants/<folder-name>/`

---

## Stage 2 — Determine entry type

Map the trigger to one of:

| Trigger | Entry type | File |
|:---|:---|:---|
| `/feedback`, 'I have feedback', 'give feedback' | `feedback` | `feedback.md` |
| `/question`, 'I have a question', 'ask a question' | `question` | `question.md` |

If the trigger is ambiguous, ask the participant which one they are submitting.

Set:
- **entry_type** — `feedback` or `question`
- **filename** — `feedback.md` or `question.md`

---

## Stage 3 — Create the participant folder if missing

```powershell
$participantDir = "participants/$folderName"
if (-not (Test-Path -LiteralPath $participantDir)) {
    New-Item -ItemType Directory -Path $participantDir | Out-Null
}
```

### Step 3.1 — Get today's date

```powershell
$today = Get-Date -Format 'yyyy-MM-dd'
```

### Step 3.2 — Set the file path

```
$filepath = "$participantDir/$filename"
```

---

## Stage 4 — Collect the entry content

### Step 4.1 — Main prompt

Ask one open question and wait for the answer:

**For feedback:**

> *"What is your feedback? Type it out — it can be about the training, an instructor, the pace, the tools, anything. I will format it but will not change your meaning."*

**For questions:**

> *"What is your question? Type it out — I will format it but will not change your meaning."*

Capture the participant's answer verbatim.

### Step 4.2 — Optional context

Ask (optional — participant can say "skip"):

> *"Any context? (Optional — e.g. which day, which tool, which instructor. Type skip if none.)"*

Capture the answer as `context`. If "skip", set `context` to empty string.

### Step 4.3 — Optional topic tag

Ask (optional):

> *"Any topic tag? (Optional — short phrase like day-2-rag, git-setup, glm-52. Type skip if none.)"*

Capture the answer as `topic`. If "skip", set `topic` to empty string.

---

## Stage 5 — Determine the sequence number

The file accumulates multiple entries across all days. Find the highest sequence number already in the file:

```powershell
$nextSeq = 1
if (Test-Path -LiteralPath $filepath) {
    $content = Get-Content -LiteralPath $filepath -Raw
    $regex = [regex]'## \d{4}-\d{2}-\d{2} #(\d+)'
    $allMatches = $regex.Matches($content)
    $maxSeq = 0
    foreach ($m in $allMatches) {
        $n = [int]$m.Groups[1].Value
        if ($n -gt $maxSeq) { $maxSeq = $n }
    }
    $nextSeq = $maxSeq + 1
}
$seqStr = '{0:D3}' -f $nextSeq
```

---

## Stage 6 — Append the entry to the file

### Step 6.1 — If the file does not exist, create it with frontmatter

Template (replace placeholders with actual values):

```markdown
---
type: <entry_type>
title: '<Entry_type capitalized> — <github-username>'
author: <github-username>
tags: [<entry_type>, training]
status: stable
---

# <Entry_type capitalized> — <full_name> (`<github-username>`)

This file collects all <entry_type> entries from this participant. Newest entries are appended at the bottom. Do not edit past entries directly unless correcting a typo.

---
```

### Step 6.2 — Compose the new entry block

Append this block to the end of the file:

```markdown
## <today> #<seqStr><if topic> — <topic></if>

**From:** <full_name> (`<github-username>`)

<if context>
**Context:** <context>
</if>

---

<participant content — formatted lightly: paragraphs preserved, URLs as markdown links, code blocks fenced>

---
```

### Step 6.3 — Format guidelines

- **Preserve the participant's voice.** Do not rewrite meaning, soften tone, or edit content. Only formatting changes are allowed.
- **Light formatting only:**
  - Preserve paragraph breaks.
  - Wrap URLs as markdown links: `[text](url)`.
  - If the participant pasted code or commands, wrap in fenced code blocks.
  - If the participant listed items clearly, you may use bullet points — but only if they are already listing items.
- **Do NOT:**
  - Summarize or shorten.
  - Add commentary, headers, or sections the participant did not write.
  - Translate or rephrase.
  - Fix grammar or spelling.

### Step 6.4 — Write or append to the file

```powershell
if (Test-Path -LiteralPath $filepath) {
    # Append the new entry to the existing file
    Add-Content -LiteralPath $filepath -Value $entryBlock -Encoding UTF8
} else {
    # Create the file with frontmatter + first entry
    Set-Content -LiteralPath $filepath -Value ($frontmatter + $entryBlock) -Encoding UTF8
}
```

---

## Stage 7 — Show the participant and get approval

### Step 7.1 — Show the entry

> *"Here is your <entry_type> entry. Review it — I will commit once you say it looks good."*
>
> *(shows the new entry block that will be appended)*
>
> *"Looks good? (yes / edit / cancel)"*

### Step 7.2 — Handle responses

- **'yes'** → proceed to Stage 8.
- **'edit'** → ask what to change. Apply the edit. Re-show. Repeat until 'yes' or 'cancel'.
- **'cancel'** → do not write/append anything. Stop. Tell participant: *'Cancelled — file not modified.'*

---

## Stage 8 — Isolated commit and push

### Step 8.1 — Stage ONLY this participant's folder

**CRITICAL:** stage only `participants/<github-username>/`. Never `git add -A`, never `git add .`, never stage other paths.

```powershell
git add participants/<github-username>/
```

### Step 8.2 — Verify the staged set

Before committing, show what is staged:

```powershell
git status --short
```

Confirm to the participant:

> *"Staged for commit (only your folder):"*
> - *`participants/<github-username>/<filename>`*
>
> *"Other files in your working tree will NOT be committed. OK to commit? (yes/no)"*

If 'no', abort: `git reset HEAD participants/<github-username>/`. Stop.

### Step 8.3 — Commit

```powershell
$dateStamp = Get-Date -Format 'yyyy-MM-dd'
git commit -m "$entryType $dateStamp-$seqStr — $githubUsername"
```

Commit message format: `<feedback|question> <YYYY-MM-DD>-<NNN> — <github-username>`

Examples:
- `feedback 2026-07-17-001 — ilhamhakm`
- `question 2026-07-17-002 — alessandro-rumampuk`

### Step 8.4 — Push

Detect the current branch first:

```powershell
$branch = git rev-parse --abbrev-ref HEAD
git push origin $branch
```

### Step 8.5 — Confirm

> *"Done! Your <entry_type> entry has been appended and pushed."*
>
> *File: `participants/<github-username>/<filename>`*
> *Entry: #<seqStr> (dated <today>)*
> *Commit: `<short-hash>`*
> *Branch: `<branch>`*
>
> *"Instructors will see it. If it is a question, they may respond inline by editing the file or opening a GitHub issue."*

---

## Edge cases

### Participant has not set up git config

If `git config user.name` is empty:
> *"Your git user.name is not set. What is your full name? I will set it: `git config user.name "<name>"`"*

### Not in the abad repo

If `git remote get-url origin` fails or is not the abad repo:
> *"You are not in the abad git repo. Clone it first: `git clone git@github.com:gasingtraining/abad.git` — or your fork. What is your fork's URL?"*

### Participant is offline

If `git push` fails (network):
> *"Commit saved locally, but push failed — you are offline. Run `git push` later when you have internet."*
>
> *"Your file is at: `participants/<github-username>/<filename>`"*

### Participant wants to submit multiple entries in one session

After each entry is committed, ask: *"Submit another? (yes/no)"* If yes, loop back to Stage 2 (entry type) — but reuse the same participant identity from Stage 1.

### Participant wants to edit a past entry

The skill does NOT edit past entries. Tell the participant:
> *"To edit a past entry, open the file directly in your editor and edit the relevant `## YYYY-MM-DD #NNN` section. The skill only appends new entries."*

### Existing folder uses spaces (e.g. 'Alessandro Rumampuk')

Per R17, folder names should be kebab-case. If the sanitized name differs from an existing folder, ask the participant:
> *"I detected an existing folder at `participants/Alessandro Rumampuk/` (with spaces). Per repo rules (R17), folder names should be kebab-case. Should I:"*
> - *"Use the existing folder (against the rules)?"*
> - *"Use a new kebab-case folder `participants/alessandro-rumampuk/` (recommended)?"*
> - *"Rename the old folder to kebab-case first?"*

Default to using the kebab-case version.

---

## OKF conformance

This skill produces OKF-conformant concept documents:
- **Required `type:` field** — set to `feedback` or `question`.
- **YAML frontmatter** — delimited by `---` (created once when the file is first created).
- **Markdown body** — standard markdown with structural headings. Each entry is a `## YYYY-MM-DD #NNN` section.
- **Producer-defined keys** — `author`, `status` are extensions (allowed by OKF 4.1).

See `docs/okf.md` for the full OKF spec.

---

## Reference

- [Participants README](../../participants/README.md) — structure and instructions
- [Daily reflection template](../../participants/_template/daily-reflection.md) — the blank template
- [OKF spec](../../docs/okf.md) — Open Knowledge Format reference
- [AGENTS.md R15](../../AGENTS.md) — rule: participant reports live in `participants/<github-username>/`
- [AGENTS.md R17](../../AGENTS.md) — rule: filenames must be cross-platform safe (kebab-case)
