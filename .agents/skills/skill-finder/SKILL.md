---
name: skill-finder
description: "Use when a participant asks 'what skills do I have', 'what can you do', 'which skill should I use', 'help me find a skill', '/skills', or '/skill finder'. Lists every skill available in this repo with a description, when to use it, and the command to invoke it. Also explains the OKF bundle at ../../resources/okf/ where every tool, tech stack component, and skill is documented as an OKF concept."
---

# Skill Finder Skill — 5-Day AI Builder Training

## When to use

The participant says any of:
- "what skills do I have?"
- "what can you do?"
- "which skill should I use?"
- "help me find a skill"
- "/skills"
- "/skill finder"
- "list skills"
- "what are the skills in this repo?"

## What this skill does

Lists every skill available in the abad repo, with:
- The skill name
- What it does (one sentence)
- When to use it (trigger phrases)
- The command to invoke it
- The location of its `SKILL.md` file

Also points the participant to the **OKF bundle** at `../../resources/okf/` where every tool, tech stack component, and skill is documented as an OKF concept document with YAML frontmatter.

---

## All skills in this repo

There are **7 skills** in `.agents/skills/`. Here is the complete list:

### 1. `setup` — Two-stage onboarding

**What it does:** Sets up the participant's machine for the training. Stage 1 configures GLM 5.2 (the AI model) with their LiteLLM API key. Stage 2 auto-installs all missing tools (Git, Node.js, Python, Ollama, models, ChromaDB, Docker, BMAD).

**When to use:** Day 0 (before training) or whenever the participant says:
- "setup"
- "set up my machine"
- "install the training stack"
- "get me ready"

**Location:** `.agents/skills/setup/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/setup.md`

---

### 2. `prereq-checker` — Scan machine for missing tools

**What it does:** Scans the participant's machine for every tool, model, config, and credential the training requires. Prints a clear green/red report showing what's installed and what's missing.

**When to use:** Before setup, after setup, or any time the participant says:
- "what am I missing?"
- "check my setup"
- "am I ready?"
- "what's missing on my machine?"
- "/check-prereqs" or "/readiness"

**Location:** `.agents/skills/prereq-checker/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/prereq-checker.md`

---

### 3. `daily-report` — End-of-day reflection

**What it does:** Guides the participant through writing a daily reflection. Auto-detects their GitHub username from git config, interviews them about what they did/learned/struggled with, writes an OKF-conformant report to `participants/<github-username>/day_N_reflection.md`, commits, and pushes.

**When to use:** End of every training day (Day 1-5), or when the participant says:
- "daily report"
- "reflection"
- "report my day"
- "write my daily reflection"
- "/daily"

**Location:** `.agents/skills/daily-report/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/daily-report.md`

---

### 4. `onboarding` — Full phased install (Windows-focused)

**What it does:** Ilham's original onboarding skill. Full phased install with MCP servers, Obsidian vault creation, and Google OAuth setup. Windows-focused.

**When to use:** After `setup` if the participant wants the full setup (MCP, Obsidian, OAuth), or when they say:
- "onboard me"
- "onboard me for the training"
- "/onboard"

**Location:** `.agents/skills/onboarding/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/onboarding.md`

---

### 5. `skill-finder` — List all available skills (this skill)

**What it does:** Lists every skill in the repo with descriptions, trigger phrases, and locations. Also points to the OKF bundle.

**When to use:** When the participant is unsure which skill to use, or says:
- "what skills do I have?"
- "what can you do?"
- "/skills" or "/skill finder"

**Location:** `.agents/skills/skill-finder/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/skill-finder.md`

---

### 6. `glm-setup` — Configure GLM 5.2

**What it does:** Configures GLM 5.2 for OpenCode via the LiteLLM Gateway. Prompts for a virtual key, writes global stored credentials (`auth.json`) and `opencode.json`, and runs strict verification checks.

**When to use:** When configuring or setting up GLM 5.2, or when the participant says:
- "configure GLM"
- "set up GLM for opencode"
- "GLM setup"

**Location:** `.agents/skills/glm-setup/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/glm-setup.md`

---

### 7. `obsidian-cli` — Obsidian CLI Integration

**What it does:** Enables the agent to query, search, and manage notes, tasks, properties, and more in active Obsidian vaults directly via the Obsidian CLI.

**When to use:** When the participant wants to manage notes, search vault content, perform vault operations from the command line, or develop and debug Obsidian plugins and themes.

**Location:** `.agents/skills/obsidian-cli/SKILL.md`

**OKF concept doc:** `../../resources/okf/skills/obsidian-cli.md`


---

### 7. `obsidian-cli` — Obsidian CLI Integration

**What it does:** Enables the agent to query, search, and manage notes, tasks, properties, and more in active Obsidian vaults directly via the Obsidian CLI.

**When to use:** When the participant wants to manage notes, search vault content, perform vault operations from the command line, or develop and debug Obsidian plugins and themes.

**Location:** `.agents/skills/obsidian-cli/SKILL.md`

**OKF concept doc:** `okf/skills/obsidian-cli.md`


---

## How to invoke a skill

In opencode or Antigravity, just say the skill name or trigger phrase:

```
> setup          # invokes the setup skill
> daily report      # invokes the daily-report skill
> what am I missing # invokes prereq-checker
```

The AI reads the matching `SKILL.md` file and follows its instructions.

---

## The OKF bundle — `../../resources/okf/`

Every tool, tech stack component, and skill is also documented as an **OKF concept document** (Open Knowledge Format — see [`resources/okf-spec.md`](../../resources/okf-spec.md)). These are at:

```
../../resources/okf/
├── index.md              # Catalog of all OKF concept documents
├── log.md                 # Update history
├── tools/                 # One file per tool
│   ├── git.md
│   ├── nodejs.md
│   ├── python.md
│   ├── ollama.md
│   ├── gemma3.md
│   └── ...
├── tech-stack/            # One file per tech stack component
│   ├── glm52.md
│   ├── litellm.md
│   ├── opencode.md
│   ├── pkc.md
│   ├── mcard.md
│   ├── clm.md
│   └── ...
└── skills/                # One file per skill
    ├── setup.md
    ├── prereq-checker.md
    ├── daily-report.md
    └── ...
```

Each file has YAML frontmatter with at minimum a `type:` field (required by OKF). Browse the bundle at [`../../resources/okf/index.md`](../../resources/okf/index.md).

---

## Decision guide — which skill should I use?

| If the participant wants to... | Use this skill |
|:---|:---|
| Set up their machine for the first time | `setup` |
| Configure GLM 5.2 (API key, base URL, verify) | `glm-setup` |
| Check what's installed / missing | `prereq-checker` |
| Write their end-of-day reflection | `daily-report` |
| Do a full phased install (MCP, Obsidian, OAuth) | `onboarding` |
| See what skills are available | `skill-finder` (this one) |
| Interact with Obsidian vault via command line | `obsidian-cli` |
| Learn about a specific tool or concept | Read the OKF bundle at `okf/` |
| Understand the training rules | Read `docs/participant-guide.md` |

---

## Reference

- [AGENTS.md](../../AGENTS.md) — the operating manual for AI agents (rules R1-R15)
- [OKF spec](../../resources/okf-spec.md) — Open Knowledge Format reference
- [Participant guide](../../resources/participant-guide.md) — rules for participants
- [Participants README](../../participants/README.md) — daily reflection structure
