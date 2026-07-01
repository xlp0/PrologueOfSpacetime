---
title: 'gitops-pull-vs-push'
date: 2026-06-30
tags: [Trivium-Logic, Seven-Liberal-Arts, gitops, ci-cd, deployment, kubernetes, argocd]
type: principle
sources: [YouTube — How to design a Deployment Pipeline (GitOps) (https://www.youtube.com/watch?v=pJ9f7w4AxtU)]
status: stable
liberal_art: Trivium-Logic
---

# GitOps push vs pull deployment models

## Insight
A GitOps deployment pipeline moves a container image from a registry into an environment, and there are two fundamentally different ways the actual apply step can happen.

**Push model.** The CI/CD server itself runs `kubectl apply` against the target cluster. It's the simplest setup — your existing CI runner already has kubeconfig credentials and just shoves manifests at the cluster. The arrows point from CI → environment. Conceptually this is barely "GitOps" — git is the source of truth for the manifests, but the apply is driven from outside the cluster, exactly like a traditional deploy script with extra steps. It works, it's a reasonable starting point, but it isn't what people mean when they talk up GitOps.

**Pull model.** An operator is installed *inside* each target cluster — Argo CD is the canonical example. The operator watches the config repo and continuously compares the cluster's live state to the declared state in git. When it detects drift, it flags the environment as "out of sync" and either auto-syncs or waits for a human to click the sync button. The arrows flip: the cluster pulls its own configuration down from the repo, instead of being pushed to.

The pull model is the "modern approach" for a reason. Because the reconciliation loop lives in-cluster, it survives CI runner outages, it catches manual `kubectl edit` drift (someone hot-fixes a deployment and the operator reverts it on the next sync), and it makes "what's deployed" a query against the cluster rather than a guess based on which pipeline job last ran green. Per-environment sync policy falls out naturally: test/QA/staging can auto-sync, production can require a manual click — same operator, different sync policy per application.

## Context
From the YouTube video "How to design a Deployment Pipeline (GitOps)" — the push/pull distinction is the core architectural fork the video spends the most time on.

## Related
- [[gitops-two-repo-pattern]]
- [[argocd-declarative-gitops-k8s]]
- [[environment-promotion-gates]]
- [[cicd-two-repo-split]]
- [[InaAI]]
