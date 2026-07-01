---
title: 'gitops-two-repo-pattern'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, gitops, ci-cd, deployment, version-control, infrastructure-as-code]
type: principle
sources: [YouTube — How to design a Deployment Pipeline (GitOps) (https://www.youtube.com/watch?v=pJ9f7w4AxtU)]
status: stable
liberal_art: Trivium-Grammar
---

# GitOps two-repo split — application repo vs config repo

## Insight
The first thing to do when designing a GitOps deployment pipeline is create a **second repository** to house configuration, separate from the application code repository. The CI/CD pipeline still checks out from the application repo (source → build → test → release → container image in registry), but the deployment pipeline reads its manifests from a dedicated config repo.

The config repo holds everything needed to deploy the application: Kubernetes manifests, Helm values, Kustomize overlays, Docker Compose files — whatever the target environment consumes. A typical manifest in this repo is a Kubernetes Deployment whose `image:` field references the tag the CI pipeline just produced (`myapp:v1.0`).

Why split? Two reasons. First, **separation of concerns and rate of change** — application code changes on every commit; deployment config changes only when the deployment shape changes. Mixing them means every app commit churns the deployment history and every deployment tweak is entangled with app PRs. Second, and more importantly, **the pipeline auto-edits the config repo**. When CI produces `myapp:v1.1`, a well-designed pipeline doesn't `kubectl apply` directly — it submits a pull request (or pushes a commit) to the config repo updating the image tag from `v1.0` to `v1.1`. The deployment step then becomes "reconcile the cluster to whatever the config repo now says," which is exactly the input a pull-model operator like Argo CD consumes.

So the data flow is: app repo → CI/CD → image in registry → automated PR to config repo → operator in cluster syncs from config repo. Git is the source of truth for both code and deployment state, but those two truths live in different repos because they change for different reasons.

## Context
From the YouTube video "How to design a Deployment Pipeline (GitOps)" — this is the first concrete design decision the video walks through before discussing push vs pull models.

## Related
- [[gitops-pull-vs-push]]
- [[argocd-declarative-gitops-k8s]]
- [[cicd-two-repo-split]]
- [[InaAI]]
