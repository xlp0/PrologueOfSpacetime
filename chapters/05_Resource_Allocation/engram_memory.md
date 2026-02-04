# Engram Memory: The Knowledge Vault

Based on the [DeepSeek Engram Presentation](https://www.youtube.com/watch?v=zt1jlTPCaps), this document details the "Engram" architecture for conditional memory.

## 1. The Core Inefficiency

Current LLMs are inefficient because they use the same expensive compute (deep neural layers) for two very different tasks:
1.  **Reasoning**: "Why did Rome fall?" (Requires depth).
2.  **Recall**: "Who was Princess Diana?" (Requires a dictionary loop-up).

> *Using a massive GPU to look up a static fact is like using a supercomputer to read a phone book.*

## 2. The Engram Solution: Memory-Compute Separation

**Engram** introduces a "Conditional Memory" axis.

*   **System 1 (Memory)**: Fast, automatic pattern recognition. Handled by a massive embedding table (stored in RAM/CPU).
*   **System 2 (Reasoning)**: Slow, deliberate thinking. Handled by the GPU layers.

### The Mechanism
1.  **N-gram Hashing**: Input text is hashed (e.g., "The quick brown fox").
2.  **Lookup**: The hash retrieves a potential memory from the table.
3.  **Context Gating**: The model checks, "Is this memory relevant to my current context?"
    *   *Match*: The gate opens, and the static fact is injected directly.
    *   *Mismatch*: The gate closes (e.g., "Apple" the fruit vs "Apple" the stock).

## 3. The Economics of Intelligence

This architecture fundamentally alters the "Resource Allocation" of the model:

*   **RAM is Cheap**: We can store 100 Billion parameters in system RAM for pennies compared to GPU VRAM.
*   **Effective Depth**: By offloading fact-checks to RAM, the GPU layers are freed up to focus purely on reasoning, improving performance on benchmarks like ARC AGI by ~5%.
*   **Throughput**: Because lookups are deterministic, they can be pre-fetched, resulting in <3% latency penalty.
