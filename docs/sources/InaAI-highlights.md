---
topic: InaAI
date: 2026-06-27
source: YouTube summaries (19 videos split into atomic notes)
tags: [ai-tools, claude-code, mcp, second-brain, physical-ai, nvidia, hermes, agentic-harness, skills, prompt-injection]
---

# InaAI highlights — YouTube

## TL;DR
19 YouTube summaries covering the AI tooling stack as of mid-2026: agentic engineering harnesses (Google masterclass, DeerFlow, Hermes, Graphify), the skills spec that connects them (skills.sh / agentskills.io / MCP), the second-brain pattern for personal knowledge (Karpathy LLM Wiki, Nick Milo AIOS, Obsidian + Claude Code), the physical-AI stack (NVIDIA world models + TI embedded processors), and the AI infrastructure capex funding all of it (Stargate, hyperscalers, the Nvidia tax vs UALink alliance). The unifying thesis across most of these notes: **the harness is 90% of the system, the model is the swappable 10%.** Own the harness (files, skills, graphs, sandboxes), rent the model.

## Agentic harness & engineering
- [[agentic-harness-90-percent]] — Google's masterclass thesis: model is 10%, harness is 90%
- [[ai-sdlc-spec-bottleneck]] — bottleneck moved from implementation to spec quality
- [[plan-build-eval-review-split]] — fresh session per stage to avoid context rot
- [[static-vs-dynamic-context]] — one generalist agent + skills > zoo of specialists
- [[token-economics-vibe-vs-agentic]] — high capex / low opex vs the inverse; harness compounds

## Skills & token-cost engineering
- [[skills-sh-markdown-spec]] — markdown + YAML header; portable procedural knowledge for agents
- [[skills-install-best-practices]] — project vs global, symlink, co-locate with tool
- [[caveman-terse-output-skill]] — drop articles, filler; 45% fewer output tokens
- [[ponytail-yagni-ladder]] — YAGNI decision ladder; 47–77% cheaper
- [[ponytail-vs-caveman-benchmark]] — head-to-head; no benefit to stacking
- [[packaging-is-the-product]] — Eberhart's critique + the counterargument
- [[skill-injection-token-economics]] — single-shot vs multi-turn caching crossover

## Agent platforms
- [[deerflow-harness-vs-framework]] — bytedance's productionized super-agent harness
- [[deerflow-sandbox-architecture]] — Docker isolation, allowed-tools, zip-bomb defense
- [[deerflow-lead-agent-dynamic-subagents]] — fixed graph → lead + dynamic subagents
- [[hermes-persistent-memory]] — notebook that never closes
- [[hermes-self-improving-skills]] — every solved problem becomes a reusable skill
- [[hermes-sub-agents]] — isolated workers, results assembled by lead
- [[hermes-background-subagents]] — auto-spawned by complex prompts; sub-agent tree UI
- [[hermes-imessage-photon-routing]] — iMessage via Photon; channel routing by task type
- [[hermes-ue5-mcp]] — UE 5.8 MCP support for AI-driven game dev
- [[catalog-vs-curator]] — OpenClaw catalog (50k+ skills) vs Hermes Curator (auto-write)
- [[openclaw-vs-hermes-security-posture]] — CVE volumes, sandbox backends, VPS discipline

## Codebase knowledge graphs & agentic OS
- [[graphify-codebase-knowledge-graph]] — graph once, query from anywhere, save tokens
- [[agentic-os-shared-brain]] — Hermes + Claude Code + Graphify = shared always-on brain
- [[understand-anything-multi-agent-pipeline]] — tree-sitter pre-batch → 5 parallel Claude agents
- [[codebase-knowledge-graph-dashboard]] — guided tour + domain view + layer color-coding

