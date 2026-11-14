import json, os, re, shutil, ast, sys
sys.path.insert(0, '/home/claude/scripts')
from e0 import E0; from e1 import E1; from e2 import E2; from e3 import E3
from e4 import E4; from e5 import E5; from e6 import E6; from e7 import E7
OUT = '/home/claude/atlas-les-canadiens-fran-ais-de-l-ouest'
AUBRY = '/home/claude/atlas-aubry'
SRC_CRAGIN = ("Cragin, Francis Whittemore, Early Far West Notebooks (1902-1923), Starsmore Center for Local History, "
              "Colorado Springs Pioneers Museum ; transcription dactylographiée (Mrs. Shaw), PDF « Cragin notebooks searchable », p. ")
THEMES = {'poste':'Poste de traite / fort','etablissement':'Établissement / colonie','famille':'Famille et descendance',
          'personnage':'Personnage','evenement':'Événement','commerce':'Commerce et métiers','migration':'Migration / origine',
          'exploration':'Exploration','religion':'Religion et sépultures','toponymie':'Toponymie'}
CANON = {
 'Antoine (Joaquin) Leroux':'Antoine Leroux','Joaquin (Antoine) Leroux':'Antoine Leroux','Joaquin Leroux':'Antoine Leroux',
 'Antoine Labrie (Lebrie)':'Antoine Labrie','Antoine Lajeunesse (deux cousins)':'Antoine Lajeunesse','Antoine LaJeunesse':'Antoine Lajeunesse',
 'Auguste Pike Vasquez':'Auguste « Pike » Vasquez','Charles Autobees (Hautbois)':'Charles Autobees','Charles Hippolyte Beaubien':'Charles Beaubien',
 'Chalifoux (Charlefoux)':'Jean-Baptiste Chalifoux','Chalifoux':'Jean-Baptiste Chalifoux','Jean-Baptiste Chalifoux (Charlefou)':'Jean-Baptiste Chalifoux',
 'Charlie Carbonneau (Charbonneau)':'Charlie Carbonneau','Dolores Lafevre (Lefebvre)':'Dolores Lefebvre',
 'Manuel Lafevre':'Manuel Lefebvre','Manuel Lefevre':'Manuel Lefebvre','Manuel Lefevre (Lefebvre)':'Manuel Lefebvre',
 'Grignet':'Grignet (Grenier)','Grignier':'Grignet (Grenier)','Grenier':'Grignet (Grenier)','José Grenier (Grignez)':'José Grenier',
 'Gus Clermont (Claymore)':'Auguste Clermont','Jeantet':'Jean Arno Jeantet','Jeantet (Juan Chantet)':'Jean Arno Jeantet',
 'Juan Boquet':'Jean-Baptiste Boquet','Josefa (Josefita) Lalande':'Josefa Lalande','Lalande':'Baptiste Lalande',
 'Joseph Barnois dit Levanway':'Joseph Levanway (Barnois)','Joseph Levanway':'Joseph Levanway (Barnois)',
 'LeDoux':'Antoine Ledoux','Lesperance':'Pierre Lesperance','Pierre Lesperance (Pedro Esperanza)':'Pierre Lesperance',
 'Pierre Lesperance (Pedro Lesperance)':'Pierre Lesperance','Louis (Joseph) Clouthier':'Louis Clouthier','Mary L. Sopris':'Mary St. Vrain (Sopris)',
 'Mary Sopris':'Mary St. Vrain (Sopris)','« Red » (Sioux)':'Red (Sioux)','Red':'Red (Sioux)','Lafontaine':'La Fontaine',
 'Gillette':'Antoine Gillette','de Bleury':'Frères de Bleury','frères de Bleury':'Frères de Bleury','Lajeunesse':'Antoine Lajeunesse',
 'Gosselin':'Albert Gosselin','Bijeau':'Bijou','Istuss':'Maurice Istuss','Metcalf':'Archa Metcalf','Maurice':'Maurice (de Taos)',
 'Luis Leroux':'Luis William Leroux','Sorel':'Sorel (trappeur)',
}
def canon(n): return CANON.get(n, n)
feats = []
n = 0
for batch in (E0,E1,E2,E3,E4,E5,E6,E7):
    for (nom, lon, lat, d, f, edtf, prec, cert, pers, desc, pages, note, theme) in batch:
        n += 1
        assert theme in THEMES, theme
        assert -125 < lon < 0 and 15 < lat < 60, nom
        assert d <= f, nom
        persons = list(dict.fromkeys(canon(p.strip()) for p in pers.split(';') if p.strip()))
        feats.append({"type":"Feature","geometry":{"type":"Point","coordinates":[round(lon,5),round(lat,5)]},
          "properties":{"id":f"C{n:03d}","nom":nom,"corpus":"Cragin","theme":theme,"debut":d,"fin":f,"date_edtf":edtf,
            "precision":prec,"certitude":cert,"personnages":persons,"description":desc,
            "sources":SRC_CRAGIN+pages+".","pages_pdf":pages,"note":note or ""}})
