"""Adresses précises : emplacements reconstitués à partir des rues citées dans les sources.

Syntaxe dans un contexte : [Rue1/Rue2] = coin de deux rues, par exemple {bâtit sa maison au coin des rues Main et Elm [Main/Elm]}.
Plan de Saint-Louis vers 1800 (noms américains employés par Billon et Houck) : rues parallèles au fleuve
Main (rue Royale), Second (rue de l'Église), Third (rue des Granges) ; rues transversales du sud au nord
Cedar, Plum, Poplar, Spruce, Almond, Myrtle, Elm, Walnut, Market, Chestnut, Pine, Olive, Locust, Vine, Washington, Green.
Repères actuels : Market Street et l'ancien palais de justice (Fourth Street). Un îlot fait environ 300 pieds français.
Positions approximatives (± 50 m), calées sur le quadrillage actuel du centre-ville.
"""
import re

SAINT_LOUIS = {
    'paralleles': {'Front': -90.1845, 'Main': -90.1856, 'Second': -90.1868, 'Third': -90.1880, 'Fourth': -90.1893},
    'transversales': {'Cedar': 38.6170, 'Plum': 38.6180, 'Poplar': 38.6190, 'Spruce': 38.6200, 'Almond': 38.6210,
                      'Myrtle': 38.6219, 'Elm': 38.6228, 'Walnut': 38.6238, 'Market': 38.6252, 'Chestnut': 38.6262,
                      'Pine': 38.6271, 'Olive': 38.6280, 'Locust': 38.6289, 'Vine': 38.6295, 'Washington': 38.6301,
                      'Green': 38.6310},
}
NOMS_FR = {'Main': 'Main (rue Royale)', 'Second': 'Second (rue de l’Église)', 'Third': 'Third (rue des Granges)'}

ANGLE = {'NE': (1, 1), 'NO': (-1, 1), 'SE': (1, -1), 'SO': (-1, -1)}

def coin(rue1, rue2, angle=None):
    P, T = SAINT_LOUIS['paralleles'], SAINT_LOUIS['transversales']
    a, b = (rue2, rue1) if rue1 in T and rue2 in P else (rue1, rue2)
    if a not in P or b not in T:
        raise ValueError(f'Adresse inconnue : {rue1}/{rue2}')
    dx, dy = ANGLE.get(angle or '', (0, 0))
    lon, lat = P[a] + dx * 0.00018, T[b] + dy * 0.00014
    nom_angle = {'NE': 'angle nord-est', 'NO': 'angle nord-ouest', 'SE': 'angle sud-est', 'SO': 'angle sud-ouest'}.get(angle or '', 'coin')
    return round(lon, 5), round(lat, 5), f"Saint-Louis, {nom_angle} des rues {NOMS_FR.get(a, a)} et {b}"

def adresse(ctx, lieu):
    """Retourne (contexte nettoyé, (lon, lat, libellé) ou None)."""
    m = re.search(r'\s*\[([A-Za-z]+)/([A-Za-z]+)\]', ctx)
    if not m:
        return ctx, None
    propre = (ctx[:m.start()] + ctx[m.end():]).strip()
    if lieu != 'Saint-Louis':
        return propre, None
    a, b = m.group(1), m.group(2)
    P, T = SAINT_LOUIS['paralleles'], SAINT_LOUIS['transversales']
    if a in T and b in P:
        a, b = b, a
    if a not in P or b not in T:
        raise ValueError(f'Adresse inconnue : {a}/{b}')
    lib = f"Saint-Louis, coin des rues {NOMS_FR.get(a, a)} et {b}"
    return propre, (P[a], T[b], lib)

# Îlots numérotés du plan de Laclède (1764-1766), d'après les concessions énumérées par Billon (1886), p. 37-39.
# Numérotation recoupée par une dizaine d'adresses données ailleurs par Billon (Lefebvre, Martigny, Ride,
# Becquet, Denis, Maréchal, Gamache, Routier, Mme Chouteau, Valleau, Reynal, Didier, Lamoureux) :
#   îlots 1 à 12 : entre le fleuve et Main, du sud au nord (7 = place d'Armes, entre Walnut et Market) ;
#   îlots 27 à 41 : entre Main et Second, du nord au sud (34 = îlot de Laclède, entre Walnut et Market) ;
#   îlots 52 à 64 : entre Second et Third, du sud au nord (59 = îlot de l'église).
_TR = ['Cedar', 'Plum', 'Poplar', 'Spruce', 'Almond', 'Myrtle', 'Elm', 'Walnut', 'Market', 'Chestnut',
       'Pine', 'Olive', 'Locust', 'Vine', 'Washington', 'Green']
def _ilot_bornes(n):
    if 1 <= n <= 12:
        col, i = ('Front', 'Main'), n          # îlot 1 = Plum-Poplar
    elif 26 <= n <= 41:
        col, i = ('Main', 'Second'), 41 - n    # îlot 41 = Cedar-Plum, 34 = Walnut-Market
    elif 52 <= n <= 64:
        col, i = ('Second', 'Third'), n - 52   # îlot 52 = Cedar-Plum, 59 = Walnut-Market
    else:
        raise ValueError(f'Îlot {n} hors du plan reconstitué')
    return col, _TR[i], _TR[i + 1]

PARTIES = {  # (fraction est-ouest depuis l'ouest, fraction nord-sud depuis le sud, libellé)
    'N': (0.5, 0.75, 'moitié nord'), 'S': (0.5, 0.25, 'moitié sud'), 'E': (0.75, 0.5, 'moitié est'), 'O': (0.25, 0.5, 'moitié ouest'),
    'NE': (0.75, 0.75, 'quart nord-est'), 'NO': (0.25, 0.75, 'quart nord-ouest'),
    'SE': (0.75, 0.25, 'quart sud-est'), 'SO': (0.25, 0.25, 'quart sud-ouest'),
    'NE6': (0.75, 0.83, 'sixième nord-est'), 'NO6': (0.25, 0.83, 'sixième nord-ouest'), 'C6': (0.5, 0.5, 'sixième central'),
    'SE6': (0.75, 0.17, 'sixième sud-est'), 'SO6': (0.25, 0.17, 'sixième sud-ouest'), '': (0.5, 0.5, 'îlot entier'),
}

def _de(rue):
    return ("d'" if rue[0] in 'AEIOU' else 'de ') + rue

def ilot(n, partie=''):
    """Retourne (lon, lat, libellé) pour une partie d'un îlot numéroté du village de Saint-Louis."""
    P, T = SAINT_LOUIS['paralleles'], SAINT_LOUIS['transversales']
    (est, ouest), sud, nord = _ilot_bornes(n)
    fx, fy, lib = PARTIES[partie]
    lon = P[ouest] + (P[est] - P[ouest]) * (1 - fx)
    lat = T[sud] + (T[nord] - T[sud]) * fy
    entre = 'entre le fleuve et la rue Main' if est == 'Front' else f"entre les rues {NOMS_FR.get(est, est)} et {NOMS_FR.get(ouest, ouest)}"
    return round(lon, 5), round(lat, 5), f"Saint-Louis, îlot {n} ({lib})", f"{entre}, {_de(sud)} à {nord}"
