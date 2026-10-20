#!/usr/bin/env python3
"""Render the Alopex DB catalog and crop manifest using only Pillow.

Run from any directory: python3 scripts/render_brand_book.py
Coordinates use half-open boxes: (x, y, x + w, y + h). No assets are exported.
"""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/assets/images/brand'
CANVAS = {'width': 2688, 'height': 7840}
P = {
    'deep': '#1E3A5F', 'blue-light': '#2E5077', 'blue-dark': '#152C4A',
    'ice': '#5FB4C9', 'aurora': '#7EC8E3', 'frost': '#B8D4E3',
    'silver': '#C0C5CE', 'silver-light': '#DFE1E8', 'night': '#0B1929',
    'panel': '#0F2137', 'snow': '#F8FAFC', 'text': '#E8EEF2',
}


def tile(name, x, y, w, h, purpose, sizes, background='transparent'):
    return dict(name=name, x=x, y=y, w=w, h=h, background=background,
                purpose=purpose, export=[dict(path=f'{name}{suffix}.png', size=size)
                                         for suffix, size in sizes])


# This is the sole geometry source for both rendering and manifest generation.
# Square exports use integer size; rectangular exports use [width, height].
TILES = [
    tile('mark-dark', 64, 160, 512, 512, 'Engine icon for dark backgrounds',
         [('', 512), ('-256', 256), ('-64', 64), ('-32', 32), ('-16', 16)]),
    tile('mark-light', 640, 160, 512, 512, 'Engine icon for light backgrounds',
         [('', 512), ('-256', 256), ('-64', 64), ('-32', 32), ('-16', 16)]),
    tile('mark-mono', 1216, 160, 512, 512, 'Single-ink silhouette with transparent eye cuts',
         [('', 512), ('-64', 64), ('-32', 32), ('-16', 16)]),
    tile('lockup-horizontal-dark', 64, 768, 1536, 384, 'README picture source for dark backgrounds',
         [('', [1536, 384]), ('-800', [800, 200]), ('-400', [400, 100])]),
    tile('lockup-horizontal-light', 64, 1248, 1536, 384, 'README picture source for light backgrounds',
         [('', [1536, 384]), ('-800', [800, 200]), ('-400', [400, 100])]),
    tile('lockup-stacked-dark', 64, 1728, 1024, 768, 'Centered engine signature with tagline for dark backgrounds',
         [('', [1024, 768]), ('-512', [512, 384])]),
    tile('submark-skulk', 1216, 1728, 384, 384, 'Skulk: shared fox with time-series signal; light backgrounds',
         [('', 384), ('-192', 192), ('-96', 96)]),
    tile('submark-chirps', 1664, 1728, 384, 384, 'Chirps: shared fox with connected mesh; light backgrounds',
         [('', 384), ('-192', 192), ('-96', 96)]),
    tile('submark-trail', 1216, 2176, 384, 384, 'Trail: shared fox with ordered event tracks; in design; light backgrounds',
         [('', 384), ('-192', 192), ('-96', 96)]),
    tile('submark-dataui', 1664, 2176, 384, 384, 'Alopex Data UI: shared fox with interface panes; early dev; light backgrounds',
         [('', 384), ('-192', 192), ('-96', 96)]),
    tile('social-preview', 64, 2656, 2560, 1280, 'Full-bleed social card with safe inset copy',
         [('', [2560, 1280]), ('-1280', [1280, 640])], P['night']),
    tile('readme-banner', 64, 4032, 2560, 640, 'Full-bleed README hero with positioning statement',
         [('', [2560, 640]), ('-1280', [1280, 320])], P['night']),
    tile('palette-strip', 64, 4768, 1536, 256, 'All twelve approved palette colors with hex values',
         [('', [1536, 256])], P['snow']),
    tile('favicon-proof', 64, 5120, 512, 128, 'Proof only: native 16 / 32 / 48 / 64 px dark-ink marks; no export',
         []),
    tile('favicon-plate', 2112, 768, 512, 512, 'Opaque snow fox on deep blue for light and dark browser chrome',
         [('', 512), ('-180', 180), ('-48', 48), ('-32', 32), ('-16', 16)], P['deep']),
    tile('avatar-org', 2112, 1344, 512, 512, 'Opaque organization avatar; fox inside centered 85% circle',
         [('', 512), ('-256', 256), ('-96', 96)], P['deep']),
]

