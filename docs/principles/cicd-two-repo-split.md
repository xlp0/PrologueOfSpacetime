---
title: 'cicd-two-repo-split'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, ci-cd, gitops, kubernetes, argocd, github-actions]
type: principle
sources: [YouTube — Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions) (https://www.youtube.com/watch?v=GlhK7mz5IJo)]
status: stable
liberal_art: Trivium-Grammar
---

# CI/CD two-repo split — app repo for CI, gitops repo for CD

## Insight
The cleanest way to wire a Kubernetes CI/CD pipeline is to split it across two repositories with sharply different responsibilities. The **application repository** holds source code plus the CI half of the pipeline; the **gitops repository** holds Kubernetes manifests (deployment.yaml, service.yaml) plus the CD half. Each repo is the source of truth for one phase, and the bridge between them is a single field: the image tag inside `deployment.yaml`.

The CI half fires when a commit lands on `main` of the app repo. GitHub Actions builds a Docker image, pushes it to a container registry, then **commits back to the gitops repo** to update the image field to the new tag. From the cluster's perspective, nothing has happened yet — only git has changed.

The CD half fires when ArgoCD, running inside the cluster, notices the gitops repo has changed. ArgoCD reconciles the desired state in git against the actual state in the cluster and rolls new pods. The pipeline is fully automated end-to-end, but the two halves are decoupled: you can rebuild the image a hundred times without touching the cluster, and you can replay a deployment by re-syncing the gitops repo without rebuilding anything.

The architectural payoff is that **CI ownership and CD ownership are separable**. The team that owns the app owns the build; the team that owns the cluster owns the deploy. Both meet at the gitops repo, which is auditable, revertible, and the single source of truth for what should be running. This is what "GitOps" actually means in practice — not "git triggers deploys" but "git IS the deployment spec, and an in-cluster reconciler enforces it."

## Context
From the "Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions)" video, which builds the entire pipeline end-to-end. The two-repo split is introduced in module 1 as the foundation everything else is built on.

## Related
- [[github-actions-ci-pipeline]]
- [[argocd-application-crd-gitops]]
- [[image-tag-unique-hash-gitops]]
- [[InaAI]]
