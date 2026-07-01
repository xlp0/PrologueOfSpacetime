#!/usr/bin/env python3
"""Add YAML frontmatter + wikilinks to teaching files."""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

# Liberal art mapping per chapter number
LIBERAL_ARTS = {
    1: 'Trivium-Rhetoric',
    2: 'Trivium-Logic',
    3: 'Quadrivium-Geometry',
    4: 'Quadrivium-Arithmetic',
    5: 'Trivium-Rhetoric',
    6: 'Trivium-Grammar',
    7: 'Trivium-Grammar',
    8: 'Trivium-Grammar',
    9: 'Quadrivium-Music',
    10: 'Trivium-Rhetoric',
    11: 'Trivium-Logic',
    12: 'Trivium-Grammar',
    13: 'Trivium-Rhetoric',
    14: 'Quadrivium-Geometry',
}

# Wikilink mappings: (plain text pattern, wikilink replacement)
# Only first occurrence will be converted
WIKILINKS = [
    (r'\bRepresentation Engine\b', '[[The_Representation_Engine|Representation Engine]]'),
    (r'\bModel Context Protocol\b', '[[mcp-anthropic-standard|Model Context Protocol]]'),
    (r'(?<!\w)MCP\b', '[[mcp-anthropic-standard|MCP]]'),
    (r'(?<!\[)context engineering\b', '[[static-vs-dynamic-context|context engineering]]'),
    (r'(?<!\[)prompt injection\b', '[[prompt-injection-anatomy|prompt injection]]'),
    (r'(?<!\w)Trivium\b', '[[Trivium]]'),
    (r'(?<!\w)Quadrivium\b', '[[Quadrivium]]'),
    (r'ABC Curriculum', '[[abc_curriculum|ABC Curriculum]]'),
    (r'local-first', '[[Local-First|local-first]]'),
    (r'SpacetimeDB', '[[SpacetimeDB_Overview|SpacetimeDB]]'),
    (r'second brain', '[[karpathy-llm-wiki-vs-rag|second brain]]'),
    (r'flow state', '[[Flow in PKC - Faster Interactive Learning|Flow State]]'),
    (r'Dungeon Master', '[[DM_as_Maxwells_Demon|Dungeon Master]]'),
]

def extract_title(content):
    m = re.match(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else 'Untitled'

def extract_chapter_num(filename):
    m = re.match(r'(\d+)', filename)
    return int(m.group(1)) if m else 0

def add_frontmatter(filepath, course, audience):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        return False  # already has frontmatter

    title = extract_title(content)
    chapter = extract_chapter_num(os.path.basename(filepath))
    la = LIBERAL_ARTS.get(chapter, 'Trivium-Grammar')
    tag = la

    fm = f"""---
title: '{title}'
date: 2026-06-25
tags: [Teaching, {course.replace(" ", "-")}, Seven-Liberal-Arts, {tag}]
type: note
sources: []
status: stable
course: {course}
chapter: {chapter}
liberal_art: {la}
audience: {audience}
---

"""
    # Add wikilinks (first occurrence only)
    for pattern, replacement in WIKILINKS:
        content = re.sub(pattern, replacement, content, count=1, flags=re.IGNORECASE if pattern.startswith('(?i') else 0)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fm + content)
    return True

def main():
    # ai_coding_guide/ (professional audience)
    guide_dir = 'docs/teaching/ai_coding_guide'
    count = 0
    for fn in sorted(os.listdir(guide_dir)):
        if fn.endswith('.md'):
            fp = os.path.join(guide_dir, fn)
            if add_frontmatter(fp, 'AI Coding Guide', 'professional'):
                count += 1
                print(f'  upgraded: {fp}')
    print(f'ai_coding_guide: {count} files upgraded')

    # handbook/ (beginner audience)
    handbook_dir = 'docs/teaching/handbook'
    count = 0
    for fn in sorted(os.listdir(handbook_dir)):
        if fn.endswith('.md'):
            fp = os.path.join(handbook_dir, fn)
            if add_frontmatter(fp, 'AI Coding Handbook', 'beginner'):
                count += 1
                print(f'  upgraded: {fp}')
    print(f'handbook: {count} files upgraded')

if __name__ == '__main__':
    main()
