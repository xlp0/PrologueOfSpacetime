---
concept: k8s-cluster-architecture
tags: [kubernetes, k8s, cluster, control-plane, worker-nodes, pods]
source: YouTube — Kubernetes Explained in 6 Minutes | k8s Architecture (https://www.youtube.com/watch?v=TlHvYWVUZyc)
date: 2026-06-30
---

# Kubernetes Cluster Architecture — Control Plane + Worker Nodes + Pods

## Insight
A Kubernetes **cluster** is a set of machines, called **nodes**, used to run containerized applications. The cluster has two core pieces, and getting the split between them straight is the foundation everything else in k8s rests on.

The first piece is the **control plane**, which is responsible for managing the state of the cluster. In production environments the control plane usually runs on multiple nodes spanning several data center zones — i.e. it's replicated for high availability, not a single point of failure. The second piece is a set of **worker nodes**, which run the actual containerized application workloads. The control plane decides what should run where; the worker nodes execute that decision.

Between the control plane and the workload sits the **Pod**, the smallest deployable unit in Kubernetes. A pod hosts one or more containers and provides shared storage and networking for those containers. Pods are created and managed by the control plane — they are the basic building blocks of Kubernetes applications, the unit of scheduling, scaling, and lifecycle. You don't deploy a container directly; you deploy a pod that wraps the container(s) and gives them shared context.

The architectural move worth noting: separating **control** (state, scheduling decisions, reconciliation) from **execution** (running the actual containers) is what lets k8s be self-healing and horizontally scalable. Worker nodes can be added or removed and the control plane re-balances pods across what's available. Tooling like ArgoCD (see [[argocd-declarative-gitops-k8s]]) plugs into this model by talking to the control plane's API rather than touching worker nodes directly — the control plane stays the single control surface. The components that make up each side are covered in [[k8s-control-plane-components]] and [[k8s-worker-node-components]].

## Context
From the "Kubernetes Explained in 6 Minutes | k8s Architecture" explainer — the segment defining a cluster, the control plane / worker node split, and pods as the smallest deployable unit.

## Related
- [[k8s-origin-and-naming]] — where Kubernetes came from (Borg, 2014) and the "k8s" numeronym
- [[k8s-control-plane-components]] — what's inside the control plane (API server, etcd, scheduler, controller manager)
- [[k8s-worker-node-components]] — what's inside a worker node (kubelet, container runtime, kube-proxy)
- [[minio-s3-compatible-object-storage]] — MinIO is an example of stateful software that runs as pods on a k8s cluster
- [[InaAI]]
