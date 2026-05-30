#!/usr/bin/env python3
"""
generate-blog-index.py
Scans docs/issue-blog/ for all blog post .md files
and auto-generates the index table in docs/issue-blog/README.md
"""

import os
import re
from pathlib import Path
from datetime import datetime

BLOG_DIR = Path(__file__).parent.parent / "docs" / "issue-blog"
README_PATH = BLOG_DIR / "README.md"

def parse_front_matter(filepath):
    """Extract metadata from the blog post header block."""
    meta = {
        "title": filepath.stem,
        "date": "Unknown",
        "severity": "—",
        "component": "—",
        "author": "—",
        "issue_id": "—",
        "tags": "",
    }
    try:
        content = filepath.read_text(encoding="utf-8")
        # Extract title from H1
        title_match = re.search(r'^# 📖 Issue Blog: (.+)$', content, re.MULTILINE)
        if title_match:
            meta["title"] = title_match.group(1).strip()

        # Extract metadata lines
        patterns = {
            "issue_id": r'\*\*Issue ID:\*\* #(\d+)',
            "date": r'\*\*Date Resolved:\*\* ([\d-]+)',
            "severity": r'\*\*Severity:\*\* (\w+)',
            "component": r'\*\*Component:\*\* (.+)',
            "author": r'\*\*Author:\*\* @([\w-]+)',
            "tags": r'\*\*Tags:\*\* (.+)',
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                meta[key] = match.group(1).strip()
    except Exception as e:
        print(f"Warning: Could not parse {filepath.name}: {e}")
    return meta


def generate_index():
    blog_files = sorted(
        [f for f in BLOG_DIR.glob("*.md") if f.name not in ("README.md", "TEMPLATE.md")],
        reverse=True
    )

    if not blog_files:
        index_content = "*No blog posts yet. Be the first to document a resolved issue!*"
    else:
        rows = []
        rows.append("| Date | Issue | Title | Severity | Component | Author |")
        rows.append("|------|-------|-------|----------|-----------|--------|")
        for f in blog_files:
            meta = parse_front_matter(f)
            link = f"./{f.name}"
            issue_link = f"#{meta['issue_id']}" if meta['issue_id'] != '—' else '—'
            rows.append(
                f"| {meta['date']} | {issue_link} | [{meta['title']}]({link}) | "
                f"{meta['severity']} | {meta['component']} | @{meta['author']} |"
            )
        index_content = "\n".join(rows)

    # Update README between markers
    readme = README_PATH.read_text(encoding="utf-8")
    new_readme = re.sub(
        r'<!-- INDEX_START -->.*?<!-- INDEX_END -->',
        f'<!-- INDEX_START -->\n{index_content}\n<!-- INDEX_END -->',
        readme,
        flags=re.DOTALL
    )
    README_PATH.write_text(new_readme, encoding="utf-8")
    print(f"✅ Blog index updated with {len(blog_files)} post(s).")


if __name__ == "__main__":
    generate_index()
