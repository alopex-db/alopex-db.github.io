#!/usr/bin/env python3
"""Pillow-only species correction. Writes only fox-book.png and fox-manifest.json.

Run: python3 scripts/render_fox_exploration.py
All imagery is 4x supersampled; every proof derives from unchanged master art.
"""
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/brand/explore'
CANVAS=(2944,4960)
S=4
P={'deep':'#1E3A5F','blue-light':'#2E5077','blue-dark':'#152C4A',
   'ice':'#5FB4C9','aurora':'#7EC8E3','frost':'#B8D4E3',
   'silver':'#C0C5CE','snow':'#F8FAFC','night':'#0B1929'}
NAMES=('muff','rime','cache','gale','listen','pounce','boreal','chirps')
FONTS={}
DETAILS={
 'muff':dict(idea='Tail over nose, eyes closed, comfortable asleep while snow settles on the fur.',
             principle='Unbreakable: a snow-covered sleeper remains comfortable without a shelter.',
             extreme_scene=True,wrapping=True,
             cute='YES: tucked cheeks, soft sleeping eyelids and a tail duvet keep the pose cozy.',
             fox='YES: short outward ears, a rough fur ruff and an immense lobed tail folded over the muzzle carry the winter-fox reading.',
             tiny='16px: ear nubs and a huge curled tail remain; the sleepy face is lost. Not a self-explanatory species icon.'),
 'rime':dict(idea='Snow piles on the head and short ears; the big-eyed fox remains perfectly composed.',
             principle='Unbreakable: accumulating snow changes the scene, not the fox posture or comfort.',
             extreme_scene=True,wrapping=True,
             cute='YES: low sparkling eyes beneath a snow hat and small cool cheeks make an unbothered little companion.',
             fox='YES: low side ears and the outsize scalloped tail wrapping a tiny body dominate over the round face.',
             tiny='16px: a fluffy face above a broad tail; snow cap merges with the white coat. Eyes remain, story is weak.'),
 'cache':dict(idea='A continuous tail curl encloses a small group of slabs; chin and paws rest on the upper layers.',
              principle='Silent + Adaptive: at home on the stored data, enclosed by its own winter tail.',
              extreme_scene=False,wrapping=True,
              cute='YES: big eyes over the chin-on-paws gesture and an enormous fluffy wrap make the store look like a nest.',
              fox='YES: a low-eared ruff above a thick, furred tail crescent; exposed muzzle bridge and tiny paws avoid a kitten posture.',
              tiny='16px: a wide-eyed fox nest with a blue centre; separate slabs disappear. Keep this as a character composition.'),
 'gale':dict(idea='Rounded fur streams sideways in a whiteout; the fox sits still inside its tail.',
             principle='Silent + Unbreakable: wind moves, the serene character does not brace or fight it.',
             extreme_scene=True,wrapping=True,
             cute='YES: huge calm eyes and tucked paws stay inviting while soft cheek tufts blow sideways.',
             fox='YES: the sideways ruff and a full-body-scale lobed tail, with short outward ears, read as winter fox fur rather than a smooth cat outline.',
             tiny='16px: a broad fluffy sitter; wind strokes become specks. The face remains clearer than the weather.'),
 'listen':dict(idea='Ears attend to something beneath the snow; a tilted face and tiny paws look down quietly.',
               principle='Silent + native search: composed attention reaches below the visible surface.',
               extreme_scene=False,wrapping=False,
               cute='YES: a tilted baby face and two little paws give the listening gesture a curious, gentle quality.',
               fox='YES: a thick descending tail with irregular fur lobes outweighs the body, behind short side ears and a cheek ruff.',
               tiny='16px: a tilted dark-eyed head joined to a very large plume; the listening action is lost.'),
 'pounce':dict(idea='A delighted snow dive, nose entering powder first; rear and enormous furred tail remain lifted.',
               principle='Native search: the fox enters the hidden layer; calm curiosity rather than a fierce attack.',
               extreme_scene=False,wrapping=False,
               cute='YES: the oversized tilted face, stubby reaching paws and soft tail turn the dive into a playful tumble.',
               fox='YES: the very thick, lobed tail rises above the tiny rump, paired with a short-eared fur ruff; it is a snow-pouncing fox silhouette.',
               tiny='16px: diagonal face, lifted tail and powder merge into a pale cluster. Pose requires 96px or more.'),
 'boreal':dict(idea='A small fox stands calmly on a snowy shelf under polar-night aurora ribbons.',
               principle='Adaptive + Unbreakable: darkness and ice are simply another scene for the same companion.',
               extreme_scene=True,wrapping=False,
               cute='YES: a small wide-eyed face and mitten paws remain warm in character despite the cool night scene.',
               fox='YES: the character has short side-set ears, a cheek ruff and a tail at least as large as the head and body combined; aurora stays separate.',
               tiny='16px: aurora becomes a faint mark above a fluffy sitter. The character stays visible, but night is not legible without context.'),
 'chirps':dict(idea='Two low-eared, enormous-tailed foxes lean toward each other, exchanging small call arcs.',
               principle='Silent + ecosystem continuity: quiet local calls keep the group connected; no shouting or speech bubbles.',
               extreme_scene=False,wrapping=False,
               cute='YES: shared eye contact, small dark noses and two fluffy tail blankets make a tender pair.',
               fox='YES: each little face belongs to a disproportionately large furred tail, with short wide ears and an irregular ruff; neither has a smooth kitten tail.',
               tiny='16px: a pair of tiny pale curls; faces and calls no longer separate reliably. This is a larger Chirps illustration.'),
}


