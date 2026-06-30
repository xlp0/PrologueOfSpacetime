---
concept: Environment promotion with manual and automatic gates
tags: [gitops, ci-cd, deployment, release-management, staging]
source: YouTube — How to design a Deployment Pipeline (GitOps) (https://www.youtube.com/watch?v=pJ9f7w4AxtU)
date: 2026-06-30
---

# Environment promotion with manual and automatic gates

## Insight
After a deployment is running in the test/QA environment, the next step is promoting it to the other environments — typically **staging** and **production**. Staging is an environment that mirrors production as closely as possible: you send deployments there first and "pretend it's production" — treat it like prod, run the same checks, but it isn't actually serving customers. Production is where live customer traffic runs.

Promotion can be **automatic** (the GitOps pipeline triggers the next environment as soon as the previous one goes green) or **manually gated** (an engineer has to click "run the pipeline" or click "sync" in Argo CD before the next environment receives the change). Companies often aren't comfortable with fully automatic promotion into staging and production, so a common shape is: test/QA auto-promotes, staging requires an engineer, production requires an engineer *and* a click on the sync button in the operator UI.

In the pull model this maps cleanly onto per-environment sync policy. Argo CD auto-syncs test/QA (and optionally staging); for production it detects drift and shows "out of sync" but waits for a human to press the sync button. Same operator, same repo, different policy per application/environment. That's the appeal — the gating decision is a config knob, not a separate pipeline stage with its own credentials and scripts.

Between promotions you should also have observability plugged in — at minimum Prometheus scraping metrics and Grafana for the QA team to visualize latency and KPIs and confirm nothing regressed before they sign off on the next promotion.

## Context
From the YouTube video "How to design a Deployment Pipeline (GitOps)" — covers the test/QA → staging → production promotion flow and the manual-vs-automatic gate decision.

## Related
- [[gitops-pull-vs-push]]
- [[argocd-declarative-gitops-k8s]]
- [[canary-deployment-traffic-shift]]
- [[prompt-injection-defense-in-depth]] — same HITL-for-high-stakes / auto-for-low-stakes thesis, applied to agent permissions
- [[InaAI]]
