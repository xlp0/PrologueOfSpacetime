# Local Model + MCP Workshop Setup (IT Dell)

> Decision log + setup guide for the few-days workshop demo. The goal: students see a **fully local AI agent** (no cloud, no API keys paid by them) drive real tools — read their Gmail, write to an Obsidian vault — from a standard school Dell laptop.

Supersedes the "no install required, browser-only" scope in [[pitch_10_minute]] and [[pre_workshop_install_list]] for this specific workshop. The browser-based pitch still stands as the *opening* pitch; this doc covers the *hands-on day* scope expansion.

---

## 1. The model decision: Qwen2.5-3B-Instruct

### Why this model

Three hard constraints shaped the pick:

1. **Standard Dell laptops, no GPU.** 16GB RAM, modern i5/i7, integrated graphics. Anything 7B+ at Q4 feels sluggish on CPU (3-5 tok/s). 3B at Q4 runs at 10-20 tok/s — feels live.
2. **MCP tool calls must be reliable.** The whole demo rests on the model emitting valid tool-call JSON. 1B-class models (Tessera-1B, MiniCPM5-1B, Qwen3-0.6B) drop or malform tool calls often enough to break a live demo.
3. **No "thinking tokens" delay.** Qwen3's `enable_thinking` mode emits reasoning tokens before the tool call — fine in production, but in front of students it looks like the agent is stuck for 5-10s. Qwen2.5 emits the tool call directly.

### Specs

| Field | Value |
| :--- | :--- |
| Model | `Qwen/Qwen2.5-3B-Instruct` |
| Released | **September 19, 2024** (~21 months old at workshop time — mature, every edge case documented) |
| Parameters | 3.09B (2.77B non-embedding) |
| Architecture | Decoder-only transformer, RoPE, SwiGLU, RMSNorm, GQA (16 Q / 2 KV heads), tied embeddings |
| Layers / d_model | 36 / 2048 |
| Context length | 32,768 tokens (generation up to 8,192) |
| Languages | 29+ (English, Chinese, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, …) |
| Ollama tag | `qwen2.5:3b` |
| Disk (Q4_K_M) | 1.9 GB |
| License | **Qwen Research License** (not Apache 2.0 — the 3B and 72B sizes are under Qwen license; 0.5B/1.5B/7B/14B/32B are Apache 2.0) |
| HuggingFace | https://huggingface.co/Qwen/Qwen2.5-3B-Instruct |
| Ollama page | https://ollama.com/library/qwen2.5:3b |

### Pull command

```powershell
ollama pull qwen2.5:3b
```

That's it. ~1.9 GB download, runs on CPU out of the box.

### What it can do reliably

- Single-shot MCP tool calls (read a note, write a note, fetch an email, send one Telegram message) — yes.
- Multi-step agent loops with retries on failure — yes, with scaffolding (opencode provides the loop).
- Long-context up to 32K — yes, fits a full Obsidian vault slice.
- Multilingual — yes (relevant if students prefer Bahasa Indonesia / Chinese / etc.).

### What it cannot do

- 24/7 autonomous long-horizon agency. That's a 70B+ problem or a tightly-scoped state machine — not a 3B problem. **Pitch it as a "next step" on the closing slide, do not demo it live.**
- Complex reasoning over many turns. Keep demo prompts concrete and bounded.
- Whisper-quality transcription, code generation at GPT-5 level, etc. It's a 3B — set expectations honestly.

---

## 2. Why not other options

