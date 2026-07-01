---
title: 'opengeoagent-architecture'
date: 2026-06-27
tags: [Quadrivium-Geometry, Seven-Liberal-Arts, opengeoagent, gis, qgis, multimodal, agent, llm, provider-agnostic]
type: concept
sources: [YouTube — OpenGeoAgent: A Multimodal AI Agent for Automated Geospatial Analysis (https://www.youtube.com/watch?v=5zkXQlHUsu8)]
status: stable
liberal_art: Quadrivium-Geometry
---

# OpenGeoAgent Architecture

## Insight
OpenGeoAgent is an open-source multimodal AI agent for geospatial analysis, shipped as a QGIS plugin (also Jupyter + Python scripting). Talk to it in text, voice, or images; it writes and executes the geospatial code for you — zoom to a city, delineate a watershed from a DEM, clip rasters to admin boundaries, compute median elevation, generate satellite imagery.

The problem it solves: GIS work has a brutally high floor. The moment you want anything beyond pan-and-zoom — watershed delineation, raster stats, clipping to a boundary — you're writing Python, debugging CRS mismatches, and remembering which Whitebox Tools function fills sinks vs. computes flow direction. For domain experts (urban planners, hydrologists, disaster-response analysts) who don't code, that means either begging a developer for help or not doing the analysis at all. LLMs alone don't fix this: a raw chat model can write the snippet but can't see your active QGIS layer, can't execute against it, and can't render the result back into the map canvas.

OpenGeoAgent puts an LLM agent inside your GIS session with three things a plain chatbot lacks:

1. **Live access to the QGIS project** — sees active layers, runs processing algorithms, drops new layers straight into the canvas.
2. **Tool-calling over a real geospatial toolkit** — Whitebox Tools for hydrology/terrain, general QGIS API, Google Earth Engine-style cloud catalogs, plus an image-generation tool.
3. **Multimodal I/O in both directions** — voice dictation (~$0.01/query via Whisper), image input, image output rendered in the chat pane, and text.

Provider-agnostic: OpenAI, Anthropic, Bedrock, Gemini, LiteLLM, local Ollama all work. Local Ollama is supported but not recommended — too slow for the multi-step tool chains the agent runs.

Chat history saves with the QGIS project, so the session becomes part of the project file — a domain-specific instance of the second-brain pattern (see [[second-brain-obsidian-foundations]]). The reusable architecture is the takeaway, not the geospatial specifics — see [[exposed-tool-source-code-pattern]].

## Context
From the OpenGeoAgent walkthrough; the architecture pattern is reusable beyond GIS.

## Related
- [[exposed-tool-source-code-pattern]]
- [[mcp-anthropic-standard]]
- [[second-brain-obsidian-foundations]]
- [[InaAI]]
