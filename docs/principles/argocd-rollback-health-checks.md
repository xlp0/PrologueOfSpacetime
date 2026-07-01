---
title: 'argocd-rollback-health-checks'
date: 2026-06-30
tags: [Trivium-Logic, Seven-Liberal-Arts, argocd, gitops, kubernetes, observability, cd]
type: principle
sources: [YouTube — What is ArgoCD (https://www.youtube.com/watch?v=p-kAqxuJNik)]
status: stable
liberal_art: Trivium-Logic
---

# ArgoCD rollback and health checks

## Insight
ArgoCD provides two operational features that make GitOps safe to actually run in production: **rollback** and **health checks**. Without these, GitOps would be a footgun — fast to push, but no way to undo or to know when something went wrong.

**Rollback.** When something bad reaches production — the video's example is Rav's cat Twinkles walking across the keyboard and pushing broken code while Rav naps at his laptop — ArgoCD can roll the cluster back to the last stable state with a single action. Because every deployment corresponds to a Git commit, "last stable state" is well-defined: it's the previous known-good commit. There's no need to reconstruct what the previous state was; it's in Git history. The whole point of pairing GitOps with one-click rollback is that the same automation that lets bad code ship fast also lets you undo fast. See [[gitops-git-as-source-of-truth]] for why the Git-as-source-of-truth model makes rollback trivially definable.

**Health checks.** ArgoCD surfaces the health of every deployment in both a UI and a CLI, so you can query the state of production without SSHing into anything. The video's example is a missing image registry secret — pods can't pull their images, so the deployment is unhealthy. ArgoCD shows that in the UI and lets you query it from the CLI. The health system is "robust" (the video's word) — it's not just a green/red dot, it surfaces the underlying reason, like a registry secret being unreachable.

Together these two features close the GitOps loop: GitOps lets you push fast, rollback lets you undo fast, and health checks let you know when you need to. The declarative YAML (see [[declarative-desired-state-yaml]]) defines what "healthy" should look like; the health check system reports whether reality matches; rollback restores the match when it doesn't. The ArgoCD UI is the unifying surface — you can see drift, see health, and trigger rollback from one place.

## Context
From the "What is ArgoCD" explainer video. Two of the three character stories (Rav and John) are used to illustrate these operational features.

## Related
- [[argocd-declarative-gitops-k8s]]
- [[gitops-git-as-source-of-truth]]
- [[declarative-desired-state-yaml]]
- [[InaAI]]
