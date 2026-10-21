#!/usr/bin/env python3
"""Verify untouched master pixels and the 74-file shipping compatibility contract."""
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageChops
from brand_mark import fox, plate, centered_plate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'assets/brand/mark-source'
MASTER = ROOT / 'assets/brand/character/mark-head-flat.png'
BRAND = ROOT / 'docs/assets/images/brand'
EYES = {'left': (325, 700, 530, 890), 'right': (720, 700, 930, 890)}


def main():
    master = Image.open(MASTER)
    expected = json.loads((SOURCE / 'shipped-sizes.json').read_text())
    actual = {p.name: list(Image.open(p).size) for p in BRAND.glob('*.png')}
    assert len(expected) == 74 and actual == expected, 'Shipping filename/dimension contract changed'
    assert {p.name for p in SOURCE.glob('*.png')} == {
        'mark-face.png', 'mark-face-small.png', 'mark-plate.png'}, 'Obsolete source PNG present'
    for name in ('mark-face.png', 'mark-face-small.png'):
        p = SOURCE / name
        assert p.read_bytes() == MASTER.read_bytes(), (name, 'not a verbatim master copy')
        im = Image.open(p)
        assert im.mode == master.mode and im.size == master.size
        assert im.tobytes() == master.tobytes(), (name, 'full-face pixel mismatch')
        for side, box in EYES.items():
            assert im.crop(box).tobytes() == master.crop(box).tobytes(), (name, side)
    source_plate = Image.open(SOURCE / 'mark-plate.png')
    assert source_plate.mode == 'RGB'
    assert source_plate.tobytes() == centered_plate(master, master.width).convert('RGB').tobytes()
    for corner in [(0,0),(0,master.height-1),(master.width-1,0),(master.width-1,master.height-1)]:
        assert source_plate.getpixel(corner) == (11,25,41)
    for size in (16,32):
        for mode in ('dark','light','mono'):
            im = Image.open(BRAND / f'mark-{mode}-{size}.png')
            assert im.tobytes() == fox(size, mode, small=True).tobytes()
        im = Image.open(BRAND / f'favicon-plate-{size}.png').convert('RGB')
        assert im.tobytes() == plate(size, small=True).convert('RGB').tobytes()
    for suffix in ('','-16','-32','-64'):
        for mode in ('light','mono'):
            assert Image.open(BRAND / f'mark-{mode}{suffix}.png').tobytes() == Image.open(
                BRAND / f'mark-dark{suffix}.png').tobytes(), 'Legacy suffix changed master artwork'
    for p in BRAND.glob('avatar-org*.png'):
        im = Image.open(p).convert('RGB')
        a = np.asarray(im).astype(int)
        visible = np.abs(a - (11,25,41)).max(axis=-1) > 12
        ys,xs = np.nonzero(visible)
        radius = np.sqrt((xs-im.width/2)**2 + (ys-im.width/2)**2).max()
        assert radius <= im.width*.425+1.5, (p.name,radius)
    for original,alias in [('favicon-plate-48.png','favicon.png'),('favicon-plate-180.png','apple-touch-icon.png')]:
        assert (BRAND/original).read_bytes() == (BRAND/alias).read_bytes()
    manifest = json.loads((BRAND/'manifest.json').read_text())
    book = Image.open(BRAND/'design-book.png')
    tile = next(t for t in manifest['tiles'] if t['name']=='mark-dark')
    x,y,w,h = (tile[k] for k in ('x','y','w','h'))
    assert book.crop((x,y,x+w,y+h)).tobytes() == Image.open(BRAND/'mark-dark.png').tobytes()
    print('PASS: master/source file bytes, full-face pixels and both eye crops identical; '
          'unaltered small source; composited plate; all 74 original paths/dimensions; '
          'no legacy recoloring; avatar crop; aliases; current catalogue.')


if __name__ == '__main__':
    main()
