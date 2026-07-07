# Pre-Workshop Install List (IT Dell)

> A consolidated list of every tool, package, model, service, and piece of hardware mentioned in the InaAI notes (markdown notes + YouTube summaries) that students may need installed or available before the workshop. Henry to triage to a "must-install" subset for students. Source: `InaAI/` vault, swept 2026-07-07.

---

## How to read this list

Each item is flagged with a status:

- **[INSTALL]** — core install, the user actively uses this
- **[OPTIONAL]** — alternative or optional, mentioned but not always adopted
- **[DISCUSSED]** — evaluated in notes/YouTube, not necessarily installed
- **[ACCOUNT]** — web service, no install — sign up only
- **[HARDWARE]** — physical device, not software

Henry: please trim to the **[INSTALL]** + **[ACCOUNT]** tiers for the student pre-install checklist. The **[OPTIONAL]** / **[DISCUSSED]** tiers are reference for Q&A and "where do I learn more" traffic.

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
| Hermes | Open-source autonomous agent (Nous Research) | [DISCUSSED] | Evaluated; user treats as "optional garnish." |
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

## Tier 8 — DevOps / Infrastructure

| Tool | What it is | Status |
| :--- | :--- | :--- |
| Docker / Docker Desktop | Container runtime | [INSTALL] |
| Kubernetes (kubeadm, kubelet, kubectl, containerd, etcd) | Container orchestration | [INSTALL] |
| ArgoCD / Argo Rollouts | GitOps for k8s | [INSTALL] |
| GitHub Actions + ARC (self-hosted runner) | CI/CD | [INSTALL] |
| nginx | Reverse proxy / example Deployment | [INSTALL] |
| UTM | Mac VM host (for k8s worker nodes) | [DISCUSSED] |
| MediaWiki | Wiki platform (PKC stack) | [DISCUSSED] |
| MariaDB | Database (PKC stack) | [DISCUSSED] |
| Matomo | Analytics (PKC stack) | [DISCUSSED] |
| Ansible | Config automation (PKC stack) | [DISCUSSED] |
| ZeroTier | Secure overlay network (Toba access) | [INSTALL] |
| Tailscale | Alternative secure overlay | [DISCUSSED] |
| Cloudflare Tunnel | Alternative secure tunnel | [DISCUSSED] |

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

If the IT Dell workshop expands the install list beyond browser-based tools, the pitch deck and presentation plan should be updated to reflect the new pre-install expectation. Henry to confirm scope before student-facing comms go out.

---

## Related

- [[sprint_outline]]
- [[pitch_10_minute]]
- [[presentation_plan]]
- [[handbook/03_the_stack]]
- [[handbook/10_the_tools_people_use]]
