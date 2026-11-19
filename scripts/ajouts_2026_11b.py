# Ajouts de novembre 2026, deuxième lot : dépouillement de treize des seize documents fournis par l'auteur.
# Les données sont dans scripts/sources_2026b/ (un module par corpus ou par groupe de sources ; voir l'en-tête de chacun).
#   « Atlas historique du Québec »  Frenette, Rivard et St-Hilaire (dir.), La francophonie nord-américaine (PUL, 2012)
#   « Franco-Amérique »             Louder et Waddell (dir.), Franco-Amérique (Septentrion, 2008)
#   « Nouvelle-France »             Margry, t. I (1876) ; Johnson, French Pathfinders (1905) ; Marchand, Ghost Empire (2005)
#   « Nouvelle-Angleterre »         Vermette, A Distinct Alien Race (2018) ; MacDonald (1898) ; Belisle (1907)
#   « Piste de l'Oregon »           Bergeron, La légende de l'Oregon était vraie
#   « Illinois français » (IF2-…)   McQuillan (1979) ; Papen (2006)
#   « Recherches » (R2-…)           allocution de Worcester ; Le Progrès du Golfe (1940)
#   « Recherches » (PV-…)           Étienne Provost à Saint-Louis, enquête versée depuis l'Atlas Aubry (dossier provost.html)
#   « Recherches » (DRV-…)          documents du Drive de l'auteur : Cimarron (Murphy 1980, parcours) et Bourbonnais (parcours 2016)
#   « Recherches » (LC78-…)         Lecompte, Pueblo, Hardscrabble, Greenhorn (1978) : épisodes francophones
#   « Recherches » (BF17-…)         Bolton, French Intrusions into New Mexico, 1749-1752 (1917)
#   « Recherches » (LR05-…)         Journal de Larocque, 1805 (éd. Burpee, 1911)
#   « Recherches » (WT85-…)         Wood et Thiessen, Early Fur Trade on the Northern Plains (1985)
# Idempotent : retire d'abord toutes les fiches dont l'identifiant porte un des préfixes ci-dessous, puis les recrée.
# À exécuter APRÈS scripts/ajouts_2026_11.py (qui recrée le corpus « Illinois français » et effacerait les fiches IF2-).
import json, os, sys, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts', 'sources_2026b'))
import atlas_historique, franco_amerique, nouvelle_france, nouvelle_angleterre, oregon, midwest, memoire, provost, drive_2026, lecompte_1978, bolton_1917, larocque_1805, wood_1985

MODULES = [atlas_historique, franco_amerique, nouvelle_france, nouvelle_angleterre, oregon, midwest, memoire, provost, drive_2026, lecompte_1978, bolton_1917, larocque_1805, wood_1985]
PREFIXES = ('AH-', 'FA-', 'NF-', 'NA-', 'OR-', 'IF2-', 'R2-', 'PV-', 'DRV-', 'LC78-', 'BF17-', 'LR05-', 'WT85-')
THEMES = {'poste', 'etablissement', 'famille', 'personnage', 'evenement', 'commerce', 'migration', 'exploration', 'religion', 'toponymie'}

d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
garde = [f for f in d['features'] if not f['properties']['id'].startswith(PREFIXES)]
nouv = [f for m in MODULES for f in m.fiches]

# contrôles
ids = [f['properties']['id'] for f in nouv]
doublons = [i for i, n in collections.Counter(ids).items() if n > 1]
assert not doublons, f'identifiants en double : {doublons}'
assert not set(ids) & {f['properties']['id'] for f in garde}, 'collision avec des identifiants existants'
for f in nouv:
    p = f['properties']; x, y = f['geometry']['coordinates']
    assert p['theme'] in THEMES, (p['id'], p['theme'])
    assert -170 < x < -50 and 15 < y < 72, (p['id'], x, y)
    assert p['debut'] <= p['fin'], p['id']

# La fiche L100 (carrefour Second et Lombard) a été retirée de l'Atlas Aubry le 14 novembre 2026 (Aubry et Provost
# ne se connaissaient pas) ; son contenu devient la fiche PV-05. On retire donc son miroir A-L100.
garde = [f for f in garde if f['properties']['id'] != 'A-L100']
d['features'] = garde + nouv
json.dump(d, open(f'{R}/data/lieux.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = collections.Counter(f['properties']['corpus'] for f in nouv)
print(f"{len(nouv)} fiches ajoutées ; total {len(d['features'])}")
for k, v in c.most_common(): print(f'  {k} : {v}')
