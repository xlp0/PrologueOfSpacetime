---
title: 'argocd-application-crd-gitops'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, argocd, gitops, kubernetes, ci-cd, declarative-sync]
type: principle
sources: [YouTube — Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions) (https://www.youtube.com/watch?v=GlhK7mz5IJo)]
status: stable
liberal_art: Trivium-Grammar
---

# ArgoCD Application CRD — pull-based GitOps reconciliation

## Insight
ArgoCD is a controller that runs **inside** the Kubernetes cluster and treats a git repository as the single source of truth for what should be deployed. The binding between ArgoCD and a target git repo is declared as an `Application` custom resource — a YAML file you `kubectl apply` into the `argocd` namespace. The Application CRD specifies: which repo to source, which path inside that repo holds the manifests, the destination cluster/namespace, and the sync policy (manual or automatic).

The control loop is **pull-based**, not push-based. Nothing in CI talks to the cluster directly. ArgoCD polls the gitops repo (or receives a webhook), detects a diff between the manifests in git and the resources currently in the cluster, and reconciles the cluster toward git. This is the opposite of `kubectl apply` from a CI runner, where the pipeline needs cluster credentials and pushes changes outward. With ArgoCD, the cluster holds its own credentials and pulls from git — the blast radius of a compromised CI runner is limited to the registry and the gitops repo, never the cluster itself.

A practical gotcha the video hits: if the image lives in a **private** container registry (GitHub Container Registry defaults to private), the pod will fail with `ErrImagePull`. The fix is an `imagePullSecret` — a Kubernetes Secret of type `dockerconfigjson`, built from the same container-registry PAT, that ArgoCD's deployment can reference. Without it, ArgoCD happily creates the Deployment and Service objects (those are just YAML) but the pods can never pull. The reconciliation loop surfaces this as a degraded Application health status in the ArgoCD UI — the manifest is synced but the workload is not healthy.

The deeper idea: ArgoCD makes "git is the deployment spec" operationally enforceable. A `git revert` is now a rollback. A diff in `deployment.yaml` is now a deployment event. The cluster is no longer a place you push to — it's a place that watches git and catches up.

## Context
From the "Kubernetes CI/CD: Build a Pipeline (ArgoCD + Github Actions)" video, module 3. Covers installing ArgoCD, port-forwarding the UI, applying the Application CRD, and resolving the imagePullSecret failure.

## Related
- [[cicd-two-repo-split]]
- [[github-actions-ci-pipeline]]
- [[image-tag-unique-hash-gitops]]
- [[InaAI]]
