#!/usr/bin/env python3
"""A fresh, Pillow-only chibi character study. No earlier geometry is imported.

Run from any directory: python3 scripts/render_cute_exploration.py
Only cute-book.png and cute-manifest.json are written, under assets/brand/explore.
"""
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/brand/explore'
CANVAS=(2944,4256)
S=4
P={'deep':'#1E3A5F','blue-light':'#2E5077','blue-dark':'#152C4A',
   'ice':'#5FB4C9','aurora':'#7EC8E3','frost':'#B8D4E3',
   'silver':'#C0C5CE','snow':'#F8FAFC','night':'#0B1929','rose':'#E99BA4'}
NAMES=('mochi','pillow','doze','peek','tumble','flurry','chime','pitter')
FONTS={}
DETAILS={
 'mochi':dict(pose='Front-on sitter, tail wrapped around its feet; steady eye contact and a tiny w smile.',
              concept='The everyday survivor: comfortable before, during and after the weather changes.',
              trait='Unbreakable: ordinary comfort is the constant, not a heroic pose.',
              expression='Open, trusting eyes; warm blush; small w smile.',
              cute_reason='YES: oversized cheeks, huge sparkling eyes and a tail blanket make it feel like a small companion.',
              at_16px='A pale big-eared face with two dark eyes; smile and blush disappear. The tail merges into a soft base.'),
 'pillow':dict(pose='Lying flat on two soft storage slabs, chin resting between round paws.',
              concept='At home on the data; relaxed enough to use the store as a pillow.',
              trait='Durable storage: data is a dependable resting place.',
              expression='Wide eyes looking up; slightly squashed cheeks and a shy smile.',
              cute_reason='YES: the chin is low between marshmallow paws; the enormous face does all the emotional work.',
              at_16px='A wide-eyed pale loaf over a blue baseline. The storage slabs merge; the relaxed face remains.'),
 'doze':dict(pose='Curled into a soft tail ball, cheek tucked against the tail, sleepy arcs above.',
              concept='Waiting out the conditions by being completely comfortable.',
              trait='Unbreakable: rest and endurance, without suffering or defiance.',
              expression='Closed smiling eyelids, tiny nose and rosy sleeping cheeks.',
              cute_reason='YES: closed curved eyelids, tucked cheeks and a huge tail make a cozy sleeping bundle.',
              at_16px='A curled pale sleeping bundle with two ear tips. Eyes, nose and sleep arcs vanish; fails as a standalone fox icon.'),
 'peek':dict(pose='Eyes and large ears above a rounded snow ledge; two tiny paws holding its top.',
              concept='Snow covers most of the body; the little fox is still happily present.',
              trait='Native search: looking out from beneath the surface.',
              expression='Curious open eyes; small smile just above the ledge.',
              cute_reason='YES: the face-to-paw scale and low eye placement make the peeking gesture inviting.',
              at_16px='Two dark eyes and ears above a rounded blue-white bank. Paws merge; curiosity survives, species is ambiguous.'),
 'tumble':dict(pose='Rear and enormous tail lifted over a tilted, delighted face diving toward soft powder.',
              concept='A hunting pounce becomes joyful curiosity, with the face kept visible.',
              trait='Native search: diving into what cannot be seen from the surface.',
              expression='Bright open eyes, rosy cheeks and a happy open mouth.',
              cute_reason='YES: the tilted oversized head, tiny reaching paws and lifted tail read as playful clumsiness.',
              at_16px='A diagonal pale puff with a dark face and tail bump. The dive is lost; illustration-only at this scale.'),
 'flurry':dict(pose='Seated and comfortable while rounded wind strokes pass; soft cheek fur streams sideways.',
              concept='Bad conditions are outside the character; its relaxed gaze does not change.',
              trait='Unbreakable: the blizzard is ordinary weather for this animal.',
              expression='Calm, wide sparkling eyes, rosy cheeks and a small w smile.',
              cute_reason='YES: rounded windblown cheek lobes and a tail blanket keep the storm scene cuddly, not embattled.',
              at_16px='A big-eyed pale sitter with faint streaks; weather becomes noise. Use the underlying sitter for a tiny icon.'),
 'chime':dict(pose='Two small chibi foxes lean nose to nose, calling through small rounded arcs.',
              concept='Chirps: a tiny exchange between companions keeps the ecosystem connected.',
              trait='Ecosystem continuity: short calls connect the group across distance.',
              expression='Both have bright open eyes, blush and gentle open smiles.',
              cute_reason='YES: the affectionate pair and giant eyes give the strongest social, sticker-like moment.',
              at_16px='Two pale heads with dark eye specks. Calls and individual expressions disappear; not a small single-character icon.'),
 'pitter':dict(pose='A tiny walker with one lifted blob paw, a body-sized tail and round prints behind it.',
              concept='Trail: keep going, leaving a readable trace in the snow.',
              trait='Runs without support: the small animal keeps moving on its own; prints also carry the Trail record metaphor.',
              expression='A soft inquisitive gaze, blush and a small smile.',
              cute_reason='YES: the lifted mitten paw and oversize face give the walk a toddler-like rhythm.',
              at_16px='A pale face with a tail and one little foot. Prints disappear; the character survives better than the walking story.'),
}