| Alternative | Why not (for this workshop) |
| :--- | :--- |
| **Tessera-1B** (newest 1B on HF, ~14h old at time of research) | Honest weak-cognition base model, not a usable assistant. Indie safety-research artifact, ~$315 to train, would fail mid-demo. |
| **MiniCPM5-1B** (released May 2026) | Strong for 1B, claims SOTA, but tool-call reliability is still 1B-tier. Custom `LlamaForCausalLM` arch means non-standard quirks. Risk too high for live demo. |
| **Qwen3:8b / Qwen3:14b** (already installed on Henry's machine) | Thinking tokens make the agent look stuck during live demo. 8B on CPU is sluggish (3-5 tok/s) on student Dells. Save these for the post-workshop "advanced" track. |
| **Llama 3.2 3B** | Fine fallback. Slightly worse tool-call reliability than Qwen2.5-3B in our use case. Pick if Qwen license is a blocker. |
| **Hermes-3-Llama-3.1-8B** (Nous Research) | No 3B variant exists. Would force us back to 8B / GPU territory. Mention as reference architecture, don't install. |
| **GLM 5.2** (powers Henry's opencode) | Cloud/proxy hosted — defeats the "fully local" demo point. |

---

## 3. Workshop demo objectives

### The demo goal, one sentence

> A student opens a terminal on a school Dell, types `opencode`, asks the agent in plain English to "find my latest Gmail and summarize it into an Obsidian note" — and watches the agent call Gmail via MCP, read the email, call Obsidian via MCP, write the note, and confirm. All local model. No cloud API keys paid by the student.

### What success looks like (live, on-stage)

1. Student runs `opencode` in PowerShell.
2. Student asks: *"Read my latest Gmail and write a 3-bullet summary to my Obsidian vault under today's date."*
3. Agent (Qwen2.5-3B + opencode) does, in order:
   - Calls `google_workspace_mcp` → `list_gmail_messages` → `get_gmail_message(id)`
   - Calls `obsidian_mcp` → `create_note(path, content)`
   - Replies in chat with the 3-bullet summary + the file path it wrote
4. Student opens Obsidian → the new note is there.

Total wall time: under 60 seconds.

### Stretch objectives (only if base demo works on the rehearsal pass)

- Cross-tool: "Find the email, then add a Google Calendar event based on it, then write the Obsidian note linking both." Three MCP calls, one prompt.
- Skills: install `caveman` skill mid-session to show how skills shape agent behavior.
- Slides: "Generate a 3-slide Google Slides deck from the email summary." (Uses the same `google_workspace_mcp` server — it covers Slides too.)

### Out of scope (do NOT demo live — closing slide only)

- **WhatsApp bot.** No official bot API for personal accounts. All paths unofficial (Baileys via OpenClaw, `whatsapp-web.js`) → ban risk, QR re-pair mid-demo. Pitch it, don't demo it.
- **24/7 always-on agent.** A school Dell that closes at 5pm cannot host a 24/7 agent. Mention as a "next step" with OpenClaw on a Raspberry Pi / VPS as the reference architecture.
- **Gmail OAuth live.** The consent screen is the highest failure point of the whole stack. Pre-record a 90-second clip of the OAuth flow as a fallback; rehearse it once live before the demo.

---

## 4. Pre-install checklist (per student laptop)

> **Flow:** OpenCode is installed **first** — it then assists the student with installing everything else. The few manual items (Google OAuth browser consent, ZeroTier network join, Obsidian vault creation) are flagged. Full ordered procedure is in [[pre_workshop_install_list]] §Installation Order.

### 4.1 Phase 0 — Manual prerequisites (before OpenCode)

| Tool | What it is | Install cmd / link | Notes |
| :--- | :--- | :--- | :--- |
| OS admin access | The student's account must be an admin | — | OpenCode needs to install software system-wide. |
| A shell | Terminal / PowerShell / WSL2 | macOS: Terminal.app. Windows: WSL2 recommended. | OpenCode runs in the shell. |
| A browser | Chrome / Edge / Firefox | — | For Google OAuth consent + account signups. |
| Git | Version control + cloning MCP servers | https://git-scm.com | `git --version` should work in the shell. |

### 4.2 Phase 1 — Install OpenCode FIRST (the foundation)

| Tool | What it is | Install cmd / link | Notes |
| :--- | :--- | :--- | :--- |
| **OpenCode** | Terminal AI coding harness — the agent that installs everything else | https://opencode.ai | Run `opencode` in the shell to confirm it launches. |

### 4.3 Phase 2 — Grant OpenCode machine access (one-time, manual)

The student explicitly grants OpenCode access so it can really assist. Without this, OpenCode is sandboxed and cannot install software.

| Permission | What it does | Action |
| :--- | :--- | :--- |
| Filesystem access | Read/write files outside its own directory | Approve home-directory access in the OpenCode prompt. macOS: grant Full Disk Access if asked. |
| Shell / bash permission | Run install commands (`brew install`, `uv pip`, `git clone`, `ollama pull`) | Set bash to `allow` for the install session, or approve each command. |
| External directory access | Read/write `~/.config/opencode/`, `~/.zshrc`, `~/.google_workspace_mcp/` | Approve `~/` access during install. |

### 4.4 Phase 3 — OpenCode assists with the rest (agent-driven)

The student asks OpenCode (in plain English) to install each of these. OpenCode runs the commands; the student approves and provides passwords/OAuth as needed.

| Tool | What it is | Install cmd / link | Notes |
| :--- | :--- | :--- | :--- |
| **Ollama** | Local model runner | https://ollama.com/download | One binary, Windows/macOS installer. OpenCode can run the installer. |
| **Qwen2.5-3B** | The model | `ollama pull qwen2.5:3b` | 1.9 GB download. Ask OpenCode to run it. |
| **Node.js 22+** | Required by opencode + most MCP servers | https://nodejs.org | LTS recommended. OpenCode can install via `brew` or `winget`. |
| **Docker Desktop** | Container runtime (for Ollama containers, mem0) | https://www.docker.com/products/docker-desktop | OpenCode can run the installer. |
| **ZeroTier** | Secure overlay network (Toba/GLM2 access) | https://www.zerotier.com/download/ | Install is agent-driven; joining the network ID is manual (Phase 4). |
| **Netbird** | WireGuard-based mesh VPN (peer-to-peer agent demos) | https://netbird.io/download | Install is agent-driven; login is manual (Phase 4). |
| **Hermes** | Open-source autonomous agent (Nous Research) | https://github.com/NousResearch/hermes | Ask OpenCode to clone + run setup. |
| **Obsidian** | The vault the agent writes to | https://obsidian.md | Free. Install is agent-driven; vault creation is manual (Phase 4). |
| **Obsidian Local REST API plugin** | Required by the Obsidian MCP server | Obsidian → Community plugins → search "Local REST API" | Manual: install inside Obsidian GUI. Generates API key + runs localhost HTTPS on port 27124. |

### 4.5 Phase 4 — Manual verification items (student must do these themselves)

These cannot be delegated to OpenCode — they require the student's hands on a browser or a GUI.

| Item | Why manual | Action |
| :--- | :--- | :--- |
| **Google Cloud OAuth credentials** | Requires Google account login in a browser | Follow [[installing_google_workspace_mcp]] Phases 1–3. OpenCode then writes the env vars to `~/.zshrc` and the `opencode.json` entry. |
| **Google OAuth consent (one-time)** | Opens in browser; student picks account and clicks Allow | Triggered automatically on first google-workspace tool call. |
| **ZeroTier network join** | Network ID + login is browser-based | Install is agent-driven; join the network ID given by the instructor. |
| **Netbird login** | Browser-based login | Install is agent-driven; peer setup is manual. |
| **GitHub account + SSH key** | Account creation is browser-based | Sign up at github.com; ask OpenCode to generate the SSH key and add it to GitHub. |
| **Obsidian vault creation** | GUI app, vault folder picker | Install is agent-driven; create the vault in `~/Documents/MyVault` manually. |
| **Obsidian Local REST API plugin** | Community plugin install inside Obsidian GUI | Install Obsidian → Settings → Community plugins → search "Local REST API" → enable. Copy the API key — OpenCode will write it into `opencode.json`. |

### 4.6 Phase 5 — Smoke test (agent-driven)

The student asks OpenCode to verify the install end-to-end:

1. *"List my Google calendars"* → confirms Google Workspace MCP + OAuth.
2. *"Pull the qwen2.5:3b model and run a test prompt"* → confirms Ollama + model.
3. *"Ping the ZeroTier network"* → confirms networking.
4. *"Clone the Hermes repo and run its --help"* → confirms Hermes.
5. *"Create a test note in my Obsidian vault"* → confirms Obsidian MCP.

If all five return successfully, the student is ready for the workshop.

---

## 5. MCP servers

### 5.1 Google Workspace MCP (Gmail + Slides + Calendar + Drive + Docs + Sheets + Chat + Forms + Tasks)

**Primary pick:** `taylorwilsdon/google_workspace_mcp`

| Field | Value |
| :--- | :--- |
| Repo | https://github.com/taylorwilsdon/google_workspace_mcp |
| Stars | ~2.8k |
| Language | Python |
| Coverage | Gmail, Calendar, Docs, Sheets, **Slides**, Chat, Forms, Tasks, Drive |
| Auth | OAuth 2.0 (per-user Google login) |
| Why this one | One server covers Gmail *and* Slides — meets both demo objectives without a second MCP install. Most stars, most active maintenance. |

**Lighter alternatives** (only if the primary has install issues on student Dells):

- `matteoantoci/google-slides-mcp` — Slides-only, TypeScript, 182 stars. https://github.com/matteoantoci/google-slides-mcp
- `piotr-agier/google-drive-mcp` — Drive + Docs + Sheets + Slides + Calendar, TypeScript, 182 stars. https://github.com/piotr-agier/google-drive-mcp

### 5.2 Obsidian MCP

**Primary pick:** `MarkusPfundstein/mcp-obsidian`

| Field | Value |
| :--- | :--- |
| Repo | https://github.com/MarkusPfundstein/mcp-obsidian |
| Stars | ~4k |
| Language | Python |
| Requires | Obsidian Local REST API community plugin (installed in Obsidian, not the MCP server) |
| Why this one | Most adopted, most documented. Uses the REST API the Local REST API plugin exposes — clean separation between vault and agent. |

**Alternatives** (no Obsidian plugin required — talk directly to vault files):

- `bitbonsai/mcpvault` — 1.5k stars, TypeScript, "safe vault access" without exposing a REST endpoint. Good if students hit trouble installing the Obsidian plugin. https://github.com/bitbonsai/mcpvault
- `cyanheads/obsidian-mcp-server` — 618 stars, TypeScript, STDIO or Streamable HTTP. https://github.com/cyanheads/obsidian-mcp-server
- `aaronsb/obsidian-mcp-plugin` — 430 stars, native Obsidian plugin with semantic search. https://github.com/aaronsb/obsidian-mcp-plugin

---

## 6. Skills

### 6.1 Browse skills

- **skills.sh** — Vercel-hosted skill marketplace for Claude Code / opencode-compatible skills. Browse during the "find the right tool" exercise on Day 3 of the sprint. https://skills.sh
- **mcp.so** — MCP server directory. Pairs with skills.sh for the research exercise. https://mcp.so

### 6.2 Skill to demo live (optional)

- **Caveman skill** — token-cost cutter. Already installed on Henry's vault at `.agents/skills/caveman/`. Easy visible behavior change ("talk like caveman") that students immediately grasp: skills shape agent behavior. Drop-in for the demo. https://github.com/IlhamAkbarSKoo/caveman-skills (or copy from Henry's `Koo/.agents/skills/caveman/`).

### 6.3 opencode native skills support

opencode reads `.agents/skills/<skill-name>/SKILL.md` files in the working directory. Same convention as Claude Code. No extra install — students just drop a `SKILL.md` into `.agents/skills/` and opencode picks it up.

---

## 7. opencode configuration (student-side)

`opencode.jsonc` snippet pointing opencode at the local Ollama + wiring the two MCP servers:

```jsonc
{
  "model": "qwen2.5:3b",
  "provider": "ollama",
  "providers": {
    "ollama": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:11434/v1"
    }
  },
  "mcp": {
    "google_workspace": {
      "type": "local",
      "command": ["python", "-m", "google_workspace_mcp"],
      "env": {
        "GOOGLE_CLIENT_ID": "<student-oauth-client-id>",
        "GOOGLE_CLIENT_SECRET": "<student-oauth-client-secret>"
      }
    },
    "obsidian": {
      "type": "local",
      "command": ["python", "-m", "mcp_obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "<from-local-rest-api-plugin>",
        "OBSIDIAN_BASE_URL": "https://127.0.0.1:27124"
      }
    }
  }
}
```

Henry has the reference config in `Koo/opencode.jsonc` (mem0 MCP entry there) — adapt that template for students.

---

## 8. Reference architectures (closing slide, not demo)

| Project | What it shows | Link |
| :--- | :--- | :--- |
| **OpenClaw** (Peter Steinberger, 382k stars) | 22-channel personal agent gateway (WhatsApp, Telegram, Slack, Discord, Signal, iMessage, …). Uses Baileys for WhatsApp (linked-device pairing via QR, no official API). Reference architecture for the "always-on 24/7 agent on a Raspberry Pi" pitch. | https://github.com/openclaw/openclaw · https://docs.openclaw.ai/channels/whatsapp |
| **Hermes** (Nous Research) | Open-source autonomous agent family. Mention as "where this grows up" — students who want the 24/7 agent path graduate to Hermes. | https://github.com/NousResearch/hermes |
| **Twilio WhatsApp Business API** | The only sanctioned WhatsApp bot path. Costs money + business verification (days). Mention as the "production" answer to "but I want WhatsApp." | https://www.twilio.com/whatsapp |

---

## 9. What NOT to demo live (risk register)

| Risk | Mitigation |
| :--- | :--- |
| Gmail OAuth consent screen fails or confuses students | Pre-record 90-second clip of the OAuth flow. Rehearse once live. Use the clip as fallback. |
| WhatsApp Baileys pairing breaks mid-demo (QR expires, number ban) | Don't demo WhatsApp. Pitch on closing slide with OpenClaw as the reference. |
| 3B model hallucinates a malformed tool call | Keep demo prompts concrete. Have a backup prompt ready. Rehearse the exact demo flow 3+ times before workshop. |
| School network blocks Ollama localhost port | Ollama binds 127.0.0.1:11434 by default — should not be affected by school network. Verify on a school Dell before workshop day. |
| Obsidian Local REST API plugin HTTPS cert rejected | Add cert exception in browser once during setup, not live. |
| Student Dell too slow (less than 8GB RAM) | Pre-check: 16GB minimum. Filter students during registration. |

---

## 10. Rehearsal plan (Henry, before workshop day)

1. **End-to-end on a fresh school Dell** — install everything from scratch, run the full demo. Time it. Fix every friction point. Target: under 30 min from `ollama pull` to working demo.
2. **Failure-mode rehearsal** — break the OAuth flow on purpose, break the Obsidian plugin on purpose, watch the model fail a tool call. Know what each failure looks like and how to recover live.
3. **Record the 90-second OAuth fallback clip** — same machine, same network, in case the live OAuth flow hiccups.
4. **Test on school network** — verify Ollama localhost works, verify Google OAuth redirects work, verify no proxy intercepts localhost.
5. **Print the one-page student install checklist** — items 4.1 to 4.8 only. Don't include this whole doc.

---

## Related

- [[pre_workshop_install_list]] — the broader install list this scope expands.
- [[pitch_10_minute]] — the opening pitch (browser-based, no install). This doc is the hands-on day that follows the pitch.
- [[sprint_outline]] — the 5-day sprint structure. The local-model demo fits Day 4 ("Letting AI Run").
- [[presentation_plan]] — full presentation plan to update if scope changes.
- [[installing_google_workspace_mcp]] — verified step-by-step OAuth + OpenCode config procedure for the `taylorwilsdon/google_workspace_mcp` server picked in §5.1. Use that guide for the actual install; this doc is the workshop scope + model decision.

---

*Drafted 2026-07-07. Model pick: Qwen2.5-3B-Instruct. Decision final pending rehearsal on a school Dell.*
