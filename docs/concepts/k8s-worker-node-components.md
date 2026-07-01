---
title: 'k8s-worker-node-components'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, kubernetes, k8s, worker-node, kubelet, container-runtime, kube-proxy]
type: concept
sources: [YouTube — Kubernetes Explained in 6 Minutes | k8s Architecture (https://www.youtube.com/watch?v=TlHvYWVUZyc)]
status: stable
liberal_art: Trivium-Grammar
---

# Kubernetes Worker Node Components — Kubelet, Container Runtime, Kube-Proxy

## Insight
Inside a Kubernetes cluster (see [[k8s-cluster-architecture]]) the **worker nodes** are where containerized application workloads actually run. Each worker node runs three core Kubernetes components on top of the OS — and the design is that the node is essentially an execution agent for the control plane (see [[k8s-control-plane-components]]).

1. **kubelet.** A daemon that runs on each worker node. It is responsible for communicating with the control plane: it receives instructions from the control plane about which pods to run on the node, and ensures the desired state of those pods is maintained. Kubelet is the local representative of the control plane on every node — when the scheduler (running in the control plane) assigns a pod to a node, it's the kubelet on that node that actually makes the pod happen and keeps it happening.

2. **Container runtime.** The component that runs the containers on the worker nodes. It is responsible for pulling container images from a registry, starting and stopping containers, and managing the containers' resources. Kubelet tells the runtime what to run; the runtime knows how to run containers (containerd, CRI-O, historically Docker). The split is intentional — k8s standardizes the interface so the runtime is pluggable.

3. **kube-proxy.** A network proxy that runs on each worker node. It is responsible for routing traffic to the correct pods and provides load balancing for the pods, ensuring traffic is distributed evenly across them. Without kube-proxy, a service exposing a set of pods would have no way to actually reach them — it's the per-node networking glue that makes the abstract "Service" primitive resolve to actual pod IPs.

The throughline: every worker node is a thin, identical stack — kubelet (control channel), container runtime (execution), kube-proxy (networking). That uniformity is what lets the cluster scale horizontally: add a node, install these three, register with the control plane, and the scheduler can immediately start placing pods on it. The control plane owns the decisions; the worker node components own the execution.

## Context
From the "Kubernetes Explained in 6 Minutes | k8s Architecture" explainer — the segment on what runs on each worker node.

## Related
- [[k8s-cluster-architecture]] — how worker nodes fit into the larger cluster (control plane + worker nodes + pods)
- [[k8s-control-plane-components]] — the control plane whose instructions (scheduler assignments, desired state) the kubelet on each worker node receives and executes
- [[argocd-declarative-gitops-k8s]] — ArgoCD and other external controllers talk to the control plane; the worker-node components are downstream of those decisions
- [[InaAI]]
