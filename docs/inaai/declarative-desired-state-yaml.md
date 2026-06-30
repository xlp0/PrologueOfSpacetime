---
concept: Declarative desired-state YAML and drift reconciliation
tags: [declarative, gitops, kubernetes, yaml, devops]
source: YouTube — What is ArgoCD (https://www.youtube.com/watch?v=p-kAqxuJNik)
date: 2026-06-30
---

# Declarative desired-state YAML and drift reconciliation

## Insight
Declarative configuration means writing down the full specification of the target architecture in YAML, so the expected state and the actual state on production stay consistent. The YAML describes how the architecture should look — pod counts, image references, secrets, services — and the system's job is to converge reality to match it. This is the opposite of imperative scripting, where you tell the system "do X then Y." Declarative says "the state should be Z, you figure out how to get there."

The video illustrates two consequences worth pulling apart.

**Recoverability.** When John, the ops guy, steps out for coffee and forgets what he was doing, he just reads the YAML to recall the intended architecture. The YAML is documentation that is always in sync with intent — it can't drift from the plan because it IS the plan. There's no separate "runbook" or wiki page that someone forgot to update; the config is the documentation.

**Self-healing drift reconciliation.** Steve, "old fashioned" and skeptical of automation, gets into the ArgoCD deployment and manually adds ten extra pods beyond what's actually needed. ArgoCD's automation scales them back down automatically, because the YAML says the cluster should have fewer pods. The bill at the end of the month stays bounded.

The principle underneath both stories: any state NOT in the YAML is drift, and drift gets reconciled away. Manual changes to production don't stick unless they're committed back to Git. This is what makes GitOps safe — Git is the source of truth (see [[gitops-git-as-source-of-truth]]), the YAML is the spec of that truth, and tools like ArgoCD (see [[argocd-declarative-gitops-k8s]]) run the reconciliation loop. The "robot" the video draws inside ArgoCD is just this loop, running continuously.

## Context
From the "What is ArgoCD" explainer video. Two of the three character stories (John and Steve) are used to illustrate different facets of the declarative model.

## Related
- [[argocd-declarative-gitops-k8s]]
- [[gitops-git-as-source-of-truth]]
- [[argocd-rollback-health-checks]]
- [[agentic-harness-90-percent]] — k8s reconciliation loop is the infra-layer harness; declarative spec = the 90% that compounds
- [[InaAI]]
