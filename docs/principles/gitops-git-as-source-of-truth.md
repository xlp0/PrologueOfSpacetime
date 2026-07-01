---
title: 'gitops-git-as-source-of-truth'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, gitops, cd, declarative, kubernetes, devops]
type: principle
sources: [YouTube — What is ArgoCD (https://www.youtube.com/watch?v=p-kAqxuJNik)]
status: stable
liberal_art: Trivium-Grammar
---

# GitOps — Git as source of truth

## Insight
GitOps is the practice of taking code committed to a Git repository (GitHub, Bitbucket, etc.) all the way from commit to a production deployment. The Git repo is the source of truth — the canonical state of what production should look like — and an automated pipeline converges the production server to match whatever is in Git.

The defining shift is that the deployment pipeline is triggered by Git events, not by an ops person running a script or clicking "deploy" in a UI. A push to the repo becomes (directly or eventually) a change in production. The video's example is Rav's cat Twinkles walking across the keyboard and pushing code: because a GitOps pipeline is in place, that push makes it all the way to production. The story is half joke, half serious — the joke is that the cat shipped broken code; the serious point is that the commit-to-deploy path is fully automated with no manual gate in the middle.

The tradeoff is real: you get speed and reproducibility (every deploy is a commit, every commit is auditable), but you also need a fast way to revert bad state, because anything that lands in Git can land in production. This is why tools like ArgoCD pair GitOps with one-click rollback and health checks — see [[argocd-rollback-health-checks]].

A second implication: anything NOT in Git is not authoritative. Manual tweaks to production are drift, not state. The declarative YAML in the repo describes the intended architecture, and the system's job is to keep reality matching it. When someone bypasses Git to change production directly, a proper GitOps setup will eventually revert that change on the next reconciliation — see [[declarative-desired-state-yaml]].

## Context
From the "What is ArgoCD" explainer video, which introduces ArgoCD by first defining GitOps as its foundation.

## Related
- [[argocd-declarative-gitops-k8s]]
- [[declarative-desired-state-yaml]]
- [[argocd-rollback-health-checks]]
- [[karpathy-llm-wiki-vs-rag]] — Git is the wiki for cluster state; RAG starts from zero, git-as-truth compounds
- [[InaAI]]
