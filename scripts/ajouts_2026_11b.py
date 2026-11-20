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
#   « Recherches » (HK19-…)         Hocking, Terror on the Santa Fe Trail (2019)
# Idempotent : retire d'abord toutes les fiches dont l'identifiant porte un des préfixes ci-dessous, puis les recrée.
# À exécuter APRÈS scripts/ajouts_2026_11.py (qui recrée le corpus « Illinois français » et effacerait les fiches IF2-).
import json, os, sys, collections, peterson_1949, brackenridge_1816, presse_memoire, cormier_1957, gitlin_2010, provost_memoire, mcdermott_1941, shepard_1870, billon_1888, paquin_1893, recits_sioux, houzeau_1862, routhier_1893, beaugrand_1878, beaugrand_1890, daoust_1886, mcdermott_1979, roden_1949, nollette_famille, hamy_1903, temple_1958, trepanier_1965, isaacs_kankakee, amsbary_1904, kantowicz_1982, pease_1934, chaloult_2003, dionne_1910, snyder_leclaire, hanson_1976, swenson_1991, ancelet_retrouvailles, podruchny_2006, turner_2015, foxcurran_2016, audubon_1843, adair_braund, smith_heroes, maxwell_fort_sumner, radisson_1885, freiberger_1999, lemoine_1864, buies_1875, eccles_1983, forrest_2020, old_mines_2016, missouri_life_2013, bolton_1913, weber_1971, cleland_1950, symposium_2015, yealy_1935, fowler_1997, trudeau_2006, nicollet_1841, brule_kent_tremblay, blanchard_1882, kerouac_navy, volney_1803, audubon_1868, mcdermott_1965, frenchways_1969, rothensteiner_1928, toft_1988, murray_terranostra, monette_2009, denuziere_2013, dziembowski_2015, marienstras_2014, bouchard_elles_2011, balesi_2016, havard_2019, mcdermott_1952, ekberg_2015, hamalainen_2022, sanborn_1978, dary_2000, flagg_1838, werich_1920, audubon_1843v1, dallas_1985, morrison_2007, ottoson_1976, wpo_2000, lecompte_autobees, murray_1978, gutierrez_beaubien, howard_1971, bernand_2019, sagard_1632, viau_amerindia, skarsten_1964, chaput_1994, louder_1992, louder_2013, french_america_1993, blanchard_stmarc
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts', 'sources_2026b'))
import atlas_historique, franco_amerique, nouvelle_france, nouvelle_angleterre, oregon, midwest, memoire, provost, drive_2026, lecompte_1978, bolton_1917, larocque_1805, wood_1985, hocking_2019, gianini_1927, ebright_1994, montoya_2002, benoit_1975, chiniquy_1857, old_rock_house, provost_1913, kienzle_2017, brettell_2015, hyde_1968, antoine_2019, hafen_1954, tom_sun, journal_village_2011, st_paul_globe_1903

MODULES = [atlas_historique, franco_amerique, nouvelle_france, nouvelle_angleterre, oregon, midwest, memoire, provost, drive_2026, lecompte_1978, bolton_1917, larocque_1805, wood_1985, hocking_2019, gianini_1927, ebright_1994, montoya_2002, benoit_1975, chiniquy_1857, old_rock_house, provost_1913, kienzle_2017, brettell_2015, hyde_1968, antoine_2019, hafen_1954, tom_sun, journal_village_2011, st_paul_globe_1903, peterson_1949, brackenridge_1816, presse_memoire, cormier_1957, gitlin_2010, provost_memoire, mcdermott_1941, shepard_1870, billon_1888, paquin_1893, recits_sioux, houzeau_1862, routhier_1893, beaugrand_1878, beaugrand_1890, daoust_1886, mcdermott_1979, roden_1949, nollette_famille, hamy_1903, temple_1958, trepanier_1965, isaacs_kankakee, amsbary_1904, kantowicz_1982, pease_1934, chaloult_2003, dionne_1910, snyder_leclaire, hanson_1976, swenson_1991, ancelet_retrouvailles, podruchny_2006, turner_2015, foxcurran_2016, audubon_1843, adair_braund, smith_heroes, maxwell_fort_sumner, radisson_1885, freiberger_1999, lemoine_1864, buies_1875, eccles_1983, forrest_2020, old_mines_2016, missouri_life_2013, bolton_1913, weber_1971, cleland_1950, symposium_2015, yealy_1935, fowler_1997, trudeau_2006, nicollet_1841, brule_kent_tremblay, blanchard_1882, kerouac_navy, volney_1803, audubon_1868, mcdermott_1965, frenchways_1969, rothensteiner_1928, toft_1988, murray_terranostra, monette_2009, denuziere_2013, dziembowski_2015, marienstras_2014, bouchard_elles_2011, balesi_2016, havard_2019, mcdermott_1952, ekberg_2015, hamalainen_2022, sanborn_1978, dary_2000, flagg_1838, werich_1920, audubon_1843v1, dallas_1985, morrison_2007, ottoson_1976, wpo_2000, lecompte_autobees, murray_1978, gutierrez_beaubien, howard_1971, bernand_2019, sagard_1632, viau_amerindia, skarsten_1964, chaput_1994, louder_1992, louder_2013, french_america_1993, blanchard_stmarc]
PREFIXES = ('AH-', 'FA-', 'NF-', 'NA-', 'OR-', 'IF2-', 'R2-', 'PV-', 'DRV-', 'LC78-', 'BF17-', 'LR05-', 'WT85-', 'HK19-', 'GI27-', 'EB94-', 'MT02-', 'BN75-', 'CQ57-', 'RH98-', 'PV13-', 'LS17-', 'BR15-', 'GB68-', 'MA19-', 'HF54-', 'TS11-', 'LJ11-', 'SPG03-', 'PT49-', 'BK16-', 'PRM-', 'CO57-', 'GT10-', 'PVM-', 'MD41-', 'SH70-', 'BL88-', 'PQ93-', 'DC13-', 'HZ62-', 'RT93-', 'BG78-', 'BG90-', 'DA86-', 'MD79-', 'RD49-', 'NOL-', 'HM03-', 'TP58-', 'TR65-', 'ISK-', 'AM04-', 'KZ82-', 'PE34-', 'CH03-', 'DN10-', 'SNL-', 'HW76-', 'SW91-', 'ANC-', 'PD06-', 'TU15-', 'FX16-', 'AU43-', 'AD05-', 'RSH-', 'MFS-', 'RD85-', 'FB99-', 'LM64-', 'BU75-', 'EC83-', 'FO20-', 'OM16-', 'ML13-', 'BO13-', 'WB71-', 'CL50-', 'FT15-', 'YE35-', 'FW97-', 'GS06-', 'NI41-', 'KE76-', 'TB15-', 'BL82-', 'KR43-', 'VO03-', 'AB68-', 'FMV65-', 'FFW69-', 'ROT28-', 'TFT88-', 'TNM-', 'MON09-', 'DZ13-', 'DZ15-', 'MR14-', 'EF11-', 'BA16-', 'HV19-', 'MD52-', 'EK15-', 'HS22-', 'SB78-', 'DY00-', 'FL38-', 'WE20-', 'AJ43-', 'DA85-', 'JM07-', 'OT76-', 'WP00-', 'LA57-', 'MU78-', 'PSG-', 'HO71-', 'BE19-', 'SG32-', 'VIA-', 'SK64-', 'CP94-', 'LO92-', 'LO13-', 'FR93-', 'BSM-')
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