def rgba(c,alpha=255):
    h=P[c].lstrip('#'); return tuple(bytes.fromhex(h))+(alpha,)


class Pen:
    def __init__(self):
        self.im=Image.new('RGBA',(640*S,640*S)); self.d=ImageDraw.Draw(self.im)
    def b(self,b): return tuple(round(v*S) for v in b)
    def e(self,b,c): self.d.ellipse(self.b(b),fill=P[c])
    def r(self,b,r,c):
        assert r>=.08*min(b[2]-b[0],b[3]-b[1])
        self.d.rounded_rectangle(self.b(b),radius=round(r*S),fill=P[c])
    def a(self,b,start,end,c,w=6):
        self.d.arc(self.b(b),start,end,fill=P[c],width=max(1,round(w*S)))
        # Round the arc endpoints, rather than leave square cut ends.
        cx=(b[0]+b[2])/2; cy=(b[1]+b[3])/2
        rx=(b[2]-b[0])/2-w/2; ry=(b[3]-b[1])/2-w/2
        for ang in (start,end):
            t=math.radians(ang); x=cx+rx*math.cos(t); y=cy+ry*math.sin(t)
            self.e((x-w/2,y-w/2,x+w/2,y+w/2),c)
    def tri(self,pts,r,c):
        """Convex triangle dilated by a radius: every vertex is a circle, not a point."""
        xs,ys=zip(*pts)
        assert r>=.08*min(max(xs)-min(xs),max(ys)-min(ys))
        self.d.polygon([(round(x*S),round(y*S)) for x,y in pts],fill=P[c])
        for i,(x,y) in enumerate(pts):
            a,b=pts[(i+1)%len(pts)]; length=math.hypot(a-x,b-y)
            nx=-(b-y)*r/length; ny=(a-x)*r/length
            self.d.polygon([(round(u*S),round(v*S)) for u,v in
                [(x+nx,y+ny),(a+nx,b+ny),(a-nx,b-ny),(x-nx,y-ny)]],fill=P[c])
            self.e((x-r,y-r,x+r,y+r),c)
    def blush(self,b,alpha=82):
        layer=Image.new('RGBA',self.im.size); d=ImageDraw.Draw(layer)
        d.ellipse(self.b(b),fill=rgba('rose',alpha)); self.im.alpha_composite(layer)
        self.d=ImageDraw.Draw(self.im)
    def blob(self,b,c='snow',border=7):
        self.e(b,'frost'); self.e((b[0]+border,b[1]+border,b[2]-border,b[3]-border),c)


