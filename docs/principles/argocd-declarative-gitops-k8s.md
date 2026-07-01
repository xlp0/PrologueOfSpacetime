---
title: 'argocd-declarative-gitops-k8s'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, argocd, gitops, kubernetes, declarative, cd]
type: principle
sources: [YouTube — What is ArgoCD (https://www.youtube.com/watch?v=p-kAqxuJNik)]
status: stable
liberal_art: Trivium-Grammar
---

# ArgoCD — declarative GitOps on Kubernetes

## Insight
ArgoCD is a declarative GitOps tool built on top of Kubernetes. The video breaks the definition into three pillars that together explain what ArgoCD actually does:

1. **GitOps** — the workflow layer. Code committed to a Git repository flows all the way to the production deployment. Git is the source of truth, covered separately in [[gitops-git-as-source-of-truth]].
2. **Declarative** — the configuration layer. The full specification of the target architecture is written in YAML. These YAML files describe how production should look, ensuring consistency between what you expect and what's actually running. Covered in [[declarative-desired-state-yaml]].
3. **Kubernetes** — the runtime layer. The unit of deployment is the pod — e.g., a backend pod and a frontend pod — scaled up to meet user demand based on the specifications in the declarative YAMLs.

The combination is what matters. GitOps gives the trigger (a commit), declarative gives the spec (the YAML), Kubernetes gives the runtime (pods). ArgoCD's job is to keep all three in agreement: when Git changes, ArgoCD updates the cluster; when the cluster drifts away from the YAML, ArgoCD reconciles it back.

Because it's Kubernetes-native, scaling is a first-class operation — the "robot" inside ArgoCD that automatically scales back excess pods in the Steve story is just the reconciliation loop doing its job. And because deployments correspond to Git commits, operational features like rollback and health checks fall out naturally — see [[argocd-rollback-health-checks]].

The video's framing of ArgoCD's value is that it makes GitOps "easy to implement and easy to understand." Without ArgoCD you'd be wiring Git webhooks to kubectl invocations yourself; ArgoCD packages the Git→cluster reconciliation loop, the UI for visibility, and the CLI for query/automation into one tool.

## Context
From the "What is ArgoCD" explainer video, which introduces ArgoCD by walking through its three-pillar definition and then illustrating each with a character story.

## Related
- [[gitops-git-as-source-of-truth]]
- [[declarative-desired-state-yaml]]
- [[argocd-rollback-health-checks]]
- [[k8s-control-plane-components]] — ArgoCD is an external controller that watches the k8s API server and runs its own reconciliation loop
- [[InaAI]]
