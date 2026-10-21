# Fox symbols on opaque plates

Six candidates generated with the built-in `image_gen` tool, followed by actual LANCZOS reduction and visual review. The symbol artwork is generated, not drawn with Pillow, SVG or code. Pillow was used only for the requested resizing, proof-sheet layout and pixel inspection.

[Open the owner proof sheet](mark-proof-sheet.png)

## Recommendation

**E — `mark-e-twotone.png` — is the favicon choice.** At actual 16 px it retains a recognizable fox-head symbol: broad ear peaks, two dark eye marks and a tapered muzzle. Its connected white mass survives without a tiny nose or blue inserts. B is the runner-up when closer correspondence to the fuller character is preferred. F is visually bold but loses the animal identity.

“Ship” below is the visual small-size verdict for the candidate, not a claim that the generated master has an exact indexed palette. See the color limitation below before treating these as strict production masters. No favicon, avatar or header has been installed or replaced.

## Proof and verification

- All six full-size masters are **1254 × 1254 RGB**, completely opaque, with navy reaching all four square edges. All generation calls used `transparent_background: false`.
- Each master was independently downscaled **directly from full size**, using Pillow `Image.Resampling.LANCZOS`, to **128, 48, 32 and 16 px**. No cascading reductions, sharpening, color quantization or manual retouching was applied.
- Actual 48, 32 and 16 px results for all six were opened and visually inspected. A nearest-neighbor enlarged view of the real 16 px samples was also inspected to distinguish pixel structure from full-size detail.
- The proof sheet shows **A through F from left to right**. Each background half repeats four rows at **128, 48, 32 and 16 actual pixels**. Top half is light grey `#E5E7EB`; bottom half is near-black `#080B10`. Icons are not enlarged inside their size rows. Labels appear only on the proof sheet, never inside the candidate masters.
- The proof-sheet image itself is **1200 × 1100 px**; inspect at 100% for actual-size judgment. A viewer that scales the whole sheet will also scale the nominal 16 px row.
- The same resized tile is used on both backgrounds. Because the plate is opaque, its internal contrast is independent of the surrounding page. On dark chrome the outside plate boundary is subtler, but the white symbol remains legible.
- Saved previews are in `previews/128/`, `previews/48/`, `previews/32/` and `previews/16/`, retaining the six candidate filenames. These files are the exact tiles pasted into the proof sheet.

## Color limitation — explicitly not hidden

The requested design palettes are three colors for A–D and two for E/F. **The image generator retained slight tonal variation and texture within nominal fills**, so these RGB masters do not literally contain only two or three unique pixel colors, nor do their navy samples exactly match `#0B1929` everywhere. This is not solely edge antialiasing. `verification.json` records unique RGB counts and corner samples from the unchanged masters. No gradients or shading were requested; the exact prompts below make that clear. The proof sheet demonstrates the generated geometry and small-size contrast honestly, without silently cleaning or redrawing the symbols. Exact flat-palette production artwork remains a separate cleanup requirement; E is the design I would carry forward.

## Small-size verdicts

| Candidate | What it reads as at 16 px | Light and dark pages | Verdict |
|---|---|---|---|
| [mark-a-detailed.png](mark-a-detailed.png) | An animal head, leaning fox; cheek points become noise and the tiny nose is weak. | Yes: white head remains legible on its opaque navy plate in both halves; the plate edge is less distinct on dark chrome. | **Maybe** |
| [mark-b-simplified.png](mark-b-simplified.png) | A fox-like animal head; the taper survives, but the nose is a small soft spot. | Yes: visible on light and dark; no disappearing white-on-white edges. | **Maybe** |
| [mark-c-geometric.png](mark-c-geometric.png) | A geometric animal head, with cat/robot-mask ambiguity. | Yes: opaque plate preserves contrast against both page treatments. | **Discard** |
| [mark-d-minimal.png](mark-d-minimal.png) | A fox-like head with a long blank muzzle; less definite than E. | Yes: the plate isolates it from both page colors. | **Maybe** |
| [mark-e-twotone.png](mark-e-twotone.png) | A fox-head symbol: ear silhouette, two eye marks and taper remain distinct; some wolf ambiguity remains at this scale. | Yes: equally recognizable on light and dark; the solid plate solves the original white-on-light failure. | **Ship** |
| [mark-f-abstract.png](mark-f-abstract.png) | A chevron / angular mask, not reliably a fox. | Yes: very visible on both, but visibility is not species recognition. | **Discard** |

## Exact prompts and individual notes

A and B used the [canonical calm face](../../explore/generated-calm/fox-b10-portrait.png) as `referenced_image_paths`. C's first attempt also used it but retained cheek detail; the saved C was regenerated from its explicit geometric prompt with no image input. D, E and F were generated without image inputs to allow actual abstraction rather than copying the portrait. F's first attempt was rejected because it was another ordinary fox face; the saved F uses the stricter three-mass abstract prompt. Both rejected prompts are retained below for reproducibility. Rejected outputs are not included among the six saved candidates or the proof sheet.

### mark-a-detailed.png

