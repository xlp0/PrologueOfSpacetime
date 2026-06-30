---
concept: Canary deployment traffic shift with Argo Rollouts
tags: [gitops, deployment, kubernetes, canary, argocd]
source: YouTube — How to design a Deployment Pipeline (GitOps) (https://www.youtube.com/watch?v=pJ9f7w4AxtU)
date: 2026-06-30
---

# Canary deployment traffic shift with Argo Rollouts

## Insight
Users don't hit a Kubernetes application directly — they go through a load balancer, which distributes traffic across the running pods. A canary deployment exploits this: you run both the old version (`v1.0`) and the new version (`v1.1`) simultaneously, then **gradually drift traffic** from old to new in increments (100/0 → 90/10 → 80/20 → ... → 0/100). Once 100% of traffic is on the new version, you cut off and remove the old pods entirely. Repeat for every release.

The point is blast-radius control: if the new version is broken, the regression shows up on the 10% slice first, and you can roll back before most users are affected. Without canary, a bad deploy is a 100%-of-users problem.

In Kubernetes this is usually done with **Argo Rollouts** (a sibling project to Argo CD). Instead of a plain `Deployment`, you create a `Rollout` object — same shape (it creates pods/containers), but with traffic-shifting awareness built in. As the rollout progresses, the controller adds pods running the new version and removes pods running the old version, and instructs the load balancer to follow that pod-weight shift. When the last old pod is terminated, the rollout is complete.

This is the production-tier complement to the basic push-vs-pull GitOps decision. Push or pull decides *how* manifests get applied to the cluster; canary decides *how* the new version is exposed to users once it's applied. They compose — Argo CD syncs the `Rollout` object from the config repo, and Argo Rollouts then executes the gradual traffic shift inside the cluster.

## Context
From the YouTube video "How to design a Deployment Pipeline (GitOps)" — the video ends with canary deployments as the recommended production-grade pattern for any deployment pipeline.

## Related
- [[gitops-pull-vs-push]]
- [[argocd-declarative-gitops-k8s]]
- [[environment-promotion-gates]]
- [[InaAI]]
