---
title: 'file-storage-hierarchical-namespace'
date: 2026-06-30
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, file-storage, block-storage, system-design, nas, storage]
type: concept
sources: [YouTube — File Storage VS Object Storage | System Design (https://www.youtube.com/watch?v=AV4Ei1qW89o)]
status: stable
liberal_art: Quadrivium-Geometry
---

# File Storage — Hierarchical Namespace on Block Devices

## Insight
File storage is the traditional model for storing data: files are organized in a **hierarchical directory structure** — folders inside folders, much like the file explorer on a personal computer. Each file is addressed via a specific file path (e.g. `/home/user/documents/file.txt`), and that path-based addressing is what makes the model intuitive to navigate and manage.

Under the hood, file storage sits on top of **block devices**. Files are broken down into fixed-size blocks of data, which are then written to disk. This block-backed design is what makes file storage efficient at reading and writing data quickly, especially for small files. Common file systems — **NTFS, FAT32, ext4** — and network protocols — **NFS (Network File System) and SMB (Server Message Block)** — are all built on this model. NFS and SMB extend the model across a network, letting users read, write, and manage files over local or networked storage as if they were local.

The advantages fall out of the structure: it is familiar and intuitive (most users already think in files and folders); it supports **granular permissions** that can be set on individual files and directories, enhancing security; and it is optimized for handling numerous small files efficiently.

The trade-offs are structural, not incidental. File storage systems struggle to scale efficiently when dealing with massive amounts of data — the hierarchical namespace that makes navigation intuitive becomes a bottleneck at scale. File systems typically allow only **basic metadata** (file size, timestamps), which is insufficient for advanced data management. And managing large unstructured data sets becomes cumbersome in a tree structure designed for human-navigable organization.

## Context
From the "File Storage VS Object Storage | System Design" explainer video, in the segment introducing file storage as the traditional baseline before contrasting it with object storage.

## Related
- [[object-storage-flat-namespace-metadata]] — the contrast: flat namespace, rich metadata, scales to petabytes
- [[file-vs-object-storage-decision-criteria]] — when to pick file storage over object storage
- [[minio-s3-compatible-object-storage]] — MinIO is positioned as a modern replacement for traditional SAN/NAS file storage
- [[InaAI]]
