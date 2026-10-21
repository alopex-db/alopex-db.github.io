# Alopex DB canonical calm character variations

Sixteen PNGs generated with the built-in `image_gen` tool. The owner selected the calm register; these variations follow the locked references below. No shipped identity or exploration file was modified, and no commit was made.

## References and prompt reuse

- **Group 1 — expressions:** [canonical b10 face](../explore/generated-calm/fox-b10-portrait.png). Happy, sleepy, curious and pleased also received the generated `face-neutral.png` as a secondary framing reference.
- **Group 2 — poses:** [canonical b10 face](../explore/generated-calm/fox-b10-portrait.png) and [canonical b11 body/product pose](../explore/generated-calm/fox-b11-summit.png), in that order.
- **Group 3 — family:** the same b10 face and b11 body references, in that order. Scenes convey the sibling projects; no different species, palette or costume was requested.
- **Group 4 — small mark:** b10 face. The final revision also received the first generated head mark as a failed-size reference, not as a replacement character identity.

The locked character/style block below each image is identical across all sixteen prompts. The opening character/style paragraphs were copied word for word from the **final correction prompt** for b10 in [the calm README](../explore/generated-calm/README.md). Additional character/style sentences were also copied word for word from that prompt's composition paragraph. Pose/framing clauses were separated so they could vary. No new character description was invented per scene. The original navy-background sentence remains inside the quoted historical block; the identical production-constraints paragraph explicitly overrides it with transparency for every call. Mark-specific simplification is explicitly confined to its pose/scene clause.

## Background and file treatment

**All sixteen use a real transparent background.** Every generation used `transparent_background: true`; all saved files are **1254 × 1254 RGBA**, with both fully transparent and fully opaque pixels verified. White snow in the family scenes is a bounded foreground object, not a white background. There is no opaque navy or white canvas mixed into the set.

The generated PNGs were copied unchanged. All artwork came from the image-generation tool; no Pillow primitives, SVG, code-drawn artwork or programmatic compositing was used. Pillow was used only to read alpha/dimensions and resample temporary small-size QA previews of the generated mark. Those previews are outside the repository and do not alter the deliverables.

**Production limitation across the set:** the transparent outputs contain visible stray white/colored pixels and ragged fringes outside some silhouettes, particularly the full-body and terrain scenes. Real alpha does not mean clean alpha. Several fills also retain slight tonal softness and nose shine despite the flat-fill prompt. These need cleanup before publication. This set is a generated candidate set with explicit exceptions, not a silently approved uniform production pack.

## Consistency review

Material or minor drift is explicitly flagged for **pose-walking**, **pose-carrying**, **pose-resting**, **family-skulk**, **family-trail**, and **family-dataui**. Walking, Trail and DataUI stretch the proportions; Skulk reduces tails; Carrying has moderate proportion drift plus a turned head; Resting adds a fuller chest fur mass. Do not treat these as interchangeable canonical poses without revision.

The five face expressions preserve the same recognizable face and similar head-and-shoulders framing, but generative placement is not pixel-registered. Curious intentionally rotates the head. A direct expression swap can shift silhouette/feature positions slightly.

The closest reference matches are **face-neutral**, **face-happy**, **face-sleepy**, **face-curious**, **face-pleased**, **pose-sitting**, **pose-presenting**, **family-alopex**, and **family-chirps**, subject to the common alpha and rendering limitations above.

## Small-size mark verification

The first mark was resampled to actual **16, 32 and 48 px** with Lanczos filtering and visually inspected, including a nearest-neighbor enlargement of the 16 px result. Its eyes/nose became too weak at 16 px. A second tool generation requested larger dark features and fewer shapes; the saved `mark-head-flat.png` is that revision.

The revised mark was tested again at all three sizes. **32 and 48 px:** recognizable fox head with distinct eyes and nose. **16 px: not a pass.** The animal-head silhouette survives, but the eyes/nose reduce to pale tiny blocks and the ear/muzzle distinction is too weak for an unmistakable arctic-fox symbol. It remains a candidate, not a signed-off 16 px favicon. The generated master also does not strictly satisfy the requested maximum of three perfectly flat colors, due to retained tonal variation and details. This limitation is recorded rather than hidden behind the master-size preview.

