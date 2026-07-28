---
name: daily-report
description: "Use when a participant says 'daily report', 'reflection', 'report my day', 'write my daily reflection', '/daily', or 'I want to report what I did today'. Collects the participant's name and GitHub username (auto-detected from git), then guides them through a structured daily reflection (what they did, learned, what was hard, artifacts), writes an OKF-conformant markdown file to participants/<github-username>/day_N_reflection.md, and commits + pushes to the abad repo."
---

# Daily Report Skill — 5-Day AI Builder Training

## When to use

The participant says any of:
- "daily report"
- "reflection"
- "report my day"
- "write my daily reflection"
- "/daily"
- "I want to report what I did today"
- "daily-report"

## What this skill does

Guides the participant through writing their daily reflection report for the 5-day training. The skill:

1. **Identifies the participant** — gets their name and GitHub username (auto-detected from git config).
2. **Creates their folder** — `participants/<github-username>/` if it doesn't exist.
3. **Detects the day** — asks which day (1-5) or auto-detects from existing reports.
4. **Interviews the participant** — asks structured questions about what they did, learned, struggled with, and would do differently.
5. **Writes the report** — OKF-conformant markdown file with YAML frontmatter (`type: reflection`).
6. **Commits and pushes** — commits to the abad repo with a clear message and pushes to GitHub.

> **Commander-Executor framing:** the participant is the commander — they decide what goes in the report. The AI is the executor — it asks the questions, writes the file, commits, and pushes. The AI never invents content; it only writes what the participant tells it.

---

## Stage 1 — Identify the participant

### Step 1.1 — Auto-detect GitHub username from git

Run these commands to gather git identity:

```bash
# Get git user name (full name)
git config user.name

# Get git user email
git config user.email

# Get the remote URL (to extract the GitHub username)
git remote get-url origin
```

### Step 1.2 — Extract GitHub username

Parse the GitHub username from the remote URL. The remote URL is usually one of:

- `git@github.com:<github-username>/<repo>.git` → username is between `:` and `/`
- `https://github.com/<github-username>/<repo>.git` → username is between `github.com/` and `/`

Example extraction:
```bash
# From: git@github.com:henrykoo/abad.git → henrykoo
# From: https://github.com/henrykoo/abad.git → henrykoo
git remote get-url origin | sed -E 's#(git@github\.com:|https://github\.com/)([^/]+)/.*#\2#'
```

### Step 1.3 — Verify with the participant

Show what was detected and confirm:

> *"I detected from your git config:*
> - *Name: `[user.name]`*
> - *Email: `[user.email]`*
> - *GitHub username: `[github-username]` (from the remote URL)*
>
> *Is this correct? If your GitHub username is different, please tell me."*

If the participant confirms, proceed to Stage 2.

If git config is empty or the remote URL doesn't reveal a username, ask:
> *"I couldn't auto-detect your GitHub username. What is your GitHub username? (This will be the folder name under `participants/`.)"*

### Step 1.4 — Record identity for this session

Remember these for the rest of the session:
- **full_name** — from `git config user.name` (or as the participant introduces themselves)
- **github_username** — extracted from remote URL (or as the participant provides)
- **folder_path** — `participants/<github-username>/`

---

## Stage 2 — Detect the day and create the folder

### Step 2.1 — Detect which day to report

Check if the participant already has existing reflection files:

```bash
ls participants/<github-username>/day_*_reflection.md 2>/dev/null
```

**If files exist:**
- Show the participant which days are already done.
- Ask: *"Which day are you reporting? (1-5)"* — or auto-suggest the next day.
- If they choose a day that already has a file, ask: *"You already have a day N reflection. Overwrite it? (yes/no)"*

**If no files exist:**
- Ask: *"Which day are you reporting? (1-5)"*

### Step 2.2 — Create the folder if it doesn't exist

```bash
mkdir -p participants/<github-username>
```

### Step 2.3 — Set the date

Get today's date:
```bash
date +%Y-%m-%d
```

This goes into the frontmatter `date:` field.

---

## Stage 3 — Interview the participant

Ask these 5 questions, one at a time. Wait for the participant's answer to each before moving to the next. The AI does NOT invent answers — it only writes what the participant says.

### Q1 — What I did today

> *"Q1: What did you do today? List the tools you used, the exercises you completed, and any commands you ran. (Just talk — I'll format it.)"*

Capture the participant's answer. Optionally help them recall by listing the day's curriculum topic:
- Day 1: Foundations — website with AI, Git, GitHub
- Day 2: Local AI + RAG — chatbot over your documents
- Day 3: Finetuning — training a model on your data
- Day 4: PKC, MCard, VCard — sovereign platform, CLM specs
- Day 5: Final project + closing

### Q2 — What I learned

> *"Q2: What did you learn today? Key concepts, aha moments, anything you want to remember. (If you mention a concept like MCard or CLM, I'll cross-link it to the wiki.)"*

