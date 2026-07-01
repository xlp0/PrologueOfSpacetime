---
title: 'k8s-control-plane-components'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, kubernetes, k8s, control-plane, api-server, etcd, scheduler, controller-manager]
type: concept
sources: [YouTube — Kubernetes Explained in 6 Minutes | k8s Architecture (https://www.youtube.com/watch?v=TlHvYWVUZyc)]
status: stable
liberal_art: Trivium-Grammar
---

# Kubernetes Control Plane Components — API Server, etcd, Scheduler, Controller Manager

## Insight
The **control plane** (see [[k8s-cluster-architecture]]) is the brain of a Kubernetes cluster, and it consists of four core components. Each one owns a distinct responsibility, and the separation is what makes the system composable: tools that want to talk to k8s only need to talk to one of these components, almost always the API server.

1. **API server.** The primary interface between the control plane and the rest of the cluster. It exposes a RESTful API that allows clients — `kubectl`, dashboards, CI/CD systems like ArgoCD (see [[argocd-declarative-gitops-k8s]]), custom controllers — to interact with the control plane and submit requests to manage the cluster. Almost every k8s integration in the ecosystem works by calling this API; it's the chokepoint that makes the platform scriptable.

2. **etcd.** A distributed key-value store that stores the cluster's persistent state. The API server and the other control plane components use etcd to store and retrieve information about the cluster. Conceptually etcd is the source of truth — desired state, current state, secrets, config, all persisted here. If the control plane is the brain, etcd is the part that actually remembers.

3. **Scheduler.** Responsible for scheduling pods onto worker nodes. It uses information about the resources required by the pods and the available resources on the worker nodes to make placement decisions. The scheduler doesn't run anything — it assigns pods to nodes, and the kubelet on the chosen node (see [[k8s-worker-node-components]]) does the actual work of running them.

4. **Controller manager.** Runs the controllers that manage cluster state. The video calls out two examples: the **replication controller**, which ensures the desired number of pod replicas are running, and the **deployment controller**, which manages rolling updates and rollbacks of deployments. The throughline across all controllers is reconciliation — they continuously observe current state via the API server and push it toward desired state.

The pattern that ties the four together: the API server is the single ingress, etcd is the persistent substrate, and the scheduler + controller manager are loops that read from and write to the API server to drive the cluster toward desired state. This is the same reconciliation loop that tools like ArgoCD (see [[argocd-declarative-gitops-k8s]] and [[declarative-desired-state-yaml]]) externalize at the deployment layer.

## Context
From the "Kubernetes Explained in 6 Minutes | k8s Architecture" explainer — the segment breaking down the four control plane components.

## Related
- [[k8s-cluster-architecture]] — how the control plane fits into the larger cluster (control plane + worker nodes + pods)
- [[k8s-worker-node-components]] — the worker-side counterparts (kubelet, container runtime, kube-proxy) that receive instructions from this control plane
- [[argocd-declarative-gitops-k8s]] — ArgoCD is an external controller that watches the API server and runs its own reconciliation loop
- [[declarative-desired-state-yaml]] — the same desired-state-vs-current-state reconciliation pattern, applied at the deployment layer
- [[agentic-harness-90-percent]] — control plane = harness (the 90%); workers = swappable executors (the 10%)
- [[InaAI]]
