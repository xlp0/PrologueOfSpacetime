---
title: 'docker-layer-caching'
date: 2026-06-30
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, docker, dockerfile, build, caching, layers]
type: concept
sources: [YouTube — The Only Docker Tutorial You Need To Get Started (https://www.youtube.com/watch?v=DQdB7wFEygo)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Docker layer caching

## Insight
Every instruction in a Dockerfile (see [[dockerfile-instructions]]) is a **layer**. Docker doesn't rebuild the image from scratch each time you run `docker build` — it walks the Dockerfile top-to-bottom and asks, for each layer, one question: *did the inputs to this layer change since the last build?* If yes, re-execute the instruction and rebuild this layer plus every layer below it. If no, reuse the cached result. That's the whole mechanic. "Layer changed → do it again. Layer did not change → use cache."

The implication is that **instruction order is a performance decision**, not just a correctness one. The video's example is the canonical one: in a Node project you have `COPY package*.json .` *before* `COPY . .` and `RUN npm install` *before* `COPY`-ing source. The reason is dependency-install cost. `npm install` is slow — it hits the network, resolves a tree, writes megabytes to disk. If you `COPY . .` first and *then* `RUN npm install`, then every time you change a single line of application code, the `COPY . .` layer changes, which invalidates the `npm install` layer below it, which means deps get re-downloaded on every build. By copying `package*.json` and running `npm install` *before* the rest of the source lands, you make dep installation depend only on whether the manifest changed — which is rare. Application code changes invalidate only the `COPY . .` layer and whatever's below it, not the dep-install layer. Build time drops from minutes to seconds on most iterations.

The cache invalidation is **positional**: once a layer rebuilds, everything downstream rebuilds regardless of whether its own inputs changed. So the rule of thumb is: **stable, slow operations early; volatile, fast operations late.** Base image first, then OS packages, then language deps, then application code, then runtime config. The video doesn't name this principle but demonstrates it with the package.json ordering.

Where caching breaks down: anything non-deterministic in a layer (network calls that fetch latest, timestamps baked into the image, `git clone` of a moving branch) will produce cache hits that are stale or misses that shouldn't be. Pinning versions — `node:22` not `node:latest`, exact package versions in `package.json` — is what makes the cache trustworthy.

The same caching model extends beyond local builds: Docker Build Cloud and CI registries let teams share a cache so one developer's build reuses another's layers. Caching is also why image tagging with a unique hash (see [[image-tag-unique-hash-gitops]]) is what gives a CI pipeline a diff signal — the cache may say "nothing to rebuild" but the gitops repo needs the tag to change anyway.

## Context
From "The Only Docker Tutorial You Need To Get Started" — the video explicitly explains layer caching to justify why `package*.json` is copied before the rest of the source code in the example Dockerfile.

## Related
- [[dockerfile-instructions]]
- [[docker-images-vs-containers]]
- [[image-tag-unique-hash-gitops]]
- [[InaAI]]