[Master](mark-a-detailed.png) · [48 px](previews/48/mark-a-detailed.png) · [32 px](previews/32/mark-a-detailed.png) · [16 px](previews/16/mark-a-detailed.png)

16 px: **An animal head, leaning fox; cheek points become noise and the tiny nose is weak.**

Light/dark: Yes: white head remains legible on its opaque navy plate in both halves; the plate edge is less distinct on dark chrome.

Verdict: **Maybe**. Clear fox at 32/48 px. Closest to the character, but too much silhouette detail for the best favicon.

Reference input: canonical calm b10 face. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate A, least simplified: head roughly as canonical face, flattened to THREE colors. Broad cheek shape with just one broad outward cheek notch per side, no individual fur. Two flat ice-blue ear inserts, two bold solid navy slanted eye marks and one navy nose. Preserve the visible tapered muzzle wedge in outer silhouette. No mouth or muzzle strokes. Opaque navy fills whole square.
```

### mark-b-simplified.png

[Master](mark-b-simplified.png) · [48 px](previews/48/mark-b-simplified.png) · [32 px](previews/32/mark-b-simplified.png) · [16 px](previews/16/mark-b-simplified.png)

16 px: **A fox-like animal head; the taper survives, but the nose is a small soft spot.**

Light/dark: Yes: visible on light and dark; no disappearing white-on-white edges.

Verdict: **Maybe**. Clear fox at 32/48 px. Good runner-up with a recognizable muzzle, but the nose adds little at 16 px.

Reference input: canonical calm b10 face. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate B, simpler: REMOVE cheek ruff completely. Clean slightly squared-up broad head sides taper inward to a trapezoidal muzzle wedge. Two small broad-based ears with rounded tips, flat blue ear inserts, two bold navy eye marks and one bold navy nose. Only broad simple shapes, no cheek notches, fur, mouth, catchlights. THREE colors. Opaque navy fills whole square.
```

### mark-c-geometric.png

[Master](mark-c-geometric.png) · [48 px](previews/48/mark-c-geometric.png) · [32 px](previews/32/mark-c-geometric.png) · [16 px](previews/16/mark-c-geometric.png)

16 px: **A geometric animal head, with cat/robot-mask ambiguity.**

Light/dark: Yes: opaque plate preserves contrast against both page treatments.

Verdict: **Discard**. Legible geometry at 32/48 px, but sharp tall ears and angular mask lose the canonical arctic-fox feel; the nose does not improve the 16 px reading.

Reference input: none for saved candidate. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate C, strict GEOMETRIC SYMBOL: ignore decorative details from the reference. ONE continuous WHITE INVERTED-PENTAGON FACE with two attached SMALL WIDE TRIANGULAR EAR peaks; all face sides straight geometric lines. Absolutely NO CHEEK POINTS, NOTCHES OR FUR RUFF. Two ice-blue triangular inner-ear inserts, two navy horizontal diamond eye holes and one navy triangular nose hole. Clean drafting geometry, no curved almond eyes, no organic fluffy face. Lower face tapers sharply into a fox muzzle wedge. Three SOLID constant colors only, no variations within shapes, flat navy entire square.
```

Rejected first C attempt: canonical b10 face supplied as reference; it reintroduced cheek points, so it did not deliver increasing simplification.

Exact rejected prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate C, geometric: reduce head to a CLEAN GEOMETRIC TAPERING FACE mass, TWO wide ear triangles with gently softened tips, TWO substantial dark eye marks, ONE dark nose triangle at muzzle tip. Ear bases WIDE, far apart. Straight deliberate diagonals define the FOX muzzle wedge, no round cheeks or ruff. Ice blue ear inserts are simple triangles. THREE colors, opaque navy fills whole square. All features bold and readable, eyes and nose each at least 2 pixels across at 16 px.
```

### mark-d-minimal.png

[Master](mark-d-minimal.png) · [48 px](previews/48/mark-d-minimal.png) · [32 px](previews/32/mark-d-minimal.png) · [16 px](previews/16/mark-d-minimal.png)

16 px: **A fox-like head with a long blank muzzle; less definite than E.**

Light/dark: Yes: the plate isolates it from both page colors.

Verdict: **Maybe**. Fox reads clearly at 32/48 px. Removing the nose helps simplicity, but ear inserts and the longer blank lower face add weight without helping at 16 px.

