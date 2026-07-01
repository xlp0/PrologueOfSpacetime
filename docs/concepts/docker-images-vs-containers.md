---
title: 'docker-images-vs-containers'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, docker, containers, images, packaging]
type: concept
sources: [YouTube — The Only Docker Tutorial You Need To Get Started (https://www.youtube.com/watch?v=DQdB7wFEygo)]
status: stable
liberal_art: Trivium-Grammar
---

# Docker images vs containers

## Insight
Docker's entire mental model collapses into two objects you have to keep straight: **images** and **containers**. The video's analogy is the cleanest one going: an image is the **recipe**, a container is the **meal**.

An image contains everything needed to run a piece of code — the runtime (Node, Python), system tools, library dependencies, environment defaults, and the application code itself. It's a read-only template. Nothing executes from inside an image; an image just *is*. A container is what gets instantiated *from* an image when you actually want the code to run. One image can spawn many container instances, all sharing the same recipe but living independently — separate process state, separate filesystem writes, separate lifecycles.

This is why the "works on my machine" problem is the canonical Docker pitch. The failure mode isn't usually that the code is wrong; it's that the execution environment differs across machines — wrong Node version, missing system lib, divergent env vars. An image bakes the environment into the artifact itself. When you hand someone an image (or a Dockerfile that produces one), you're handing them the recipe plus the kitchen, not just the dish. Their container can differ from yours only if they explicitly change the inputs.

The packaging framing matters because it tells you where Docker sits in the stack: it's a **packaging and runtime-isolation technology**, not a virtualization technology. There's no guest OS per container; containers share the host kernel. That's the reason a container starts in milliseconds where a VM takes seconds-to-minutes — there's no boot sequence, just process start. The tradeoff is that an image only runs on a kernel compatible with the one it was built against (a Linux image runs on Linux hosts or a Linux VM on Mac/Windows).

The image/container split also explains the rest of Docker's surface area. `docker build` produces an image from a Dockerfile. `docker run` turns an image into a container. `docker pull` / `docker push` move images between a registry and a host. Nothing in the CLI operates on a container that doesn't first exist as an image — the image is the source of truth for what the container will look like when it starts.

## Context
From "The Only Docker Tutorial You Need To Get Started" — the video opens with this recipe-vs-meal analogy as the foundation everything else (Dockerfile, build, run, compose) builds on.

## Related
- [[dockerfile-instructions]]
- [[docker-layer-caching]]
- [[image-tag-unique-hash-gitops]]
- [[k8s-cluster-architecture]]
- [[InaAI]]
