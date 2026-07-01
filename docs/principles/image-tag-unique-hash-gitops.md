---
title: 'image-tag-unique-hash-gitops'
date: 2026-06-30
tags: [Quadrivium-Arithmetic, Seven-Liberal-Arts, gitops, ci-cd, docker, argocd, kubernetes]
type: principle
sources: [YouTube — Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions) (https://www.youtube.com/watch?v=GlhK7mz5IJo)]
status: stable
liberal_art: Quadrivium-Arithmetic
---

# Image tags must change for GitOps to detect a deploy

## Insight
In a GitOps pipeline, the only signal ArgoCD gets that something should be redeployed is a **diff in the gitops repo's manifests**. If every CI run tags the new image as `latest` and the `deployment.yaml` image field stays `ghcr.io/me/app:latest`, then as far as ArgoCD is concerned nothing has changed — git matches the cluster, sync is a no-op, the new image never rolls out. This is the single most common silent failure in hand-rolled GitOps pipelines.

The fix is to tag every image with a **unique, monotonically identifiable value** — typically the git commit SHA or the GitHub Actions run number — alongside the human-readable `latest` tag. The CI pipeline's final step writes that unique tag into the gitops repo's `deployment.yaml`. Now the image field actually changes on every push, ArgoCD sees a diff, and reconciliation kicks off. The unique tag is not for humans (we read `latest`); it's the deployment trigger for the reconciler.

This is the bridge concept between the CI half and the CD half of the pipeline. The CI side produces the artifact (image) and the diff signal (new tag in git); the CD side consumes both. Get either wrong and the pipeline stalls: missing artifact → `ErrImagePull`; missing diff signal → ArgoCD happily idle while you wonder why your commit didn't deploy. The video debugs a related failure — a `sed` pattern in the gitops-update step that didn't match the existing image field, so the file was committed unchanged and the pipeline reported success while nothing deployed. The lesson: the success of a GitOps pipeline is measured at the cluster, not at the CI runner.

## Context
From the "Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions)" video, module 2. The presenter explicitly explains why a unique tag is needed alongside `latest` — without it the gitops repo's image field wouldn't change and ArgoCD would have nothing to reconcile.

## Related
- [[github-actions-ci-pipeline]]
- [[argocd-application-crd-gitops]]
- [[cicd-two-repo-split]]
- [[InaAI]]