print('Cragin', n)
# --- Atlas Aubry: points
d = json.load(open(f'{AUBRY}/data/lieux.geojson'))
copied = 0
for f0 in d['features']:
    p = dict(f0['properties'])
    imgs = []
    for im in (p.get('images') or []):
        if isinstance(im, str): im = {'src': im}
        src = im.get('src','')
        if src and not src.startswith('http'):
            dst = 'images/aubry/' + src.split('/',1)[1] if src.startswith('images/') else 'images/aubry/'+os.path.basename(src)
            os.makedirs(os.path.dirname(f'{OUT}/{dst}'), exist_ok=True)
            if os.path.exists(f'{AUBRY}/{src}'):
                if not os.path.exists(f'{OUT}/{dst}'): shutil.copy(f'{AUBRY}/{src}', f'{OUT}/{dst}'); copied += 1
                im = dict(im, src=dst)
            else: continue
        imgs.append(im)
    if p.get('image') and not p['image'].startswith('http') and os.path.exists(f"{AUBRY}/{p['image']}"):
        dst = 'images/aubry/' + os.path.basename(p['image'])
        if not os.path.exists(f'{OUT}/{dst}'): shutil.copy(f"{AUBRY}/{p['image']}", f'{OUT}/{dst}'); copied += 1
        imgs.insert(0, {'src': dst, 'legende': ''})
    t = p.get('type')
    theme = {'evenement':'evenement','lieu':'etablissement','contexte':'evenement'}.get(t,'evenement')
    pers = [x for x in [p.get('acteur')] if x]
    txt = (p.get('nom','')+' '+p.get('description',''))
    ALIAS = {'François-Xavier Aubry':['Aubry'], 'Moïse Lamoureux':['Moïse Lamoureux','Moses Lamoureux'],
             'Elzéar Blanchard':['Elzéar Blanchard','Elzear Blanchard'], 'Henri Mercure':['Henri Mercure','Henry Mercure'],
             'Joseph Mercure':['Joseph Mercure'], 'Charles Blanchard':['Charles Blanchard'], 'Michel Desmarais':['Michel Desmarais','Miguel Desmarais'],
             'Céran St. Vrain':['Céran St. Vrain','Ceran St. Vrain','St. Vrain'], 'Alexis Godey':['Alexis Godey','Alex Godey'],
             'Rosalie Vasquez':['Rosalie Vasquez'], 'Amelina Vasquez':['Amelina Vasquez'], 'Benito Vasquez':['Benito Vasquez'],
             'Avila Sénécal':['Avila Sénécal'], 'Antoine Leroux':['Antoine Leroux']}
    for nm, als in ALIAS.items():
        if any(a in txt for a in als) and nm not in pers: pers.append(nm)
    feats.append({"type":"Feature","geometry":f0['geometry'],"properties":{
        "id":"A-"+str(p.get('id')),"nom":p.get('nom'),"corpus":"Atlas Aubry","theme":theme,
        "debut":float(p.get('debut') or 1824),"fin":float(p.get('fin') or p.get('debut') or 1824),
        "date_edtf":p.get('date_edtf',''),"precision":p.get('precision',''),"certitude":p.get('certitude','approximative'),
        "personnages":pers,"description":p.get('description',''),"sources":p.get('sources',''),"note":p.get('note',''),
        "images":imgs,"transcription":p.get('transcription','')}})
print('total', len(feats), 'images copied', copied)
json.dump({"type":"FeatureCollection","name":"lieux","features":feats}, open(f'{OUT}/data/lieux.geojson','w'), ensure_ascii=False, indent=1)
json.dump(THEMES, open(f'{OUT}/data/themes.json','w'), ensure_ascii=False, indent=1)

# --- Corpus « Recherches » (web et littérature)
from recherches import R
k = 0
for (nom, lon, lat, d, f, edtf, prec, cert, pers, desc, src, note, theme) in R:
    k += 1
    feats.append({"type":"Feature","geometry":{"type":"Point","coordinates":[lon,lat]},
      "properties":{"id":f"R{k:03d}","nom":nom,"corpus":"Recherches","theme":theme,"debut":d,"fin":f,"date_edtf":edtf,
        "precision":prec,"certitude":cert,"personnages":[canon(p.strip()) for p in pers.split(';') if p.strip()],
        "description":desc,"sources":src,"note":note or ""}})
# --- Maurice LeDuc : chronologie de vie
from leduc import L, BIBLIO
lf = []
for (o, nom, lon, lat, d, f, edtf, cert, phase, desc, src, note) in L:
    lf.append({"type":"Feature","geometry":{"type":"Point","coordinates":[lon,lat]},
      "properties":{"id":f"M{o:02d}","ordre":o,"nom":nom,"corpus":"Maurice LeDuc","theme":"personnage","phase":phase,
        "debut":d,"fin":f,"date_edtf":edtf,"precision":"","certitude":cert,"personnages":["Maurice LeDuc"],
        "description":desc,"sources":src,"note":note or ""}})
vie = [x for x in lf if x['properties']['phase'] not in ('Mémoire',)]
ligne = {"type":"Feature","geometry":{"type":"LineString","coordinates":[x['geometry']['coordinates'] for x in sorted(vie,key=lambda x:x['properties']['ordre'])]},
         "properties":{"id":"M-parcours","nom":"Parcours de vie de Maurice LeDuc (ordre chronologique)"}}
json.dump({"type":"FeatureCollection","name":"maurice-leduc","bibliographie":BIBLIO,"features":lf+[ligne]},
          open(f'{OUT}/data/maurice-leduc.geojson','w'), ensure_ascii=False, indent=1)
json.dump({"type":"FeatureCollection","name":"lieux","features":feats}, open(f'{OUT}/data/lieux.geojson','w'), ensure_ascii=False, indent=1)
print('final total', len(feats), 'leduc', len(lf))