class Pen:
    def __init__(self):
        self.im=Image.new('RGBA',(640*S,640*S)); self.d=ImageDraw.Draw(self.im)
    def b(self,b): return tuple(round(v*S) for v in b)
    def e(self,b,c): self.d.ellipse(self.b(b),fill=P[c])
    def r(self,b,r,c):
        assert r>=.08*min(b[2]-b[0],b[3]-b[1])
        self.d.rounded_rectangle(self.b(b),radius=round(r*S),fill=P[c])
    def a(self,b,start,end,c,w=5):
        self.d.arc(self.b(b),start,end,fill=P[c],width=max(1,round(w*S)))
        cx=(b[0]+b[2])/2; cy=(b[1]+b[3])/2
        for ang in (start,end):
            t=math.radians(ang); x=cx+((b[2]-b[0])/2-w/2)*math.cos(t); y=cy+((b[3]-b[1])/2-w/2)*math.sin(t)
            self.e((x-w/2,y-w/2,x+w/2,y+w/2),c)
    def tri(self,pts,r,c):
        xs,ys=zip(*pts); assert r>=.08*min(max(xs)-min(xs),max(ys)-min(ys))
        self.d.polygon([(round(x*S),round(y*S)) for x,y in pts],fill=P[c])
        for i,(x,y) in enumerate(pts):
            a,b=pts[(i+1)%len(pts)]; length=math.hypot(a-x,b-y)
            nx=-(b-y)*r/length; ny=(a-x)*r/length
            self.d.polygon([(round(u*S),round(v*S)) for u,v in [(x+nx,y+ny),(a+nx,b+ny),(a-nx,b-ny),(x-nx,y-ny)]],fill=P[c])
            self.e((x-r,y-r,x+r,y+r),c)
    def blob(self,b,c='snow',edge=6):
        self.e(b,'frost'); self.e((b[0]+edge,b[1]+edge,b[2]-edge,b[3]-edge),c)
    def blush(self,b):
        layer=Image.new('RGBA',self.im.size); d=ImageDraw.Draw(layer)
        d.ellipse(self.b(b),fill=tuple(bytes.fromhex(P['ice'][1:]))+(75,))
        self.im.alpha_composite(layer); self.d=ImageDraw.Draw(self.im)
    def composite(self,im,xy=(0,0)):
        self.im.alpha_composite(im,(round(xy[0]*S),round(xy[1]*S))); self.d=ImageDraw.Draw(self.im)


def fur_mask(b,depth=12):
    """A continuous plume with shallow, irregular rounded fur lobes, no sharp flick."""
    x,y,r,z=b; w=r-x; h=z-y
    mask=Image.new('L',(640*S,640*S)); d=ImageDraw.Draw(mask)
    d.ellipse(tuple(round(v*S) for v in b),fill=255)
    for i in range(22):
        t=2*math.pi*i/22; q=depth*(.78+(i%4)*.11)
        # Lobes overlap the main oval; no disconnected fur specks.
        px=(x+r)/2+(w/2-q*.58)*math.cos(t)
        py=(y+z)/2+(h/2-q*.58)*math.sin(t)
        rx=q*1.55; ry=q
        d.ellipse(tuple(round(v*S) for v in (px-rx,py-ry,px+rx,py+ry)),fill=255)
    return mask