Reference input: none for saved candidate. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate D, minimal: ONLY the smooth white tapered HEAD SILHOUETTE with broad wide-set ears and TWO solid navy eye marks. NO NOSE, no mouth, no cheeks or ruff. Lower silhouette ends in a distinctly narrow FOX MUZZLE WEDGE; eyes low and widely separated. Simple ice-blue inner-ear triangles allowed, no other detail. THREE colors. Head nearly fills plate, navy background to every edge.
```

### mark-e-twotone.png

[Master](mark-e-twotone.png) · [48 px](previews/48/mark-e-twotone.png) · [32 px](previews/32/mark-e-twotone.png) · [16 px](previews/16/mark-e-twotone.png)

16 px: **A fox-head symbol: ear silhouette, two eye marks and taper remain distinct; some wolf ambiguity remains at this scale.**

Light/dark: Yes: equally recognizable on light and dark; the solid plate solves the original white-on-light failure.

Verdict: **Ship**. Strongest 16 px candidate. Clear at 32/48 px too. No blue ear inserts or tiny nose to lose, and its broad connected white mass stays readable.

Reference input: none for saved candidate. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate E, TWO COLORS ONLY overriding the ice-blue allowance: white #F8FAFC and navy #0B1929, NO BLUE ear inserts at all. One clean WHITE FOX HEAD silhouette: wide-set small broad rounded ear peaks, straight smooth tapering face sides ending in a distinct MUZZLE WEDGE. TWO BOLD NAVY EYE CUTOUTS, low and wide. No separate nose, no mouth, no ruff, no fur strokes, no highlights or inner-ear detail. Make silhouette carry species: NOT round cat head and not puppy. Head almost fills full square navy plate. Bold instantly readable favicon, two colors ONLY.
```

### mark-f-abstract.png

[Master](mark-f-abstract.png) · [48 px](previews/48/mark-f-abstract.png) · [32 px](previews/32/mark-f-abstract.png) · [16 px](previews/16/mark-f-abstract.png)

16 px: **A chevron / angular mask, not reliably a fox.**

Light/dark: Yes: very visible on both, but visibility is not species recognition.

Verdict: **Discard**. Crisp at all sizes, but the abstract three-wedge emblem looks more like a shield/monogram than the approved fox.

Reference input: none for saved candidate. Background: opaque navy square, `transparent_background: false`.

Exact prompt:

```text
Use case: logo-brand.
Generate a NEW abstract favicon symbol, NOT a fox illustration or a drawn animal face.
Solid opaque night navy #0B1929 square plate bleeding to all four edges. TWO COLORS ONLY: white #F8FAFC and that navy. No blue.
Build an abstract FOX-HEAD EMBLEM from THREE BOLD WHITE ANGULAR MASSES: two broad upper ear wedges angled inward and a large lower tapering muzzle chevron. Let wide navy V-shaped negative-space channels separate the ear masses from the muzzle chevron. The overall gestalt suggests a fox head using just ear-and-muzzle negative space, almost a monogram but NO actual letters. NO almond eyes, NO eye dots, NO nose, NO mouth, NO ear inserts, NO cheek ruff, NO animal facial features at all. It is an abstract geometric symbol composed of large wedges and negative-space cuts. At 16px its three white masses and navy channels must remain separate and bold. Occupy 85-90 percent of square. Perfectly flat constant solid fills, no shading, no gradient, no texture, no shine, no contour. No text or lettering. This candidate must be dramatically MORE ABSTRACT than a face silhouette, and simpler than a two-eyed fox head.
```

Rejected first F attempt: no reference supplied; it returned a conventional fox face with eyes and nose rather than a negative-space abstraction.

Exact rejected prompt:

```text
Use case: logo-brand.
Asset: one square opaque favicon / repository avatar symbol for Alopex DB, not an illustration.
A SOLID NIGHT NAVY #0B1929 PLATE fills the ENTIRE SQUARE, bleeding to all four edges, no margins outside the plate, no transparency, no rounded outer corners needed. On it a SNOW WHITE #F8FAFC ARCTIC FOX HEAD fills about 85-90 percent of the width. Face tapers downward into a clear narrow FOX MUZZLE WEDGE. Two SMALL BROAD-BASED rounded-tip ears set WIDE APART, not tall narrow kitten ears. Eye marks and nose when present are the SAME navy as plate, as holes in white.
Maximum THREE SOLID COLORS TOTAL including the plate: night navy #0B1929, snow white #F8FAFC, ice blue #5FB4C9 inner ears only. No shading, no gradient, no glow, no texture, no outline, no fur detail, no whiskers, no glossy catchlights, no tiny decorative strokes. No text, lettering, numerals or watermark. Simple hard-edged bold symbol with large connected masses, designed to survive at 16 pixels. Calm fox identity conveyed by WIDE EAR BASES and TAPERED MUZZLE, not interior illustration detail.
Input image role: canonical arctic fox identity reference ONLY, reduce it to the specified symbol; do not copy its rendering, body or tail.
Candidate F, MOST ABSTRACT: an abstract fox-head SYMBOL almost like a monogram, but NO actual letters. Use a single broad geometric WHITE MASS with TWO NAVY NEGATIVE-SPACE V-NOTCHES at upper sides suggesting widely set broad ears, and a deep tapering lower WHITE WEDGE suggesting fox muzzle. Use NAVY CUTOUTS / negative spaces to suggest the eye sockets rather than drawing detailed eyes. At most one tiny ice-blue broad ear accent per side, but prefer TWO COLORS white/navy. No realistic anatomy, nose dot, mouth, fur, strokes, letters or decorative elements. Clean bilateral geometric emblem, enormous simple shapes occupying most of the opaque navy square, fox identity carried by ear/muzzle negative space.
```

