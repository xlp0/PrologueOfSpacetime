#!/usr/bin/env python3
"""Distribute inaai/ files into typed subfolders + upgrade frontmatter + tag with seven liberal arts."""
import os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mapping: filename -> (subfolder, liberal_art, type)
FM = {
# Agent platforms -> concepts
'deerflow-harness-vs-framework.md': ('concepts','Trivium-Logic','concept'),
'deerflow-lead-agent-dynamic-subagents.md': ('concepts','Trivium-Logic','concept'),
'deerflow-sandbox-architecture.md': ('concepts','Trivium-Grammar','concept'),
'hermes-persistent-memory.md': ('concepts','Quadrivium-Astronomy','concept'),
'hermes-self-improving-skills.md': ('concepts','Trivium-Logic','concept'),
'hermes-sub-agents.md': ('concepts','Trivium-Logic','concept'),
'hermes-background-subagents.md': ('concepts','Quadrivium-Astronomy','concept'),
'hermes-imessage-photon-routing.md': ('concepts','Quadrivium-Music','concept'),
'hermes-ue5-mcp.md': ('concepts','Trivium-Rhetoric','concept'),
'catalog-vs-curator.md': ('concepts','Trivium-Logic','concept'),
'openclaw-vs-hermes-security-posture.md': ('principles','Trivium-Logic','principle'),
# Codebase knowledge graphs -> concepts
'graphify-codebase-knowledge-graph.md': ('concepts','Quadrivium-Geometry','concept'),
'agentic-os-shared-brain.md': ('concepts','Quadrivium-Astronomy','concept'),
'understand-anything-multi-agent-pipeline.md': ('concepts','Trivium-Logic','concept'),
'codebase-knowledge-graph-dashboard.md': ('concepts','Quadrivium-Geometry','concept'),
'wiki-backlinks-vs-kg-edges.md': ('concepts','Quadrivium-Geometry','concept'),
# Second brain -> concepts
'second-brain-obsidian-foundations.md': ('concepts','Trivium-Grammar','concept'),
'second-brain-business-os-wiring.md': ('concepts','Quadrivium-Music','concept'),
'karpathy-llm-wiki-vs-rag.md': ('concepts','Trivium-Logic','concept'),
'llm-wiki-three-layers.md': ('concepts','Trivium-Grammar','concept'),
'nick-milo-aios-three-layers.md': ('concepts','Trivium-Grammar','concept'),
'five-levels-second-brain.md': ('concepts','Quadrivium-Arithmetic','concept'),
'claude-fable-gets-it.md': ('concepts','Trivium-Rhetoric','concept'),
'visual-graph-layer-second-brain.md': ('concepts','Quadrivium-Geometry','concept'),
'second-brain-agency-product.md': ('concepts','Trivium-Rhetoric','concept'),
'reverse-engineer-data-shape.md': ('concepts','Quadrivium-Geometry','concept'),
'vector-retrieval-chunking-limit.md': ('concepts','Quadrivium-Geometry','concept'),
# Physical AI -> concepts
'physical-ai-chatgpt-moment.md': ('concepts','Quadrivium-Astronomy','concept'),
'nvidia-cosmos-world-model.md': ('concepts','Quadrivium-Astronomy','concept'),
'isaac-groot-reference-platform.md': ('concepts','Quadrivium-Astronomy','concept'),
'sim-to-real-gap.md': ('concepts','Quadrivium-Astronomy','concept'),
'pru-live-reprogramming.md': ('concepts','Quadrivium-Astronomy','concept'),
'ti-automotive-ai-hidden-products.md': ('concepts','Quadrivium-Astronomy','concept'),
# AI infra -> concepts
'ai-capex-not-bubble.md': ('concepts','Quadrivium-Arithmetic','concept'),
'ai-server-anatomy-h100.md': ('concepts','Quadrivium-Arithmetic','concept'),
'nvidia-tax-vs-ualink-alliance.md': ('concepts','Trivium-Logic','concept'),
'dwarf-star-ssd-streaming.md': ('concepts','Quadrivium-Astronomy','concept'),
# Other concepts
'packaging-is-the-product.md': ('concepts','Trivium-Rhetoric','concept'),
'static-vs-dynamic-context.md': ('concepts','Trivium-Logic','concept'),
'opengeoagent-architecture.md': ('concepts','Quadrivium-Geometry','concept'),
'k8s-cluster-architecture.md': ('concepts','Quadrivium-Geometry','concept'),
'k8s-control-plane-components.md': ('concepts','Trivium-Grammar','concept'),
'k8s-origin-and-naming.md': ('concepts','Trivium-Grammar','concept'),
'k8s-worker-node-components.md': ('concepts','Trivium-Grammar','concept'),
'minio-s3-compatible-object-storage.md': ('concepts','Quadrivium-Geometry','concept'),
# Principles: skills and token-cost
'skills-sh-markdown-spec.md': ('principles','Trivium-Grammar','principle'),
'skills-install-best-practices.md': ('principles','Trivium-Grammar','principle'),
'caveman-terse-output-skill.md': ('principles','Quadrivium-Arithmetic','principle'),
'ponytail-yagni-ladder.md': ('principles','Trivium-Logic','principle'),
'ponytail-vs-caveman-benchmark.md': ('principles','Quadrivium-Arithmetic','principle'),
'skill-injection-token-economics.md': ('principles','Quadrivium-Arithmetic','principle'),
'token-economics-vibe-vs-agentic.md': ('principles','Quadrivium-Arithmetic','principle'),
# Principles: agentic engineering
'agentic-harness-90-percent.md': ('principles','Trivium-Logic','principle'),
'ai-sdlc-spec-bottleneck.md': ('principles','Trivium-Grammar','principle'),
'plan-build-eval-review-split.md': ('principles','Trivium-Logic','principle'),
'session-start-prompt-pattern.md': ('principles','Trivium-Rhetoric','principle'),
# Principles: security
'prompt-injection-anatomy.md': ('principles','Trivium-Logic','principle'),
'prompt-injection-defense-in-depth.md': ('principles','Trivium-Logic','principle'),
# Principles: DevOps and GitOps
'cicd-two-repo-split.md': ('principles','Trivium-Grammar','principle'),
'github-actions-ci-pipeline.md': ('principles','Quadrivium-Music','principle'),
'argocd-application-crd-gitops.md': ('principles','Trivium-Grammar','principle'),
'argocd-declarative-gitops-k8s.md': ('principles','Trivium-Grammar','principle'),
'argocd-rollback-health-checks.md': ('principles','Trivium-Logic','principle'),
'canary-deployment-traffic-shift.md': ('principles','Quadrivium-Music','principle'),
'declarative-desired-state-yaml.md': ('principles','Trivium-Grammar','principle'),
'environment-promotion-gates.md': ('principles','Quadrivium-Music','principle'),
'gitops-git-as-source-of-truth.md': ('principles','Trivium-Grammar','principle'),
'gitops-pull-vs-push.md': ('principles','Trivium-Logic','principle'),
'gitops-two-repo-pattern.md': ('principles','Trivium-Grammar','principle'),
'image-tag-unique-hash-gitops.md': ('principles','Quadrivium-Arithmetic','principle'),
'physical-ai-real-time-constraints.md': ('principles','Quadrivium-Astronomy','principle'),
# Other principles
'me-md-vault-map-skill-map.md': ('principles','Trivium-Grammar','principle'),
'claude-md-routing-rules.md': ('principles','Trivium-Grammar','principle'),
'llm-wiki-lint-pass.md': ('principles','Trivium-Logic','principle'),
'second-brain-ingest-curation.md': ('principles','Trivium-Logic','principle'),
'exposed-tool-source-code-pattern.md': ('principles','Trivium-Rhetoric','principle'),
'daily-summaries.md': ('principles','Trivium-Rhetoric','principle'),
}

