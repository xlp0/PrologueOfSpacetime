# Token Mechanics: The Engine of Meaning

Based on the [Deep Dive Video](https://www.youtube.com/watch?v=AtYtuVTZCQU), this document details the technical operations of LLM Tokenization.

## 1. The Lifecycle of a Prompt

The process of "Thinking" in an LLM is a three-step cycle:

1.  **Encoding**: The input text is sliced into chunks and converted into a list of integers (Tokens) based on the model's specific vocabulary.
2.  **Processing**: The Model (Neural Network) ingests these integers and calculates the probable next integer.
3.  **Decoding**: The output integers are converted back into human-readable text.

> *Tokens are the "Currency of LLMs" representing the numeric values that models actually process.*

## 2. Tokenizer Variance

Not all drops of water are the same size. Similarly, not all tokenizers use the same vocabulary.

*   **Claude 3.5 vs. Gemini 2.0**: The same input string (e.g., "hello world") produces different token counts on different platforms.
*   **Implication**: Code tuned for one model's context window may overflow another's.

## 3. Vocabulary & Efficiency

The efficiency of a language depends on the **Granularity** of its tokenizer.

*   **Character-Level (Inefficient)**: 1 character = 1 token. "The" = 3 tokens.
*   **Subword-Level (Efficient)**: Common groups are fused. "The" = 1 token.
*   **Trade-off**: Larger vocabularies (more subwords) make processing faster (fewer steps for the LLM) but increase the model's memory footprint (larger embedding tables).

## 4. The "Rare Data" Penalty

The system is optimized for the "Happy Path" (Common English, JavaScript).

*   **Common Data**: "const a = 5;" is highly compressed.
*   **Rare Data**: Lewis Carroll's "frabjous" or Haskell code is split into many small fragments because the tokenizer has no dedicated pre-built token for them.
*   **Result**: Rare languages are literally "more expensive" to speak in terms of compute and cash.
