---
title: 'object-storage-tiered-pricing-by-access-frequency'
date: 2026-06-30
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, object-storage, cloud-pricing, cold-storage, data-infrastructure]
type: concept
sources: [YouTube — What is Object Storage? (https://www.youtube.com/watch?v=ZfTOQJlLsAs)]
status: stable
liberal_art: Quadrivium-Geometry
---

# Object Storage — Tiered Pricing by Access Frequency

## Insight
Object storage pricing is metered around three axes: storage volume (how much you store), request count (how many GETs and PUTs), and responsiveness (how fast you need reads back). Every vendor meters these slightly differently, but the structural tradeoff is the same: **the more performance you want, the more you pay.**

The IBM framing collapses this into a small number of access-frequency tiers, ordered from coldest to warmest:

- **Cold×10 (coldest of cold)** — data parked for 20+ years, the modern equivalent of writing to tape vaults where it will "probably never be seen again." Lowest cost. Regulatory and legal archives.
- **Cold** — data accessed every so often, maybe once every six months. Slightly more expensive than cold×10.
- **Cold-ish** — data accessed regularly, e.g. website assets served out of object-storage buckets. Higher-cost tier.

Notably, **a true "warm" tier doesn't really exist in object storage** — even the "regularly accessed" tier is still "cold-ish." Object storage is fundamentally not a high-performance tier; if you need hot data, you reach for block or file storage, or a CDN in front of the bucket.

The economic logic: cold data is cheap because the provider can pack it densely on slow media and not provision retrieval bandwidth. Warm-ish data costs more because the provider has to keep it on faster media and pay egress bandwidth when you read it. The pricing surface lets you tier your data — regulatory archives in cold×10, website assets in cold-ish — and pay roughly the right amount for each.

The front-end API is identical across tiers — the bucket and object model doesn't change. Tier is a back-end placement and billing decision, not a different API surface.

## Context
From the IBM "What is Object Storage?" explainer video — the pricing-tier framing as a responsiveness-vs-cost tradeoff.

## Related
- [[object-storage-flat-namespace-metadata]] — the primitives being priced
- [[object-storage-bucket-virtual-construct-replication]] — the bucket architecture whose durability and retrieval cost the tiers meter
- [[object-storage-workload-patterns]] — workloads land on different tiers depending on access frequency
- [[minio-s3-compatible-object-storage]] — MinIO is self-hosted, so cloud-tier pricing doesn't directly apply, but the access-frequency tradeoff still informs capacity planning
- [[InaAI]]