def plume(p,b,depth=13,tip='right',notch=False):
    mask=fur_mask(b,depth)
    if notch:
        ImageDraw.Draw(mask).ellipse(tuple(round(v*S) for v in (80,110,446,440)),fill=0)
    fill=Image.new('RGBA',p.im.size,P['frost']); fill.putalpha(mask)
    p.composite(fill)
    # A blue-grey underside shapes volume; a broad snow tip stays in the mask.
    x,y,r,z=b; w=r-x; h=z-y
    light=Image.new('RGBA',p.im.size); d=ImageDraw.Draw(light)
    d.ellipse(p.b((x+w*.05,y+h*.04,r-w*.05,z-h*.17)),fill=P['snow'])
    if tip=='left': box=(x-w*.08,y+h*.14,x+w*.49,z-h*.10)
    else: box=(x+w*.49,y-h*.05,r+w*.06,z-h*.09)
    d.ellipse(p.b(box),fill=P['snow'])
    # Clip ALL highlights to the fur outline.
    a=light.getchannel('A'); a=Image.composite(a,Image.new('L',a.size),mask); light.putalpha(a)
    p.composite(light)
    return mask


def face(p,cx=260,top=210,k=1,mood='neutral',gaze=0,wind=False):
    """Chibi face width 340, height 220; 68px eyes remain 20% wide."""
    def B(b): return (cx+b[0]*k,top+b[1]*k,cx+b[2]*k,top+b[3]*k)
    def E(b,c): p.e(B(b),c)
    def T(pts,r,c): p.tri([(cx+x*k,top+y*k) for x,y in pts],r*k,c)
    def A(b,a,z,w=5): p.a(B(b),a,z,'deep',w*k)
    # Short, broad, side-set winter ears. No pink, no tall upright spikes.
    for sign in (-1,1):
        T([(sign*158,-25),(sign*178,50),(sign*77,37)],16,'blue-light')
        T([(sign*154,-19),(sign*166,43),(sign*89,34)],12,'snow')
        T([(sign*149,2),(sign*152,29),(sign*115,28)],9,'ice')
    E((-151,0,151,219),'frost')
    # Irregular side ruff: all lobes overlap the rounded skull.
    lobes=[(-165,84,-93,142),(-174,118,-94,177),(-159,151,-82,211),
           (91,82,165,143),(96,116,174,179),(80,151,156,210)]
    for b in lobes: E(b,'frost')
    E((-144,7,144,212),'snow')
    for x,y,r,z in lobes: E((x+5,y+4,r-5,z-6),'snow')
    if wind:
        for b in [(117,90,202,126),(119,128,198,163),(107,162,184,192)]: E(b,'snow')
    # A visible forehead-to-nose bridge replaces the flat cat muzzle.
    E((-27+gaze,88,33+gaze,189),'frost')
    E((-22+gaze,85,28+gaze,183),'snow')
    E((-50+gaze,158,57+gaze,215),'frost')
    E((-46+gaze,154,53+gaze,210),'snow')
    for x in (-55+gaze,55+gaze):
        if mood=='sleeping': A((x-31,111,x+31,150),9,171,7)
        else:
            E((x-34,99,x+34,175),'night')
            E((x-22,111,x-5,128),'snow')
            E((x+13,151,x+22,160),'snow')
    p.blush(B((-131,167,-94,182))); p.blush(B((94,167,131,182)))
    E((-11+gaze,174,11+gaze,190),'night')
    A((-17+gaze,184,18+gaze,207),14,166,4)


def wrapped(mood='neutral',nose_cover=False,wind=False,gaze=0):
    p=Pen()
    # Two heads tall before tail enclosure; paws are joint-free blobs.
    p.blob((206,347,368,558)); p.blob((198,493,264,564)); p.blob((322,491,385,563))
    # Rear plume larger than the whole baby animal, not just the torso.
    plume(p,(300,165,606,568),17,notch=True)
    face(p,225,208,1,mood,gaze,wind)
    # The front tail is the return sweep of that same plume, not a second tail.
    if nose_cover:
        plume(p,(73,373,552,579),17,'left')
        plume(p,(68,359,241,497),12,'left')
    else:
        plume(p,(65,418,567,588),17,'left')
    # One curved fur fold shows the return sweep without sharp vertices.
    p.a((224,477,534,565),8,118,'ice',5)
    return p.im