## Exact prompts and per-image assessments

### face-neutral.png

[View image](face-neutral.png)

Group: 1. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10.

Assessment: MATCH — closely preserves b10 face, ear placement, muzzle and tail-shoulder layout; no material identity drift, but the generated alpha has stray edge speckles and the fills retain faint softness.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Head-and-shoulders portrait, SAME FRAMING as canonical b10: fixed head scale, fixed camera, head centered, ears fully inside safe margin, chest cropped at lower edge, large simple plume tail behind viewer-right shoulder. Keep all anatomy and colors fixed; expression is the only change. Calm neutral expression, open matte dark eyes looking straight at viewer, tiny relaxed closed mouth.
```

### face-happy.png

[View image](face-happy.png)

Group: 1. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then `face-neutral.png`.

Assessment: MATCH — same canonical face with appropriately closed contented eye curves; no material identity drift, but tiny scale/position differences prevent a guaranteed pixel-perfect swap with neutral.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Head-and-shoulders portrait, SAME FRAMING as canonical b10: fixed head scale, fixed camera, head centered, ears fully inside safe margin, chest cropped at lower edge, large simple plume tail behind viewer-right shoulder. Keep all anatomy and colors fixed; expression is the only change. Contented happy expression: both eyes CLOSED in gentle upward smiling curves, no catchlights in closed eyes, small contented smile. No big grin.
```

### face-sleepy.png

[View image](face-sleepy.png)

Group: 1. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then `face-neutral.png`.

Assessment: MATCH — same canonical muzzle, ears and head silhouette, with half-closed eyes; no material identity drift, though the narrowed eyes can read more knowing than drowsy.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Head-and-shoulders portrait, SAME FRAMING as canonical b10: fixed head scale, fixed camera, head centered, ears fully inside safe margin, chest cropped at lower edge, large simple plume tail behind viewer-right shoulder. Keep all anatomy and colors fixed; expression is the only change. Sleepy expression: eyes HALF CLOSED, small matte dark slivers beneath gently drooping lids, about to doze. Relaxed neutral little mouth. Not sad.
```

### face-curious.png

[View image](face-curious.png)

Group: 1. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then `face-neutral.png`.

Assessment: MATCH — head tilt preserves the same facial design rather than introducing another fox; the rotated ears change the outer bounds, so the expression is not pixel-registered to neutral.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Head-and-shoulders portrait, SAME FRAMING as canonical b10: fixed head scale, fixed camera, head centered, ears fully inside safe margin, chest cropped at lower edge, large simple plume tail behind viewer-right shoulder. Keep all anatomy and colors fixed; expression is the only change. Curious expression: head tilted slightly to one side while its center and scale remain the same, small rounded ears directed forward, open matte eyes alert, tiny closed mouth.
```

### face-pleased.png

[View image](face-pleased.png)

Group: 1. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then `face-neutral.png`.

Assessment: MATCH — same canonical face and restrained satisfied smile; no material identity drift, with small generated placement differences from neutral.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Head-and-shoulders portrait, SAME FRAMING as canonical b10: fixed head scale, fixed camera, head centered, ears fully inside safe margin, chest cropped at lower edge, large simple plume tail behind viewer-right shoulder. Keep all anatomy and colors fixed; expression is the only change. Pleased expression: eyes OPEN, small SATISFIED SMILE clearly distinct from neutral, calm friendly expression, one small catchlight per eye.
```

### pose-sitting.png

[View image](pose-sitting.png)

Group: 2. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: MATCH — canonical three-quarter face and full-body design, with a clear tail curl around the feet; no material identity drift, but substantial stray alpha speckling needs cleanup.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Full body in three-quarter view, sitting upright comfortably with enormous plume tail CURLED AROUND ITS FEET. Fine muzzle visible, open matte eyes, approximately 2.5 heads tall, all paws and tail visible with generous margins. No props or ground patch.
```

### pose-walking.png

[View image](pose-walking.png)

