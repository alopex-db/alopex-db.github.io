"""Compose only the approved master artwork; never recolor or reshape a face."""
from functools import lru_cache
from pathlib import Path
import numpy as np
from PIL import Image

SOURCE = Path(__file__).resolve().parents[1] / 'assets/brand/mark-source'


@lru_cache(maxsize=2)
def source_face(mode='dark', small=False):
    if mode not in ('dark', 'light', 'mono'):
        raise ValueError(mode)
    # Legacy suffixes are path compatibility, not permission to change pixels.
    return Image.open(SOURCE / ('mark-face-small.png' if small else 'mark-face.png')).convert('RGBA')


def fox(size, mode='dark', small=None):
    if small is None:
        small = size <= 32
    return source_face(mode, small).resize((size, size), Image.Resampling.LANCZOS)


def centered_plate(face, size, avatar=False):
    a = np.asarray(face.getchannel('A'))
    # Alpha is used only to measure framing. It is never changed or thresholded
    # in the artwork: even the master's faint edge pixels are composited intact.
    ys, xs = np.nonzero(a > (0 if avatar else 127))
    cx, cy = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
    if avatar:
        radius = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2).max()
        scale = (size * .425 - 2) / radius
    else:
        scale = size / face.width
    artwork = face if scale == 1 else face.resize(
        (round(face.width * scale), round(face.height * scale)), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (size, size), '#0B1929')
    canvas.alpha_composite(artwork, (round(size/2 - cx*scale), round(size/2 - cy*scale)))
    return canvas


def plate(size, small=None, avatar=False):
    if small is None:
        small = size <= 32
    if avatar or small:
        return centered_plate(source_face(small=small), size, avatar)
    return Image.open(SOURCE / 'mark-plate.png').convert('RGBA').resize(
        (size, size), Image.Resampling.LANCZOS)
