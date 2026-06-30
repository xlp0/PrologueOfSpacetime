---
concept: GitHub Actions CI pipeline structure (build-push-update-gitops)
tags: [github-actions, ci-cd, docker, gitops, kubernetes]
source: YouTube — Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions) (https://www.youtube.com/watch?v=GlhK7mz5IJo)
date: 2026-06-30
---

# GitHub Actions CI pipeline — build, push, update gitops

## Insight
A minimal but production-shaped CI pipeline in GitHub Actions has a recognizable skeleton: a **trigger** (`on: push` to `main`), a single **job** (`build-and-push`), and a sequence of **steps** that mix built-in actions with bash. The pattern is composable — most steps are off-the-shelf (`actions/checkout`, `docker/login-action`, `docker/setup-buildx-action`, `docker/build-push-action`), and the irreducible domain logic (cloning the gitops repo, editing `deployment.yaml`, committing back) is plain shell.

Two design choices deserve attention. First, **secrets are scoped per step, not per pipeline**. Two personal access tokens are stored as repo secrets: `CR_PAT` (container registry: `write:packages`, `repo`, `workflow`) is used only by the login + build/push steps; `GS_PAT` (gitops repo manipulation only) is used only by the final git-clone-and-push step. Reusing the container-registry token for the gitops update would work but violates least privilege — the pipeline only gets the permissions each step actually needs. Second, **the image is tagged twice**: with `latest` for human readability, and with a unique hash (commit SHA) so the gitops repo's image field actually changes on every push. Without the unique tag, the gitops repo's `deployment.yaml` would stay `latest` forever and ArgoCD would never see a diff to reconcile.

The pipeline uses a **self-hosted runner** rather than GitHub-hosted, configured under Settings → Actions → Runners → New self-hosted runner. This matters because the Docker build steps require a Docker daemon — the runner machine itself must have Docker Desktop (or equivalent) installed and running. A common failure mode is the `setup-buildx-action` step silently erroring because the daemon isn't up. When troubleshooting, the discipline is the same as any pipeline: read each step's logs, `cat` the file before and after the edit step to see what actually changed, and re-run.

## Context
From the "Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions)" video, module 2. Walks through every step of the workflow file, the two PATs, and a debugging session when an `sed` pattern failed to match.

## Related
- [[cicd-two-repo-split]]
- [[image-tag-unique-hash-gitops]]
- [[argocd-application-crd-gitops]]
- [[InaAI]]
