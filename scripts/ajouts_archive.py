# Corpus « Bibliothèque archive.org » : dépouillement des livres du domaine public d'archive.org sur les francophones
# d'Amérique du Nord hors Québec (novembre 2026, en cours, par lots). Un fichier texte par livre dans scripts/sources_archive/.
# Idempotent : retire toutes les fiches du corpus puis les recrée. À lancer après ajouts_2026_11b.py et avant hub.py.
import json, os, sys, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts', 'sources_archive'))
from archive_commun import fiches_livre, CORPUS

D = os.path.join(R, 'scripts', 'sources_archive')
LIVRES = [
    # (fichier, préfixe, description du livre, identifiant archive.org, citation)
    ('morice_1908.txt', 'MO',
     {'court': 'Morice (1908)',
      'ref': "Morice, Adrien-Gabriel (1908), Dictionnaire historique des Canadiens et des Métis français de l'Ouest, Québec, J.-P. Garneau"},
     'dictionnairehist00mori', lambda nom, ref: f"s.v. « {nom.split(',')[0].strip()} »"),
    ('larpenteur_1898.txt', 'LP',
     {'court': 'Larpenteur (1898)',
      'ref': "Larpenteur, Charles (1898), Forty Years a Fur Trader on the Upper Missouri, éd. Elliott Coues, New York, F. P. Harper, 2 vol."},
     lambda ref: 'fortyyearsfurtra01larpiala' if ref.startswith('vol. 1') else 'fortyyearsfurtra02larpiala',
     lambda nom, ref: ref),
    ('tasse_1878.txt', 'TA',
     {'court': 'Tassé (1878)',
      'ref': "Tassé, Joseph (1878), Les Canadiens de l'Ouest, Montréal, Compagnie d'imprimerie canadienne, 2 tomes"},
     lambda ref: 'cihm_33779' if ref.startswith('t. II') else 'cihm_33778',
     lambda nom, ref: ref),
]

d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
garde = [f for f in d['features'] if not f['properties']['corpus'].startswith(CORPUS)]
nouv, bilan = [], []
for fic, pre, livre, ident, citer in LIVRES:
    fs, inconnus, sans_date = fiches_livre(os.path.join(D, fic), pre, livre, ident, citer)
    nouv += fs
    bilan.append((livre['court'], len(fs), sans_date, sorted(inconnus)))
ids = [f['properties']['id'] for f in nouv]
dbl = [i for i, n in collections.Counter(ids).items() if n > 1]
assert not dbl, dbl
# Corrections et renvois particuliers
for f in nouv:
    p = f['properties']
    if p['id'] == 'MO-aubry-francois-xavier-santa-fe':
        p['note'] = "Morice date la mort d'Aubry de 1855 ; elle eut lieu le 18 août 1854 à Santa Fe. " + p['note']
        p['voir_aussi'].append({"url": "https://geolas2023.github.io/Atlas-Aubry/index.html#lieu=L31", "texte": "La mort d'Aubry dans l'Atlas Aubry →"})
    if p['corpus'].endswith('Tassé (1878)') and 'François-Xavier Aubry' in p['personnages']:
        p['voir_aussi'].append({"url": "https://geolas2023.github.io/Atlas-Aubry/", "texte": "Aubry dans l'Atlas Aubry →"})
d['features'] = garde + nouv
json.dump(d, open(f'{R}/data/lieux.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for b in bilan:
    print(f"{b[0]} : {b[1]} fiches ; {b[2]} lieux sans date ignorés" + (f" ; lieux inconnus : {b[3]}" if b[3] else ''))
print(f"Total Bibliothèque archive.org : {len(nouv)} ; atlas : {len(d['features'])}")
