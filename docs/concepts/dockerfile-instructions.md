---
title: 'dockerfile-instructions'
date: 2026-06-30
tags: [Trivium-Grammar, Seven-Liberal-Arts, docker, dockerfile, images, build]
type: concept
sources: [YouTube — The Only Docker Tutorial You Need To Get Started (https://www.youtube.com/watch?v=DQdB7wFEygo)]
status: stable
liberal_art: Trivium-Grammar
---

# Dockerfile instructions

## Insight
A Dockerfile is the literal recipe that produces a Docker image (see [[docker-images-vs-containers]]). Every Dockerfile starts with `FROM`, which selects a **base image** — your starting point. The video uses `FROM node:22` to inherit the official Node.js runtime plus everything it needs, so you don't reinvent a Linux image from scratch. The choice of base image is the single biggest determinant of what your final image looks like.

After `FROM`, a typical Node Dockerfile walks through: `WORKDIR /app` (sets the working directory inside the image so subsequent commands have a known location), `COPY package*.json .` (copies the package manifest *before* the source code — see [[docker-layer-caching]] for why the order matters), `RUN npm install` (executes a shell command at build time to install dependencies), `COPY . .` (copies the rest of the source), `ENV PORT=...` (sets an environment variable baked into the image), and `EXPOSE <port>` (documents which port the container listens on — it doesn't actually publish it; that's what `-p` on `docker run` does).

The single non-obvious distinction the video draws is **`RUN` vs `CMD`**. `RUN` executes at **build time** — it modifies the image (e.g. installing deps, compiling assets). `CMD` executes at **container start time** — it's the process that gets launched when the container runs (e.g. `npm start`). If you used `RUN npm start` instead of `CMD ["npm", "start"]`, the start command would have executed during the build and finished, leaving the resulting container with nothing to do at runtime. The container would never actually start as a server. This is the most common beginner Dockerfile mistake and the one the video spends a beat on.

A `.dockerignore` file pairs with the Dockerfile the same way `.gitignore` pairs with git — it tells `COPY . .` what to skip. The canonical entry is `node_modules/`: you don't want your host's `node_modules` (which may have been built for the host OS) clobbering the image's `node_modules` (which was installed by `RUN npm install` inside the Linux image). The build context shrinks, the build gets faster, and the image stays consistent with its base image's architecture.

The Dockerfile is also where layer caching lives — every instruction is a layer, and the ordering of those instructions decides what rebuilds and what doesn't.

## Context
From "The Only Docker Tutorial You Need To Get Started" — the video walks through writing a Dockerfile for a simple Node server step by step, with the `RUN` vs `CMD` distinction called out explicitly.

## Related
- [[docker-images-vs-containers]]
- [[docker-layer-caching]]
- [[docker-compose-multi-container]]
- [[InaAI]]
