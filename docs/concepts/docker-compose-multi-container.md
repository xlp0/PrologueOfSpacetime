---
title: 'docker-compose-multi-container'
date: 2026-06-30
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, docker, docker-compose, multi-container, orchestration]
type: concept
sources: [YouTube — The Only Docker Tutorial You Need To Get Started (https://www.youtube.com/watch?v=DQdB7wFEygo)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Docker Compose multi-container applications

## Insight
Once you have more than one service — a backend plus a database, say — you face a choice: stuff everything into one giant container, or split each service into its own container. The video is blunt: don't do the first one. "Please don't do that, it's pretty stupid." One-container-per-service is the standard pattern, called a **multi-container application**.

The problem this creates is operational. If you have three containers, you have to start them individually, in the right order, with the right environment, on the right network, and stop them all when you're done. Doing this with bare `docker run` commands is brittle and unreadable. **Docker Compose** solves it by declaring the whole topology in a single `compose.yaml` (the video says `composed.yo` — auto-captions; the real file is `compose.yaml` or `docker-compose.yml`).

The shape of the file is simple: a top-level `services:` key, and under it one key per container. Each service is configured declaratively — you tell Compose what the container should look like and it figures out the `docker run` invocations. The two most common service shapes the video shows:

- **Build from a Dockerfile** — use `build: .` (or a path), and Compose will run `docker build` on that Dockerfile. Used when the service is *your* code.
- **Pull a prebuilt image** — use `image: postgres` and Compose will pull it from a registry. Used when the service is off-the-shelf software.

Other service-level keys shown: `ports:` (port forwarding, same as `-p` on `docker run`), and `environment:` (env vars for the container, used here to set the database's credentials). Anything you'd pass as a flag to `docker run` has a Compose equivalent.

The lifecycle is two commands: `docker compose up` (builds + starts every service in the file, wiring their networking together) and `docker compose down` (stops and removes them). The file is the single source of truth for the application's local shape — anyone with the repo can run the same stack with `docker compose up` and no further setup.

Compose is the bridge between local dev and production orchestration. It's deliberately smaller than Kubernetes — no reconciliation loops, no control plane — but the multi-container, declarative-service-list pattern is the same one k8s uses (a Pod per service, manifests instead of YAML, see [[k8s-cluster-architecture]]). Compose is also where [[docker-volumes-persistence]] get declared, so a database survives a `compose down`.

## Context
From "The Only Docker Tutorial You Need To Get Started" — step 9 of the video, where the example Node server is extended with a Postgres database via a `compose.yaml` file.

## Related
- [[docker-volumes-persistence]]
- [[dockerfile-instructions]]
- [[docker-images-vs-containers]]
- [[k8s-cluster-architecture]]
- [[InaAI]]