Capture the answer. If the participant mentions concepts that exist in the parent wiki (MCard, PCard, VCard, CLM, Representation Engine, Trivium, etc.), note them for cross-linking in §4.6.

### Q3 — What was hard

> *"Q3: What was hard today? Where did you get stuck? What would you ask the instructor next time?"*

Capture the answer honestly. This is for learning, not for grading.

### Q4 — What I'd do differently

> *"Q4: If you redid today, what would you do differently? Any changes to your workflow?"*

Capture the answer.

### Q5 — Artifacts

> *"Q5: What did you build or produce today? Paste any links — commits, repos, screenshots, deployed URLs, anything you're proud of. (Type 'none' if nothing.)"*

Capture the answer. Format each URL as a markdown link.

---

## Stage 4 — Write the report

### Step 4.1 — Compose the OKF-conformant markdown

Using all the answers, compose the report. The file is:

`participants/<github-username>/day_<N>_reflection.md`

Template (replace `<PLACEHOLDERS>` with actual values from the interview):

```markdown
---
type: reflection
title: 'Day <N> — Reflection'
date: <YYYY-MM-DD>
author: <github-username>
day: <N>
tags: [reflection, day-<N>, training]
status: stable
---

# Day <N> Reflection — <full_name>

## What I did today

<formatted answer from Q1 — bullet points if the participant listed multiple things>

## What I learned

<formatted answer from Q2>

## What was hard

<formatted answer from Q3>

## What I'd do differently

<formatted answer from Q4>

## Artifacts

<formatted answer from Q5 — markdown links for URLs>

---

## Concept cross-links

<if Q2 mentioned wiki concepts, list them as [[Wikilinks]] here. If none, omit this section.>
```

### Step 4.2 — Format guidelines

- Convert the participant's conversational answers into clean markdown bullet points or short paragraphs.
- Preserve the participant's voice — don't rewrite their meaning, just format it.
- Use bullet points (`-`) for lists of tools, exercises, or artifacts.
- Format URLs as markdown links: `[text](url)`.
- For concept cross-links, use Obsidian wikilinks: `[[MCard]]`, `[[CLM]]`, etc. Only link concepts that actually exist or are mentioned in the parent wiki.
- Set `status: stable` (the participant reviewed it verbally; it's done).
- If the participant wants to mark it as draft, use `status: draft`.

### Step 4.3 — Write the file

Write the composed markdown to:
```
participants/<github-username>/day_<N>_reflection.md
```

If the file already exists (overwrite confirmed in Step 2.1), overwrite it.

---

## Stage 5 — Commit and push

### Step 5.1 — Show the participant the report

Before committing, show the participant the full content of the file:

> *"Here's your Day <N> reflection. Review it — I'll commit once you say it looks good.*
>
> *(shows file content)*
>
> *Looks good? (yes/no/edit)"*

If the participant says "edit", ask what to change, make the edit, and re-show.

### Step 5.2 — Commit

Once the participant approves:

```bash
git add participants/<github-username>/
git commit -m "day <N> reflection — <full_name>"
```

### Step 5.3 — Push

```bash
git push origin main
```

### Step 5.4 — Confirm

> *"Done! Your Day <N> reflection is committed and pushed.*
>
> *File: `participants/<github-username>/day_<N>_reflection.md`*
> *Commit: `<commit-hash>`*
> *View on GitHub: [link to the file on github.com]"*

---

## Edge cases

### Participant hasn't set up git config

If `git config user.name` is empty:
> *"Your git user.name isn't set. Let's fix that first.*
>
> *What's your full name? I'll set it with: `git config user.name "<name>"`"*

### Participant hasn't forked/cloned the repo

If the participant is working in a directory that isn't a git repo, or the remote isn't set:
> *"It looks like you're not in the abad git repo. Make sure you've cloned it first:*
> *`git clone git@github.com:gasingtraining/abad.git`*
>
> *If you've forked it, clone your fork instead. What's your fork's URL?"*

### Participant wants to skip questions

If the participant says "skip" to a question, leave that section in the file with a note:
```markdown
## What was hard

*(skipped by participant)*
```

### Participant is offline

If `git push` fails because there's no internet:
> *"Commit saved locally, but I couldn't push — you're offline. Run `git push` later when you have internet."*

---

## OKF conformance

This skill produces OKF-conformant concept documents:
- **Required `type:` field** — set to `reflection`.
- **YAML frontmatter** — delimited by `---`.
- **Markdown body** — standard markdown with structural headings.
- **Producer-defined keys** — `author`, `day`, `status` are extensions (allowed by OKF §4.1).

See [`resources/okf-spec.md`](../../resources/okf-spec.md) for the full OKF spec.

---

## Reference

- [Participants README](../../participants/README.md) — structure and instructions
- [Daily reflection template](../../participants/_template/daily-reflection.md) — the blank template
- [OKF spec](../../resources/okf-spec.md) — Open Knowledge Format reference
- [AGENTS.md R15](../../AGENTS.md) — rule: participant reports live in `participants/<github-username>/`