def environment(name):
    p=Pen()
    if name=='gale':
        for b in [(25,134,603,218),(32,245,614,331),(22,375,609,463)]: p.a(b,205,327,'aurora',7)
        for i,(x,y) in enumerate([(46,215),(571,179),(597,346),(41,462),(562,526)]):
            p.r((x,y,x+22,y+6),3,'frost')
    elif name=='boreal':
        for b,w,c in [((49,35,596,215),18,'ice'),((68,45,562,197),10,'aurora'),((98,63,527,182),7,'frost')]: p.a(b,185,343,c,w)
        for x,y in [(79,173),(553,206),(113,230),(491,114)]: p.e((x-4,y-4,x+4,y+4),'frost')
        p.blob((75,541,585,584),'frost')
    return p.im


def master(name):
    p=Pen()
    if name in ('muff','rime','gale'):
        p.composite(environment(name))
        p.composite(wrapped('sleeping' if name=='muff' else 'neutral',name=='muff',name=='gale'))
        if name=='muff':
            for b in [(371,280,497,319),(433,252,522,294),(158,519,259,542)]: p.e(b,'snow')
        if name=='rime':
            for b in [(80,173,159,207),(103,181,302,228),(268,178,371,217),(438,281,554,321)]:
                p.e(b,'frost'); p.e((b[0],b[1]-5,b[2],b[3]-6),'snow')
    elif name=='cache':
        # Tail forms a full C around the store: back, bottom and front lip.
        plume(p,(300,165,606,568),17,notch=True)
        p.blob((170,338,350,548))
        face(p,225,193,.97)
        for y,w in [(397,214),(431,239),(465,207)]:
            p.r((217,y,217+w,y+27),12,'blue-light'); p.r((225,y+5,209+w,y+11),3,'ice')
        p.blob((171,386,244,436)); p.blob((349,386,419,436))
        plume(p,(65,474,563,589),16,'left')
        plume(p,(66,387,202,548),11,'left')
    elif name=='listen':
        plume(p,(300,149,606,563),18,notch=True)
        p.blob((181,353,360,551))
        q=Pen(); face(q,225,238,.94)
        p.composite(q.im.rotate(12,Image.Resampling.BICUBIC,center=(225*S,358*S)))
        p.blob((146,455,228,521)); p.blob((295,461,376,527))
        plume(p,(73,485,563,590),16,'left')
        p.e((74,559,522,590),'frost'); p.e((82,558,518,580),'snow')
        for b in [(133,526,208,545),(304,532,377,552)]: p.a(b,5,173,'ice',4)
    elif name=='pounce':
        plume(p,(241,66,586,418),19)
        p.blob((248,217,412,430))
        q=Pen(); face(q,241,329,.87)
        p.composite(q.im.rotate(22,Image.Resampling.BICUBIC,center=(241*S,440*S)))
        p.blob((109,478,181,537)); p.blob((300,485,373,545))
        p.e((70,534,524,589),'frost'); p.e((80,529,519,577),'snow')
        for b in [(64,489,108,524),(501,478,549,518)]: p.e(b,'frost')
    elif name=='boreal':
        p.composite(environment(name))
        # Uniform scene placement only: no stretch/grow/shrink character trait.
        im=wrapped().resize((528*S,528*S),Image.Resampling.LANCZOS)
        p.composite(im,(51,78))
    elif name=='chirps':
        # Both keep the same infant anatomy, with tails placed outside the pair.
        a=wrapped(gaze=-48).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        a=a.resize((368*S,368*S),Image.Resampling.LANCZOS)
        b=a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        p.composite(a.rotate(-9,Image.Resampling.BICUBIC),(-17,155))
        p.composite(b.rotate(9,Image.Resampling.BICUBIC),(285,155))
        for b in [(285,261,307,282),(324,250,347,277)]: p.a(b,209,334,'ice',4)
    else: raise ValueError(name)
    return p.im


def flat(im,size):
    a=im.getchannel('A').resize(size,Image.Resampling.LANCZOS)
    solid=Image.new('RGBA',size,P['snow']); solid.putalpha(a)
    out=Image.new('RGBA',size); out.alpha_composite(solid)
    return out


