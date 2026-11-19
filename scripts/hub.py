# Hub entre les atlas (novembre 2026) : chaque fiche vit dans un seul atlas, les autres y renvoient.
#   - Les fiches du corpus « Atlas Aubry » (identifiants A-Lxx, conservés pour ne briser aucun lien partagé) deviennent
#     des renvois courts : nom, dates, lieu, personnages, une phrase de résumé et un bouton vers la fiche complète.
#   - Quelques fiches d'autres corpus qui recoupent l'Atlas Aubry reçoivent le même bouton (VOIR_AUSSI ci-dessous).
# Le champ « voir_aussi » (liste de {"url", "texte"}) est commun aux atlas : js/atlas.js l'affiche dans la fiche.
# Idempotent. Ordre de la chaîne : build.py → ajouts_2026_11.py → ajouts_2026_11b.py → hub.py → page_provost.py
import json, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUBRY = 'https://geolas2023.github.io/Atlas-Aubry/'
IBERVILLE = 'https://geolas2023.github.io/Atlas-Iberville/'
IBERVILLE_LOCAL = os.environ.get('IBERVILLE', '/home/claude/atlas-iberville')  # clone local de l'Atlas Iberville
JOLLIET = 'https://geolas2023.github.io/Atlas-Jolliett/'
JOLLIET_LOCAL = os.environ.get('JOLLIET', '/home/claude/atlas-jolliett-depot')  # clone local de l'Atlas Jolliet
ROBIDOUX = 'https://geolas2023.github.io/Les-Robidoux/'
ROBIDOUX_LOCAL = os.environ.get('ROBIDOUX', '/home/claude/les-robidoux')  # clone local de l'Atlas Robidoux
THEME_IB = {'combat': 'evenement', 'escale': 'exploration', 'decouverte': 'exploration', 'port': 'poste', 'fondation': 'etablissement',
            'vie': 'personnage', 'naissance': 'famille', 'concession': 'etablissement', 'mort': 'evenement'}
TXT_FICHE = "Fiche complète dans l'Atlas Aubry →"

def fiche_aubry(lid, texte=TXT_FICHE):
    return {"url": f"{AUBRY}index.html#lieu={lid}", "texte": texte}

# Renvois ajoutés à des fiches d'autres corpus (même sujet traité en détail dans l'Atlas Aubry)
VOIR_AUSSI = {
    'AH-sf15': [{"url": f"{AUBRY}grande-course.html", "texte": "La grande course de 1848 dans l'Atlas Aubry →"}],
    'AH-sf16': [fiche_aubry('L79', "Fort Aubry et Aubry's Spring dans l'Atlas Aubry →")],
    'AH-sf17': [fiche_aubry('L56', "La maison J. & H. Mercure dans l'Atlas Aubry →"), fiche_aubry('L31', "La mort d'Aubry chez les Mercure →")],
    'AH-sf18': [fiche_aubry('L103', "Aubry Town dans l'Atlas Aubry →")],
    'AH-sf19': [fiche_aubry('L78', "Aubrey Landing dans l'Atlas Aubry →"), fiche_aubry('L64', "Le vapeur F. X. Aubrey dans l'Atlas Aubry →")],
    'R2-10':   [fiche_aubry('L78', "Les lieux de l'Arizona qui portent son nom (Atlas Aubry) →")],
}

def premiere_phrase(t, n=220):
    t = re.sub(r'\s+', ' ', t or '').strip()
    m = re.match(r'(.+?[.!?»])(\s|$)', t)
    s = m.group(1) if m and len(m.group(1)) >= 40 else t
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' …'

