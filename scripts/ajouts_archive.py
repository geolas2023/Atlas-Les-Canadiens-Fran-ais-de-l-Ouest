# Corpus « Bibliothèque archive.org » : dépouillement des livres du domaine public d'archive.org sur les francophones
# d'Amérique du Nord hors Québec (novembre 2026, en cours, par lots). Un fichier texte par livre dans scripts/sources_archive/.
# Idempotent : retire toutes les fiches du corpus puis les recrée. À lancer après ajouts_2026_11b.py et avant hub.py.
import json, os, sys, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts', 'sources_archive'))
from archive_commun import fiches_livre, lire_contextes, CORPUS

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
    ('billon_1886.txt', 'BI',
     {'court': 'Billon (1886)',
      'ref': "Billon, Frederic L. (1886), Annals of St. Louis in its Early Days under the French and Spanish Dominations, Saint-Louis"},
     'cihm_00427', lambda nom, ref: ref),
    ('hamon_1891.txt', 'HA',
     {'court': 'Hamon (1891)',
      'ref': "Hamon, Édouard (1891), Les Canadiens-français de la Nouvelle-Angleterre, Québec, N.-S. Hardy"},
     'cihm_39098', lambda nom, ref: ref),
    ('dugas_1896.txt', 'DU',
     {'court': 'Dugas (1896)',
      'ref': "Dugas, Georges (1896), L'Ouest canadien : sa découverte par le sieur de La Vérendrye, son exploitation par les compagnies de traiteurs jusqu'à l'année 1822, Montréal, Cadieux et Derome"},
     'cihm_30150', lambda nom, ref: ref),
    ('dugas_1906.txt', 'DH',
     {'court': 'Dugas (1906)',
      'ref': "Dugas, Georges (1906), Histoire de l'Ouest canadien de 1822 à 1869 : époque des troubles, Montréal, Beauchemin"},
     'histoiredelouest00dugauoft', lambda nom, ref: ref),
    ('dugas_1890.txt', 'DV',
     {'court': 'Dugas (1890)',
      'ref': "Dugas, Georges (1890), Un voyageur des pays d'en haut, Montréal, C.-O. Beauchemin et fils"},
     'unvoyageurdespay00duga', lambda nom, ref: ref),
    ('dugas_1883.txt', 'DG',
     {'court': 'Dugas (1883)',
      'ref': "Dugas, Georges (1883), La première Canadienne du Nord-Ouest, ou biographie de Marie-Anne Gaboury, Montréal, Librairie Saint-Joseph"},
     'lapremirecanadi00duga', lambda nom, ref: ref),
    ('dugas_1889.txt', 'DP',
     {'court': 'Dugas (1889)',
      'ref': "Dugas, Georges (1889), Monseigneur Provencher et les missions de la Rivière-Rouge, Montréal, C.-O. Beauchemin"},
     'monseigneurprove00duga', lambda nom, ref: ref),
    ('houck_1908_v2.txt', 'HK',
     {'court': 'Houck (1908), vol. 2',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 2"},
     'historyofmissour02houc', lambda nom, ref: ref),
    ('houck_1908_v1.txt', 'H1',
     {'court': 'Houck (1908), vol. 1',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 1"},
     'historyofmissour01houc', lambda nom, ref: ref),
    ('houck_1908_v3.txt', 'H3',
     {'court': 'Houck (1908), vol. 3',
      'ref': "Houck, Louis (1908), A History of Missouri from the Earliest Explorations and Settlements until the Admission of the State into the Union, Chicago, R. R. Donnelley, vol. 3"},
     'historyofmissour03houc', lambda nom, ref: ref),
    ('spanish_regime_1909_v1.txt', 'SR',
     {'court': 'Houck (1909), Spanish Regime, vol. 1',
      'ref': "Houck, Louis (1909), The Spanish Regime in Missouri: A Collection of Papers and Documents Relating to Upper Louisiana, Chicago, R. R. Donnelley, vol. 1"},
     'spanishregimeinm01houc', lambda nom, ref: ref),
    ('spanish_regime_1909_v2.txt', 'SS',
     {'court': 'Houck (1909), Spanish Regime, vol. 2',
      'ref': "Houck, Louis (1909), The Spanish Regime in Missouri: A Collection of Papers and Documents Relating to Upper Louisiana, Chicago, R. R. Donnelley, vol. 2"},
     'spanishregimeinm02houc', lambda nom, ref: ref),
    ('chittenden_1902_v1.txt', 'CH',
     {'court': 'Chittenden (1902), vol. 1',
      'ref': "Chittenden, Hiram Martin (1902), The American Fur Trade of the Far West, New York, Francis P. Harper, vol. 1"},
     'americanfurtrade01chit', lambda nom, ref: ref),
    ('chittenden_1902_v2.txt', 'CI',
     {'court': 'Chittenden (1902), vol. 2-3',
      'ref': "Chittenden, Hiram Martin (1902), The American Fur Trade of the Far West, New York, Francis P. Harper, vol. 2-3"},
     'americanfurtrade00chit_0', lambda nom, ref: ref),
    ('franchere_1854.txt', 'FR',
     {'court': 'Franchère (1854)',
      'ref': "Franchère, Gabriel (1854), Narrative of a Voyage to the Northwest Coast of America in the Years 1811, 1812, 1813 and 1814, trad. J. V. Huntington, New York, Redfield"},
     'cihm_35175', lambda nom, ref: ref),
    ('masson_1889_v1.txt', 'MA',
     {'court': 'Masson (1889)',
      'ref': "Masson, Louis-Rodrigue (1889), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 1, « Liste des bourgeois, commis, engagés et voyageurs de la Compagnie du Nord-Ouest après la fusion de 1804 »"},
     'cihm_30414', lambda nom, ref: ref),
    ('masson_1889_v1_recits.txt', 'MB',
     {'court': 'Masson (1889), récits',
      'ref': "Masson, Louis-Rodrigue (1889), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 1 : journaux de Malhiot (1804-1805), McDonnell (1793-1795), Larocque (1804-1805) et Charles McKenzie (1804-1806)"},
     'cihm_30414', lambda nom, ref: ref),
    ('masson_1890_v2.txt', 'MC',
     {'court': 'Masson (1890)',
      'ref': "Masson, Louis-Rodrigue (1890), Les Bourgeois de la Compagnie du Nord-Ouest, Québec, A. Côté, vol. 2 (deuxième série)"},
     'cihm_30415', lambda nom, ref: ref),
    ('coues_1897_v1.txt', 'CO',
     {'court': 'Coues (1897), vol. 1',
      'ref': "Coues, Elliott (dir.) (1897), New Light on the Early History of the Greater Northwest. The Manuscript Journals of Alexander Henry and of David Thompson, New York, F. P. Harper, vol. 1"},
     'newlightonearlyh01henr', lambda nom, ref: ref),
    ('coues_1897_v2.txt', 'CQ',
     {'court': 'Coues (1897), vol. 2',
      'ref': "Coues, Elliott (dir.) (1897), New Light on the Early History of the Greater Northwest. The Manuscript Journals of Alexander Henry and of David Thompson, New York, F. P. Harper, vol. 2"},
     'newlightonearlyh02henr', lambda nom, ref: ref),
    ('perrault_1910.txt', 'PE',
     {'court': 'Perrault (1910)',
      'ref': "Perrault, Jean-Baptiste (1909-1910), « Narrative of the Travels and Adventures of a Merchant Voyageur… 1783-1820 », éd. J. S. Fox, Michigan Pioneer and Historical Collections, vol. 37"},
     'michiganhistoric37michuoft', lambda nom, ref: ref),
    ('cox_1832.txt', 'CX',
     {'court': 'Cox (1832)',
      'ref': "Cox, Ross (1832), Adventures on the Columbia River, New York, J. & J. Harper"},
     'adventuresoncolu00coxr', lambda nom, ref: ref),
    ('ross_1855.txt', 'RS',
     {'court': 'Ross (1855)',
      'ref': "Ross, Alexander (1855), The Fur Hunters of the Far West, Londres, Smith, Elder & Co., 2 vol."},
     'cihm_40228', lambda nom, ref: ref),
    ('burton_1896.txt', 'BU',
     {'court': 'Burton (1896)',
      'ref': "Burton, Clarence Monroe (1896), Cadillac's Village, or Detroit under Cadillac, with List of Property Owners, 1701 to 1710, Détroit"},
     'cadillacsvillage00burt', lambda nom, ref: ref),
    ('hamlin_1884.txt', 'HM',
     {'court': 'Hamlin (1884)',
      'ref': "Hamlin, Marie Caroline Watson (1884), Legends of le Détroit, Détroit, Thorndike Nourse"},
     'legendsofledtr00haml', lambda nom, ref: ref),
    ('mphc_1904_v33.txt', 'CP',
     {'court': 'Cadillac Papers (1904)',
      'ref': "Burton, C. M. (éd.) (1904), « Cadillac Papers », Michigan Pioneer and Historical Collections, vol. 33, Lansing"},
     'michiganhistoric33michuoft', lambda nom, ref: ref),
    ('mphc_1905_v34.txt', 'CQ2',
     {'court': 'Cadillac Papers (1905)',
      'ref': "Burton, C. M. (éd.) (1905), « Cadillac Papers » (suite), « Cadillac's Records » et « Detroit Rulers », Michigan Pioneer and Historical Collections, vol. 34, Lansing"},
     'michiganhistoric34michuoft', lambda nom, ref: ref),
    ('ross_catlin_1898.txt', 'RC',
     {'court': 'Ross et Catlin (1898)',
      'ref': "Ross, Robert B., et George B. Catlin (1898), Landmarks of Detroit: a History of the City, Détroit, Evening News Association"},
     'landmarksofdetr00ross', lambda nom, ref: ref),
    ('andreas_1884.txt', 'AN',
     {'court': 'Andreas (1884)',
      'ref': "Andreas, A. T. (1884), History of Chicago from the Earliest Period to the Present Time, Chicago, vol. 1"},
     'historyofchicago01andr', lambda nom, ref: ref),
    ('kankakee_1892.txt', 'KK',
     {'court': 'Kankakee (1892)',
      'ref': "Portrait and Biographical Record of Kankakee County, Illinois (1892), Chicago, Lake City Publishing Co."},
     'portraitbiographica00lake', lambda nom, ref: ref),
    ('nebraska_morton_1905.txt', 'NM', {'court': 'Morton (1905)', 'ref': "J. Sterling Morton (dir.), Illustrated History of Nebraska, vol. 1 (1905)"}, 'cu31924092232747', lambda nom, ref: ref),
    ('nebraska_transactions_1885.txt', 'NT', {'court': 'NSHS (1885)', 'ref': "Transactions and Reports of the Nebraska State Historical Society, vol. 1 (1885)"}, 'transactionsrepo00nebr', lambda nom, ref: ref),
    ('nebraska_placenames_1925.txt', 'NP', {'court': 'Fitzpatrick (1925)', 'ref': "Lilian L. Fitzpatrick, Nebraska Place-Names (1925)"}, 'bwb_P8-BLU-581', lambda nom, ref: ref),
    ('nebraska_dakota_1893.txt', 'ND', {'court': 'Warner (1893)', 'ref': "M. M. Warner, Warner's History of Dakota County, Nebraska (1893)"}, 'cu31924028874141', lambda nom, ref: ref),
    ('nebraska_reminiscences_1916.txt', 'NR', {'court': 'DAR (1916)', 'ref': "Nebraska Society of the Daughters of the American Revolution, Collection of Nebraska Pioneer Reminiscences (1916)"}, 'collectionofnebr00daug', lambda nom, ref: ref),
    ('nebraska_andreas_1882.txt', 'NB', {'court': 'Andreas (1882)', 'ref': "A. T. Andreas (éd.), History of the State of Nebraska (1882), Chicago, Western Historical Company"}, 'https://kancoll.org/books/andreas_ne/hon_tabl.html', lambda nom, ref: ref),
    ('idaho_rees_1918.txt', 'IR', {'court': 'Rees (1918)', 'ref': "John E. Rees, Idaho Chronology, Nomenclature, Bibliography (1918)"}, 'idahochronologyn00reesrich', lambda nom, ref: ref),
    ('idaho_brosnan_1918.txt', 'IB', {'court': 'Brosnan (1918)', 'ref': "Cornelius J. Brosnan, History of the State of Idaho (1918)"}, 'historyofstateof00bros', lambda nom, ref: ref),
    ('idaho_northidaho_1903.txt', 'IN', {'court': 'North Idaho (1903)', 'ref': "An Illustrated History of North Idaho (1903), Western Historical Publishing Co."}, 'illustratedhisto00slwe', lambda nom, ref: ref),
    ('idaho_driggs_1926.txt', 'ID', {'court': 'Driggs (1926)', 'ref': "B. W. Driggs, History of Teton Valley, Idaho (1926)"}, 'driggs', lambda nom, ref: ref),
    ('idaho_hawley_1920.txt', 'IH', {'court': 'Hawley (1920)', 'ref': "James H. Hawley (dir.), History of Idaho: The Gem of the Mountains, vol. 1 (1920)"}, 'historyofidahoge01hawl', lambda nom, ref: ref),
]

d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
garde = [f for f in d['features'] if not f['properties']['corpus'].startswith(CORPUS)]
from adresses import coin, ilot
from lieux_ouest import G as _G
from archive_commun import cle_personne, beau_nom, slug

def appliquer_adresses(fs, fichier, pre, livre, ident):
    """Place à leur adresse précise les fiches dont la source donne un coin de rues ; crée la fiche si elle n'existe pas."""
    deplacees = creees = 0
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#'): continue
        brut, annees, rues, angle, quoi, page = [x.strip() for x in ligne.split('|')]
        r1, r2 = rues.split('/')
        lon, lat, lib = coin(r1, r2, angle or None)
        a0 = int(annees[:4])
        a1 = int(annees.split('-')[1]) if '-' in annees else a0
        k = cle_personne(brut)
        cible = [f for f in fs if f['properties']['id'].endswith(tuple(['-saint-loui', '-saint-loui-2', '-saint-loui-3', '-saint-loui-4']))
                 and cle_personne(f['properties'].get('_brut', '')) == k and int(f['properties']['debut']) == a0]
        nom = beau_nom(brut)
        if cible:
            f = cible[0]; p = f['properties']
            f['geometry']['coordinates'] = [lon, lat]
            p['nom'] = f"{lib} : {nom}"
            p['certitude'] = 'approximative'
            p['description'] += f" Emplacement : {lib.split(', ', 1)[1]} ({quoi}), d'après Billon, {page} ; position reconstituée sur le plan du village (± 50 m)."
            deplacees += 1
        else:
            idf = f"{pre}-{slug(brut)}-adr-{slug(r1 + '-' + r2)}"
            fs.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": {
                "id": idf, "nom": f"{lib} : {nom}", "corpus": f"{CORPUS} · {livre['court']}", "theme": 'personnage',
                "date_edtf": f"{a0}/{a1}" if a1 != a0 else str(a0), "debut": a0, "fin": a1 + 0.999, "precision": "annee",
                "certitude": 'approximative', "personnages": [nom],
                "description": f"{lib}, {a0 if a0 == a1 else f'{a0}-{a1}'}. {nom} {quoi}. D'après {livre['court']} ; position reconstituée sur le plan du village (± 50 m).",
                "sources": f"{livre['ref']}, {page} ; texte intégral : archive.org, {ident}.",
                "note": "Adresse tirée du texte intégral (OCR) d'archive.org ; l'emplacement du coin de rues est reconstitué sur le quadrillage actuel du centre-ville de Saint-Louis.",
                "livre": livre['court'], "voir_aussi": [{"url": f"https://archive.org/details/{ident}", "texte": "Lire le livre sur archive.org →"}]}})
            creees += 1
    print(f"  adresses : {deplacees} fiches placées à leur adresse, {creees} fiches d'adresse créées")
    return fs