# Append the family collection without moving any approved tile.
for family, x in zip(('skulk', 'chirps', 'trail', 'dataui'), (64, 640, 1216, 1792)):
    TILES.append(tile(f'submark-{family}-dark', x, 5440, 384, 384,
                      f'{family}: shared fox and functional symbol for dark backgrounds',
                      [('', 384), ('-192', 192), ('-96', 96)]))
for family, mode, y in (('skulk', 'dark', 5920), ('skulk', 'light', 6400),
                        ('chirps', 'dark', 6880), ('chirps', 'light', 7360)):
    TILES.append(tile(f'lockup-{family}-{mode}', 64, y, 1536, 384,
                      f'Alopex {family.title()} README signature for {mode} backgrounds',
                      [('', [1536, 384]), ('-800', [800, 200]), ('-400', [400, 100])]))

FONT_CANDIDATES = {
    'brand': [('/System/Library/Fonts/Supplemental/Futura.ttc', 0),
              ('/System/Library/Fonts/HelveticaNeue.ttc', 1)],
    # SFNS includes the capability line's right-arrow glyph; Helvetica Neue does not.
    'body': [('/System/Library/Fonts/SFNS.ttf', 0),
             ('/System/Library/Fonts/Supplemental/Arial.ttf', 0)],
}
SELECTED_FONTS = {}


def font(size, role='body'):
    for path, index in FONT_CANDIDATES[role]:
        if Path(path).is_file():
            try:
                f = ImageFont.truetype(path, round(size), index=index)
                SELECTED_FONTS[role] = {'path': path, 'index': index}
                return f
            except OSError:
                pass
    SELECTED_FONTS[role] = {'path': 'Pillow default', 'index': 0}
    return ImageFont.load_default(size=round(size))


def text(im, xy, value, size, color, role='body', center=False):
    d = ImageDraw.Draw(im)
    f = font(size, role)
    box = d.textbbox((0, 0), value, font=f)
    x, y = xy
    if center:
        x -= (box[2] - box[0]) / 2
    d.text((x - box[0], y - box[1]), value, font=f, fill=color)


def fox(size, mode='light'):
    """One connected fox silhouette. Eye apertures remain empty in every mode."""
    s = 4
    im = Image.new('RGBA', (size * s, size * s))
    d = ImageDraw.Draw(im)
    def poly(points, fill):
        d.polygon([(round(x * size * s / 100), round(y * size * s / 100))
                   for x, y in points], fill=fill)
    ink = P['snow'] if mode == 'dark' else P['deep']
    poly([(14, 8), (38, 25), (62, 25), (86, 8), (90, 57),
          (72, 78), (50, 94), (28, 78), (10, 57)], ink)
    if mode != 'mono':
        poly([(38, 25), (62, 25), (50, 47)], P['ice'])
    for points in [[(20, 44), (43, 53), (37, 61), (23, 55)],
                   [(80, 44), (57, 53), (63, 61), (77, 55)]]:
        poly(points, (0, 0, 0, 0))
    return im.resize((size, size), Image.Resampling.LANCZOS)


def paste_fox(im, x, y, size, mode='dark'):
    im.alpha_composite(fox(size, mode), (x, y))


