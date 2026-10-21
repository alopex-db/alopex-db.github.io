#!/usr/bin/env python3
"""Independent Pillow-only mascot study. No shipped assets are written.

Run: python3 scripts/render_character_exploration.py
All crop coordinates are half-open. Native size proofs have no enlargement.
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw
from render_brand_book import fox, font, SELECTED_FONTS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/brand/explore'
CANVAS = (2400, 3136)
P = dict(deep='#1E3A5F', blue_light='#2E5077', blue_dark='#152C4A',
         ice='#5FB4C9', aurora='#7EC8E3', frost='#B8D4E3',
         silver='#C0C5CE', snow='#F8FAFC', night='#0B1929')
NAMES = ('puff', 'perch', 'drift', 'beacon')
DETAILS = {
    'puff': dict(why='A friendly head-only avatar: winter cheek volume and open eyes communicate welcome without props.',
                 distinction='Soft circular head; expression lives in two large eyes.',
                 use='Community avatar, docs welcome, primary mascot beside the existing mark.',
                 tradeoff='Most overtly cute; the round ears can read as a polar bear at tiny sizes.',
                 small_size_assessment={'64': 'Clear cheeks, ears, eyes and muzzle.', '48': 'Expression remains open and friendly.', '32': 'Fox cheek shape survives; eye highlights soften.', '16': 'Readable face, but fox species is ambiguous: round ears and muzzle can read as a polar bear. Not an unqualified favicon.'}),
    'perch': dict(why='A whole companion that can sit beside documentation or peek above a panel; posture adds personality beyond a logo.',
                  distinction='Alert seated body, tucked paws and a tail wrapped across the feet.',
                  use='Repo avatar at 48px+, docs companion, release illustrations.',
                  tradeoff='Body reduces available face pixels; more mascot than symbol.',
                  small_size_assessment={'64': 'Seated pose, tail and face remain clear.', '48': 'Paws merge slightly; seated silhouette remains clear.', '32': 'Tail wrap reads; face becomes secondary.', '16': 'Pale seated silhouette survives, but eyes and tail separation become muddy. Too ambiguous for a standalone favicon.'}),
    'drift': dict(why='Quiet reliability expressed by a fox asleep inside its own tail: a calm alternative to an alert guardian.',
                  distinction='Asymmetric curled sleeping body; pose carries the expression.',
                  use='Docs empty states, idle terminal companion, larger stickers.',
                  tradeoff='Suggests rest rather than speed; weak species recognition when reduced.',
                  small_size_assessment={'64': 'Sleeping face and enveloping tail read clearly.', '48': 'Curled pose reads; eyelids become delicate.', '32': 'Sleep expression fades; tail remains a crescent.', '16': 'Unreadable as a fox: a pale curled smudge with a dark notch. Reject as favicon; keep as an illustration option.'}),
    'beacon': dict(why='A bridge from the current geometric identity to a friendly mascot: fewer large shapes, broad eye spacing, and no decorative details.',
                   distinction='Compact graphic face with rounded ear caps, two-tone cheeks and bold eyes.',
                   use='Best favicon candidate, repo avatar, compact software lockup.',
                   tradeoff='Less expressive than Puff or Perch; still somewhat emblem-like.',
                   small_size_assessment={'64': 'All face shapes are distinct.', '48': 'Broad cheeks and dark eyes remain clear.', '32': 'Strong face and muzzle; minimal detail loss.', '16': 'Best of the four: eyes, nose and broad ears remain separated. Still reads as a face more readily than an unmistakable fox; stronger candidate than proof of species recognition.'}),
}


def character(name):
    """Draw once at 2048px. Every output derives from this same master."""
    s = 4
    im = Image.new('RGBA', (512*s, 512*s))
    d = ImageDraw.Draw(im)
    def box(b): return tuple(round(v*s) for v in b)
    def e(b, c): d.ellipse(box(b), fill=P[c])
    def rr(b, r, c): d.rounded_rectangle(box(b), radius=r*s, fill=P[c])
    def poly(points, c): d.polygon([(int(x*s), int(y*s)) for x,y in points], fill=P[c])
    def arc(b, start, end, c, w): d.arc(box(b), start, end, fill=P[c], width=w*s)
    def eye(x,y,r=15,highlight=True):
        e((x-r,y-r,x+r,y+r+3),'night')
        if highlight: e((x-5,y-7,x+1,y-1),'snow')
    if name == 'puff':
        # Low, round ear caps deliberately reflect a winter arctic coat.
        poly([(96,210),(110,106),(132,88),(150,90),(211,190)],'deep')
        poly([(301,190),(362,90),(380,88),(402,106),(416,210)],'deep')
        e((113,87,156,130),'deep'); e((356,87,399,130),'deep')
        poly([(106,207),(119,111),(137,97),(149,101),(202,191)],'snow')
        poly([(310,191),(363,101),(375,97),(393,111),(406,207)],'snow')
        e((120,96,150,128),'snow'); e((362,96,392,128),'snow')
        poly([(128,166),(139,116),(176,176)],'frost')
        poly([(336,176),(373,116),(384,166)],'frost')
        e((61,132,451,428),'deep'); e((69,139,443,421),'snow')
        poly([(79,263),(49,301),(93,303),(66,328),(137,360),(182,388),(256,417),(330,388),(375,360),(446,328),(419,303),(463,301),(433,263)],'deep')
        poly([(85,264),(65,295),(109,298),(81,324),(143,353),(188,381),(256,409),(324,381),(369,353),(431,324),(403,298),(447,295),(427,264)],'snow')
        e((99,185,413,395),'snow')
        e((159,283,353,409),'frost'); e((166,277,346,395),'snow')
        eye(179,264,18); eye(333,264,18)
        e((236,313,276,340),'night')
        arc((230,328,256,359),5,100,'deep',5); arc((256,328,282,359),80,175,'deep',5)
    elif name == 'perch':
        e((153,205,358,442),'deep'); e((161,211,350,434),'frost')
        e((206,258,310,426),'snow')
        e((129,91,217,193),'deep'); e((295,91,383,193),'deep')
        e((137,99,209,185),'snow'); e((303,99,375,185),'snow')
        poly([(153,157),(169,113),(193,160)],'ice')
        poly([(319,160),(343,113),(359,157)],'ice')
        e((103,120,409,329),'deep'); e((111,128,401,321),'snow')
        poly([(122,230),(91,255),(126,258),(109,278),(179,297),(256,321),(333,297),(403,278),(386,258),(421,255),(390,230)],'deep')
        poly([(124,230),(107,250),(142,254),(125,274),(182,290),(256,313),(330,290),(387,274),(370,254),(405,250),(388,230)],'snow')
        e((134,166,378,298),'snow')
        poly([(173,246),(256,265),(339,246),(256,309)],'frost')
        e((209,248,303,303),'snow')
        eye(189,221,14); eye(323,221,14)
        e((239,256,273,278),'night')
        arc((239,272,273,292),0,180,'deep',4)
        # Tail crosses the body, with a broad pale tip rather than fine fur.
        e((86,334,397,458),'deep'); e((94,340,389,450),'frost')
        e((91,344,241,447),'snow')
        e((242,409,302,446),'snow'); e((310,405,361,441),'snow')
    elif name == 'drift':
        e((63,150,449,426),'deep'); e((71,158,441,418),'frost')
        e((91,182,332,388),'snow')
        e((150,133,232,248),'deep'); e((157,141,225,247),'snow')
        e((176,160,210,214),'ice')
        e((274,162,351,261),'deep'); e((281,170,344,258),'snow')
        e((166,202,365,357),'snow')
        arc((207,253,246,281),8,171,'night',7)
        arc((285,253,324,281),8,171,'night',7)
        e((256,291,284,312),'night')
        # Overlapping tail forms the curl; its tip cradles the muzzle.
        e((69,295,438,431),'deep'); e((77,301,430,423),'frost')
        e((92,305,294,415),'snow')
        arc((129,328,403,409),5,108,'ice',8)
    elif name == 'beacon':
        rr((86,84,195,248),48,'deep'); rr((317,84,426,248),48,'deep')
        rr((94,92,187,244),43,'snow'); rr((325,92,418,244),43,'snow')
        rr((119,112,166,193),23,'ice'); rr((346,112,393,193),23,'ice')
        rr((68,155,444,360),83,'deep'); rr((76,163,436,352),76,'snow')
        poly([(92,288),(177,308),(256,393),(335,308),(420,288),(368,370),(256,433),(144,370)],'deep')
        poly([(91,280),(183,303),(256,382),(329,303),(421,280),(362,364),(256,423),(150,364)],'frost')
        poly([(174,298),(256,324),(338,298),(256,407)],'snow')
        rr((150,242,184,282),16,'night'); rr((328,242,362,282),16,'night')
        rr((235,325,277,351),12,'night')
    else: raise ValueError(name)
    return im


def text(im, xy, value, size=24, color='frost', role='body'):
    d = ImageDraw.Draw(im); f = font(size, role)
    b = d.textbbox((0,0), value, font=f)
    d.text((xy[0]-b[0],xy[1]-b[1]),value,font=f,fill=P[color])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    masters = {n: character(n) for n in NAMES}
    book = Image.new('RGBA',CANVAS,P['night'])
    tiles = []
    def add(name,x,y,im,background='transparent',**metadata):
        w,h = im.size
        t=dict(name=name,x=x,y=y,w=w,h=h,bbox=[x,y,x+w,y+h],background=background,**metadata)
        tiles.append(t)
        text(book,(x,y-36),f'{name} / {w} x {h}',21)
        book.paste(im,(x,y))  # Replace alpha exactly, never bake a preview matte.
    text(book,(64,40),'ALOPEX DB / CHARACTER EXPLORATION',42,'snow','brand')
    text(book,(64,105),'Four alternatives. No identity replacement. Arctic palette only. / 01',25)
    text(book,(64,155),'Transparent crops; inspect on light and dark. Proofs below are actual pixels, not enlarged.',23)
    for i,n in enumerate(NAMES):
        x=64+i*576
        add(f'char-{n}-hero',x,272,masters[n].resize((512,512),Image.Resampling.LANCZOS))
        proof=Image.new('RGBA',(512,128)); samples=[]
        for cx,size in zip((64,192,320,448),(64,48,32,16)):
            px,py=cx-size//2,(128-size)//2
            proof.alpha_composite(masters[n].resize((size,size),Image.Resampling.LANCZOS),(px,py))
            samples.append(dict(size=size,bbox=[px,py,px+size,py+size]))
        add(f'char-{n}-sizes',x,880,proof,samples=samples,
            rasterization='2048px master -> target via LANCZOS; composited 1:1')
        for cx,size in zip((64,192,320,448),(64,48,32,16)):
            text(book,(x+cx-20,1024),f'{size}px',18)
        lock=Image.new('RGBA',(1024,256))
        lock.alpha_composite(masters[n].resize((256,256),Image.Resampling.LANCZOS),(0,0))
        text(lock,(298,91),'Alopex DB',98,'snow','brand')
        add(f'char-{n}-lockup',64+(i%2)*1152,1152+(i//2)*352,lock)
    add('compare-current',64,1920,fox(512,'dark'),
        geometry_source='scripts/render_brand_book.py:fox',mode='dark',geometry_modified=False)
    text(book,(672,1936),'THE CURRENT MARK',32,'snow','brand')
    for j,line in enumerate((
        'Exact shipped geometry; snow + ice dark-background variant.',
        'A single sharp silhouette. Strong at small sizes; more severe in tone.',
        'Puff: the most welcoming face. Perch: a companion with posture.',
        'Drift: quiet and illustrative. Beacon: the strongest compact candidate.',
        'The row below normalizes visible area, not nominal image squares.',
        'Labels stay in gutters. No frames, names or captions inside crops.',
        '16px: Beacon leads; Puff is species-ambiguous; Perch loses detail;',
        'Drift becomes a pale curl and is unsuitable as a favicon.',
    )): text(book,(672,2005+j*44),line,24)
    row=Image.new('RGBA',(2048,512),P['deep']); placements=[]
    # Equal alpha coverage gives different silhouettes comparable optical mass.
    images=[masters[n] for n in NAMES]+[fox(1024,'dark')]
    target_area=54000
    for i,(n,im) in enumerate(zip((*NAMES,'current'),images)):
        b=im.getbbox(); cropped=im.crop(b)
        area=sum(cropped.getchannel('A').histogram()[k]*k/255 for k in range(256))
        factor=(target_area/area)**0.5
        dims=tuple(round(v*factor) for v in cropped.size)
        reduced=cropped.resize(dims,Image.Resampling.LANCZOS)
        x=round((i+0.5)*2048/5-dims[0]/2); y=round(256-dims[1]/2)
        row.alpha_composite(reduced,(x,y))
        placements.append(dict(name=n,bbox=[x,y,x+dims[0],y+dims[1]],
                               alpha_area_px=round(sum(reduced.getchannel('A').histogram()[k]*k/255 for k in range(256)))))
    add('compare-row',176,2544,row,P['deep'],optical_normalization='Equal alpha-weighted visible area: approximately 54000 px per character, centered in five equal cells.',placements=placements)
    for i,n in enumerate((*NAMES,'current')):
        text(book,(176+round((i+.5)*2048/5)-36,3080),n.title(),22)
    for i,a in enumerate(tiles):
        x,y,r,b=a['bbox']; assert 0<=x<r<=CANVAS[0] and 0<=y<b<=CANVAS[1]
        for t in tiles[i+1:]:
            u,v,w,z=t['bbox']; assert max(u-r,x-w,v-b,y-z)>=48,(a['name'],t['name'])
    manifest=dict(canvas=dict(width=CANVAS[0],height=CANVAS[1],mode='RGBA'),
        status='Exploration only; no shipped identity replacement.',
        bbox_convention='Half-open [x, y, x+w, y+h]; all tile bboxes are exact crop regions.',
        palette=P,warm_accent=None,
        palette_reason='No warm accent needed. Night is the palette near-black used for noses and eyes; snow and frost express a winter coat.',
        rendering='Pillow primitives only. Characters drawn at 2048x2048; all outputs LANCZOS downsampled from unchanged masters.',
        preview='Catalog gutters are night; transparent tile bboxes retain alpha 0. Snow wordmarks are intended for dark backgrounds.',
        fonts=SELECTED_FONTS,directions=[dict(name=n,**DETAILS[n]) for n in NAMES],
        recommendation=dict(ranking=['beacon','puff','perch','drift'],
            reasons=['Beacon best preserves face structure at 16px and bridges software mark and mascot.',
                     'Puff is the friendliest avatar; use at 32px+ where the face has room.',
                     'Perch offers richer companion poses but needs more pixels.',
                     'Drift is distinctive at illustration size; unsuitable for a favicon.'],
            deployment='Consider Beacon as a replacement candidate or Puff as a companion to the current mark; no replacement authorized.'),
        tiles=tiles)
    book.save(OUT/'character-book.png')
    (OUT/'character-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with Image.open(OUT/'character-book.png') as check:
        check.load(); assert check.size==CANVAS and check.mode=='RGBA'
        for t in tiles:
            crop=check.crop(t['bbox']); a=crop.getchannel('A')
            if t['background']=='transparent':
                assert all(a.getpixel(p)==0 for p in [(0,0),(crop.width-1,0),(0,crop.height-1),(crop.width-1,crop.height-1)])
                assert a.getextrema()==(0,255)
            else: assert a.getextrema()==(255,255)
    print(f'Verified {len(tiles)} tiles, minimum 48px gutters, {CANVAS[0]} x {CANVAS[1]} RGBA')


if __name__=='__main__':
    main()
