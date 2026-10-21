# Alopex DB brand assets

The sole approved mark master is
`assets/brand/character/mark-head-flat.png`, from the calm character set.
Candidate A and the other plate experiments are historical alternatives, not
production sources. The retired geometric face is also no longer used.
**Never hand-edit a shipped PNG or redraw, flatten, recolor or reshape the face.**

## Two registers, one fox

| Surface | Identity to use |
|:--|:--|
| GitHub repositories, organization profiles and the documentation site | The mark in this directory; the calm-tone character in `assets/brand/character/` for figures and illustrations. |
| asopi.tech, video, social and merchandise | The glossy cute character maintained in the **asopitech-labs** organization, not this repository's shipping kit. |

Both characters are the same arctic fox in different registers. Local exploration
folders remain historical work. GitHub social-preview cards here use the mark.

## Sources and rebuilding

`assets/brand/mark-source/` contains:

- `mark-face.png`: a **byte-for-byte copy** of the approved transparent master.
- `mark-face-small.png`: another byte-for-byte copy of that same master. There
  are no simplified eyes, enlarged glints, trimmed cheeks or other retouches.
- `mark-plate.png`: that artwork centered on an opaque night `#0B1929` plate.
  Framing is measured from alpha; the artwork's alpha is not cleaned or changed.
- `shipped-sizes.json`: the 74 original filenames and measured pixel dimensions.

From the repository root:

```bash
python3 -m pip install -r requirements-brand.txt
python3 scripts/prepare_brand_mark.py
python3 scripts/compose_brand_assets.py
python3 scripts/verify_brand_assets.py
```

The preparation command copies the master and composites the plate. The old
normalization script has been removed: there is no palette classification,
feature drawing, morphological simplification or eye-highlight reconstruction.
The compositor scales and places the sources in the established layouts,
preserving typography, copy and project symbols. It rebuilds the catalogue,
manifest and all 74 PNG paths at their original dimensions.

Verification checks file-byte and full-image pixel identity for both transparent
sources, plus separate left/right eye crops against the master. It also checks
the plate composition, legacy export paths and sizes, small exports, avatar
framing, aliases and the current catalogue. Never replace these identity checks
with a subjective similarity assessment.

## Legacy filenames and limitations

The existing filenames remain for compatibility with live pages and open pull
requests. **The `dark`, `light` and `mono` face exports now use the same original
artwork and original colours.** The suffixes do not authorize recoloring it.
Consequently, `mark-mono*.png` is **not a single-ink asset**, and the white face
has limited contrast on light backgrounds. A genuine monochrome adaptation or
new light-background face treatment needs separate approval; do not invent one.

| Use | Existing file |
|:--|:--|
| Transparent mark, best on dark backgrounds | `mark-dark.png` and its size variants |
| Legacy light/mono references, same unchanged artwork | `mark-light*.png`, `mark-mono*.png` |
| Browser tab with a visible opaque plate | `favicon.png`, `favicon-plate-16.png`, `favicon-plate-32.png` |
| iOS home screen | `apple-touch-icon.png` |
| Organization avatar | `avatar-org.png` and its size variants |
| README lockups | `lockup-horizontal-{light,dark}*`, `lockup-stacked-dark*` |
| Sibling project lockups | `lockup-{skulk,chirps}-{light,dark}*` |
| Family figures | `submark-{skulk,chirps,trail,dataui}*` |
| GitHub social preview | `social-preview.png`, `social-preview-1280.png` |
| README banner | `readme-banner.png`, `readme-banner-1280.png` |

Plates bleed night to every edge. Avatar artwork fits within a centered circle
about 85% of the square edge for round GitHub crops. Small-size exports use
LANCZOS scaling of the same original artwork. At 16 px the subtle eye glints and
fur detail may disappear; accept that limitation rather than changing features.
A plate supplies contrast against uncontrolled light or dark browser chrome.

The functional symbols retain their existing meanings: Skulk a time-series
signal, Chirps a connected mesh, Trail ordered event tracks, Data UI interface
panes. Their shapes, colours, typography and layout remain as before; only the
fox artwork has been replaced.

## Palette and history

![Alopex DB palette](palette-strip.png)

The palette strip and surrounding kit retain their established colours.
The master retains **all original pixel colours and antialiasing**, including its
subtle eye glints. Do not quantize it to the palette strip or erase faint edges.

The old geometric fox is gone from the compositor.
[`../logo.svg`](../logo.svg) remains only as history.
Candidates A–F stay in `assets/brand/character/mark/` as a record and must never be
used as fallback sources. Every production face comes from the one master.