Group: 2. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT — the canonical face/palette survive, but legs, neck and body stretch toward a more naturalistic long-legged fox instead of the compact product proportions; revise before strict-set use.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Full body in right-facing SIDE PROFILE WALKING LEFT TO RIGHT. Gentle natural gait, one front paw advancing, enormous long plume tail carried low behind. Fine muzzle profile visible, calm open matte eye, approximately 2.5 heads tall, whole animal inside margins. No props, ground patch or paw prints.
```

### pose-presenting.png

[View image](pose-presenting.png)

Group: 2. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: MATCH — canonical seated face/body and storage design remain recognizable, with one paw raised clearly toward the stack; no material identity drift, though the tail approaches the right edge.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Full body three-quarter fox SITTING BESIDE a stack of four thick horizontal rectangular storage slabs. ONE FRONT PAW raised TOWARD THE STACK as if indicating it in a diagram. Other forepaw on ground. Huge plume tail relaxed around feet. Structured flat frost slabs with navy separation gaps and small regular ice-blue square data indicators, no gem/crystal or glow. Entire fox and stack visible, ordinary calm explaining gesture.
```

### pose-carrying.png

[View image](pose-carrying.png)

Group: 2. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT (moderate proportions) — canonical face remains recognizable, but body and legs are longer and the head turns toward the viewer instead of staying in profile; the rectangular data slab reads correctly and uses a flat bright edge rather than a halo.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Full body right-facing side profile WALKING while carefully CARRYING ONE SINGLE HORIZONTAL DATA SLAB IN ITS MOUTH. Thin wide rectangular storage layer with parallel straight edges and tiny ice-blue square data indicators, not a gem or crystal. Muzzle grips middle upper edge gently; slab does not hide whole face. User requested a glowing slab: convey light only by a flat pale accent edge, no airbrushed halo or lighting on fox. Enormous plume tail low behind, careful calm gait.
```

### pose-resting.png

[View image](pose-resting.png)

Group: 2. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT (minor fur mass) — canonical face and tail remain, and the crossed-paw pose works, but the chest/ruff is busier and fuller than b11; retain as a candidate rather than an exact fur-shape match.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Full body three-quarter fox LYING DOWN, front paws CROSSED, eyes OPEN and composed. Fine muzzle visible, relaxed ears, enormous plume tail curled alongside its body. Awake and comfortably resting. All paws and tail within margins, no props or ground patch.
```

### family-alopex.png

[View image](family-alopex.png)

Group: 3. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: MATCH — strongest full-body continuity with canonical b11, preserving the seated product pose, exposed muzzle, hanging tail and four slab layers; no material identity drift.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Same product pose as canonical b11: fox sits calmly ON TOP OF FOUR LAYERED STORAGE SLABS, huge plume tail hanging DOWN THE SIDE almost to base. Fine muzzle visible in three-quarter view, approximately 2.5 heads tall. Clearly horizontal thick rectangular layers, navy separation gaps, small regular ice-blue square indicators. No gem, crystal or glow. Whole fox and stack inside generous margins, minimal snow base only.
```

### family-skulk.png

[View image](family-skulk.png)

Group: 3. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT — regular receding observations read clearly, but tail-to-body ratios shrink across the group and the distant animals do not preserve the enormous canonical plume; revise before strict-set use.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: FIVE copies of the EXACT SAME FOX at EVEN INTERVALS along a snowfield path receding diagonally into the distance, regular scheduled observations. Near fox larger at lower left, others progressively smaller along evenly spaced positions in perspective toward upper right. Same face, body and huge tail on all five, calm sitting or standing, no species variation. Small connected simple frost-white snowfield island only, everything beyond that terrain island transparent; no sky field. Entire group within margins.
```

### family-chirps.png

[View image](family-chirps.png)

