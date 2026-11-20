# Ajouts de novembre 2026 : trois corpus versés depuis les dépouillements faits pour l'Atlas Aubry.
#   « Tassé »            Les Canadiens de l'Ouest (1878), t. I et II : 174 lieux
#   « Hafen MM »         The Mountain Men and the Fur Trade of the Far West, vol. 2, 4-9 : lieux datés des biographies de francophones
#   « Illinois français » onze sources sur l'Illinois français et l'archipel du Midwest (dont les 181 habitants de Peoria, East 1933)
# Le script est idempotent : il retire d'abord les fiches de ces corpus, puis les recrée. Les points provisoires « H… » du corpus
# Hafen dont la notice a maintenant été dépouillée sont retirés (remplacés par le corpus « Hafen MM »).
import json, os, re, unicodedata
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(R, 'scripts', 'sources_2026')
NOUVEAUX = ('Tassé', 'Hafen MM', 'Illinois français')
d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
feats = [f for f in d['features'] if f['properties']['corpus'] not in NOUVEAUX]

def sans_accents(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()

def theme_de(nom, txt, defaut='personnage'):
    t = sans_accents(nom + ' ' + txt)
    if re.search(r'\b(fort|poste|comptoir|post|house|agence)\b', t): return 'poste'
    if re.search(r'\btraite\b|\btraites\b|bataille|siege|combat|massacre|tue|proces|attaque', t): return 'evenement'
    if re.search(r'\bnaissance|\bnee?\b|bapteme|parti(e)? de', t): return 'migration'
    if re.search(r'mission|eglise|paroisse|meurt|mort|tombeau|chapelle|college', t): return 'religion'
    if re.search(r'expedition|guide|explor', t): return 'exploration'
    if re.search(r'commerce|marchand|convoi|journal|imprim', t): return 'commerce'
    return defaut

def an(x, defaut):
    try: return float(x) if x else float(defaut)
    except Exception: return float(defaut)

# ---- Tassé
g = json.load(open(f'{S}/tasse.geojson', encoding='utf-8'))
for f in g['features']:
    p = f['properties']
    etab = p['categorie'] == 'etablissement'
    y = an(p.get('annee'), 1878 if etab else 1800) or 1878
    feats.append({"type": "Feature", "geometry": f['geometry'], "properties": {
        "id": p['id'], "nom": f"{p['lieu']} : {p['nom_personne']}" if not etab else p['lieu'], "corpus": "Tassé",
        "theme": 'etablissement' if etab else theme_de(p['lieu'], p['texte']), "debut": y, "fin": y,
        "date_edtf": p.get('date', ''), "precision": "", "certitude": "approximative",
        "personnages": [] if etab else [p['nom_personne']], "description": p['texte'],
        "sources": p['source'], "note": f"Tome {'I' if p['tome'] == 1 else 'II'}, p. {p['pages']}."}})

# ---- Hafen MM (francophones seulement)
pers = json.load(open(f'{S}/hafen_personnes.json', encoding='utf-8'))
g = json.load(open(f'{S}/hafen.geojson', encoding='utf-8'))
TYPES = {'naissance': 'migration', 'mort': 'religion', 'construction': 'poste', 'commerce': 'commerce', 'chasse': 'commerce',
         'combat': 'evenement', 'rendez-vous': 'evenement', 'mariage': 'famille', 'hivernage': 'commerce'}
TYPES_FR = {'naissance': 'naissance', 'mort': 'mort', 'construction': 'construction', 'commerce': 'commerce', 'chasse': 'chasse',
            'combat': 'combat', 'rendez-vous': 'rendez-vous', 'mariage': 'mariage', 'hivernage': 'hivernage'}
SRC = "Hafen, LeRoy R. (dir.), The Mountain Men and the Fur Trade of the Far West, Glendale, Arthur H. Clark, 1965-1972"
# Fiches retirées après vérification (relevé automatique non confirmé ou contraire aux faits) : voir hafen_mm_retires.json.
RETIREES = json.load(open(f'{S}/hafen_mm_retires.json', encoding='utf-8'))['retirees']
couverts = set(); k = 0
for f in g['features']:
    q = f['properties']
    if not q['fr'] or not q['a']: continue
    P = pers[q['p']]; k += 1
    couverts.add(sans_accents(P['nom'].split(',')[0].split('(')[0]).split()[-1])
    nat = [TYPES_FR[t] for t in q['t'] if t in TYPES_FR]
    desc = (f"{P['nom']} ({P['dates'] or 'dates inconnues'}), {P['role']}. Sa biographie mentionne {q['lf']} en {q['a']}"
            + (f" (année déduite du contexte)" if not q['ax'] else '') + (f" : {', '.join(nat)}" if nat else '') + '.')
    if f"MM-{q['p']}-{k:04d}" in RETIREES: continue
    feats.append({"type": "Feature", "geometry": f['geometry'], "properties": {
        "id": f"MM-{q['p']}-{k:04d}", "nom": f"{q['lf']} : {P['nom']}", "corpus": "Hafen MM",
        "theme": next((TYPES[t] for t in q['t'] if t in TYPES), 'personnage'), "debut": float(q['a']), "fin": float(q['a']),
        "date_edtf": str(q['a']) if q['ax'] else f"{q['a']}~", "precision": "annee" if q['ax'] else "circa", "certitude": "approximative",
        "personnages": [P['nom']], "description": desc,
        "sources": f"{SRC}, vol. {P['vol']}, notice « {P['nom']} » par {P['auteur']}, p. {P['page']}-{P['fin']} ; mention p. {q['pg']}.",
        "note": "Lieu repéré automatiquement dans le texte de la notice (répertoire de 327 lieux de la traite) ; confirmé par une autre source de l'atlas (même lieu à 40 km près, même date à 2 ans près)."}})
n_mm = k
# retirer les points provisoires « H… » remplacés
avant = len(feats)
def remplace(p):
    if p['corpus'] != 'Hafen' or not p['id'].startswith('H'): return False
    noms = ' '.join(p.get('personnages') or [])
    return any(w in couverts for w in sans_accents(noms).replace(',', ' ').split())
feats = [f for f in feats if not remplace(f['properties'])]
retires = avant - len(feats)

# ---- Illinois français
g = json.load(open(f'{S}/illinois_francais.geojson', encoding='utf-8'))
peo = json.load(open(f'{S}/peoria_habitants.json', encoding='utf-8'))['habitants']
VIL = {'vieuxpeoria': 'old', 'maillet': 'maillet', 'traitepeoria': 'traite'}
CAT = {'colonial': 'poste', 'peoria': 'etablissement', 'kankakee': 'etablissement', 'presse': 'commerce', 'midwest': 'etablissement'}
for f in g['features']:
    p = f['properties']
    noms = [h['nom'] for h in peo if VIL.get(p['id']) == h['village']]
    desc = p['texte'] + (f" Habitants connus ({len(noms)}) : " + ' ; '.join(noms) + '.' if noms else '')
    feats.append({"type": "Feature", "geometry": f['geometry'], "properties": {
        "id": f"IL-{p['id']}", "nom": p['nom'], "corpus": "Illinois français",
        "theme": 'religion' if re.search(r'Viateur|Sainte-Anne|mission|paroisse', p['nom']) else CAT[p['categorie']],
        "debut": float(p['annee']), "fin": float(p['annee']), "date_edtf": str(p['annee']), "precision": "annee",
        "certitude": "approximative", "personnages": noms, "description": desc, "sources": p['source'], "note": ""}})
d['features'] = feats
json.dump(d, open(f'{R}/data/lieux.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
print('Hafen MM', n_mm, '; provisoires retirés', retires, '; total', len(feats), collections.Counter(f['properties']['corpus'] for f in feats))