def face(p,cx=320,top=220,k=1,mood='neutral',blush=True,wind=False,gaze=0):
    """Fresh face geometry: head width 336, height 220; eyes 68px (20.2%)."""
    def B(b): return (cx+b[0]*k,top+b[1]*k,cx+b[2]*k,top+b[3]*k)
    def E(b,c): p.e(B(b),c)
    def A(b,a,z,c='deep',w=5): p.a(B(b),a,z,c,w*k)
    def T(pts,r,c): p.tri([(cx+x*k,top+y*k) for x,y in pts],r*k,c)
    # Broad triangular ears with circularly rounded tips and soft inner triangles.
    for sign in (-1,1):
        T([(sign*127,-73),(sign*151,51),(sign*58,30)],12,'frost')
        T([(sign*125,-65),(sign*141,43),(sign*69,25)],9,'snow')
        T([(sign*123,-36),(sign*130,21),(sign*92,13)],7,'rose' if blush else 'frost')
    E((-160,0,160,220),'frost'); E((-168,82,168,223),'frost')
    E((-153,7,153,212),'snow'); E((-160,83,160,215),'snow')
    if wind:
        E((105,95,190,137),'frost'); E((111,94,191,129),'snow')
        E((113,141,183,177),'frost'); E((117,140,183,169),'snow')
    # Rounded muzzle depth 65 / 336 = 19.3% head width, no wedge.
    E((-59+gaze,153,59+gaze,215),'frost'); E((-57+gaze,150,57+gaze,209),'snow')
    if blush:
        p.blush(B((-143,159,-91,185))); p.blush(B((91,159,143,185)))
    for x in (-55+gaze,55+gaze):
        if mood=='happy':
            # Smooth ^ ^ gestures: upper semicircles, with rounded ends.
            A((x-31,118,x+31,168),190,350,'night',8)
        elif mood=='sleeping':
            A((x-31,114,x+31,151),10,170,'night',7)
        else:
            y=137
            if mood=='sleepy':
                E((x-34,y-6,x+34,y+29),'night')
                E((x-19,y-2,x-2,y+15),'snow')
                E((x+15,y+16,x+23,y+24),'snow')
            else:
                E((x-34,y-38,x+34,y+38),'night')
                E((x-22,y-26,x-5,y-9),'snow')  # 17px = 25% eye diameter.
                E((x+13,y+14,x+22,y+23),'snow')
    E((-11+gaze,173,11+gaze,188),'rose')
    if mood=='surprised':
        E((-12+gaze,194,12+gaze,219),'deep'); E((-5+gaze,198,5+gaze,204),'rose')
    elif mood=='delighted':
        E((-21+gaze,192,21+gaze,221),'deep'); E((-13+gaze,208,13+gaze,220),'rose')
    else:
        A((-23+gaze,182,gaze,207),3,130,'deep',4)
        A((gaze,182,23+gaze,207),50,177,'deep',4)


def sitter(mood='neutral',wind=False,gaze=0):
    p=Pen()
    # Head height 220; total character from ear y135 to toe y574 = 439.
    p.blob((327,344,568,561))  # body-sized rear tail
    p.e((421,365,558,511),'snow')
    p.blob((218,373,425,564))
    p.e((251,418,389,559),'snow')
    p.blob((204,483,281,567)); p.blob((358,483,435,567))
    face(p,320,220,1,mood,wind=wind,gaze=gaze)
    p.blob((137,489,530,574),border=6)  # tail curls over both feet
    p.e((147,494,300,566),'snow')
    p.a((269,507,500,564),6,119,'frost',5)
    return p.im


def pawprint(p,x,y,k=1):
    p.e((x-12*k,y-6*k,x+12*k,y+12*k),'blue-light')
    for dx,dy in [(-13,-14),(0,-20),(13,-14)]:
        p.e((x+(dx-5)*k,y+(dy-5)*k,x+(dx+5)*k,y+(dy+5)*k),'blue-light')