def appliquer_ilots(fs, fichier, livre):
    """Place dans son îlot numéroté la fiche restée au point générique de Saint-Louis."""
    x0, y0 = _G['Saint-Louis'][:2]
    n_ok, manques = 0, []
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#'): continue
        brut, annee, num, partie, page = [x.strip() for x in ligne.split('|')]
        lon, lat, lib, entre = ilot(int(num), partie)
        k = cle_personne(brut)
        cible = [f for f in fs if cle_personne(f['properties'].get('_brut', '')) == k and int(f['properties']['debut']) == int(annee)
                 and abs(f['geometry']['coordinates'][0] - x0) < 1e-6 and abs(f['geometry']['coordinates'][1] - y0) < 1e-6]
        if not cible:
            manques.append(brut); continue
        f = cible[0]; p = f['properties']
        f['geometry']['coordinates'] = [lon, lat]
        p['nom'] = f"{lib} : {beau_nom(brut)}"
        p['certitude'] = 'approximative'
        p['description'] += (f" Emplacement : {lib.split(', ', 1)[1]} du plan du village tracé par Laclède et Auguste Chouteau, {entre}"
                             f" (concessions de 1765 énumérées par Billon, {page}) ; position reconstituée sur le quadrillage actuel (± 50 m).")
        n_ok += 1
    print(f"  îlots : {n_ok} fiches placées dans leur îlot" + (f" ; non trouvées : {manques}" if manques else ''))
    return fs

nouv, bilan = [], []
for fic, pre, livre, ident, citer in LIVRES:
    ctxf = os.path.join(D, fic.replace('.txt', '_contextes.txt'))
    fs, inconnus, sans_date = fiches_livre(os.path.join(D, fic), pre, livre, ident, citer,
                                           contextes=lire_contextes(ctxf) if os.path.exists(ctxf) else None)
    adrf = os.path.join(D, fic.replace('.txt', '_adresses.txt'))
    if os.path.exists(adrf):
        fs = appliquer_adresses(fs, adrf, pre, livre, ident)
    ilf = os.path.join(D, fic.replace('.txt', '_ilots.txt'))
    if os.path.exists(ilf):
        fs = appliquer_ilots(fs, ilf, livre)
    nouv += fs
    bilan.append((livre['court'], len(fs), sans_date, sorted(inconnus)))
for f in nouv: f['properties'].pop('_brut', None)
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
