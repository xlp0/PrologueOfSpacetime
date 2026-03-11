---
description: OpenClaw Local Memory Setup and Document Indexing
---

# Fully Local AI Memory Architecture (OpenClaw)

This workflow describes the process for setting up a scalable, 100% local memory architecture using OpenClaw, Ollama, ChromaDB, and BAAI/bge-large-en-v1.5 to handle over 10,000 documents without requiring any cloud API.

## Step 1: Update OpenClaw Base Dependencies

1. Pull the local embedding model into Ollama for OpenClaw's native memory:
   ```bash
   ollama pull nomic-embed-text
   ```

2. Modify `openclaw.json` config settings:
   - Change `memorySearch.provider` to `"ollama"`.
   - Update multi-tasking thresholds:
     ```json
     "maxConcurrent": 6,
     "subagents": {
       "maxConcurrent": 8
     },
     "debounceMs": 1500
     ```

## Step 2: Set Up Python Virtual Environment using `uv`

Initialize a separate virtual environment using `uv` for handling the document ingestion pipeline. `uv` is significantly faster and more reliable.

```bash
# Install uv if not already installed
# curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv
source .venv/bin/activate
uv pip install chromadb sentence-transformers pymupdf python-docx
```

## Step 3: Implement Document Indexing Pipeline

Create `doc_search.py` in your workspace. This script connects the embeddings model to the persistent ChromaDB storage.

Keys to the pipeline:
- **Embedding Model:** `BAAI/bge-large-en-v1.5` for high-quality semantic similarity.
- **Chunking Strategy:** ~500 tokens with 50-token overlaps format handling for Markdown, PDF, JSONL, and Word.
- **Database:** Auto-embeds and stores to `.openclaw/vector_db/`.

## Step 4: Create the OpenClaw "document-search" Skill

OpenClaw bots need explicit permissions to query the documents folder. Integrate the `skill_document_search.json` reference file into your OpenClaw agent's skills list.

- The reference file uses `uv run doc_search.py --query "{{query}}"`
- This will return the top-K relevant chunks with their context strings to the agent context.

## Step 5: Background Indexing Service (systemd)

To keep your document embeddings constantly up to date without blocking the LLM, deploy the provided systemd service and path watcher.

1. Copy `openclaw-indexer.service` and `openclaw-indexer.path` to `/etc/systemd/system/`.
2. Edit them to replace `YOUR_USERNAME` with your actual Linux user and paths to the cloned scripts.
3. Enable and start the watcher:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now openclaw-indexer.path
   sudo systemctl start openclaw-indexer.service
   ```

Now, anytime you drop a new PDF or Markdown file into `~/.openclaw/documents`, it will automatically be chunked and embedded by `BAAI/bge-large-en-v1.5` in the background.
