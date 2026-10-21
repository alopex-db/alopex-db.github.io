#!/usr/bin/env python3
"""Pillow-only guardian study; writes only guardian-book.png and its manifest.

Run from any directory: python3 scripts/render_guardian_exploration.py
Hero, native proofs and single-ink silhouette all share a 2560px master.
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw
from render_brand_book import font, SELECTED_FONTS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/brand/explore'
CANVAS = (2944, 4352)
P = {'deep':'#1E3A5F','blue-light':'#2E5077','blue-dark':'#152C4A',
     'ice':'#5FB4C9','aurora':'#7EC8E3','frost':'#B8D4E3',
     'silver':'#C0C5CE','snow':'#F8FAFC','night':'#0B1929'}
NAMES = ('coil','den','summit','mantle','vigil','cache','patrol','kin')
IDEAS = {
 'coil': ('Sleeping enclosure', 'A sleeping fox encircles layered records; protection continues at rest.', 'Curled around a stack: retained because the tail can become the boundary of the store.', 'Resilience: passive enclosure rather than a security prop.'),
 'den': ('Watch at the threshold', 'An alert fox occupies the entrance of a cutaway snow burrow; records lie inside its arch.', 'Burrow entrance: retained to make storage feel like a habitat, not an adjacent object.', 'Search: ears attend to activity at the store entrance.'),
 'summit': ('The lookout', 'A seated fox perches directly on three broad storage strata, tail descending alongside them.', 'Layered perch: retained for its direct association with an LSM-style store.', 'Adaptability: a stable lookout above changing storage strata.'),
 'mantle': ('Tail as shelter', 'An oversized tail arches over a compact record cluster while the fox watches from one end.', 'Tail shelter: retained because the data is underneath the animal, never beside a badge.', 'Resilience: the winter tail insulates what is stored.'),
 'vigil': ('Living perimeter', 'A frontal fox stands with chest forward and tail closing the perimeter around a small core.', 'Head-on guardian: retained, using anatomy to form the boundary without drawing a shield.', 'Watchfulness: forward ears and steady eyes express attention.'),
 'cache': ('Resident in the store', 'A fox emerges from a gap between data strata; its tail stays visible beyond the layers.', 'Half-hidden inhabitant: retained to explore the database as the fox habitat.', 'Embedded: the guardian lives within the stored layers.'),
 'patrol': ('Paw on the records', 'A long-bodied fox spans a horizontal run of segments; one forepaw rests on the middle segment.', 'Standing watch: retained for the clearest physical claim of care and responsibility.', 'Search: a listening profile surveys the data beneath its feet.'),
 'kin': ('Shared watch', 'An adult watches outward while a smaller fox sleeps inside the arc of its tail.', 'Parent and child: retained to revisit the old pair as an explicit character narrative.', 'Continuity: a protected smaller member represents the entrusted data, without literal records.'),
}
# Conservative visual judgements; revisited against every proof after rendering.
ASSESS = {
 'coil': ('A pale oval with a small head and dark layered centre. Curl survives; fox identity is weak.', False, 'FAIL: a curled animal / oval. The snout touches the enclosing tail and disappears in one ink.'),
 'den': ('An arch with a small pale animal at its threshold; the burrow dominates. Not a fox icon.', False, 'FAIL: arch and animal merge into a grotto-like mass; exposed muzzle is too small.'),
 'summit': ('An upright long-eared animal on stripes. Perch reads; species needs more pixels.', True, 'PASS at 256px: long tapered snout, triangular ears and large outward tail remain exposed. Stack still adds visual weight.'),
 'mantle': ('A low canopy with a pointed head at one end. Tail shelter survives more than facial detail.', True, 'PASS at 256px: projecting snout, ears and the high bushy tail describe a side-profile fox.'),
 'vigil': ('An alert pointed face over a pale body; the tiny protected core merges. Strongest small character.', False, 'FAIL strict species test: a frontal pointed-eared animal; hidden snout and merged tail permit a cat reading.'),
 'cache': ('A pale head between stripes with a tail on the side; the embedded idea becomes clutter.', False, 'FAIL: slabs dominate and erase the animal anatomy. Not a reliable fox silhouette.'),
 'patrol': ('A long animal standing on a short baseline; muzzle and rear tail remain directional. Records merge.', True, 'PASS at 256px: long snout, triangular ears, standing legs and a very bushy tail remain distinct.'),
 'kin': ('Two pale bumps enclosed by a large tail; the smaller fox becomes a fleck.', True, 'PASS for the adult at 256px: outward pointed muzzle and ears are clear. FAIL for the child, which merges into the tail.'),
}


class Pen:
    def __init__(self):
        self.im=Image.new('RGBA',(2560,2560)); self.d=ImageDraw.Draw(self.im)
    def b(self,b): return tuple(round(v*4) for v in b)
    def e(self,b,c): self.d.ellipse(self.b(b),fill=P[c])
    def r(self,b,r,c): self.d.rounded_rectangle(self.b(b),radius=round(r*4),fill=P[c])
    def p(self,pts,c): self.d.polygon([(round(x*4),round(y*4)) for x,y in pts],fill=P[c])
    def a(self,b,start,end,c,w): self.d.arc(self.b(b),start,end,fill=P[c],width=round(w*4))
    def head(self,x,y,k=1,sleep=False):
        # Profile points left. Projecting long muzzle is part of the outer alpha.
        def pts(ps): return [(x+u*k,y+v*k) for u,v in ps]
        def bb(b): return [x+b[0]*k,y+b[1]*k,x+b[2]*k,y+b[3]*k]
        self.p(pts([(36,78),(47,-30),(95,22),(112,-20),(146,84)]),'snow')
        self.p(pts([(49,40),(54,-6),(80,35),(106,47),(114,3),(131,57)]),'frost')
        self.e(bb((30,35,161,161)),'snow')
        self.p(pts([(57,71),(-48,112),(21,150),(104,155),(148,112)]),'snow')
        self.p(pts([(-37,116),(44,113),(112,137),(67,157),(15,145)]),'frost')
        self.p(pts([(-37,116),(51,120),(101,138),(32,140)]),'snow')
        self.e(bb((-50,104,-30,120)),'night')
        if sleep: self.a(bb((29,82,67,103)),12,168,'night',5*k)
        else:
            self.e(bb((39,79,55,98)),'night')
            self.e(bb((41,81,46,86)),'snow')
    def front(self,x,y,k=1):
        def pts(ps): return [(x+u*k,y+v*k) for u,v in ps]
        def bb(b): return [x+b[0]*k,y+b[1]*k,x+b[2]*k,y+b[3]*k]
        self.p(pts([(-112,42),(-98,-95),(-37,-22),(37,-22),(98,-95),(112,42),(85,105),(0,163),(-85,105)]),'snow')
        self.e(bb((-108,-12,108,113)),'snow')
        self.p(pts([(-88,-59),(-83,9),(-47,-10)]),'frost')
        self.p(pts([(88,-59),(83,9),(47,-10)]),'frost')
        self.p(pts([(-104,60),(-18,87),(0,145),(-82,104)]),'frost')
        self.p(pts([(104,60),(18,87),(0,145),(82,104)]),'frost')
        self.e(bb((-65,44,-44,65)),'night'); self.e(bb((44,44,65,65)),'night')
        self.r(bb((-13,109,13,126)),7*k,'night')
    def slabs(self,x,y,w=210,h=29,count=3):
        for i in range(count):
            self.r((x,y+i*(h+9),x+w,y+i*(h+9)+h),9,'ice' if i%2 else 'blue-light')
            self.r((x+10,y+i*(h+9)+5,x+w-10,y+i*(h+9)+10),2,'aurora')
    def plume(self,b,tip='snow'):
        self.e(b,'frost')
        x,y,r,z=b; w=r-x; h=z-y
        self.p([(x+w*.50,y+h*.06),(r,y+h*.40),(x+w*.80,z),(x+w*.48,y+h*.89),(x+w*.68,y+h*.48)],tip)


def master(name):
    p=Pen()
    if name=='coil':
        p.e((93,195,551,532),'frost')
        # Clear central opening, cut out rather than filled with a fake matte.
        p.d.ellipse(p.b((218,275,453,432)),fill=(0,0,0,0))
        p.slabs(247,298,169,25,3)
        p.head(157,185,.98,True)
        p.e((92,382,552,553),'frost'); p.e((97,390,343,544),'snow')
        p.a((142,416,517,536),8,105,'ice',8)
    elif name=='den':
        # Burrow is a snow arch around a genuine transparent opening.
        p.e((60,105,581,562),'frost')
        p.d.ellipse(p.b((130,207,510,615)),fill=(0,0,0,0))
        p.d.rounded_rectangle(p.b((60,535,581,615)),radius=0,fill=(0,0,0,0))
        p.slabs(293,422,170,24,2)
        p.plume((178,290,327,534))
        p.e((123,325,227,522),'snow')
        p.r((130,440,165,533),14,'snow'); p.r((197,437,228,533),13,'snow')
        p.head(133,254,.82)
    elif name=='summit':
        p.slabs(121,410,340,36,3)
        p.plume((337,211,555,486))
        p.e((218,228,377,428),'frost'); p.e((232,258,315,422),'snow')
        p.r((219,358,261,427),16,'snow'); p.r((295,355,336,427),16,'snow')
        p.head(234,130,1.03)
    elif name=='mantle':
        # Tail itself is a roof: the underside and records remain open.
        p.e((173,127,562,486),'frost')
        p.d.ellipse(p.b((204,264,504,537)),fill=(0,0,0,0))
        p.e((354,138,557,312),'snow')
        p.e((105,273,230,489),'snow')
        p.head(114,214,.98)
        for x,y in [(263,365),(341,365),(302,421),(380,421)]:
            p.r((x,y,x+55,y+43),9,'ice'); p.r((x+9,y+9,x+45,y+15),2,'aurora')
        p.r((119,417,161,502),17,'snow')
    elif name=='vigil':
        p.plume((315,274,534,553))
        p.e((173,236,433,548),'frost')
        p.p([(224,296),(321,274),(399,305),(366,476),(274,531),(199,466)],'snow')
        p.slabs(259,421,105,20,2)
        p.r((192,348,244,548),20,'snow'); p.r((378,348,427,548),20,'snow')
        p.front(307,186,1.13)
    elif name=='cache':
        p.plume((387,235,564,545))
        p.slabs(116,190,351,34,2)
        p.e((173,294,405,477),'frost')
        p.head(210,266,1.05)
        p.slabs(110,439,363,34,2)
        p.r((178,420,236,470),17,'snow'); p.r((321,420,377,470),17,'snow')
    elif name=='patrol':
        p.plume((364,188,577,454))
        p.e((177,249,456,390),'frost')
        p.e((166,267,324,392),'snow')
        p.r((182,329,219,484),14,'snow'); p.r((369,329,405,483),14,'snow')
        p.head(143,178,.94)
        for i in range(5):
            p.r((105+i*84,478,176+i*84,521),9,'ice' if i%2 else 'blue-light')
            p.r((114+i*84,485,165+i*84,492),3,'aurora')
        p.r((209,351,246,470),14,'snow'); p.e((209,450,282,491),'snow')
    elif name=='kin':
        p.plume((263,274,563,562))
        p.e((159,276,337,524),'frost'); p.e((174,298,265,509),'snow')
        p.r((160,428,199,540),16,'snow')
        p.head(165,172,1.03)
        # Child is intentionally inside the adult's tail perimeter.
        p.e((302,427,472,527),'snow'); p.head(325,394,.50,True)
        p.e((238,496,533,568),'frost'); p.e((239,501,361,563),'snow')
    else: raise ValueError(name)
    return p.im


def label(im,xy,value,size=23,color='frost',role='body'):
    d=ImageDraw.Draw(im); f=font(size,role); b=d.textbbox((0,0),value,font=f)
    d.text((xy[0]-b[0],xy[1]-b[1]),value,font=f,fill=P[color])


def validate(book,tiles):
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
        if t['name'].endswith('-silhouette'):
            rgb=crop.convert('RGB'); colors=rgb.getcolors(crop.width*crop.height)
            assert {color for count,color in colors} <= {(0,0,0),tuple(bytes.fromhex(P['snow'][1:]))}
            assert all(rgb.getpixel((px,py))==tuple(bytes.fromhex(P['snow'][1:]))
                       for py in range(crop.height) for px in range(crop.width)
                       if alpha.getpixel((px,py))>0)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    book=Image.new('RGBA',CANVAS,P['night']); tiles=[]
    masters={n:master(n) for n in NAMES}
    label(book,(64,40),'ALOPEX DB / GUARDIANS OF THE STORE',43,'snow','brand')
    label(book,(64,111),'08 character concepts / anatomy before props / companions to the shipped mark',27)
    label(book,(64,163),'Heroes 640px | proofs 64 / 48 / 32 / 16px at native size | silhouette 256px in one ink',23)
    def add(name,x,y,im,background='transparent',**extra):
        w,h=im.size; t=dict(name=name,x=x,y=y,w=w,h=h,bbox=[x,y,x+w,y+h],background=background,**extra)
        tiles.append(t); label(book,(x,y-34),f'{name} / {w} x {h}',21)
        book.paste(im,(x,y))
    for i,n in enumerate(NAMES):
        x=64+(i%2)*1472; y=272+(i//2)*816; m=masters[n]
        add(f'guard-{n}-hero',x,y,m.resize((640,640),Image.Resampling.LANCZOS))
        proof=Image.new('RGBA',(512,128)); samples=[]
        for cx,size in zip((64,192,320,448),(64,48,32,16)):
            px=cx-size//2; py=(128-size)//2
            reduced=m.resize((size,size),Image.Resampling.LANCZOS)
            proof.alpha_composite(reduced,(px,py))
            samples.append(dict(size=size,bbox=[px,py,px+size,py+size]))
        add(f'guard-{n}-sizes',x+688,y,proof,samples=samples)
        for cx,size in zip((64,192,320,448),(64,48,32,16)):
            label(book,(x+688+cx-20,y+143),f'{size}px',18)
        # Pure single ink: alpha is the ONLY source of shape, no eye cutouts added.
        silhouette=Image.new('RGBA',(256,256),P['snow'])
        silhouette.putalpha(m.getchannel('A').resize((256,256),Image.Resampling.LANCZOS))
        canonical=Image.new('RGBA',(256,256))
        canonical.alpha_composite(silhouette)  # Zero-alpha RGB stays empty, like hero tiles.
        add(f'guard-{n}-silhouette',x+688,y+224,canonical,ink=P['snow'])
        title,concept,chosen,mapping=IDEAS[n]
        label(book,(x+688,y+519),title,25,'snow')
        verdict='FOX SILHOUETTE: '+('PASS' if ASSESS[n][1] else 'FAIL')
        label(book,(x+688,y+562),verdict,21,'aurora')
        label(book,(x+688,y+603),'Hero + proof share unchanged artwork.',20)
    row=Image.new('RGBA',(2560,640),P['deep']); placements=[]
    for i,n in enumerate(NAMES):
        m=masters[n]; c=m.crop(m.getbbox()); h=c.getchannel('A').histogram()
        area=sum(k*v/255 for k,v in enumerate(h)); factor=(28000/area)**.5
        dims=tuple(round(v*factor) for v in c.size)
        assert dims[0]<=292 and dims[1]<=540,(n,dims)
        c=c.resize(dims,Image.Resampling.LANCZOS)
        px=round(i*320+160-dims[0]/2); py=round(320-dims[1]/2)
        row.alpha_composite(c,(px,py))
        placements.append(dict(name=n,bbox=[px,py,px+dims[0],py+dims[1]],
            alpha_weighted_area_px=round(sum(k*v/255 for k,v in enumerate(c.getchannel('A').histogram())))))
    add('guard-compare-row',192,3616,row,P['deep'],placements=placements,
        optical_normalization='Equal visible alpha-weighted area, approximately 28000px per composition; centered in eight equal cells. Data is included in visual mass.')
    for i,n in enumerate(NAMES): label(book,(192+i*320+117,4279),n.title(),24,'snow')
    directions=[]
    for n in NAMES:
        title,concept,chosen,mapping=IDEAS[n]; tiny,passed,sil=ASSESS[n]
        directions.append(dict(name=n,guarding_idea=title,concept=concept,starting_point_and_reason=chosen,
            product_mapping=mapping,species_cues='Long profile muzzle (Vigil uses a frontal tapered muzzle), triangular ears, pale coat with blue-grey shadow, body-scale bushy tail.',
            visual_review=dict(at_16px=tiny,silhouette_fox=passed,silhouette_assessment=sil,
                reviewed_tiles=[f'guard-{n}-sizes',f'guard-{n}-silhouette']),
            role='Character layer; not a proposed automatic replacement for the shipped mark.'))
    manifest=dict(canvas=dict(width=CANVAS[0],height=CANVAS[1],mode='RGBA'),
        bbox_convention='Half-open [x,y,x+w,y+h]; minimum 48px between artwork tiles.',
        palette=P,warm_accent=None,ink_note='Night is the approved near-black for noses and eyes; no extra black or warm accent.',
        research_basis='Design brief supplied by the owner; no new external research or independent factual verification claimed.',
        rendering='Pillow only. 2560px RGBA masters -> LANCZOS at every target size. Proofs composited at 1:1, with no hand-tuned small variants. Silhouettes preserve master alpha and use one constant snow RGB.',
        small_variant_decision='No stripped-down production icon is supplied: these tiles deliberately expose what unchanged artwork loses. A separate small variant would be a follow-up after concept selection.',
        selection_criteria=['Fox species recognition in silhouette','Guarding communicated by physical relationship to stored data','Native 16px legibility','Mature character tone beside software typography'],
        directions=directions,fonts=SELECTED_FONTS,tiles=tiles,
        recommendation=dict(ranking=['patrol','mantle','summit','kin','vigil','coil','den','cache'],
            reasons={'patrol':'Best exposed fox anatomy and explicit paw-to-record relationship; simplify the records for future small use.',
                     'mantle':'Most ownable guardian idea: winter tail as shelter. Fewer storage shapes would improve reduction.',
                     'summit':'Strong fox silhouette and clear storage strata; slightly conventional lookout metaphor.',
                     'kin':'Warm continuity narrative and an identifiable adult; child fails in silhouette and at 16px.',
                     'vigil':'Strongest small frontal face but fails the strict fox silhouette test; revise before advancing.',
                     'coil':'Protective curl is coherent at hero size, but snout and tail collapse into an oval.',
                     'den':'A habitat story with too much architectural mass; the fox becomes subordinate.',
                     'cache':'Embedded concept is direct, but anatomy is fragmented by data layers.'},
            discard=['den','cache'],
            restrict_to_large_illustration=['coil','kin'],
            revise_species_before_advancing=['vigil'],
            favicon='None passes both unmistakable fox recognition and integrated guardian meaning at 16px. Keep the shipped mark for tiny icons pending a separate reduction study.'))
    validate(book,tiles)
    book.save(OUT/'guardian-book.png')
    (OUT/'guardian-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with Image.open(OUT/'guardian-book.png') as check:
        check.load(); validate(check,tiles)
        assert check.size==(manifest['canvas']['width'],manifest['canvas']['height'])
        for t in tiles:
            if t['name'].endswith('-sizes'):
                for sample in t['samples']:
                    size=sample['size']; expected=Image.new('RGBA',(size,size))
                    expected.alpha_composite(masters[t['name'].split('-')[1]].resize((size,size),Image.Resampling.LANCZOS))
                    assert check.crop(t['bbox']).crop(sample['bbox']).tobytes()==expected.tobytes()
    print(f'Verified {len(tiles)} tiles / {CANVAS[0]} x {CANVAS[1]} RGBA / 48px gutters / 32 exact native samples')


if __name__=='__main__': main()