d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
nr = nv = 0
for f in d['features']:
    p = f['properties']
    if p['corpus'] == 'Atlas Aubry' and p['id'].startswith('A-'):
        lid = p['id'][2:]
        if not p.get('renvoi'):
            p['description'] = premiere_phrase(p.get('description'))
        p['sources'] = f"Atlas Aubry, fiche {lid} (sources détaillées dans la fiche complète)."
        p['note'] = ''
        p['images'] = []
        p['transcription'] = ''
        p['renvoi'] = True
        p['voir_aussi'] = [fiche_aubry(lid)]
        nr += 1
    elif p['id'] in VOIR_AUSSI:
        p['voir_aussi'] = VOIR_AUSSI[p['id']]
        if p.get('note', '').startswith("Fiche de l'univers Aubry"):
            p['note'] = re.sub(r"^Fiche de l'univers Aubry[^.;]*[.;]?\s*", '', p['note'])
        nv += 1
# Atlas Iberville : renvois courts I-Lxx (recréés à chaque passage si le clone local est présent)
ni = 0
fic = f'{IBERVILLE_LOCAL}/data/lieux.geojson'
if os.path.exists(fic):
    d['features'] = [f for f in d['features'] if f['properties']['corpus'] != 'Atlas Iberville']
    for f0 in json.load(open(fic, encoding='utf-8'))['features']:
        q = f0['properties']
        if f0['geometry']['type'] != 'Point': continue
        d['features'].append({"type": "Feature", "geometry": f0['geometry'], "properties": {
            "id": f"I-{q['id']}", "nom": q['nom'], "corpus": "Atlas Iberville", "theme": THEME_IB.get(q.get('categorie'), 'evenement'),
            "debut": float(q['debut']), "fin": float(q.get('fin') or q['debut']), "date_edtf": q.get('date_edtf', ''),
            "precision": q.get('precision', ''), "certitude": q.get('certitude', 'approximative'),
            "personnages": ["Pierre Le Moyne d'Iberville"], "description": premiere_phrase(q.get('description')),
            "sources": f"Atlas Iberville, fiche {q['id']} (d'après Frégault, Iberville le conquérant, 1944).", "note": "",
            "renvoi": True, "voir_aussi": [{"url": f"{IBERVILLE}index.html#lieu={q['id']}", "texte": "Fiche complète dans l'Atlas Iberville →"}]}})
        ni += 1
# Atlas Jolliet : renvois courts J-Lxx (recréés à chaque passage si le clone local est présent)
nj = 0
fic = f'{JOLLIET_LOCAL}/data/lieux.geojson'
if os.path.exists(fic):
    d['features'] = [f for f in d['features'] if f['properties']['corpus'] != 'Atlas Jolliet']
    for f0 in json.load(open(fic, encoding='utf-8'))['features']:
        q = f0['properties']
        d['features'].append({"type": "Feature", "geometry": f0['geometry'], "properties": {
            "id": f"J-{q['id']}", "nom": q['nom'], "corpus": "Atlas Jolliet", "theme": THEME_IB.get(q.get('categorie'), 'evenement'),
            "debut": float(q['debut']), "fin": float(q.get('fin') or q['debut']), "date_edtf": q.get('date_edtf', ''),
            "precision": q.get('precision', ''), "certitude": q.get('certitude', 'approximative'),
            "personnages": ["Louis Jolliet"], "description": premiere_phrase(q.get('description')),
            "sources": f"Atlas Jolliet, fiche {q['id']} (d'après Gagnon, Louis Jolliet, 1913 ; Récit du P. Marquette ; BAnQ).", "note": "",
            "renvoi": True, "voir_aussi": [{"url": f"{JOLLIET}index.html#lieu={q['id']}", "texte": "Fiche complète dans l'Atlas Jolliet →"}]}})
        nj += 1
# Atlas Robidoux : renvois courts R-Lxx
MEMBRES_ROB = {'joseph1': 'Joseph Robidoux (v. 1720-1771)', 'joseph2': 'Joseph Robidoux (v. 1750-1809)', 'joseph3': 'Joseph Robidoux (1783-1868)',
               'antoine': 'Antoine Robidoux', 'louis': 'Louis Robidoux', 'freres': 'François et Michel Robidoux', 'jules': 'Jules Robidoux', 'famille': 'Famille Robidoux'}
