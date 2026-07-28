---
name: setup
description: "Use when the user says 'setup', '/setup', 'help me set up', 'set up my machine', 'install the training stack', 'get me ready', or asks anything about installing/configuring the 5-day training stack. setup works in THREE STAGES: Stage 0 scans the participant's hardware and writes a profile to participants/<batch>/<github-username>/hardware.md (auto-pushed), Stage 1 verifies opencode has a working AI model configured (provider-agnostic: DeepSeek free tier by default, Ollama local as fallback, LiteLLM GLM 5.2 if the school provides a key), Stage 2 installs all remaining tools (git, Node.js, Python, Ollama, models, Netbird). setup scans, walks through model setup, installs everything automatically, and verifies. Works on macOS, Linux, and Windows. Requires opencode already installed."
---

# setup — Three-Stage Onboarding Agent

## When to use

The user says any of:
- "setup" / "/setup"
- "help me set up" / "set up my machine"
- "install the training stack" / "get me ready"
- "what do I still need?" / "what's missing?"

## Prerequisite

**opencode must be installed and running before invoking this skill.** opencode cannot bootstrap itself. The participant installs opencode manually (one command from https://opencode.ai), launches `opencode chat` in their terminal, then types `/setup`. This skill runs inside opencode.

## The Three Stages

setup works in three stages. **Stage 0 runs first** to capture a hardware snapshot so instructors can see each participant's machine before exercises begin. **Stage 1 is the most important** — it makes sure opencode has a working AI model, by any means (free DeepSeek key, local Ollama, or school-provided LiteLLM). Once that's done, Stage 2 installs everything else.

| Stage | What happens | Why this order |
|:---|:---|:---|
| **Stage 0 — Hardware scan + tool detection** | Detect GitHub username + batch → run `scripts/Scan-Hardware.ps1` (or `.sh`) → push `hardware.md` to `participants/<batch>/<github-username>/` → confirm opencode is running | Captures a baseline snapshot of each participant's machine on Day 1. Instructors can spot weak machines before exercises begin. |
| **Stage 1 — opencode model setup (provider-agnostic)** | Check if opencode has any working model → if not, walk participant through `/connect` for DeepSeek (free, default), Ollama (local fallback), or LiteLLM GLM 5.2 (if school provides a key) → verify with a test prompt | The participant needs *some* working AI model so opencode can help with Stage 2. Any provider works — the school provides LiteLLM GLM 5.2 keys to the 50 selected students on Day 1 of the workshop, but for the filter test (or as a fallback) DeepSeek free tier or local Ollama works fine. |
| **Stage 2 — Install everything else** | Scan for missing tools → auto-install git, Node.js, Python, Ollama, models, Netbird → verify | With a working AI model in opencode, the participant can use opencode to help with the rest if anything goes wrong. |

> **Never skip Stage 1.** If no model is configured, opencode can't do anything — the participant has no AI tool. Stage 0 first, Stage 1 second, always. The model can be from any provider; we don't care which, as long as opencode works.

---

## Stage 0 — Hardware Scan + Tool Detection (DO THIS FIRST)

Stage 0 has two parts: **0A** captures a hardware snapshot and pushes it to abad so instructors can review the cohort's hardware before Day 1 exercises begin. **0B** confirms opencode is running (this skill runs inside opencode, so if the participant is reading this, opencode is already running).

### Step 0A.1 — Resolve batch

Read the batch from `participants/.current-batch`:

```bash
cat participants/.current-batch
```

If the file is missing or empty, ask the participant:
> *"I couldn't find the batch assignment file. Ask your instructor which batch you're in (e.g. `batch-2`), then tell me."*

Record the batch as `batch` for the rest of the session.

### Step 0A.2 — Auto-detect GitHub username

```bash
git config user.name
git remote get-url origin
```

Parse the username from the remote URL:
- `git@github.com:<github-username>/<repo>.git` → username is between `:` and `/`
- `https://github.com/<github-username>/<repo>.git` → username is between `github.com/` and `/`

PowerShell extraction:
```powershell
$url = git remote get-url origin
if ($url -match 'github\.com[:/]([^/]+)/') { $githubUsername = $Matches[1] }
```

Bash extraction:
```bash
url="$(git remote get-url origin)"
username="$(echo "$url" | grep -oE 'github\.com[:/][^/]+/' | sed -E 's#github\.com[:/]##; s#/$##')"
```

### Step 0A.3 — Verify with the participant

> *"I detected your GitHub username: `<github-username>`. Your hardware profile will be saved at `participants/<batch>/<github-username>/hardware.md`. Is this correct? If different, tell me your GitHub username."*

If the participant corrects it, use the new value. Sanitize to kebab-case (lowercase, no spaces, letters/numbers/hyphens/dots only).

> **Fork check:** If the detected username matches the org name (`gasingtraining`), the participant is probably working from a direct clone of the abad repo, not their fork. Tell them:
> *"It looks like you're working from the main abad repo, not your fork. To get your hardware file committed under your name, fork abad on GitHub first, then update your remote: `git remote set-url origin git@github.com:<your-username>/abad.git`. Or just tell me your GitHub username now and I'll use it."*

### Step 0A.4 — Run the hardware scanner

- **macOS/Linux:** `bash scripts/scan-hardware.sh --batch <batch> --username <github-username>`
- **Windows:** `powershell -File scripts/Scan-Hardware.ps1 -Batch <batch> -GithubUsername <github-username>`

The script:
1. Creates `participants/<batch>/<github-username>/` if it does not exist.
2. Captures: OS, CPU, RAM, disk free, GPU, Git version, Node.js version, Python version, Ollama version, Ollama models pulled.
3. Writes `hardware.md` with OKF frontmatter (`type: hardware-profile`).
4. Prints the file path on success.

### Step 0A.5 — Isolated commit + push

Use the reusable push script to commit ONLY the participant's hardware file:

- **macOS/Linux:** `bash scripts/push-participant-file.sh --path participants/<batch>/<github-username>/hardware.md --message "hardware profile - <github-username>"`
- **Windows:** `powershell -File scripts/Push-ParticipantFile.ps1 -Path "participants/<batch>/<github-username>/hardware.md" -Message "hardware profile - <github-username>"`

The push script:
1. Stages ONLY `participants/<batch>/<github-username>/hardware.md` (never `git add -A`).
2. Verifies the staged set with `git status --short`.
3. Commits with the given message.
4. Pushes to `origin/<current-branch>`.

**If push fails (network, auth, no fork set up):**
> *"Hardware profile saved locally at `participants/<batch>/<github-username>/hardware.md`, but I couldn't push to GitHub. This is probably a network issue or your fork isn't set up yet. Continuing to Stage 0B — you can push later with `git push`."*

Do not block on a push failure. Continue.

### Step 0A.6 — Confirm + continue

> *"Stage 0A done. Your hardware profile is at `participants/<batch>/<github-username>/hardware.md`. Instructors can see your machine specs now. Moving to Stage 0B — detecting your AI tool."*

### Step 0B — Confirm opencode is running

This skill runs inside opencode. If the participant is reading this, opencode is already running. Confirm:
> *"You're running this in opencode. GLM 5.2 will be configured for opencode. Config files go to `~/.config/opencode/`."*

No tool detection needed. Antigravity is not supported.

---

## Stage 1 — Get opencode Working with Any AI Model (DO THIS FIRST)

> **opencode needs *some* model configured to do anything.** We are provider-agnostic here: any working model counts. The school provides LiteLLM GLM 5.2 keys to the 50 selected students on Day 1 of the workshop, but for the filter test (or as a fallback) DeepSeek's free tier or a local Ollama model works fine. We don't care which provider — we care that opencode works.

### Step 1.1 — Check if opencode already has a working model

Ask the participant to run a test prompt:

> *"Stage 1: Making sure opencode has a working AI model.*
>
> *In your opencode session, just type: `hi, what model are you?` and hit enter.*
>
> *- If you get a response → great, opencode is working. Tell me what model it said, then we'll move on to Stage 2.*
> *- If opencode says 'no model configured' or shows a provider picker → continue below."*

**If they got a response:**
> *"Stage 1 complete — opencode is working with `<model>`. You have a working AI tool. Moving to Stage 2."*

Proceed to Stage 2.

**If no model is configured:**
Continue to Step 1.2.

### Step 1.2 — Help the participant pick a provider

Present the options in this order. **DeepSeek is the default recommendation** for the filter test (free, fast signup, no school infrastructure needed). LiteLLM GLM 5.2 is only used if the school has given them a key.

Say:
> *"opencode needs an AI model to work. Here are your options — pick one:*
>
> ***Option A — DeepSeek (RECOMMENDED, free, 2 minutes)** *
> *1. Go to https://platform.deepseek.com/ and sign up (any email)*
> *2. Click **Create new API key** and copy it (starts with `sk-`)*
> *3. In opencode, type `/connect`, select **DeepSeek**, paste your key, hit enter*
> *4. Type `/models` and pick `deepseek-chat` or `deepseek-reasoner`*
>
> ***Option B — Local Ollama (fully offline, no account, ~2 GB download)** *
> *1. We'll install Ollama in Stage 2 first — skip Stage 1 for now, come back after Stage 2 finishes*
> *2. Then in opencode, type `/connect`, select **Ollama**, no key needed*
> *3. Type `/models` and pick `qwen2.5:3b`*
>
> ***Option C — LiteLLM GLM 5.2 (school-provided, only if instructor gave you a key)** *
> *1. The school hosts GLM 5.2 at https://litellm.pkc.pub/ui/ — log in, create a virtual key*
> *2. Paste the key when I ask below — I'll configure it for you*
>
> *Which option do you want? (A/B/C):*"

Wait for the participant to pick. If they pick:
- **A (DeepSeek)** → Step 1.3A
- **B (Ollama)** → Step 1.3B
- **C (LiteLLM)** → Step 1.3C

### Step 1.3A — DeepSeek setup (participant-driven)

The participant does this themselves in opencode's `/connect` flow. setup doesn't run any scripts. Just guide them:

> *"DeepSeek setup — follow these steps in opencode:*
>
> *1. Open https://platform.deepseek.com/ in your browser*
> *2. Sign up with any email, verify it*
> *3. Click **Create new API key** — give it any name, copy the key (starts with `sk-`)*
> *4. Back in opencode, type `/connect`*
> *5. Use arrow keys to find **DeepSeek**, hit enter*
> *6. Paste your key, hit enter*
> *7. Type `/models`, select `deepseek-chat`*
> *8. Now type `hi, what model are you?` to test it*
>
> *Tell me when you get a response, or if anything fails."*

**If they get a response:** Stage 1 complete. Continue to Stage 2.

**If `/connect` fails or DeepSeek returns errors:**
> *"DeepSeek not working? Try Option B (Ollama local) or Option C (LiteLLM) instead. Or check your internet connection."*

### Step 1.3B — Ollama local setup (deferred to Stage 2)

> *"Ollama local — we need to install Ollama first. Skipping to Stage 2 now. After Stage 2 finishes (Ollama installed + qwen2.5:3b pulled), come back and:*
>
> *1. In opencode, type `/connect`*
> *2. Select **Ollama** (no API key needed — it's local)*
> *3. Type `/models`, pick `qwen2.5:3b`*
> *4. Test with: `hi, what model are you?`*
>
> *Skipping to Stage 2 now."*

Proceed directly to Stage 2.

### Step 1.3C — LiteLLM GLM 5.2 setup (school-provided key)

This is the original flow — only used when the school has provided the participant with a LiteLLM API key. setup runs the setup script to write `.env` + `opencode.jsonc` automatically.

Say:
> *"LiteLLM GLM 5.2 setup — the school hosts GLM 5.2 on the LiteLLM gateway at `litellm.pkc.pub`. You don't install or run the model yourself — you just get an API key (like an OpenAI key, but sovereign) and opencode will use it.*
>
> *Here's how to get your key:*
>
> *1. Open your browser and go to: https://litellm.pkc.pub/ui/*
> *2. Log in (ask your instructor for credentials if you don't have them)*
> *3. Click **Virtual Keys** on the left sidebar*
> *4. Click **+ Create Key***
> *5. Fill in: User ID (your name), Key Alias (e.g. 'my-key'), Max Budget ($20), Models (glm-5.2), RPM Limit (60)*
> *6. Click **Create***
> *7. **Copy the key immediately** — it starts with `sk-` and is shown only once*
>
> *Your key stays on your machine only — in a `.env` file. It's never committed to git, never shared.*
>
> *Paste your key here (sk-...):*"

Wait for the participant to paste the key. Validate:
- Starts with `sk-`? If not, warn but let them continue.
- Empty? Don't proceed — ask again.

Once the key is in hand, setup runs the setup script:
- **macOS/Linux:** `bash scripts/setup-glm52-litellm.sh -k <key>`
- **Windows:** `powershell -File scripts/Setup-Glm52Litellm.ps1 -ApiKey <key>`

This:
1. Creates `~/.config/opencode/.env` with `LITELLM_API_KEY`, `LITELLM_BASE_URL`, `LITELLM_MODEL`
2. Writes `~/.config/opencode/opencode.jsonc` with the LiteLLM provider config
3. Pings the gateway (`/models` endpoint) to verify the key works
4. Reports success or failure

**If the gateway returns 200 OK:**
> *"Stage 1 complete. You now have access to the school's GLM 5.2 — your AI tool is ready. You can now launch opencode with `opencode chat` and it will call GLM 5.2 on the school's gateway. You don't run the model yourself; opencode sends requests to `litellm.pkc.pub` and gets responses back. Moving to Stage 2 to install the remaining tools."*

**If the gateway fails (401/403):**
> *"The gateway rejected your key. Go back to the dashboard and create a new key, then paste it here again."*

Go back to Step 1.3C.

**If the gateway is unreachable (network):**
> *"The gateway at litellm.pkc.pub is not reachable. Check your internet connection. If you're on a restricted network, ask the instructor for an alternative endpoint — or switch to Option A (DeepSeek) for now."*

### Step 1.4 — Stage 1 complete

At this point, the participant has a working AI model in opencode — from any provider:
- **DeepSeek free tier** (most common for filter test) — `/connect` flow, key in opencode's auth store
- **Local Ollama** (offline) — `/connect` flow, no key needed
- **LiteLLM GLM 5.2** (school-provided) — `.env` + `opencode.jsonc` configured

setup should tell the participant:
> *"Stage 1 done. opencode has a working model (`<provider>`). If you want to test it right now, type a message. Otherwise, I'll continue to Stage 2 to install the rest of the training stack.*
>
> *Note: the school provides GLM 5.2 keys to selected participants on Day 1 of the workshop. If you're using DeepSeek or Ollama now, you can switch to GLM 5.2 later by running `/setup` again and picking Option C."*

---

## Stage 2 — Install Everything Else

### Step 2.1 — Scan for missing tools

Run the full prerequisite scanner:
- **macOS/Linux:** `bash scripts/check-prereqs.sh`
- **Windows:** `powershell -File scripts/Check-Prereqs.ps1` (or `scripts/Test-Prereqs.ps1`)

Read the report. List every FAIL item:
> *"Stage 2: Installing missing tools. I found these: [list]. I'll install them all now."*

### Step 2.2 — Auto-install all missing tools

setup installs each missing tool automatically. The participant only approves OS password prompts when they appear.

**macOS install commands:**

| # | Tool | Command |
|:---|:---|:---|
| 1 | Git | `xcode-select --install` (or already installed) |
| 2 | Node.js 22+ | `brew install node` |
| 3 | Python 3.10+ | `brew install python@3.12` |
| 4 | uv | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| 5 | Ollama | `curl -fsSL https://ollama.com/install.sh \| sh` |
| 6 | qwen2.5:3b | `ollama pull qwen2.5:3b` |
| 7 | nomic-embed-text | `ollama pull nomic-embed-text` |
| 8 | Netbird | `brew install --cask netbird` |

**Linux install commands:**

| # | Tool | Command |
|:---|:---|:---|
| 1 | Git | `sudo apt-get install -y git` |
| 2 | Node.js 22+ | `curl -fsSL https://deb.nodesource.com/setup_22.x \| sudo -E bash - && sudo apt-get install -y nodejs` |
| 3 | Python 3.10+ | `sudo apt-get install -y python3 python3-pip` |
| 4 | uv | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| 5 | Ollama | `curl -fsSL https://ollama.com/install.sh \| sh` |
| 6 | qwen2.5:3b | `ollama pull qwen2.5:3b` |
| 7 | nomic-embed-text | `ollama pull nomic-embed-text` |
| 8 | Netbird | `curl -fsSL https://pkgs.netbird.io/install.sh \| sh` |

**Windows install commands (PowerShell / winget):**

| # | Tool | Command |
|:---|:---|:---|
| 1 | Git | `winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements` |
| 2 | Node.js 22+ | `winget install --id OpenJS.NodeJS.LTS -e --accept-source-agreements --accept-package-agreements` |
| 3 | Python 3.10+ | `winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements` |
| 4 | uv | `powershell -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| 5 | Ollama | `winget install --id Ollama.Ollama -e --accept-source-agreements --accept-package-agreements` |
| 6 | qwen2.5:3b | `ollama pull qwen2.5:3b` |
| 7 | nomic-embed-text | `ollama pull nomic-embed-text` |
| 8 | Netbird | `winget install --id Netbird.Netbird -e --accept-source-agreements --accept-package-agreements` |

**How setup runs them:**
1. Install each tool in sequence.
2. Read the output of each command.
3. If a command fails, try a fallback method.
4. After each install, verify the tool is now present.
5. Report progress: *"✓ Node.js installed (v22.5.0)"*, *"⏳ Pulling qwen2.5:3b (1.9 GB — this takes a minute)..."*

> **Model pull warning:** Before pulling models, say: *"This will download ~2.2 GB of models. On slow internet this could take 5-15 minutes. Proceeding now..."*

> **Netbird note:** Netbird is installed now but NOT connected. Participants will connect to the instructor's mesh network on Day 4 (`netbird up --management-url https://vpn.pkc.pub`). Installing it here just saves time later.

### Step 2.3 — Verify everything is green

After all installs, re-run the scanner:
- **macOS/Linux:** `bash scripts/check-prereqs.sh`
- **Windows:** `powershell -File scripts/Check-Prereqs.ps1`

If everything is PASS:
> *"All checks passed. Here's what I installed: [summary]. You're ready for the training. To launch: `opencode chat`."*

If anything is still FAIL, address it — try an alternative method, or flag it as a manual step (GitHub account, Google OAuth, Obsidian vault).

### Step 2.4 — Day-1 handoff

> *"Machine ready. You're set for Day 1. Your first task: build a simple website by commanding AI. The full curriculum is at `Documents/abad/curriculum`. To start: `opencode chat`."*

---

## What setup does vs. what the participant does

| Task | Who |
|:---|:---|
| **STAGE 0** | |
| Tell setup their GitHub username (if auto-detect fails) | **Participant** (only if needed) |
| Fork abad on GitHub (if not already done) | **Participant** (browser, one-time) |
| Tell setup their batch (if `.current-batch` is missing) | **Participant** (only if needed) |
| Scan hardware | setup |
| Write `hardware.md` (now includes setup checklist) | setup |
| Commit + push hardware profile | setup |
| **STAGE 1** | |
| Pick a provider (DeepSeek free / Ollama local / LiteLLM GLM 5.2) | **Participant** |
| Sign up at DeepSeek + create key (Option A) | **Participant** (browser, ~2 min) |
| Run `/connect` in opencode + paste key | **Participant** (in opencode TUI) |
| Or: paste LiteLLM key (Option C, school-provided only) | **Participant** (only if school gave them a key) |
| Write `.env` + `opencode.jsonc` (LiteLLM path only) | setup |
| Verify gateway (LiteLLM path only) | setup |
| **STAGE 2** | |
| Scan machine | setup |
| Install git, Node.js, Python, uv | setup |
| Install Ollama + pull qwen2.5:3b + nomic-embed-text | setup |
| Install Netbird | setup |
| Approve OS password prompts | **Participant** (when OS asks) |
| GitHub account signup | **Participant** (browser) |
| Final verification | setup |

> **For the filter test (2000 candidates → 50 selected): participants pick DeepSeek (free, no school infrastructure needed). For the workshop (50 selected): school gives them LiteLLM GLM 5.2 keys on Day 1, they re-run `/setup` and switch to Option C.** setup does ~80% of the work. The participant picks a provider, signs up (browser), pastes a key into opencode's `/connect`, approves OS prompts, and handles 2-3 browser-based steps.

## Rules

- **Stage 0 first, then Stage 1, then Stage 2.** Never install tools before opencode has a working model. The model is the foundation.
- **Stage 0 push is best-effort.** If `git push` fails, warn the participant and continue to Stage 1. Do not block the onboarding flow on a push failure.
- **Stage 0 stages ONLY the participant's hardware file.** Never `git add -A` or `git add .`. Use `scripts/Push-ParticipantFile.ps1` (or `.sh`) which enforces this.
- **Stage 1 is provider-agnostic.** Any working model counts. DeepSeek free tier is the default recommendation (no school infrastructure needed). Ollama local works offline. LiteLLM GLM 5.2 is only used when the school provides a key. Never force LiteLLM — accept whatever the participant picks.
- **Never hardcode any API key** — keys go in `.env` only (LiteLLM path) or opencode's auth store (DeepSeek path via `/connect`). Never log or echo keys.
- **Auto-install everything in Stage 2** — setup runs the commands, not the participant.
- **Idempotent** — re-running setup resumes from where it left off. Stage 0 re-scans and overwrites the prior `hardware.md` (snapshots refresh, not append). Stage 1 re-checks for a working model and only walks through `/connect` if none is configured.
- **Cross-platform** — bash on macOS/Linux, PowerShell/winget on Windows.
- **opencode only** — this skill runs inside opencode. Antigravity is not supported. The participant must install opencode manually before invoking `/setup`.