def master(name):
    if name=='mochi': return sitter()
    if name=='flurry':
        p=Pen()
        for b in [(62,179,568,259),(38,277,595,354),(61,398,587,466)]:
            p.a(b,210,318,'aurora',7)
        p.im.alpha_composite(sitter(wind=True)); return p.im
    p=Pen()
    if name=='pillow':
        p.blob((101,273,355,504)); p.blob((352,217,573,461))
        p.e((427,235,559,373),'snow')
        for y in (508,549):
            p.r((112,y,528,y+33),15,'blue-light'); p.r((124,y+5,516,y+13),4,'ice')
        face(p,315,279,.95)
        p.blob((178,472,279,541)); p.blob((353,472,454,541))
    elif name=='doze':
        p.blob((97,253,560,563)); p.e((375,287,538,470),'snow')
        face(p,295,268,.92,'sleeping')
        p.blob((97,450,556,566)); p.e((108,457,344,556),'snow')
        p.a((260,472,525,551),2,113,'frost',6)
        for i in range(3): p.a((429+i*25,190-i*31,461+i*25,211-i*31),196,341,'ice',5)
    elif name=='peek':
        p.blob((365,303,564,562)); p.e((455,326,551,476),'snow')
        face(p,305,229,1.06)
        p.r((87,453,555,562),48,'frost'); p.r((89,449,550,546),46,'snow')
        p.blob((159,434,248,503)); p.blob((367,434,456,503))
        p.e((113,496,201,524),'frost'); p.e((450,509,518,530),'frost')
    elif name=='tumble':
        p.blob((284,134,474,374)); p.blob((388,91,571,343))
        p.e((448,104,560,250),'snow')
        q=Pen(); face(q,298,300,.92,'delighted')
        p.im.alpha_composite(q.im.rotate(18,Image.Resampling.BICUBIC,center=(298*S,410*S)))
        p.blob((179,456,261,535)); p.blob((325,471,409,550))
        for b in [(111,540,489,581),(91,512,160,554),(481,497,549,544)]: p.e(b,'frost')
        p.e((122,535,478,573),'snow')
        for x,y in [(104,465),(531,449),(481,569)]: p.e((x-10,y-10,x+10,y+10),'aurora')
    elif name=='chime':
        # Independent, fresh chibi sitters; each remains two-heads-tall.
        left=sitter('delighted',gaze=-24).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        left=left.resize((376*S,376*S),Image.Resampling.LANCZOS)
        right=left.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        left=left.rotate(-16,Image.Resampling.BICUBIC)
        right=right.rotate(16,Image.Resampling.BICUBIC)
        p.im.alpha_composite(left,(7*S,165*S)); p.im.alpha_composite(right,(257*S,165*S))
        for b in [(287,228,310,253),(322,218,350,252)]: p.a(b,210,326,'ice',5)
    elif name=='pitter':
        for x,y,k in [(482,544,.95),(536,498,.82),(555,439,.7)]: pawprint(p,x,y,k)
        p.blob((343,332,560,519)); p.e((435,344,551,468),'snow')
        p.blob((226,385,420,548))
        p.blob((231,502,311,565)); p.blob((353,471,428,536))
        face(p,296,217,.92)
        p.blob((180,419,249,494)); p.blob((358,422,419,495))
    else: raise ValueError(name)
    return p.im


