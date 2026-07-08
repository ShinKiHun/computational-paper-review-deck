#!/usr/bin/env python3
"""Extract embedded bitmap images from a PDF into an assets directory."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract embedded PDF images into assets/ without OCR or internet access."
    )
    parser.add_argument("pdf", type=Path, help="Path to the paper PDF.")
    parser.add_argument("--out", type=Path, default=Path("assets"), help="Output directory.")
    parser.add_argument("--min-width", type=int, default=120, help="Skip images narrower than this.")
    parser.add_argument("--min-height", type=int, default=120, help="Skip images shorter than this.")
    parser.add_argument("--min-area", type=int, default=20000, help="Skip images with fewer pixels.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("ERROR: PyMuPDF is required. Install it with: pip install pymupdf", file=sys.stderr)
        return 1

    if not args.pdf.exists():
        print(f"ERROR: PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)

    try:
        doc = fitz.open(args.pdf)
    except Exception as exc:
        print(f"ERROR: Could not open PDF: {exc}", file=sys.stderr)
        return 1

    saved = 0
    skipped = 0
    seen_xrefs: set[int] = set()

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        image_number = 0
        for image in images:
            xref = image[0]
            width = image[2]
            height = image[3]

            if xref in seen_xrefs:
                skipped += 1
                continue

            if width < args.min_width or height < args.min_height or width * height < args.min_area:
                skipped += 1
                continue

            try:
                extracted = doc.extract_image(xref)
            except Exception:
                skipped += 1
                continue

            ext = extracted.get("ext", "png")
            data = extracted.get("image")
            if not data:
                skipped += 1
                continue

            seen_xrefs.add(xref)
            image_number += 1
            output_name = f"fig_p{page_index + 1:02d}_{image_number:02d}.{ext}"
            output_path = args.out / output_name
            output_path.write_bytes(data)
            saved += 1
            print(f"saved {output_path} ({width}x{height})")

    doc.close()
    print(f"done: saved {saved} image(s), skipped {skipped} image(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