def upgrade_frontmatter(filepath, liberal_art, page_type):
    """Upgrade YAML frontmatter to wiki standard."""
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # Extract existing frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return False, "no frontmatter"

    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    # Extract title from first H1
    title_match = re.match(r'^#\s+(.+)$', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.splitext(os.path.basename(filepath))[0]

    # Extract existing fields
    source_match = re.search(r'^source:\s*(.+)$', fm_text, re.MULTILINE)
    source_val = source_match.group(1).strip() if source_match else ''
    sources = f"[{source_val}]" if source_val else "[]"

    date_match = re.search(r'^date:\s*(.+)$', fm_text, re.MULTILINE)
    date_val = date_match.group(1).strip() if date_match else '2026-06-27'

    tags_match = re.search(r'^tags:\s*(.+)$', fm_text, re.MULTILINE)
    existing_tags = tags_match.group(1).strip() if tags_match else '[]'

    # Build new frontmatter
    new_fm = f"""---
title: '{title}'
date: {date_val}
tags: [{liberal_art}, Seven-Liberal-Arts, {existing_tags.strip('[]')}]
type: {page_type}
sources: {sources}
status: stable
liberal_art: {liberal_art}
---"""

    new_content = new_fm + '\n' + body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True, "ok"


def main():
    os.chdir(REPO)
    moved = 0
    errors = []

    for filename, (subfolder, liberal_art, page_type) in FM.items():
        src = os.path.join('docs', 'inaai', filename)
        if not os.path.exists(src):
            errors.append(f"NOT FOUND: {src}")
            continue

        # Upgrade frontmatter first
        ok, msg = upgrade_frontmatter(src, liberal_art, page_type)
        if not ok:
            errors.append(f"FM FAIL: {src} ({msg})")
            continue

        # git mv to target
        dst_dir = os.path.join('docs', subfolder)
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, filename)

        result = subprocess.run(['git', 'mv', src, dst], capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"MV FAIL: {src} -> {dst}: {result.stderr.strip()}")
            continue
        moved += 1

    # Handle koo-project/ -> docs/records/koo_project/
    koo_src = os.path.join('docs', 'inaai', 'koo-project')
    koo_dst = os.path.join('docs', 'records', 'koo_project')
    if os.path.exists(koo_src):
        os.makedirs(os.path.join('docs', 'records'), exist_ok=True)
        result = subprocess.run(['git', 'mv', koo_src, koo_dst], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Moved koo-project/ -> docs/records/koo_project/")
        else:
            errors.append(f"KOO MV FAIL: {result.stderr.strip()}")

    # Handle source pages -> docs/sources/
    for sf in ['InaAI-highlights.md', 'InaAI.md', 'prof-ben-koo-speeches.md']:
        s = os.path.join('docs', 'inaai', sf)
        if os.path.exists(s):
            d = os.path.join('docs', 'sources', sf)
            os.makedirs(os.path.join('docs', 'sources'), exist_ok=True)
            subprocess.run(['git', 'mv', s, d], capture_output=True, text=True)
            print(f"Moved {sf} -> docs/sources/")

    # Clean up empty inaai dir
    inaai_dir = os.path.join('docs', 'inaai')
    if os.path.exists(inaai_dir):
        remaining = os.listdir(inaai_dir)
        if not remaining:
            os.rmdir(inaai_dir)
            print("Removed empty docs/inaai/")
        else:
            print(f"docs/inaai/ still has: {remaining}")

    print(f"\nMoved and upgraded: {moved} files")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    else:
        print("No errors!")

if __name__ == '__main__':
    main()
