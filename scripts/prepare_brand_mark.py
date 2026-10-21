#!/usr/bin/env python3
"""Copy the sole approved master verbatim and composite its opaque plate.

No quantization, drawing, feature masks, recoloring or retouching is permitted.
"""
from pathlib import Path
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / 'assets/brand/character/mark-head-flat.png'
SOURCE = ROOT / 'assets/brand/mark-source'


def main():
    SOURCE.mkdir(parents=True, exist_ok=True)
    im = Image.open(MASTER)
    assert im.mode == 'RGBA', 'Master must already have transparency; do not invent a cutout'
    for name in ('mark-face.png', 'mark-face-small.png'):
        shutil.copyfile(MASTER, SOURCE / name)
    from brand_mark import centered_plate
    centered_plate(im, im.width).convert('RGB').save(SOURCE / 'mark-plate.png', optimize=True)
    # Remove obsolete candidate-A evidence, not the original candidate records.
    for name in ('eye-highlight-proof.png', 'eye-highlight-verification.json'):
        (SOURCE / name).unlink(missing_ok=True)
    print('Copied approved master verbatim to both face sources; composited night plate.')


if __name__ == '__main__':
    main()
