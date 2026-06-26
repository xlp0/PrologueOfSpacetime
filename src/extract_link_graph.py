#!/usr/bin/env python3
"""Extract the wikilink graph from all wiki markdown files."""
import os
import re
import json
from collections import defaultdict

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]|]*)?\]\]')

# Collect all wiki md files (exclude raw/, venv/, .agents/, .obsidian/, mcard_studio/Public, Fleeting)
EXCLUDE_DIRS = {'venv', '.agents', '.agent', '.obsidian', 'node_modules', 'raw'}
EXCLUDE_SUBSTRINGS = ['mcard_studio/Public', 'docs/Fleeting']

def should_exclude(path):
    parts = path.split(os.sep)
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if any(s in path for s in EXCLUDE_SUBSTRINGS):
        return True
    return False

def collect_md_files(root):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith('.md'):
                full = os.path.join(dirpath, fn)
                if not should_exclude(full):
                    files.append(full)
    return sorted(files)

def extract_links(content):
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(content)]

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_files = collect_md_files(root)

    # Build a lookup: basename (no .md) -> set of full paths (for resolving targets)
    basename_to_paths = defaultdict(set)
    for f in md_files:
        base = os.path.splitext(os.path.basename(f))[0]
        basename_to_paths[base].add(f)

    # Also index by relative path (for path-based targets like Hub/.../Directionality)
    # We'll resolve by basename primarily.

    out_links = {}  # file -> [target basenames]
    in_links = defaultdict(set)  # target basename -> set of source files

    dangling = defaultdict(set)  # target basename -> set of source files (no target page exists)

    for f in md_files:
        rel = os.path.relpath(f, root)
        try:
            with open(f, encoding='utf-8') as fh:
                content = fh.read()
        except Exception:
            content = ''
        links = extract_links(content)
        seen = set()
        for target in links:
            # Normalize: take the last path segment as the basename target
            target_base = target.split('/')[-1].strip()
            if not target_base:
                continue
            if target_base in seen:
                continue
            seen.add(target_base)
            out_links.setdefault(rel, []).append(target_base)
            in_links[target_base].add(rel)
            if target_base not in basename_to_paths:
                dangling[target_base].add(rel)

    # Compute stats
    # Hubs: most inbound links
    hub_list = sorted(in_links.items(), key=lambda x: -len(x[1]))
    # Out-degree
    out_degree = sorted(out_links.items(), key=lambda x: -len(x[1]))

    # Orphans: files with no inbound and no outbound links
    file_basenames = {os.path.splitext(os.path.basename(f))[0] for f in md_files}
    orphans = []
    for f in md_files:
        rel = os.path.relpath(f, root)
        base = os.path.splitext(os.path.basename(f))[0]
        has_in = base in in_links and len(in_links[base]) > 0
        has_out = rel in out_links and len(out_links[rel]) > 0
        if not has_in and not has_out:
            orphans.append(rel)

    # Dangling targets sorted by mention count
    dangling_sorted = sorted(dangling.items(), key=lambda x: -len(x[1]))

    result = {
        'total_files': len(md_files),
        'total_out_links': sum(len(v) for v in out_links.values()),
        'unique_targets': len(in_links),
        'dangling_targets': len(dangling),
        'hubs_inbound': [(t, len(sources), sorted(sources)[:5]) for t, sources in hub_list[:25]],
        'top_out_degree': [(f, len(tgts)) for f, tgts in out_degree[:20]],
        'orphans': orphans,
        'dangling_top': [(t, len(sources)) for t, sources in dangling_sorted[:30]],
    }

    # Save full graph as JSON for deeper analysis
    full_graph = {
        'files': sorted(os.path.relpath(f, root) for f in md_files),
        'out_links': {k: sorted(v) for k, v in out_links.items()},
        'in_links': {k: sorted(v) for k, v in in_links.items()},
        'dangling': {k: sorted(v) for k, v in dangling.items()},
    }
    with open('/tmp/wiki_graph.json', 'w') as fh:
        json.dump(full_graph, fh, indent=2)

    print(json.dumps(result, indent=2))
    print(f"\nFull graph written to /tmp/wiki_graph.json")

if __name__ == '__main__':
    main()