## Second brain & personal knowledge
- [[second-brain-obsidian-foundations]] — vault + folders + claude.md + readmes
- [[second-brain-business-os-wiring]] — Gmail/Calendar/Drive MCP + scheduled sub-agents
- [[karpathy-llm-wiki-vs-rag]] — RAG starts from zero; wiki compounds
- [[llm-wiki-three-layers]] — raw sources + AI-maintained wiki + schema
- [[llm-wiki-lint-pass]] — surface contradictions, orphans, broken links
- [[nick-milo-aios-three-layers]] — Ideaverse + translation layer + external AI
- [[me-md-vault-map-skill-map]] — three load-bearing files, portable across AIs
- [[session-start-prompt-pattern]] — explicit load step before any work
- [[five-levels-second-brain]] — Level 1-5 retrieval ladder; pick the lowest level that fixes your pain, 2026-06-28
- [[claude-md-routing-rules]] — claude.md as router not just system prompt; agents.md portability, 2026-06-28
- [[reverse-engineer-data-shape]] — start with the question; basketball-hoop analogy, 2026-06-28
- [[vector-retrieval-chunking-limit]] — chunking breaks holistic retrieval; vectors are a targeted optimization, 2026-06-28
- [[wiki-backlinks-vs-kg-edges]] — untyped "see also" vs typed edges; backlinks are enough for most PKM, 2026-06-28
- [[second-brain-ingest-curation]] — Four C's (context/connections/capabilities/cadence) + evergreen filter, 2026-06-28
- [[claude-fable-gets-it]] — Claude Fable (public Mythos 5) dropped June 9 2026; Karpathy's "gets it" framing; 2x Opus cost, 2026-06-28
- [[visual-graph-layer-second-brain]] — 3D/2D graph UI rendered over a markdown second brain; localhost viewer, 2026-06-28
- [[second-brain-agency-product]] — selling second-brain setups to businesses ($2-3k + retainer); white-label vs free, 2026-06-28

## Tooling standards & integrations
- [[mcp-anthropic-standard]] — one protocol between LLMs and tools; replaces N×M integrations
- [[exposed-tool-source-code-pattern]] — agent prints the code it ran; code-teaching surface
- [[opengeoagent-architecture]] — provider-agnostic LLM + tool-mode switching inside QGIS

## Physical AI & robotics
- [[physical-ai-chatgpt-moment]] — world / world-action models will be the breakthrough
- [[nvidia-cosmos-world-model]] — physically accurate world model; Omniverse + Cosmos grow together
- [[isaac-groot-reference-platform]] — Unitree + Thor + Shadow Hand; "research required, assembly not"
- [[sim-to-real-gap]] — assume gap; world models' slight imperfections help
- [[physical-ai-real-time-constraints]] — 100ms delay matters; no "try again"
- [[pru-live-reprogramming]] — TI's PRU; reprogram without power-cycling
- [[ti-automotive-ai-hidden-products]] — TDA5 driver assist + AM62A driver/passenger monitoring

## AI infrastructure & capex
- [[ai-capex-not-bubble]] — necessary capex, not a bubble; AGI prisoner's dilemma
- [[ai-server-anatomy-h100]] — DGX H100 breakdown; 75-80% of capex → compute + network
- [[nvidia-tax-vs-ualink-alliance]] — NVLink lock-in vs UALink open protocol
- [[dwarf-star-ssd-streaming]] — 284B DeepSeek V4 Flash on a laptop via SSD streaming + MoE expert caching; RAM cliff becomes a slope, 2026-06-29