def font(size):
    for path in ['/System/Library/Fonts/Supplemental/Arial.ttf','/System/Library/Fonts/Helvetica.ttc','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if Path(path).is_file():
            FONTS['catalog']={'path':path}; return ImageFont.truetype(path,size)
    FONTS['catalog']={'path':'Pillow default'}; return ImageFont.load_default(size=size)


def label(im,xy,value,size=22,c='frost'):
    d=ImageDraw.Draw(im); f=font(size); b=d.textbbox((0,0),value,font=f)
    d.text((xy[0]-b[0],xy[1]-b[1]),value,font=f,fill=P[c])


def validate(book,tiles,masters):
    assert book.size==CANVAS and book.mode=='RGBA'
    for i,t in enumerate(tiles):
        x,y,r,b=t['bbox']; assert 0<=x<r<=book.width and 0<=y<b<=book.height
        for u in tiles[i+1:]:
            a,c,e,f=u['bbox']; assert max(a-r,x-e,c-b,y-f)>=48,(t['name'],u['name'])
        crop=book.crop(t['bbox']); alpha=crop.getchannel('A')
        assert alpha.getextrema()==(0,255)
        assert all(alpha.getpixel(pt)==0 for pt in [(0,0),(crop.width-1,0),(0,crop.height-1),(crop.width-1,crop.height-1)])
        if t['name'].endswith('-sizes'):
            n=t['name'].split('-')[1]
            for sample in t['samples']:
                size=sample['size']; e=Image.new('RGBA',(size,size))
                e.alpha_composite(masters[n].resize((size,size),Image.Resampling.LANCZOS))
                assert crop.crop(sample['bbox']).tobytes()==e.tobytes()
        if t['name'].endswith('-thumb'):
            assert crop.tobytes()==masters[t['name'].split('-')[1]].resize((192,192),Image.Resampling.LANCZOS).tobytes()


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    masters={n:master(n) for n in NAMES}
    book=Image.new('RGBA',CANVAS,P['night']); tiles=[]
    label(book,(64,39),'ALOPEX / LITTLE FOX, BIG WORLD',44,'snow')
    label(book,(64,112),'Cuteness first. Fresh geometry. One soft companion, eight ways to feel at home.',27)
    label(book,(64,166),'Heroes 640px | actual 96 / 64 / 32 / 16px proofs | 192px thumbnail = the deciding view',23)
    def add(name,x,y,im,**extra):
        w,h=im.size; t=dict(name=name,x=x,y=y,w=w,h=h,bbox=[x,y,x+w,y+h],background='transparent',**extra)
        tiles.append(t); label(book,(x,y-34),f'{name} / {w} x {h}',21)
        book.paste(im,(x,y))
    for i,n in enumerate(NAMES):
        x=64+(i%2)*1472; y=272+(i//2)*816; m=masters[n]
        add(f'cute-{n}-hero',x,y,m.resize((640,640),Image.Resampling.LANCZOS))
        proof=Image.new('RGBA',(512,128)); samples=[]
        for cx,size in zip((64,192,320,448),(96,64,32,16)):
            px=cx-size//2; py=(128-size)//2
            proof.alpha_composite(m.resize((size,size),Image.Resampling.LANCZOS),(px,py))
            samples.append(dict(size=size,bbox=[px,py,px+size,py+size]))
        add(f'cute-{n}-sizes',x+688,y,proof,samples=samples)
        for cx,size in zip((64,192,320,448),(96,64,32,16)): label(book,(x+688+cx-20,y+143),f'{size}px',18)
        add(f'cute-{n}-thumb',x+688,y+240,m.resize((192,192),Image.Resampling.LANCZOS))
        label(book,(x+688,y+470),'192px judgement: YES',24,'snow')
        for j,line in enumerate({
            'mochi':['Tail blanket. Looking right at you.','Two heads tall; no heroic stance.'],
            'pillow':['Chin down. Paws forward.','The store becomes a comfy pillow.'],
            'doze':['Sleepy eyelids, warm cheeks.','A tail big enough to be a duvet.'],
            'peek':['Huge eyes, tiny gripping paws.','Still here, even under the snow.'],
            'tumble':['Rear up, delighted face visible.','Search as a playful snow dive.'],
            'flurry':['Weather moves. Comfort stays.','Windblown cheeks stay soft.'],
            'chime':['A tiny call between companions.','Chirps keeps the group connected.'],
            'pitter':['One mitten paw in mid-step.','Round tracks make a little Trail.'],
        }[n]): label(book,(x+688,y+521+j*39),line,21)
    exp=Image.new('RGBA',(1536,384)); moods=('neutral','happy','sleepy','surprised')
    expressions=[]
    for i,mood in enumerate(moods):
        im=sitter(mood).resize((384,384),Image.Resampling.LANCZOS)
        exp.alpha_composite(im,(i*384,0))
        expressions.append(dict(expression=mood,bbox=[i*384,0,(i+1)*384,384]))
    add('cute-expressions',64,3632,exp,character='mochi',expressions=expressions)
    for i,mood in enumerate(moods): label(book,(64+i*384+125,4040),mood,23,'snow')
    label(book,(1744,3654),'THE EVERYDAY FOX',30,'snow')
    for j,line in enumerate(['Mochi is the lead character candidate.','Its face stays alive at thumbnail size.','Four moods share the same anatomy.','Closed eyelids replace open eyes only','for the happy and sleeping expressions.','At 16px, story detail still disappears.','This is a character layer, not a forced','replacement for the shipped mark.']):
        label(book,(1744,3715+j*41),line,24)
    label(book,(64,4180),'Exploration only / prior sheets and shipped identity untouched / no production export',23)
    ratios=dict(head_width=336,head_height=220,total_height=439,total_height_to_head_height=round(439/220,3),
        eye_diameter=68,eye_diameter_to_head_width=68/336,eye_center_y_from_head_top=137,
        head_horizontal_midline=110,eye_pair_outer_span=178,eye_pair_span_to_head_width=178/336,
        catchlight_diameter=17,catchlight_to_eye_diameter=.25,nose_width=22,nose_to_eye_diameter=22/68,
        muzzle_depth=65,muzzle_depth_to_head_width=65/336,ear_height_above_head=85,
        ear_height_to_head_height=85/220,minimum_polygon_corner_radius_ratio=.08,
        base_body_bbox=[218,373,425,564],base_tail_bbox=[327,344,568,561],front_tail_bbox=[137,489,530,574])
    assert ratios['eye_diameter_to_head_width']>=.18
    assert ratios['eye_center_y_from_head_top']>ratios['head_horizontal_midline']
    assert ratios['muzzle_depth_to_head_width']<=.20
    assert .35<=ratios['ear_height_to_head_height']<=.50
    assert abs(ratios['total_height_to_head_height']-2)<.05
    manifest=dict(canvas=dict(width=CANVAS[0],height=CANVAS[1],mode='RGBA'),
        bbox_convention='Half-open [x,y,x+w,y+h]. Exact artwork crops; labels only in gutters. Minimum gap 48px.',
        status='Cute redo. Cuteness governs. Earlier geometry is not imported, traced or reused.',
        prior_sheet_diagnosis=['Long profile muzzles, small high eyes and pointed tails made the guardian sheet read as adult diagrams.',
                               'Angular surfaces overpowered expression. This redo uses chibi anatomy, soft cheeks, large low eyes and rounded tails.'],
        palette=P,warm_accent=dict(name='rose',hex=P['rose'],uses=['nose','blush','inner ears','tiny mouth interior'],
            blush_opacity=82,reason='One soft rose hue makes the nose and cheeks feel warm against snow without changing the pale coat.'),
        geometry_rules=ratios,
        geometry_notes=['Measurements are local construction coordinates, before pose transforms; head height measures the face mass excluding protruding ears.',
            'Sitter total height is approximately twice its face height; crouched, curled and peeking poses compress visible height further.',
            'Body and tail use ellipse blobs; paws have no joints. Tail area exceeds the body area.',
            'Rounded triangles are built by dilating a convex triangle with circular caps. Every vertex receives >=8% radius; no sharp polygon tip is left exposed.',
            'Open eyes always have a solid night ellipse and a 25% upper-left snow catchlight, plus a smaller lower-right catchlight.',
            'Closed eyes in sleeping and happy expressions use curved eyelids instead of an iris; these intentional expression exceptions have no catchlight.',
            'The sleepy expression keeps open oval eyes and both catchlights. All direction faces except Doze have open eyes.',
            'Blush is on all eight directions; the single warm hue is alpha-composited over the opaque cheek, not baked into a rectangular matte.'],
        rendering='Pillow only; 2560px RGBA masters. LANCZOS for every final size. Pose rotations use Pillow BICUBIC at master resolution. No hand-tuned tiny variants.',
        directions=[dict(name=n,**DETAILS[n],blush=True,cuteness_review=dict(size_px=192,is_cute=True,reason=DETAILS[n]['cute_reason']),
                         construction_metrics='Shared face measurements in geometry_rules; uniform per-pose scaling preserves these ratios.') for n in NAMES],
        expressions=dict(character='mochi',order=list(moods),same_body_and_ears=True,
            only_changes='Eyelid/eye shape and mouth; catchlights remain on every open eye.'),
        recommendation=dict(cuteness_ranking=['mochi','chime','pillow','peek','doze','tumble','pitter','flurry'],
            owner_shortlist=['mochi','chime','pillow','flurry'],
            reasons={'mochi':'Strongest single companion: eye contact, round face and tail blanket; versatile expression system.',
                     'chime':'Most affectionate interaction; a natural Chirps character story.',
                     'pillow':'Chin on paws gives the clearest cozy database scene.',
                     'peek':'A simple face-and-paws sticker that remains inviting at small scales.',
                     'doze':'Cozy sleeping bundle; expression is deliberately quiet and weak at 16px.',
                     'tumble':'Playful and energetic; pose needs thumbnail space to read.',
                     'pitter':'Sweet lifted-paw walk, but the Trail prints need more pixels.',
                     'flurry':'The base character is cute; wind adds noise. Shortlisted for the survival message rather than novelty.'},
            discard=[],tiny_icon_limit='Doze, Tumble and Chime lose their stories at 16px; none is approved as a final favicon.'),
        fonts=FONTS,tiles=tiles)
    validate(book,tiles,masters)
    book.save(OUT/'cute-book.png')
    (OUT/'cute-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with Image.open(OUT/'cute-book.png') as check:
        check.load(); validate(check,tiles,masters)
        assert check.size==(manifest['canvas']['width'],manifest['canvas']['height'])
    print(f'Verified {len(tiles)} tiles, {CANVAS[0]} x {CANVAS[1]} RGBA, 48px gutters, 32 native samples, eight exact thumbnails.')


if __name__=='__main__': main()