Group: 3. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: MATCH — both profiles share the canonical fine snout, dark matte eyes and simplified plume design; the gap and three call arcs read clearly, with no material identity drift apparent at this scale.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: TWO copies of the EXACT SAME FOX in side profile facing each other ACROSS A CLEAR GAP, softly calling. Three simple thin navy or ice-blue CURVED ARCS between muzzles indicate exchanged calls, no speech bubbles or letters. Tiny open mouths, calm eyes, low rounded ears, enormous plume tails sweeping outward. Whole tails inside generous margins, no ground patch. Same character proportions and design on both.
```

### family-trail.png

[View image](family-trail.png)

Group: 3. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT — the rear walking view and clean print trail work, but neck/legs are elongated and the body is more naturalistic than b11; prints are stylized paw shapes rather than plain round dots.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Fox seen FROM BEHIND in rear three-quarter view WALKING AWAY toward upper center. Enormous fluffy plume tail visible, a small portion of fine muzzle in profile, no frontal portrait. A CLEAN SINGLE LINE OF ROUND PAW PRINTS leads back from the fox toward the viewer at bottom foreground. Minimal narrow white/frost snow-path island under prints and fox, everything beyond that island transparent. Logs/events: clear record of what passed.
```

### family-dataui.png

[View image](family-dataui.png)

Group: 3. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then canonical b11.

Assessment: DRIFT — the animal is taller and more slender with a smaller head than the canonical product fox; terrain-overview concept works, but trees/mountains make the scene busier and less uniform than requested.

Exact prompt:

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: Fox on a ridge, seen in REAR THREE-QUARTER PROFILE looking out over a broad snowfield. Whole TERRAIN VISIBLE AHEAD: a few clean layered frost-white snow planes spread from foreground ridge toward distant horizon within a bounded landscape island. Fox in near lower-right foreground, enormous plume tail and fine side snout visible, calm observing posture, not heroic. Main point is one viewpoint over the entire terrain. No sky field; everything beyond bounded terrain and fox transparent.
```

### mark-head-flat.png

[View image](mark-head-flat.png)

Group: 4. Background tool argument: `transparent_background: true`.

Reference image arguments: canonical b10, then first mark output `exec-ada2b4fc-8d90-43b5-a7d1-a6d1634a0100.png` (supplied at the deliverable path before replacement).

Assessment: INTENTIONAL SYMBOL SIMPLIFICATION, not a second character — tapered head/ears/nose derive from b10, but the tool retained minor fur/ear cuts, catchlights and subtle tonal variation instead of a strict three-solid-color mark; 32/48 px are usable, but it does NOT pass a strict 16 px legibility sign-off.

Exact prompt (saved revision):

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the character identity reference; the second image is the initial mark that failed at 16 pixels. Keep the canonical identity, correct the mark's small-size legibility.
Pose/scene clause: HEAD-ONLY FRONT-VIEW MICRO SYMBOL optimized specifically for 16 PIXELS. The initial mark had eyes and nose too small, too much forehead, and residual detail; correct those. ONE smooth white tapered fox head silhouette filling 90 percent of square, TWO small rounded WIDE-SET ears, no fur spikes or ear tufts. Exactly THREE solid fills maximum: white #F8FAFC head, frost #B8D4E3 simple ear inserts, dark navy #1E3A5F facial features. NO gradients, NO shading, NO highlight dots, NO eyebrows, NO muzzle strokes, NO mouth, NO colored outline, NO stray pixels outside silhouette. TWO BOLD SOLID DARK EYES each roughly 15 percent of head width (at least TWO PIXELS wide at 16 px) set low and wide. ONE BOLD DARK NOSE roughly 16 percent head width, spaced clearly below the eyes. Lower head tapers to create a fox muzzle in its OUTER SILHOUETTE. Cut all minor detail so ear silhouette, dark eyes and dark nose survive downsampling to 16 px. This is an intentional small-size simplification of canonical fox, NOT a cute detailed face illustration. No shoulders or tail, transparent outside head.
```

First mark attempt (rejected for weak 16 px features): used canonical b10 only and `transparent_background: true`. The tool output remains in its original generated-images location; it is not an extra deliverable in this directory.

Exact prompt (first attempt):