## Kubernetes & DevOps
- [[cicd-two-repo-split]] — app repo holds CI, gitops repo holds CD; meet at the image tag in deployment.yaml, 2026-06-30
- [[github-actions-ci-pipeline]] — trigger on push to main, mix built-in actions + bash, two scoped PATs as secrets, self-hosted runner, 2026-06-30
- [[argocd-application-crd-gitops]] — pull-based reconciliation; cluster watches git, never the reverse; imagePullSecret gotcha for private registries, 2026-06-30
- [[image-tag-unique-hash-gitops]] — tag every image with commit SHA so the gitops diff is visible to ArgoCD; `latest` alone silently never deploys, 2026-06-30
- [[minio-s3-compatible-object-storage]] — S3-compatible software-defined object store; erasure-coded, runs on k8s/cloud/bare metal, 2026-06-30
- [[k8s-origin-and-naming]] — Kubernetes descends from Google Borg (2014 open-source); "k8s" is a numeronym (8 letters between k and s), 2026-06-30
- [[k8s-cluster-architecture]] — a k8s cluster = control plane + worker nodes, with the pod as the smallest deployable unit, 2026-06-30
- [[k8s-control-plane-components]] — control plane = API server + etcd (state) + scheduler + controller manager; reconciliation loops drive current → desired state, 2026-06-30
- [[k8s-worker-node-components]] — each worker node runs kubelet (control channel) + container runtime (execution) + kube-proxy (networking), 2026-06-30
- [[k8s-orchestration-why-conductor-metaphor]] — the "why" of k8s: conductor metaphor, workload variability (Robinhood), horizontal scaling + failover + replica sets for HA, 2026-06-30
- [[gitops-pull-vs-push]] — CI server does kubectl apply vs in-cluster operator (Argo CD) reconciles from config repo; pull model catches drift and survives CI outages, 2026-06-30
- [[gitops-two-repo-pattern]] — application repo (source) vs config repo (deployment manifests); CI auto-PRs the image tag bump into config repo, 2026-06-30
- [[environment-promotion-gates]] — test/QA → staging → production; per-environment auto-sync vs manual click gates; staging = prod-like pretend, 2026-06-30
- [[canary-deployment-traffic-shift]] — load balancer gradually shifts traffic old→new (100/0→0/100); Argo Rollouts Rollout object replaces Deployment, 2026-06-30
- [[gitops-git-as-source-of-truth]] — Git repo as canonical state; commit-to-deploy pipeline automated, no manual gate, 2026-06-30
- [[argocd-declarative-gitops-k8s]] — ArgoCD's three pillars: GitOps trigger + declarative YAML spec + Kubernetes pod runtime, 2026-06-30
- [[declarative-desired-state-yaml]] — YAML describes intended architecture; recoverability + self-healing drift reconciliation, 2026-06-30
- [[argocd-rollback-health-checks]] — one-click rollback to last good commit + UI/CLI health surfaces (e.g. missing registry secrets), 2026-06-30
- [[docker-images-vs-containers]] — image = recipe (read-only template with runtime + deps + code), container = meal (running instance); one image spawns many containers, 2026-06-30
- [[dockerfile-instructions]] — FROM/WORKDIR/COPY/RUN/ENV/EXPOSE/CMD; RUN executes at build, CMD executes at container start; .dockerignore skips host dirs, 2026-06-30
- [[docker-layer-caching]] — every Dockerfile instruction is a layer; reorder so stable slow steps (deps) come before volatile fast steps (code) so cache isn't invalidated on every change, 2026-06-30
- [[docker-compose-multi-container]] — one container per service declared in compose.yaml; `build:` for your code, `image:` for off-the-shelf; `docker compose up` / `down` lifecycle, 2026-06-30
- [[docker-volumes-persistence]] — host-managed folder mounted into container(s); persists data across container restarts and shares data between containers; decouples stateless compute from stateful storage, 2026-06-30
- [[file-storage-hierarchical-namespace]] — file storage as hierarchical directory on block devices; NTFS/ext4/NFS/SMB; pros/cons, 2026-06-30
- [[object-storage-flat-namespace-metadata]] — object storage as flat namespace with data + unique ID + rich metadata; S3/GCS/Azure Blob, 2026-06-30
- [[file-vs-object-storage-decision-criteria]] — when to pick file vs object storage; shared network drive vs Netflix/YouTube streaming workloads, 2026-06-30
- [[object-storage-bucket-virtual-construct-replication]] — bucket as virtual namespace + physical replication to N devices for durability; API-only access, 2026-06-30
- [[object-storage-tiered-pricing-by-access-frequency]] — cold×10 / cold / cold-ish tiers; no warm tier; price scales with responsiveness, 2026-06-30
- [[object-storage-workload-patterns]] — streaming + global replication, file sharing via metadata versioning, cold archives, 2026-06-30
- [[rust-ownership-borrowing-model]] — memory safety without GC: ownership (one owner, moves on reassign/pass) + borrowing (`&T` shared / `&mut T` exclusive); borrow checker enforces at compile time, 2026-07-01
- [[rust-type-system-safety]] — make invalid states unrepresentable: no null (Option<T>), immutability default, no exceptions (Result<T,E>); signature tells caller everything, 2026-07-01

## Related
- [[koo-project-highlights]]
- [[InaAI]]
