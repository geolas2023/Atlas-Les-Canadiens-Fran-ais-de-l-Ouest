# Salle de lecture multi-personnages : French Fur Traders and Voyageurs in the American West
import json, os, sys, importlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffv'))
OUT = '/home/claude/atlas-les-canadiens-fran-ais-de-l-ouest'
from registre import ORDRE, COULEURS
from commun import FF

def charger():
    mods = []
    for mid in ORDRE:
        try: mods.append(importlib.import_module('f_'+mid))
        except ModuleNotFoundError: pass
    return mods

def construire(feats_atlas, leduc_L=None, leduc_biblio=None, leduc_blocs=None):
    os.makedirs(f'{OUT}/data/personnages', exist_ok=True)
    index, remplaces = [], set()
    for m in charger():
        P = dict(m.P); pid = P['id']
        P['couleur'] = COULEURS.get(pid, '#888')
        etapes = [dict(nom=e[0], lon=e[1], lat=e[2], debut=e[3], fin=e[4], edtf=e[5], cert=e[6], phase=e[7], desc=e[8], src=e[9], note=e[10]) for e in m.E]
        biblio = [f"{P['auteur']}, « {P['nom']} », dans {FF}, p. {P['pages']}."]
        if pid == 'leduc' and leduc_L:
            for (o, nom, lon, lat, d, f, edtf, cert, phase, desc, src, note) in leduc_L:
                etapes.append(dict(nom=nom, lon=lon, lat=lat, debut=d, fin=f, edtf=edtf, cert=cert, phase=phase, desc=desc, src=src, note=note))
            biblio += leduc_biblio or []
        etapes.sort(key=lambda e: (e['phase'] == 'Mémoire', e['debut'], e['fin']))
        pts = []
        for i, e in enumerate(etapes, 1):
            pts.append({"type":"Feature","geometry":{"type":"Point","coordinates":[round(e['lon'],4), round(e['lat'],4)]},
              "properties":{"id":f"{pid}-{i:02d}","ordre":i,"nom":e['nom'],"phase":e['phase'],"debut":e['debut'],"fin":e['fin'],
                "date_edtf":e['edtf'],"certitude":e['cert'],"description":e['desc'],"sources":e['src'],"note":e['note'] or ""}})
            if pid != 'leduc':   # LeDuc a déjà sa couche propre dans l'atlas
                feats_atlas.append({"type":"Feature","geometry":pts[-1]['geometry'],"properties":{
                  "id":f"F-{pid}-{i:02d}","nom":e['nom'],"corpus":"Hafen","theme":"personnage","debut":e['debut'],"fin":e['fin'],
                  "date_edtf":e['edtf'],"precision":"","certitude":e['cert'],"personnages":[P['nom']]+list(P.get('autres',[])),
                  "description":e['desc'],"sources":e['src'],"note":e['note'] or "","salle":pid}})
        vie = [p for p in pts if p['properties']['phase'] != 'Mémoire']
        ligne = {"type":"Feature","geometry":{"type":"LineString","coordinates":[p['geometry']['coordinates'] for p in vie]},
                 "properties":{"id":f"{pid}-parcours","nom":f"Parcours de {P['nom']}"}}
        doc = {"type":"FeatureCollection","name":pid,"personnage":P,"bibliographie":biblio,
               "inedits":getattr(m,'INEDITS',[]),"blocs":(leduc_blocs if pid=='leduc' else getattr(m,'BLOCS',[])),"features":pts+[ligne]}
        json.dump(doc, open(f'{OUT}/data/personnages/{pid}.geojson','w'), ensure_ascii=False, indent=1)
        if pid == 'leduc':
            json.dump(doc, open(f'{OUT}/data/maurice-leduc.geojson','w'), ensure_ascii=False, indent=1)
        d0 = min(p['properties']['debut'] for p in vie); d1 = max(p['properties']['fin'] for p in vie)
        index.append({"id":pid,"nom":P['nom'],"couleur":P['couleur'],"vie":P.get('vie',''),"auteur":P['auteur'],"pages":P['pages'],
                      "etapes":len(pts),"debut":d0,"fin":d1})
        if P.get('hafen'): remplaces.add(P['hafen'])
    json.dump({"livre":FF,"personnages":index}, open(f'{OUT}/data/personnages/index.json','w'), ensure_ascii=False, indent=1)
    return remplaces, index