```text
Use case: logo-brand.
Asset type: Alopex DB arctic fox mascot, QUIET EDITORIAL VECTOR REGISTER for technical documentation and conference slides.
SAME CHARACTER as the reference: a white arctic fox with an enormous fluffy long plume tail as big as head and body combined, small rounded wide-based ears with pale ice-blue insides, fine projecting tapered fox muzzle and neat small dark nose, dark eyes. Preserve this recognizable identity while changing the register radically.
CALM REGISTER, essential: smaller MATTE dark eyes relative to the head, exactly ONE tiny white catchlight per visible eye, no colored irises, no glossy anime eyes or sparkles. About 2.5 to 3 heads tall when full body is visible, a little more poise than the reference, still cute. REDUCED NECK RUFF, a few broad smooth cheek masses and clearly exposed fine muzzle, never a Pomeranian collar. Fur simplified into a FEW LARGE CLEAN SHAPES, almost smooth silhouette, at most two or three subtle tufts, no individual fur spikes or wisps. Thin outlines or NO outlines; color boundaries define shapes. Flat hard-edged color shapes, only TWO OR THREE SOLID TONES per shape, absolutely no gradients, blur, airbrushing, glow, glossy shine, 3D, texture or anime cel lighting. Muted cool editorial vector illustration, composed and self-possessed, friendly understated expression.
Palette strictly restrained: white #F8FAFC, frost #B8D4E3, ice blue #5FB4C9 as a small accent only, deep navy #1E3A5F, plain night #0B1929 background. No bright cyan lighting. Minimal snow if needed. Silent, Adaptive, Unbreakable conveyed as ordinary calm comfort. No heroic pose, no cape, no suffering.
Species: unmistakable ARCTIC FOX, not kitten or puppy. Fine slightly elongated muzzle bridge and low widely separated small rounded ears. Let the muzzle show, particularly in front views.
No text, lettering, numbers, logos, wordmarks or watermark anywhere. One standalone finished illustration, no sheet or collage.
Draw as a minimal EDITORIAL PAPER-CUT VECTOR illustration using only about 10 to 15 broad FLAT shapes total. One solid white tapered head silhouette, two small rounded wide-based ears with single flat frost-blue inserts, two small solid navy oval eyes with ONE tiny white dot each, narrow clearly visible long tapered muzzle bridge and neat solid navy nose. NO eyeliner or lashes. Reduce cheek fur to ONE small point on each side. NO forehead spikes; smooth gently rounded crown. NO large fur collar: slim neck connecting head to simple narrow shoulder/chest shape. Only SOLID fills, constant colors within every region. No gradients whatsoever, no subtle airbrush shading, no nose shine, no fur strokes, no texture, no thick contour. Friendly, quiet, self-possessed, unmistakably fox through fine snout and widely set low small ears.
Production constraints for this set: TRUE TRANSPARENT BACKGROUND with alpha, replacing the earlier prompt's navy background. No colored field, no white backdrop, no checkerboard drawn into pixels, no drop shadow or sticker border. Square canvas. Same exact character as supplied canonical reference(s), not a redesign. Full body approximately 2.5 heads tall. All sixteen images use this same treatment. No text or lettering.

Input images: canonical b10 is the face/identity reference; canonical b11, when supplied, is the full-body proportion and product-pose reference. Preserve those exact designs.
Pose/scene clause: HEAD ALONE, straight front view, simple SMALL-SIZE SYMBOL, no shoulders, no tail. Derived from canonical b10 facial proportions, broad tapered head silhouette and small wide-set rounded ears, visible narrow muzzle and small neat nose. EXACTLY THREE SOLID COLORS MAXIMUM: white #F8FAFC, frost #B8D4E3 ear inserts, navy #1E3A5F eyes/nose. NO SHADING, cheek patches, fur detail, mouth hairlines, eyebrow lines, muzzle bridge strokes or tiny decorations. Mark-specific simplification overrides extra fur and catchlight detail where too small. Large bold solid eye dots, neat dark nose, one clean silhouette; use negative space for muzzle. Design to remain recognizable at 48,32,16 pixels, with generous clear gaps between eyes and nose, minimal simple shapes. Transparent outer canvas, head fills about 80 percent of square.
```

