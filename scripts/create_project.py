#!/usr/bin/env python3
"""Initialize files for a new computational paper review deck."""

from __future__ import annotations

import shutil
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    papers = root / "papers"
    assets = root / "assets"
    content_template = root / "CONTENT_TEMPLATE.md"
    content = root / "CONTENT.md"

    papers.mkdir(exist_ok=True)
    assets.mkdir(exist_ok=True)

    if not content.exists():
        shutil.copyfile(content_template, content)
        print("created CONTENT.md from CONTENT_TEMPLATE.md")
    else:
        print("CONTENT.md already exists; leaving it unchanged")

    print()
    print("Next steps:")
    print("1. Put the paper PDF in papers/")
    print("2. Run: python scripts/extract_figures.py papers/example.pdf --out assets")
    print("3. Fill CONTENT.md")
    print("4. Paste PROMPT_TEMPLATE.md into Codex")
    print("5. Open index.html locally")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
