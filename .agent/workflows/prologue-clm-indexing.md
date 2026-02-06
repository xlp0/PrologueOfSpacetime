---
description: How to index and relate content using the Cubical Logic Model (CLM)
---

# Prologue of Spacetime: CLM Indexing Workflow

This workflow describes how to index any content in the **Prologue of Spacetime** project using the **Cubical Logic Model (CLM)**.

## The Three Handles

Every piece of content MUST be relatable to one of three CLM dimensions. If a document is purely one type, leave the other fields as the content hash.

| Dimension | Handle Name | Description | Example |
| :--- | :--- | :--- | :--- |
| **Abstract Specification** | `Spec` | The Intent, Requirement, or "Why" of the content. | A user story, a design doc, a lesson objective. |
| **Concrete Implementation** | `Impl` | The Code, Process, or "How" of the content. | A Python script, a workflow, a procedure. |
| **Balanced Expectations** | `Exp` | The Test Data, Verification, or "Proof" of the content. | Unit tests, historical data samples, audit logs. |

## Indexing a New Document

1.  **Determine the Primary Type**: Is this document primarily a `Spec`, `Impl`, or `Exp`?
2.  **Add YAML Frontmatter**: Add CLM metadata to the document's frontmatter:

    ```yaml
    ---
    clm:
      type: Spec # or Impl, or Exp
      related_impl: <hash or path to implementation>
      related_exp: <hash or path to test data>
    ---
    ```

3.  **Generate Content Hash**: If the document has no explicit relations, use its content hash as the fallback handle.

    ```bash
    # Generate SHA-256 hash of the file content
    shasum -a 256 path/to/document.md
    ```

4.  **Update the Index**: Add the document to the project's CLM index (typically in `docs/` or the main README).

## The CLM Guarantee

> "We always have a handle. The worst case is the content hash."

This means:
- No content is ever "lost" or "orphaned."
- All content is addressable and relatable.
- **Latent opportunities** (hidden connections) can be surfaced by comparing vectors.

## Example: Indexing a Chapter MVP Card

For `chapters/01_The_Value_of_Counting/MVP_The_Counter.md`:

-   **CLM Type**: `Spec` (It describes *what* the Counter station is).
-   **Related Impl**: `chapters/01_The_Value_of_Counting/mcard_generator.js` (A script that creates MCards).
-   **Related Exp**: `chapters/01_The_Value_of_Counting/tests/counter_tests.json` (Sample data and test cases).

## Relating Content Across Chapters

Use **Cosine Similarity** to measure relatedness between any two CLM vectors.

-   If `Spec_A` and `Spec_B` have similarity > 0.85, they are "effectively the same intent."
-   If `Impl_C` and `Exp_D` have low similarity, there may be a bug or drift.

This is the foundation of **Pre-Established Harmony**: Consensus via vector alignment, not negotiation.