def render(t):
    w, h, name = t['w'], t['h'], t['name']
    # Supersample each tile independently: no artwork can leak into a neighbor.
    scale = 2
    im = Image.new('RGBA', (w * scale, h * scale),
                   (0, 0, 0, 0) if t['background'] == 'transparent' else t['background'])
    def label(x, y, value, size, color, role='body', center=False):
        text(im, (x * scale, y * scale), value, size * scale, color, role, center)
    def mark(x, y, size, mode='dark'):
        paste_fox(im, x * scale, y * scale, size * scale, mode)
    d = ImageDraw.Draw(im)
    def line(points, fill, width=8):
        d.line([(x * scale, y * scale) for x, y in points], fill=fill,
               width=width * scale, joint='curve')
    def rect(box, fill):
        d.rectangle(tuple(v * scale for v in box), fill=fill)

    if name.startswith('mark-'):
        mark(0, 0, 512, name.removeprefix('mark-'))
    elif name == 'favicon-plate':
        # Large silhouette: ~13px wide at 16px, with two broad eye apertures.
        # Alpha compositing fills the apertures with the opaque plate color.
        mark(0, -5, 512)
    elif name == 'avatar-org':
        # Center the actual silhouette, not its nominal square. The ear tips
        # stay within radius 217.6px even when GitHub applies a circular crop.
        mark(64, 60, 384)
    elif name.startswith(('lockup-skulk-', 'lockup-chirps-')):
        _, family, mode = name.split('-')
        sibling_name = f'submark-{family}' + ('-dark' if mode == 'dark' else '')
        sibling = render(dict(name=sibling_name, w=384, h=384, background='transparent'))
        im.alpha_composite(sibling.resize((328*scale, 328*scale), Image.Resampling.LANCZOS),
                           (24*scale, 28*scale))
        label(408, 124, f'Alopex {family.title()}', 144,
              P['snow'] if mode == 'dark' else P['deep'], 'brand')
    elif name.startswith('lockup-horizontal'):
        mode = name.rsplit('-', 1)[1]
        mark(24, 28, 328, mode)
        label(408, 124, 'Alopex DB', 144, P['snow'] if mode == 'dark' else P['deep'], 'brand')
    elif name == 'lockup-stacked-dark':
        mark(302, 26, 420)
        label(512, 495, 'Alopex DB', 114, P['snow'], 'brand', True)
        label(512, 650, 'Silent. Adaptive. Unbreakable.', 38, P['frost'], center=True)
    elif name.startswith('submark-'):
        dark = name.endswith('-dark')
        family = name.split('-')[1]
        mark(58, 0, 268, 'dark' if dark else 'light')
        ink, accent = P['snow'] if dark else P['deep'], P['ice']
        if family == 'skulk':
            line([(96, 334), (128, 334), (152, 290), (184, 350),
                  (216, 306), (240, 322), (288, 322)], ink, 12)
        elif family == 'chirps':
            nodes = [(112, 332), (192, 286), (272, 332)]
            line([nodes[0], nodes[1], nodes[2], nodes[0]], ink, 10)
            for x, y in nodes:
                d.ellipse(((x-14)*scale, (y-14)*scale, (x+14)*scale, (y+14)*scale), fill=accent)
        elif family == 'trail':
            for y, end in [(290, 282), (318, 238), (346, 260)]:
                rect((104, y, 116, y+12), accent)
                rect((138, y, end, y+12), ink)
        else:
            rect((100, 284, 284, 356), ink)
            rect((112, 296, 144, 344), accent)
            rect((156, 296, 272, 312), P['deep'] if dark else P['snow'])
            rect((156, 324, 200, 344), P['frost'])
            rect((212, 324, 272, 344), P['ice'])
    elif name in ('social-preview', 'readme-banner'):
        # Abstract ice shelf facets use only approved flat palette fills.
        d.polygon([(2080*scale, 0), (w*scale, 0), (w*scale, h*scale),
                   (1800*scale, h*scale)], fill=P['panel'])
        line([(2310, 0), (1950, h)], P['blue-dark'], 3)
        if name == 'social-preview':
            mark(160, 238, 600)
            label(890, 330, 'Alopex DB', 170, P['snow'], 'brand')
            label(898, 570, 'Silent. Adaptive. Unbreakable.', 58, P['aurora'])
            rect((900, 706, 1044, 714), P['ice'])
            label(220, 978, 'SQL + Vector (HNSW) + Columnar · embedded → distributed · Rust', 48, P['text'])
        else:
            mark(140, 90, 420)
            label(660, 146, 'Alopex DB', 130, P['snow'], 'brand')
            label(668, 330, 'Silent. Adaptive. Unbreakable.', 46, P['aurora'])
            label(668, 430, 'One Rust engine. Native SQL, vector search (HNSW), and columnar storage.', 32, P['text'])
            label(668, 484, 'From a single embedded file to a distributed cluster.', 32, P['frost'])
    elif name == 'palette-strip':
        for i, (key, color) in enumerate(P.items()):
            x = i * 128
            rect((x, 0, x+127, 172), color)
            label(x+10, 190, color.upper(), 19, P['deep'])
            label(x+10, 224, key, 16, P['deep'])
    elif name == 'favicon-proof':
        # Actual final-size rasterization, then nearest-neighbor placement.
        # Do not render a large fox and scale the whole proof down afterward.
        proof = Image.new('RGBA', (w, h))
        for cx, size in zip((64, 192, 320, 448), (16, 32, 48, 64)):
            proof.alpha_composite(fox(size), (cx-size//2, (h-size)//2))
        return proof
    else:
        raise ValueError(name)
    return im.resize((w, h), Image.Resampling.LANCZOS)


def validate_geometry():
    for i, a in enumerate(TILES):
        assert a['x'] >= 0 and a['y'] >= 0
        assert a['x'] + a['w'] <= CANVAS['width']
        assert a['y'] + a['h'] <= CANVAS['height']
        for b in TILES[i+1:]:
            gap_x = max(b['x']-a['x']-a['w'], a['x']-b['x']-b['w'])
            gap_y = max(b['y']-a['y']-a['h'], a['y']-b['y']-b['h'])
            assert max(gap_x, gap_y) >= 48, (a['name'], b['name'])


def main():
    validate_geometry()
    OUT.mkdir(parents=True, exist_ok=True)
    book = Image.new('RGBA', (CANVAS['width'], CANVAS['height']), P['snow'])
    text(book, (64, 30), 'ALOPEX DB / ARCTIC IDENTITY', 38, P['deep'], 'brand')
    text(book, (1760, 42), '01   SINGLE FOX / FLAT COLOR / OPEN SOURCE', 21, P['deep'])
    for t in TILES:
        name, x, y = t['name'], t['x'], t['y']
        # A caption ends above its tile; a simple paste replaces alpha exactly.
        text(book, (x, y-40), f"{name}   /   {t['w']} × {t['h']}", 22, P['deep'])
        artwork = render(t)
        book.paste(artwork, (x, y))
        if t['background'] == 'transparent':
            assert artwork.getpixel((0, 0))[3] == 0
    text(book, (1840, 210), 'ONE FOX. ONE ENGINE.', 31, P['deep'], 'brand')
    text(book, (1840, 282), 'Parent + child reduced to one silhouette.', 24, P['deep'])
    text(book, (1840, 330), 'Family identity lives in sibling submarks.', 24, P['deep'])
    text(book, (1840, 378), 'Transparent eye cuts survive one ink.', 24, P['deep'])
    text(book, (1840, 466), 'Dark variants use snow + ice.', 24, P['deep'])
    text(book, (1840, 514), 'Light variants use deep blue + ice.', 24, P['deep'])
    text(book, (1840, 562), 'Empty tile areas are alpha 0.', 24, P['deep'])
    for cx, size in zip((128, 256, 384, 512), (16, 32, 48, 64)):
        text(book, (cx, 5268), f'{size}px', 18, P['deep'], center=True)
    book.save(OUT / 'design-book.png')
    manifest = {
        'canvas': CANVAS, 'bbox_convention': 'half-open: [x, y, x+w, y+h]',
        'design_decisions': [
            'Use one fox instead of parent + child to retain a clear small-size silhouette.',
            'Use flat approved fills and transparent eye apertures; mono is one ink.',
            'Canvas widened to 2688px to contain native 2560px tiles with 64px margins.',
            'Submarks share the fox silhouette and functional symbols; light uses deep blue, dark uses snow with ice accents.',
            'Skulk and Chirps README lockups reuse the corresponding submarks and the engine wordmark typeface treatment.',
            'Favicon proof contains actual 16/32/48/64px rasterizations; labels are outside its bbox.',
            'Transparent dark variants must be previewed on a dark background; no matte is baked in.',
            'Favicon and avatar plates use deep blue #1E3A5F: snow contrast and a visible plate against both light and dark chrome.',
            'Avatar fox is optically centered and contained inside a centered 85%-diameter circle; plate bleeds to all corners.',
        ],
        'palette': P, 'fonts': SELECTED_FONTS,
        'export_size_convention': 'integer = square edge; [width, height] = rectangle; empty export = proof only',
        'tiles': TILES,
    }
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    with Image.open(OUT / 'design-book.png') as check:
        assert check.mode == 'RGBA'
        assert check.size == (CANVAS['width'], CANVAS['height'])
        for t in manifest['tiles']:
            x, y, w, h = (t[k] for k in ('x', 'y', 'w', 'h'))
            assert 0 <= x < x+w <= check.width
            assert 0 <= y < y+h <= check.height
            alpha = check.crop((x, y, x+w, y+h)).getchannel('A')
            if t['background'] == 'transparent':
                assert all(alpha.getpixel(p) == 0 for p in
                           ((0, 0), (w-1, 0), (0, h-1), (w-1, h-1))), t['name']
            else:
                assert alpha.getextrema() == (255, 255), t['name']
    print(f"Rendered {len(TILES)} tiles: {CANVAS['width']} × {CANVAS['height']} RGBA")


if __name__ == '__main__':
    main()
