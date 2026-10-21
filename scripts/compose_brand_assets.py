#!/usr/bin/env python3
"""Rebuild all 74 legacy paths from the unchanged approved master artwork."""
import json
from pathlib import Path

from PIL import Image
import render_brand_book
import export_brand_assets

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'docs/assets/images/brand'


def main():
    master = (ROOT / 'assets/brand/character/mark-head-flat.png').read_bytes()
    for name in ('mark-face.png', 'mark-face-small.png'):
        assert (ROOT / 'assets/brand/mark-source' / name).read_bytes() == master, (
            name, 'Source must be a verbatim copy of the approved master; rebuild stopped')
    sizes = json.loads((ROOT / 'assets/brand/mark-source/shipped-sizes.json').read_text())
    render_brand_book.main()
    assert export_brand_assets.main() == 0
    actual = {p.name: list(Image.open(p).size) for p in BRAND.glob('*.png')}
    assert actual == sizes, {'missing': sizes.keys() - actual.keys(),
                             'unexpected': actual.keys() - sizes.keys(),
                             'resized': [k for k in sizes.keys() & actual.keys() if sizes[k] != actual[k]]}
    print(f'Verified all {len(sizes)} original PNG paths and exact dimensions.')


if __name__ == '__main__':
    main()
