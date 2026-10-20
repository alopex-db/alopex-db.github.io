#!/usr/bin/env python3
"""Crop the shipped brand assets out of the design book.

`scripts/render_brand_book.py` draws one large catalog image
(`docs/assets/images/brand/design-book.png`) plus `manifest.json`, which records
the exact pixel box of every tile and the sizes it ships at. This script is the
second half of that pipeline: it slices the catalog into the individual files
that the README, the org profile, and the MkDocs theme reference.

Run after any change to the design book:

    python3 scripts/render_brand_book.py
    python3 scripts/export_brand_assets.py

Tiles whose manifest `export` list is empty (proof sheets) are skipped.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs" / "assets" / "images" / "brand"
BOOK = BRAND / "design-book.png"
MANIFEST = BRAND / "manifest.json"

# Assets that are copies of a tile export under the name other files reference.
ALIASES = {
    "favicon-plate-48.png": "favicon.png",
    "favicon-plate-180.png": "apple-touch-icon.png",
}


def target_size(size) -> tuple[int, int]:
    """Manifest convention: an integer is a square edge, a pair is (w, h)."""
    if isinstance(size, (list, tuple)):
        width, height = size
        return int(width), int(height)
    return int(size), int(size)


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    book = Image.open(BOOK)
    book.load()

    canvas = manifest["canvas"]
    if book.size != (canvas["width"], canvas["height"]):
        raise SystemExit(
            f"design-book.png is {book.size}, manifest claims "
            f"{(canvas['width'], canvas['height'])} — re-run render_brand_book.py"
        )

    written: list[str] = []
    for tile in manifest["tiles"]:
        exports = tile.get("export") or []
        if not exports:
            continue

        x, y, w, h = (tile[k] for k in ("x", "y", "w", "h"))
        if x < 0 or y < 0 or x + w > book.width or y + h > book.height:
            raise SystemExit(f"tile {tile['name']} falls outside the canvas")

        crop = book.crop((x, y, x + w, y + h))
        opaque = tile.get("background", "transparent") != "transparent"

        for export in exports:
            size = target_size(export["size"])
            out = crop if size == crop.size else crop.resize(size, Image.LANCZOS)
            if opaque:
                out = out.convert("RGB")
            path = BRAND / export["path"]
            out.save(path, optimize=True)
            written.append(export["path"])

            alias = ALIASES.get(export["path"])
            if alias:
                out.save(BRAND / alias, optimize=True)
                written.append(alias)

    print(f"Exported {len(written)} files to {BRAND.relative_to(ROOT)}:")
    for name in written:
        print(f"  {name}")
    missing = [a for a in ALIASES.values() if not (BRAND / a).exists()]
    if missing:
        print(
            "\nNote: no tile produced " + ", ".join(missing) +
            " — add the source tile to the design book.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
