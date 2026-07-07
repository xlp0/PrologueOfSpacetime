# Pre-Workshop Install List (IT Dell)

> A consolidated list of every tool, package, model, service, and piece of hardware mentioned in the InaAI notes (markdown notes + YouTube summaries) that students may need installed or available before the workshop. Henry to triage to a "must-install" subset for students. Source: `InaAI/` vault, swept 2026-07-07.

---

## How to read this list

> **Start with the [Installation Order](#installation-order--opencode-is-the-foundation) section above** — it gives the phased flow: OpenCode first → grant machine access → OpenCode assists with the rest → manual verification. The tier tables below are the **what to install** reference that OpenCode reads from when assisting.

Each item is flagged with a status:

- **[INSTALL]** — core install, the user actively uses this
- **[OPTIONAL]** — alternative or optional, mentioned but not always adopted
- **[DISCUSSED]** — evaluated in notes/YouTube, not necessarily installed
- **[ACCOUNT]** — web service, no install — sign up only
- **[HARDWARE]** — physical device, not software

Henry: please trim to the **[INSTALL]** + **[ACCOUNT]** tiers for the student pre-install checklist. The **[OPTIONAL]** / **[DISCUSSED]** tiers are reference for Q&A and "where do I learn more" traffic.

> **2026-07-07 revision:** this list is now the **definitive pre-workshop install checklist**. Tier 8 was trimmed (removed Kubernetes/ArgoCD/nginx/MediaWiki/MariaDB/Matomo/Ansible stack — students don't touch these). ZeroTier + Netbird both promoted to required [INSTALL] (networking mesh for Toba access + peer-to-peer agent demos). Hermes promoted from [DISCUSSED] to [INSTALL] (students will work with it as the 24/7 agent reference architecture). See [[local_model_demo_setup]] for the hands-on demo scope and [[installing_google_workspace_mcp]] for the verified Google Workspace MCP install procedure.

---

## Background Concepts

> Three terms come up throughout this list: **harness**, **skills**, and **OKF** (Open Knowledge Foundation). Brief definitions so students and OpenCode itself have shared context before the install begins.

### Harness — the AI coding agent shell

A **harness** is the terminal/GUI application that hosts an AI agent, gives it tools (filesystem, shell, MCP servers), and routes the model's tool calls. The harness is the substrate; the model is the brain.

| Harness | Vendor | Notes |
|:---|:---|:---|
| **OpenCode** | open-source (sst) | **The workshop's chosen harness.** Terminal-based, reads `opencode.json`, supports `.agents/skills/`, MCP servers, subagents. Installed Phase 1. |
| Claude Code | Anthropic | Reference commercial harness; uses `AGENTS.md`/`CLAUDE.md`. Mentioned as comparison. |
| Cursor | Cursor Inc. | GUI harness, popular for IDE-native AI. |
| Codex | OpenAI | Harness alternative; uses `agents.md`. |
| Aider | open-source | Terminal harness, git-native. |

The student picks **one** harness. This workshop standardizes on OpenCode so the agent can install everything else for the student.

### Skills — drop-in agent behavior modules

A **skill** is a small markdown file (`SKILL.md`) that teaches an agent a specialized behavior, vocabulary, or workflow. Skills are the lightest extension mechanism — no code, no package, just a markdown prompt the harness loads on demand.

- **Location:** `.agents/skills/<skill-name>/SKILL.md` (opencode convention, same as Claude Code).
- **Marketplaces:**
  - **skills.sh** — Vercel-hosted marketplace for opencode/Claude Code-compatible skills. Browse during the workshop's "find the right tool" exercise.
  - **mcp.so** — MCP server directory. Pairs with skills.sh for research.
- **Examples:**
  - `caveman` — token-cost cutter; terse output. Demo'd live in the workshop.
  - `baoyu-youtube-transcript` — fetches YouTube transcripts + cover images.
  - `youtube-video-analyst` — forensic video deconstruction for content cloning.

A skill is **not** an MCP server. MCP servers expose external capabilities (Gmail, Drive, Obsidian). Skills shape how the agent reasons and responds. Both compose: an agent can have the `caveman` skill active while calling the `google_workspace_mcp` server.

### OKF — Open Knowledge Foundation

The **Open Knowledge Foundation (OKF)** is a UK-based non-profit (founded 2004) that promotes open knowledge and open data. It is **not** a Google product — the name is sometimes confused with Google's Knowledge Graph, but OKF is an independent standards body.

What OKF gives the workshop:

- **The Open Definition** — the canonical answer to "what does *open* mean?" for data and content. A workshop that calls itself "open" should meet this bar.
- **CKAN** — the open-source data management platform OKF maintains. Powers data.gov, europeandataportal.eu, and thousands of open data catalogs. Relevant if students want to publish datasets they generate.
- **Frictionless Data** — OKF's spec for tabular data with embedded schema (Data Package, Tabular Data Package). Pairs naturally with the project's CLM `Spec/Impl/Exp` triples.
- **Open Knowledge Network** — global network of working groups; the local node is often the right place to ask licensing/attribution questions.

**Why it matters here:** the PrologueOfSpacetime wiki is an open knowledge artifact (MIT license, public git repo, raw sources preserved). OKF's Open Definition is the canonical reference when students ask "is this actually open?" It is the standards layer above the technical choices in this install list.

> **Stubs for expansion:** dedicated concept pages for `[[Harness]]`, `[[Skills]]`, and `[[Open_Knowledge_Foundation]]` should be filed under `docs/concepts/` when this section grows. For now, this section is the canonical reference inside the install list.

---

## Installation Order — OpenCode is the foundation

> **The flow:** Student installs OpenCode first → grants OpenCode machine access → OpenCode assists with installing everything else. Only a few items stay manual (browser-based OAuth consent, network joins, account creation).

The tier tables below are the **what**. This section is the **how, in order**. OpenCode itself can read this doc and drive the install for the student.

### Phase 0 — Prerequisites (manual, before OpenCode)

The student must arrive with these. OpenCode cannot install its own prerequisites.

| # | Item | Why it's manual | Action |
|:---|:---|:---|:---|
| 0.1 | OS-level admin access | OpenCode needs to install software system-wide; on macOS the student must approve install prompts with their password | Ensure the account is an admin on the machine |
| 0.2 | A terminal / shell | OpenCode runs in the terminal — needs a working shell | macOS: Terminal.app. Windows: PowerShell or WSL2. |
| 0.3 | A browser (Chrome/Edge/Firefox) | Google OAuth consent opens in the browser; account signups happen here | Have one installed and logged into a Google account |
| 0.4 | Git (basic install) | OpenCode uses git to clone MCP servers and skills; some hosts ship without git | `git --version` should work in the shell |

### Phase 1 — Install OpenCode (the foundation, manual)

OpenCode is installed **first**, before anything else. It becomes the agent that installs the rest.

| # | Item | Why manual | Action |
|:---|:---|:---|:---|
| 1.1 | **OpenCode** | Cannot bootstrap itself | Install from <https://opencode.ai> (or `github.com/sst/opencode`). Run `opencode` in the shell to confirm it launches. |

### Phase 2 — Grant OpenCode machine access (manual, one-time)

OpenCode can only really assist once the student has explicitly granted it access to the whole machine. This is a deliberate permission step — the student is choosing to trust the agent with their system.

| # | Item | Why manual | Action |
|:---|:---|:---|:---|
| 2.1 | Filesystem access | OpenCode needs to read/write files outside its own directory (clone repos, edit configs, install MCP servers) | In the OpenCode permission prompt, choose **Allow** for the home directory and any project directories. On macOS, approve the "Full Disk Access" prompt if it appears. |
| 2.2 | Shell / bash permission | OpenCode runs install commands (`brew install`, `uv pip`, `git clone`, `ollama pull`) on the student's behalf | In OpenCode, set bash permission to `allow` for the install session, or approve each command when prompted. |
| 2.3 | External directory access | OpenCode will read/write `~/.config/opencode/`, `~/.zshrc`, `~/.google_workspace_mcp/`, etc. | Approve external-directory access for `~/` during the install session. |

### Phase 3 — OpenCode assists with the rest (agent-driven)

From here on, the student asks OpenCode (in plain English) to install the remaining tools. OpenCode reads the tier tables below and walks the student through each. The student approves commands as they run.

**What OpenCode can install for the student:**

- **Ollama** + the model (`ollama pull qwen2.5:3b`) — see Tier 3
- **Docker Desktop** — see Tier 8
- **uv / uvx** (Python package manager) — see Tier 7
- **Node.js 22+** — required by OpenCode and most MCP servers
- **ZeroTier** + **Netbird** — see Tier 8 (OpenCode runs the installer, student joins the network)
- **Hermes** (clone + setup) — see Tier 3
- **Obsidian** — see Tier 12 (download + vault creation)
- **MCP servers**: Google Workspace MCP, Obsidian MCP, mem0, @playwright/mcp — see Tier 5 (OpenCode clones, installs deps, writes the `opencode.json` entry)
- **Skills**: caveman, baoyu-youtube-transcript, etc. — see Tier 6 (OpenCode drops `SKILL.md` files into `.agents/skills/`)
- **Python / Rust / etc.** language toolchains — see Tier 9

**How the student drives it:** in an OpenCode session, say things like *"install Ollama and pull the qwen2.5:3b model"*, *"install ZeroTier and Netbird"*, *"set up the Google Workspace MCP server"*. OpenCode runs the commands; the student approves and provides passwords/OAuth as needed.

### Phase 4 — Manual verification items (student must do these themselves)

These cannot be delegated to OpenCode — they require the student's hands on a browser or a physical device.

| # | Item | Why manual | Action |
|:---|:---|:---|:---|
| 4.1 | Google Cloud OAuth client | Requires the student's Google account login in a browser | Follow [[installing_google_workspace_mcp]] Phases 1–3. OpenCode can then write the env vars to `~/.zshrc` and the entry to `opencode.json`. |
| 4.2 | Google OAuth consent (one-time) | Opens in browser; the student picks their account and clicks Allow | Triggered automatically on first google-workspace tool call — see [[installing_google_workspace_mcp]] Phase 6. |
| 4.3 | ZeroTier network join | Requires the student's ZeroTier account login in a browser | Install is agent-driven; joining the network ID is manual. Get the network ID from the instructor. |
| 4.4 | Netbird setup / login | Same — login is browser-based | Install is agent-driven; peer setup is manual. |
| 4.5 | GitHub account + SSH key | Account creation is browser-based; SSH key generation OpenCode can do | Sign up at github.com; ask OpenCode to generate the SSH key and add it to GitHub. |
| 4.6 | Obsidian vault creation | GUI app, vault folder picker | Install is agent-driven; creating the vault in `~/Documents/MyVault` is manual. |
| 4.7 | Obsidian Local REST API plugin | Community plugin install inside Obsidian GUI | Install Obsidian → Settings → Community plugins → search "Local REST API" → enable. Copy the API key (OpenCode will write it into `opencode.json`). |

### Phase 5 — Smoke test (agent-driven)

Once Phases 0–4 are done, the student asks OpenCode to verify the install end-to-end:

1. *"List my Google calendars"* → confirms Google Workspace MCP + OAuth.
2. *"Pull the qwen2.5:3b model and run a test prompt"* → confirms Ollama + model.
3. *"Ping the ZeroTier network"* → confirms networking.
4. *"Clone the Hermes repo and run its --help"* → confirms Hermes.
5. *"Create a test note in my Obsidian vault"* → confirms Obsidian MCP.

If all five return successfully, the student is ready for the workshop.

---



---

## Tier 1 — Core Install (AI coding harness + model access)

These are the tools the user actually runs day-to-day. Students who want to mirror the workflow should install these.

| Tool | What it is | Status | Notes |
| :--- | :--- | :--- | :--- |
| OpenCode | Open-source terminal AI coding interface (github.com/sst/opencode) | [INSTALL] | Primary harness. Currently runs GLM 5.2 via GLM proxy at `glm.pkc.pub/v1`. |
| Ollama | Local model runner | [INSTALL] | Runs local 7B/8B/12B models on the laptop. Also serves `nomic-embed-text` for mem0 embeddings. |
| Docker Desktop | Container runtime | [INSTALL] | Required for mem0 stack, Odysseus-style self-hosting, and most infra notes. |
| Git | Version control | [INSTALL] | Already on most machines; verify. |
| GitHub account | Code/doc hosting | [ACCOUNT] | Sign up. Used as storage layer for pkc/prologue pipeline. |

---

## Tier 2 — Cloud AI Services (account, no install)

| Service | What it is | Status | Notes |
| :--- | :--- | :--- | :--- |
| ChatGPT | OpenAI cloud AI | [ACCOUNT] | User's primary cloud AI. |
| Custom GPT | Tailored ChatGPT instance | [ACCOUNT] | Used for resume-tailoring workflow — load Master Resume + writing samples. |
| Claude (Anthropic) | Cloud AI subscription | [ACCOUNT] | $20/mo option; discussed. |
| OpenRouter | Multi-model API gateway | [ACCOUNT] | Bridges to OpenAI / Anthropic / Gemini APIs. |
| skills.sh | Vercel skill marketplace CLI | [ACCOUNT] | Browse/install Claude Code skills. |
| mcp.so | MCP server directory | [ACCOUNT] | Browse MCP servers. |

---

## Tier 3 — Local Inference & Models

| Tool / Model | What it is | Status | Notes |
| :--- | :--- | :--- | :--- |
| Local 7B/8B/12B models | Small LLMs running on laptop via Ollama | [INSTALL] | Comfortable size for HP Spectre x360-class hardware. |
| GLM 2 | Sovereign model at Toba data center | [INSTALL] | Accessed via Pi Agent / ZeroTier tunnel. |
| GLM 5.2 | Current session model | [INSTALL] | Powers OpenCode sessions via GLM proxy. |
| Hermes | Open-source autonomous agent (Nous Research) | [INSTALL] | Promoted from "discussed" to required — students will work with Hermes as the reference architecture for the "where this grows up" 24/7 agent path. See [[local_model_demo_setup]] §8 (reference architectures) for context. |
| llama.cpp | C++ inference runtime | [DISCUSSED] | Mentioned in Odysseus architecture. |
| vLLM | High-throughput inference server | [DISCUSSED] | Mentioned in Odysseus architecture. |
| llmfit | VRAM-aware model selector | [DISCUSSED] | Odysseus component. |
| Whisper | Voice dictation | [DISCUSSED] | Mentioned in OpenGeoAgent context. |
| Dwarf Star | 284B DeepSeek V4 Flash via SSD streaming | [DISCUSSED] | Project by Redis creator; not yet adopted. |

---

## Tier 4 — AI Coding Harnesses (alternatives to OpenCode)

| Tool | Status | Notes |
| :--- | :--- | :--- |
| Claude Code | [OPTIONAL] | Discussed; user doesn't currently have it. Requires Claude subscription. |
| Cursor | [OPTIONAL] | Mentioned as alternative harness. |
| Codex | [OPTIONAL] | Discussed as harness alternative; uses `agents.md` instead of `claude.md`. |
| Antigravity | [OPTIONAL] | Part of pkc/GitHub/Kubernetes/opencode pipeline. |
| Aider | [DISCUSSED] | Listed as example harness in stack chapter. |

---

## Tier 5 — MCP Servers

| MCP | What it does | Status |
| :--- | :--- | :--- |
| mem0 MCP | Conversation memory (custom Python wrapper → self-hosted mem0 server) | [INSTALL] |
| @playwright/mcp | Browser automation MCP | [INSTALL] |
| UE 5.8 MCP | Unreal Engine control (Hermes skill) | [DISCUSSED] |
| Gmail MCP | Email ingest | [DISCUSSED] |
| Google Calendar MCP | Calendar context | [DISCUSSED] |
| Google Drive MCP | Document ingest | [DISCUSSED] |
| server-github | GitHub access | [DISCUSSED] |
| server-filesystem | Filesystem access | [DISCUSSED] |
| server-postgres | Postgres access | [DISCUSSED] |

---

## Tier 6 — Skills / Plugins / Extensions

| Skill / Plugin | What it does | Status |
| :--- | :--- | :--- |
| Caveman skill | Token-cost cutter (terse output) | [DISCUSSED] |
| Ponytail skill | YAGNI decision ladder, 47–77% cheaper | [DISCUSSED] |
| Graphify | Codebase knowledge graph skill (Claude Code) | [DISCUSSED] |
| Understand Anything | Multi-agent codebase analysis plugin | [DISCUSSED] |
| baoyu-youtube-transcript | YouTube transcript fetcher | [INSTALL] |
| agentskills.io | Open skill standard | [DISCUSSED] |
| ClawHub | OpenClaw skill marketplace | [DISCUSSED] |
| Obsidian Web Clipper | Chrome extension — web articles → markdown | [INSTALL] |
| tree-sitter | Code parser (used by Understand Anything) | [DISCUSSED] |

---

## Tier 7 — Storage / Memory / Vector Layer

| Tool | What it is | Status |
| :--- | :--- | :--- |
| Postgres + pgvector | Vector DB (mem0 backing store) | [INSTALL] |
| SQLite | Local machine memory | [INSTALL] |
| MinIO | S3-compatible object storage | [INSTALL] |
| Pinecone | Managed vector DB | [DISCUSSED] |
| Supabase | Postgres + vector hosting | [DISCUSSED] |
| Qdrant | Open-source vector DB | [DISCUSSED] |
| LightRAG | KG visualization layer | [DISCUSSED] |
| ChromaDB | Local vector DB (OpenClaw memory dep) | [DISCUSSED] |
| sentence-transformers | Embedding models (Python) | [DISCUSSED] |
| pymupdf, python-docx | Doc parsers (Python) | [DISCUSSED] |
| uv | Python package manager | [INSTALL] |

---

## Tier 8 — Networking & Container Runtime

> Trimmed from the original DevOps/Infrastructure tier. Heavy infra (Kubernetes, ArgoCD, GitHub Actions runners, nginx, MediaWiki/MariaDB/Matomo, Ansible) has been removed — students do not touch these in the workshop. Docker stays (needed for Ollama containers, mem0, etc.). ZeroTier + Netbird are both required: ZeroTier for Toba/GLM2 access, Netbird as the modern WireGuard-based mesh alternative.

| Tool | What it is | Status | Notes |
| :--- | :--- | :--- | :--- |
| Docker / Docker Desktop | Container runtime | [INSTALL] | Required for Ollama containers, mem0 stack, and most infra demos. |
| ZeroTier | Secure overlay network (Toba access) | [INSTALL] | Required — provides the tunnel to the Toba data center and GLM2. Install before workshop day. |
| Netbird | WireGuard-based mesh VPN (open-source Tailscale alternative) | [INSTALL] | Required — modern peer-to-peer mesh with self-hostable control plane. Install alongside ZeroTier; students use it for peer-to-peer agent mesh demos. |

**Removed from this tier (not needed for the workshop):**
Kubernetes stack (kubeadm/kubelet/kubectl/containerd/etcd), ArgoCD/Argo Rollouts, GitHub Actions + ARC, nginx, UTM, MediaWiki, MariaDB, Matomo, Ansible, Tailscale, Cloudflare Tunnel. These remain documented elsewhere in the vault for the post-workshop "advanced / production" track — see `docs/plans/utm-macstudio-kubernetes-setup.md` and related pages.

---

## Tier 9 — Programming Languages

| Language | Status | Notes |
| :--- | :--- | :--- |
| Python | [INSTALL] | In user's skill set. |
| Rust | [INSTALL] | User has learning notes (`rust-ownership-borrowing-model.md`, `rust-type-system-safety.md`). |
| JavaScript / Next.js | [INSTALL] | Used for smartboard payloads. |
| SQL | [INSTALL] | In user's skill set. |
| LaTeX | [OPTIONAL] | Used for CV drafting. |

---

## Tier 10 — GIS / Geospatial (specialized track)

| Tool | What it is | Status |
| :--- | :--- | :--- |
| QGIS | Open-source desktop GIS | [DISCUSSED] |
| Whitebox Tools | Open-source geospatial analysis | [DISCUSSED] |
| OpenGeoAgent | Multimodal AI agent for geospatial analysis | [DISCUSSED] |

---

## Tier 11 — Agent Frameworks (discussed, not necessarily installed)

| Framework | What it is | Status |
| :--- | :--- | :--- |
| DeerFlow 2.0 | Bytedance open-source Super Agent harness | [DISCUSSED] |
| OpenClaw | Open-source agent with ClawHub marketplace | [DISCUSSED] |
| Gbrain + Gstack | Garry Tan's memory-syncing agent + stack | [DISCUSSED] |
| Eve | Vercel agent framework ("NextJS of agents") | [DISCUSSED] |
| LangGraph | Agentic framework | [DISCUSSED] |
| CrewAI | Agentic framework | [DISCUSSED] |
| AutoGen | Agentic framework | [DISCUSSED] |
| Hugging Face | ML library / hub | [DISCUSSED] |
| PyTorch | ML framework | [DISCUSSED] |
| GitNexus | Codebase intelligence tool | [DISCUSSED] |

---

## Tier 12 — Knowledge / Note Tooling

| Tool | What it is | Status |
| :--- | :--- | :--- |
| Obsidian | Vault / knowledge base substrate | [INSTALL] |
| Microsoft Edge (headless) | PDF rendering for daily reports | [INSTALL] |
| Marp | Markdown slides | [DISCUSSED] |
| Dataview (Obsidian plugin) | Frontmatter queries | [DISCUSSED] |

---

## Tier 13 — Hardware / Edge / IoT (workshop may include for demos)

| Hardware | Status | Notes |
| :--- | :--- | :--- |
| HP Spectre x360 (Intel Core Ultra 7 155H, 32GB RAM) | [HARDWARE] | User's personal laptop. |
| ESP32 | [HARDWARE] | Microcontroller; wiring guide in repo. |
| Hikvision IP cameras | [HARDWARE] | Shopper analytics pipeline. |
| NVIDIA Jetson | [HARDWARE] | Edge compute. |
| YOLO / YOLOv11s | [HARDWARE] | Object detection model. |
| NVIDIA Thor | [HARDWARE] | Edge compute for robotics. |
| NVIDIA DGX H100 | [HARDWARE] | AI server. |
| Unitree / Shadow Hand | [HARDWARE] | Robotics reference platform. |
| LiDAR (3D) | [HARDWARE] | Triangular stereo vision setup. |
| LAR sensors | [HARDWARE] | Camera-based motion detection. |
| Raspberry Pi 4 | [HARDWARE] | Edge inference alternative. |
| 3D printer | [HARDWARE] | Used daily for Saturn V Lego parts. |
| Drone | [HARDWARE] | Site bird's-eye view. |
| Hisense smartboard | [HARDWARE] | Strategy board. |
| Quest 3 (Meta) | [HARDWARE] | VR headset; remote desktop to laptop. |
| iPad | [HARDWARE] | Smartboard fake. |
| Microscope | [HARDWARE] | Lab equipment. |
| Lego Saturn V | [HARDWARE] | Assembled kit. |

---

## Tier 14 — Communication Channels (for agent integration)

| Channel | Status |
| :--- | :--- |
| Telegram | [DISCUSSED] — Hermes channel |
| Discord | [DISCUSSED] — Hermes channel |
| Slack | [DISCUSSED] — Hermes channel |
| WhatsApp | [DISCUSSED] — Hermes channel; also used to draft to Ben Koo |
| iMessage | [DISCUSSED] — via Photon textable number |

---

## Source Notes (InaAI vault)

The list above was compiled by sweeping every `.md` file in `InaAI/` (90+ notes, including `koo-project/`) and extracting:

- Anything described as "installed", "downloaded", "set up", "started using"
- Anything appearing in frontmatter `tags:`
- Anything appearing in note titles, headings, or "Related" sections
- Anything appearing in YouTube summary notes (frontmatter `source: YouTube — ...`)
- Install commands (`pip install`, `npm install`, `winget`, `docker pull`, `git clone`, etc.)

Source notes of particular relevance:

- `InaAI/koo-project/opencode-vs-claude-code-vs-pi-agent.md` — harness landscape
- `InaAI/koo-project/chatgpt-vs-claude-vs-local-ai-verdict.md` — model landscape
- `InaAI/koo-project/odysseus-pewdiepie-self-hosted-workspace.md` — self-hosted stack
- `InaAI/koo-project/toba-data-center-and-glm2.md` — Toba/GLM2 stack
- `InaAI/koo-project/second-brain-three-layer-architecture.md` — memory architecture
- `InaAI/second-brain-business-os-wiring.md` — MCP wiring pattern
- `InaAI/skills-install-best-practices.md` — skill install conventions
- `InaAI/minio-s3-compatible-object-storage.md` — MinIO
- `InaAI/rust-ownership-borrowing-model.md`, `InaAI/rust-type-system-safety.md` — Rust
- `InaAI/hermes-*.md` — Hermes agent family

---

## Reconciliation note

`docs/teaching/pitch_10_minute.md` and `docs/teaching/presentation_plan.md` currently state: **"No software installation required — the course is designed to work with browser-based tools (ChatGPT, Claude, skills.sh, mcp.so). Day 4 has an optional installation of opencode or Cursor."**

This is now **superseded** by the 2026-07-07 revision: the workshop requires a substantial pre-install (OpenCode + Ollama + Qwen2.5-3B + Docker + ZeroTier + Netbird + Hermes + Google OAuth credentials). The browser-based pitch still works as the *opening* pitch; the hands-on day scope is in [[local_model_demo_setup]]. The pitch deck and presentation plan **must be updated** to reflect the new pre-install expectation before student-facing comms go out. Henry to confirm before student-facing comms go out.

---

## Related

- [[sprint_outline]]
- [[pitch_10_minute]]
- [[presentation_plan]]
- [[handbook/03_the_stack]]
- [[handbook/10_the_tools_people_use]]
- [[local_model_demo_setup]] — hands-on day scope: model pick (Qwen2.5-3B), demo flow, MCP picks, risk register.
- [[installing_google_workspace_mcp]] — verified OAuth + OpenCode config procedure for the Google Workspace MCP server used in the demo.