nb = 0
fic = f'{ROBIDOUX_LOCAL}/data/lieux.geojson'
if os.path.exists(fic):
    d['features'] = [f for f in d['features'] if f['properties']['corpus'] != 'Atlas Robidoux']
    for f0 in json.load(open(fic, encoding='utf-8'))['features']:
        q = f0['properties']
        d['features'].append({"type": "Feature", "geometry": f0['geometry'], "properties": {
            "id": f"R-{q['id']}", "nom": q['nom'], "corpus": "Atlas Robidoux", "theme": 'evenement',
            "debut": float(q['debut']), "fin": float(q.get('fin') or q['debut']), "date_edtf": q.get('date_edtf', ''),
            "precision": q.get('precision', ''), "certitude": q.get('certitude', 'approximative'),
            "personnages": [MEMBRES_ROB.get(q.get('categorie'), 'Famille Robidoux')], "description": premiere_phrase(q.get('description')),
            "sources": f"Atlas Robidoux, fiche {q['id']} ({q.get('sources', '')})", "note": "",
            "renvoi": True, "voir_aussi": [{"url": f"{ROBIDOUX}index.html#lieu={q['id']}", "texte": "Fiche complète dans l'Atlas Robidoux →"}]}})
        nb += 1
# Atlas Chalifoux : les fiches reprises de ce réseau (champ « reseau ») reçoivent un bouton vers l'atlas ;
# les fiches propres à l'Atlas Chalifoux deviennent des renvois courts X-Lxx.
CHALIFOUX = 'https://geolas2023.github.io/Atlas_Chalifoux/'
CHALIFOUX_LOCAL = os.environ.get('CHALIFOUX', '/home/claude/atlas_chalifoux')
nc = 0
fic = f'{CHALIFOUX_LOCAL}/data/lieux.geojson'
if os.path.exists(fic):
    d['features'] = [f for f in d['features'] if f['properties']['corpus'] != 'Atlas Chalifoux']
    par_id = {f['properties']['id']: f for f in d['features']}
    for f0 in json.load(open(fic, encoding='utf-8'))['features']:
        q = f0['properties']
        bouton = {"url": f"{CHALIFOUX}index.html#lieu={q['id']}", "texte": "Voir dans l'Atlas Chalifoux →"}
        if q.get('reseau'):
            g = par_id.get(q['reseau'])
            if g is not None:
                va = [v for v in g['properties'].get('voir_aussi') or [] if CHALIFOUX not in v['url']]
                g['properties']['voir_aussi'] = va + [bouton]
            continue
        d['features'].append({"type": "Feature", "geometry": f0['geometry'], "properties": {
            "id": f"X-{q['id']}", "nom": q['nom'], "corpus": "Atlas Chalifoux", "theme": 'personnage',
            "debut": float(q['debut']), "fin": float(q.get('fin') or q['debut']), "date_edtf": q.get('date_edtf', ''),
            "precision": q.get('precision', ''), "certitude": q.get('certitude', 'approximative'),
            "personnages": ["Jean-Baptiste Chalifoux"], "description": premiere_phrase(q.get('description')),
            "sources": f"Atlas Chalifoux, fiche {q['id']} ({q.get('sources', '')})", "note": "",
            "renvoi": True, "voir_aussi": [{"url": f"{CHALIFOUX}index.html#lieu={q['id']}", "texte": "Fiche complète dans l'Atlas Chalifoux →"}]}})
        nc += 1
json.dump(d, open(f'{R}/data/lieux.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{nc} renvois Chalifoux')
print(f'{nr} fiches Aubry en renvoi court ; {nv} autres fiches avec renvoi ; {ni} renvois Iberville ; {nj} renvois Jolliet ; {nb} renvois Robidoux')