def alpha_area(im): return sum(i*v/255 for i,v in enumerate(im.getchannel('A').histogram()))


def font(size):
    for path in ['/System/Library/Fonts/Supplemental/Arial.ttf','/System/Library/Fonts/Helvetica.ttc','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if Path(path).is_file():
            FONTS['catalog']=path; return ImageFont.truetype(path,size)
    return ImageFont.load_default(size=size)


def label(im,xy,value,size=22,c='frost'):
    d=ImageDraw.Draw(im); f=font(size); b=d.textbbox((0,0),value,font=f)
    d.text((xy[0]-b[0],xy[1]-b[1]),value,font=f,fill=P[c])


def validate(book,tiles,masters):
    assert book.mode=='RGBA' and book.size==CANVAS
    for i,t in enumerate(tiles):
        x,y,r,b=t['bbox']; assert 0<=x<r<=book.width and 0<=y<b<=book.height
        for u in tiles[i+1:]:
            a,c,e,f=u['bbox']; assert max(a-r,x-e,c-b,y-f)>=48,(t['name'],u['name'])
        crop=book.crop(t['bbox']); alpha=crop.getchannel('A')
        if t['background']=='transparent':
            assert alpha.getextrema()==(0,255)
            assert all(alpha.getpixel(pt)==0 for pt in [(0,0),(crop.width-1,0),(0,crop.height-1),(crop.width-1,crop.height-1)])
        else: assert alpha.getextrema()==(255,255)
        if t['name']=='fox-species-check':
            snow=tuple(bytes.fromhex(P['snow'][1:]))
            assert all(pixel[:3]==snow for count,pixel in crop.getcolors(crop.width*crop.height) if pixel[3])
        if t['name'].endswith('-sizes'):
            for sample in t['samples']:
                size=sample['size']; expected=Image.new('RGBA',(size,size))
                expected.alpha_composite(masters[t['name'].split('-')[1]].resize((size,size),Image.Resampling.LANCZOS))
                assert crop.crop(sample['bbox']).tobytes()==expected.tobytes()
        if t['name'].endswith('-thumb'):
            assert crop.tobytes()==masters[t['name'].split('-')[1]].resize((192,192),Image.Resampling.LANCZOS).tobytes()


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    masters={n:master(n) for n in NAMES}
    book=Image.new('RGBA',CANVAS,P['night']); tiles=[]
    label(book,(64,39),'ALOPEX / THE TAIL TELLS YOU',44,'snow')
    label(book,(64,109),'Silent. Adaptive. Unbreakable. / Same little fox, whatever the scene.',28)
    label(book,(64,165),'Short side ears / ice inner ears / cheek ruff / enormous furred tail / no pink',23)
    def add(name,x,y,im,bg='transparent',**extra):
        w,h=im.size; t=dict(name=name,x=x,y=y,w=w,h=h,bbox=[x,y,x+w,y+h],background=bg,**extra)
        tiles.append(t); label(book,(x,y-34),f'{name} / {w} x {h}',21)
        book.paste(im,(x,y))
    for i,n in enumerate(NAMES):
        x=64+i%2*1472; y=272+i//2*816; m=masters[n]
        add(f'fox-{n}-hero',x,y,m.resize((640,640),Image.Resampling.LANCZOS))
        proof=Image.new('RGBA',(512,128)); samples=[]
        for cx,size in zip((64,192,320,448),(96,64,32,16)):
            px=cx-size//2; py=(128-size)//2
            proof.alpha_composite(m.resize((size,size),Image.Resampling.LANCZOS),(px,py))
            samples.append(dict(size=size,bbox=[px,py,px+size,py+size]))
        add(f'fox-{n}-sizes',x+688,y,proof,samples=samples)
        for cx,size in zip((64,192,320,448),(96,64,32,16)): label(book,(x+688+cx-20,y+143),f'{size}px',18)
        add(f'fox-{n}-thumb',x+688,y+240,m.resize((192,192),Image.Resampling.LANCZOS))
        label(book,(x+688,y+471),'CUTE: YES / FOX SILHOUETTE: YES',20,'snow')
        for j,line in enumerate({
            'muff':['Snow outside. Tail over the nose.','A winter fox asleep in its own fur.'],
            'rime':['Snow piles up. The fox stays fine.','Low ears; a big tail blanket.'],
            'cache':['Chin on the store. Tail around it.','Data enclosed, never placed beside.'],
            'gale':['The fur moves. The fox is still.','A calm face inside a whiteout.'],
            'listen':['Big ears listen below the surface.','Small paws; no predator stance.'],
            'pounce':['A soft nose-first snow dive.','The tail is bigger than the animal.'],
            'boreal':['Polar night is another ordinary scene.','Aurora above; the same calm fox.'],
            'chirps':['Small calls between two companions.','Two huge tails; no speech bubbles.'],
        }[n]): label(book,(x+688,y+523+j*39),line,21)
    # Full-art optical area normalization, including environmental marks.
    row=Image.new('RGBA',(2560,640),P['deep']); entries=[]
    crops={n:masters[n].crop(masters[n].getbbox()) for n in NAMES}
    # Choose one common visible area that also fits all scenes in 288px cells.
    target=min(28000,min(alpha_area(c)*min(288/c.width,530/c.height)**2 for c in crops.values()))
    for i,n in enumerate(NAMES):
        c=crops[n]; scale=(target/alpha_area(c))**.5; dims=tuple(round(v*scale) for v in c.size)
        reduced=c.resize(dims,Image.Resampling.LANCZOS)
        x=round(i*320+160-dims[0]/2); y=round(320-dims[1]/2)
        row.alpha_composite(reduced,(x,y))
        entries.append(dict(name=n,bbox=[x,y,x+dims[0],y+dims[1]],alpha_area_px=round(alpha_area(reduced))))
    add('fox-compare-row',192,3632,row,P['deep'],placements=entries,optical_normalization='Equal full-art alpha-weighted area, including scenery.',target_alpha_area_px=round(target))
    for i,n in enumerate(NAMES): label(book,(192+i*320+119,4293),n.title(),23,'snow')
    strongest=('rime','cache','muff')
    proof=Image.new('RGBA',(1536,384)); silhouettes=[]
    for i,n in enumerate(strongest):
        c=masters[n].crop(masters[n].getbbox()); factor=min(440/c.width,336/c.height)
        dims=tuple(round(v*factor) for v in c.size); shape=flat(c,dims)
        x=i*512+round((512-dims[0])/2); y=round((384-dims[1])/2)
        proof.alpha_composite(shape,(x,y))
        silhouettes.append(dict(name=n,bbox=[i*512,0,(i+1)*512,384],art_bbox=[x,y,x+dims[0],y+dims[1]]))
    add('fox-species-check',64,4464,proof,ink=P['snow'],directions=silhouettes)
    for i,n in enumerate(strongest): label(book,(64+i*512+206,4871),n.title(),24,'snow')
    label(book,(1744,4479),'THE SPECIES TEST',29,'snow')
    for j,line in enumerate(['One ink. No eyes. No colour cues.','Short side ears, fur ruff and a tail','as large as head and body combined.','All eight reviewed this way at 256px.','The three strongest are shown here.','At 16px, species detail still weakens.']): label(book,(1744,4535+j*43),line,24)
    # Numerically compare component masks: visible tail area exceeds head+body.
    f=Pen(); face(f); b=Pen(); b.blob((206,347,368,558));
    rear=fur_mask((300,165,606,568),17); ImageDraw.Draw(rear).ellipse(tuple(round(v*S) for v in (80,110,446,440)),fill=0); front=fur_mask((65,418,567,588),17)
    union=Image.new('L',rear.size); union.paste(rear); union.paste(255,(0,0),front)
    area=lambda mask:sum(i*v/255 for i,v in enumerate(mask.histogram()))/S**2
    tail_area=area(union); animal_area=alpha_area(f.im)/S**2+alpha_area(b.im)/S**2
    # The silhouette is not a cosmetic enlargement: its actual filled area is dominant.
    assert tail_area>=animal_area,(tail_area,animal_area)
    manifest=dict(canvas=dict(width=CANVAS[0],height=CANVAS[1],mode='RGBA'),
        bbox_convention='Half-open [x,y,x+w,y+h]. Minimum 48px separation; labels outside all artwork crops.',
        palette=P,warm_accent=None,palette_decision='Dark rounded nose; ice inner ears; low-opacity ice blush. No pink anywhere.',
        concept=dict(words=['Silent','Adaptive','Unbreakable'],
            interpretation='The fox stays composed and comfortable while its scene changes. Unbreakable already means survives in every scene.',
            prohibited_trait='No stretching, growing or shrinking trait. Ordinary uniform scaling is only used for scene layout and raster proofs.',
            scene_count=sum(d['extreme_scene'] for d in DETAILS.values()),
            wrapping_directions=[n for n,d in DETAILS.items() if d['wrapping']]),
        geometry=dict(head_width=348,head_height=220,eye_diameter=68,eye_to_head_width=68/348,wind_ruff_width=376,eye_to_wind_ruff_width=68/376,
            eye_y=137,head_midline_y=110,eye_pair_outer_span=178,eye_pair_span_ratio=178/348,
            catchlight_diameter=17,catchlight_to_eye=.25,nose_width=22,nose_to_eye=22/68,
            muzzle_depth=61,muzzle_to_head_width=61/348,total_baby_body_height_without_tail=406,
            body_height_to_head_height=406/220,ears='Wide-based, lateral and short; explicit species correction supersedes the previous tall-ear height rule.',
            ear_height_above_skull=41,ear_base_width=133,ear_tip_radius=16,inner_ear=P['ice'],
            tail_filled_area_px=round(tail_area),head_plus_body_filled_area_px=round(animal_area),
            tail_to_head_and_body_area=round(tail_area/animal_area,3),
            geometry_note='Pose crouching and tail enclosure reduce visible height; infant head/body relation remains approximately two heads tall, with head allowed larger.',
            ruff='Six irregular overlapping rounded cheek lobes; no whisker dots.',
            tail='A continuous rear plume and return sweep, built from overlapping elliptical fur lobes; no smooth thin kitten tail.',
            roundness='Ear polygons are dilated with circular caps >=8% of their smaller dimension; all other shapes use ellipses, rounded rectangles or round-ended arcs.'),
        rendering='Pillow only; 2560px masters. Every 96/64/32/16px proof and 192px thumb is LANCZOS-downsampled from unchanged master art. Silhouettes use unchanged full-art alpha and one snow ink.',
        directions=[dict(name=n,**d,cuteness_review=dict(answer='yes',reason=d['cute'],size=192),
            species_review=dict(answer='yes',reason=d['fox'],size=256,method='Full-art flat single-colour silhouette, including any scene marks; imagine the caption cat.'),
            limitations='The yes judgement applies to the large silhouette, not guaranteed species recognition at 16px.') for n,d in DETAILS.items()],
        recommendation=dict(ranking=['rime','cache','muff','gale','listen','boreal','chirps','pounce'],
            reasons={'rime':'Best combination of huge tail, short side ears, affectionate gaze and an unmistakable adverse scene.',
                     'cache':'Strong wrapping composition; chin and paws connect the cute character to the enclosed data.',
                     'muff':'Most species-specific resting behaviour; enormous tail covers the nose in snow.',
                     'gale':'Direct performance of Silent and Unbreakable; weather adds some noise.',
                     'listen':'Quiet curiosity with a clear search metaphor; scene is less extreme.',
                     'boreal':'A calm continuation of the same animal in darkness; aurora costs pixels.',
                     'chirps':'Affectionate ecosystem illustration; two animals need more space.',
                     'pounce':'Cute and fox-specific activity, but the angled pose is least clear at tiny sizes.'},
            owner_shortlist=['rime','cache','muff','gale'],discard=[],
            favicon='No production favicon selected: all scene meanings and some species details weaken at 16px.'),
        fonts=FONTS,tiles=tiles)
    assert manifest['geometry']['eye_to_head_width']>=.18
    assert manifest['geometry']['eye_to_wind_ruff_width']>=.18
    assert manifest['geometry']['muzzle_to_head_width']<=.20
    assert manifest['concept']['scene_count']>=4 and len(manifest['concept']['wrapping_directions'])>=2
    validate(book,tiles,masters)
    book.save(OUT/'fox-book.png'); (OUT/'fox-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with Image.open(OUT/'fox-book.png') as check:
        check.load(); validate(check,tiles,masters)
        assert check.size==(manifest['canvas']['width'],manifest['canvas']['height'])
    print(f'Verified {len(tiles)} tiles; {CANVAS[0]} x {CANVAS[1]} RGBA; 32 native samples; tail/animal area {tail_area/animal_area:.2f}.')


if __name__=='__main__': main()
