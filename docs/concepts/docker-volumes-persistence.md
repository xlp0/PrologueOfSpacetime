---
title: 'docker-volumes-persistence'
date: 2026-06-30
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, docker, volumes, persistence, storage]
type: concept
sources: [YouTube — The Only Docker Tutorial You Need To Get Started (https://www.youtube.com/watch?v=DQdB7wFEygo)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Docker volumes for persistence and sharing

## Insight
A container's filesystem is **ephemeral**. Stop the container, remove it, start a new one from the same image, and everything written to disk during the previous run is gone — the new container starts from the image's baked-in filesystem as if nothing had happened. For stateless services (a web frontend) this is fine. For stateful ones (a database) it's a disaster. The video's framing: "whenever we close our containers we lose all the state and data."

The second problem volumes solve is **data sharing between containers**. In a multi-container app (see [[docker-compose-multi-container]]) the backend and the database don't share a filesystem by default — each container has its own isolated root. If you want a file written by one container to be readable by another, you need a shared storage location that lives outside any individual container's lifecycle.

A **volume** is that shared storage. Concretely it's a folder on the host machine that Docker manages and exposes to one or more containers. The container sees a normal directory at a path you choose; Docker maps reads and writes on that path to the host folder. Because the folder belongs to the host, not the container, the data persists across container restarts, replacements, and removals — the container can die and be replaced with a fresh one from the same image, and the volume's contents are untouched.

In a `compose.yaml` you declare volumes in two parts: a top-level `volumes:` block that *creates* the named volume (e.g. `postgres_data:`), and a per-service `volumes:` list that *mounts* it into a container at a path (e.g. `postgres_data:/var/lib/postgresql/data`). The first tells Docker "make this volume exist"; the second tells a specific container "use this volume here." A single named volume can be mounted into multiple containers, which is how data sharing works.

The deeper architectural move is the **separation of compute and state**. A container is replaceable precisely *because* its state lives outside it. You can rebuild the image, change the base image version, swap the runtime, run the container on a different host — none of that touches the data, because the data was never inside the container to begin with. This is the same principle that makes Kubernetes pods disposable (a pod dies, a new one replaces it, the volume reattaches — see [[k8s-cluster-architecture]]) and the same principle that makes object storage (see [[minio-s3-compatible-object-storage]]) a different persistence tier: stateless compute, stateful storage, decoupled lifecycles.

Volumes are not the only persistence option (bind mounts map a host path directly, and tmpfs mounts live in RAM), but for multi-container apps managed by Compose, named volumes are the default and the one the video demonstrates.

## Context
From "The Only Docker Tutorial You Need To Get Started" — step 9 of the video, added to the Compose example so the Postgres database survives container restarts.

## Related
- [[docker-compose-multi-container]]
- [[docker-images-vs-containers]]
- [[minio-s3-compatible-object-storage]]
- [[k8s-cluster-architecture]]
- [[InaAI]]
