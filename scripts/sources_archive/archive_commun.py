# Outils communs aux dépouillements des livres d'archive.org (corpus « Bibliothèque archive.org »).
# Chaque livre est noté dans un fichier texte, une ligne par personne :
#     NOM, Prénoms | naissance (année, lieu) | lieu, année; lieu, année-année; … | référence (facultative : page ou chapitre)
# Les lieux sont résolus par le répertoire lieux_ouest.G ; une fiche par lieu daté. Les lieux sans date sont ignorés.
import re, unicodedata
from lieux_ouest import G

CORPUS = 'archive.org'  # préfixe : chaque livre forme un corpus « archive.org · <livre> »
CERT = {'c': 'certaine', 'a': 'approximative', 'h': 'hypothetique'}
RELIGION = re.compile(r"\b(Sœur|Mère|abbé|Mgr|O\.M\.I\.|frère|père\b|Rév)", re.I)
EVENEMENTS = {('Grenouillère', 1816), ('Batoche', 1885), ('Fish Creek', 1885), ('Frog Lake', 1885), ('Duck Lake', 1885), ('Regina', 1885)}

def slug(s):
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:28]

def beau_nom(brut):
    """« LAGIMODIÈRE, Jean-Baptiste » → « Jean-Baptiste Lagimodière »."""
    brut = re.sub(r'\s*\((bis|ter)\)', '', brut)
    if ',' not in brut: return brut.strip().title()
    nom, prenoms = [x.strip() for x in brut.split(',', 1)]
    nom = ' '.join(w if w in ('de', 'la', 'du', 'des', 'dit') else w.capitalize() for w in nom.lower().split())
    nom = re.sub(r"-(\w)", lambda m: '-' + m.group(1).upper(), nom)
    m = re.match(r"^(.*?)\s*(\(.*\))?$", prenoms)
    p, extra = m.group(1).strip(), (m.group(2) or '')
    if p in ('X.', ''): return f"{nom}{(' ' + extra) if extra else ''}".strip()
    return f"{p} {nom} {extra}".strip()

def dates(seg):
    """Extrait (edtf, an_debut) d'un segment « lieu, 1804-05 » ; None si pas de date."""
    m = re.search(r'(c\.\s*)?(\d{4})(?:-(\d{2,4}))?(s)?\s*$', seg)
    if not m: return None, None, seg.strip()
    lieu = seg[:m.start()].strip().rstrip(',').strip()
    a = int(m.group(2)); circa = '~' if m.group(1) else ''
    if m.group(4): return f"{a}/{a + 9}", a, lieu
    if m.group(3):
        b = m.group(3); b = int(str(a)[:4 - len(b)] + b) if len(b) < 4 else int(b)
        if b < a: b = a
        return f"{a}{circa}/{b}{circa}", a, lieu
    return f"{a}{circa}", a, lieu

def bornes(edtf):
    p = edtf.replace('~', '').split('/')
    d = float(p[0]); f = float(p[-1]) + (0.999 if '/' in edtf else 0)
    return d, round(f, 3), ('circa' if '~' in edtf else 'annee')

def cle_personne(brut):
    """Clé de rapprochement : nom de famille sans particule + premier prénom, sans accents."""
    sans = lambda t: unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode()
    nom, _, pren = brut.partition(',')
    nom = re.sub(r'^(LA|LE|DE|DU|DES)\s+', '', sans(nom).upper().strip())
    nom = re.sub(r'^(LA|LE|DE|DU|DES)\s+', '', nom)
    pren = re.sub(r'\(.*?\)', '', sans(pren)).strip().lower()
    return nom.split()[0] if nom else '', (pren.split() or [''])[0].rstrip('.')

def lire_contextes(fichier):
    """Fichier « NOM, Prénoms | lieu, année {contexte}; … » → {(clé, année): contexte}."""
    out = {}
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#') or '|' not in ligne: continue
        brut, segs = [x.strip() for x in ligne.split('|', 1)]
        k = cle_personne(brut)
        for sg in re.split(r';(?![^{]*\})', segs):
            m = re.search(r'(\d{4})[^{]*\{(.*?)\}', sg)
            if m:
                lieu = sg[:m.start()].strip().rstrip(',')
                out.setdefault((k, int(m.group(1))), []).append((lieu, m.group(2).strip().rstrip('.')))
    return out

def _mots(t):
    t = unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode().lower()
    return {w for w in re.findall(r'[a-z]{4,}', t)} - {'fort', 'lake', 'river', 'riviere', 'house', 'saint', 'sainte', 'grand', 'grande', 'haut', 'haute', 'lower', 'upper'}

REGIONS = {'saskatchewan', 'colombie', 'columbia', 'missouri', 'manitoba', 'oregon', 'rouge', 'dakota', 'minnesota',
           'athabasca', 'athabaska', 'mackenzie', 'californie', 'california', 'texas', 'wisconsin', 'illinois', 'assiniboia', 'ouest'}

def choisir_contexte(cands, lieu, lieu_fr, n_segments_annee):
    """Retient le contexte dont le lieu correspond ; sans correspondance, seulement s'il n'y a aucune ambiguïté."""
    cible = _mots(lieu) | _mots(lieu_fr)
    for l, c in cands:
        if _mots(l) & cible: return c
    if len(cands) == 1 and n_segments_annee == 1 and _mots(cands[0][0]) <= REGIONS: return cands[0][1]
    return ''

def fiches_livre(fichier, prefixe, livre, ident, citer, lien_recherche=True, theme_defaut='personnage', contextes=None):
    """Construit les fiches d'un livre. citer(nom_brut, ref) → texte de la référence (ex. « s.v. LAGIMODIÈRE »)."""
    out, inconnus, sans_date = [], set(), 0
    vus = {}
    for ligne in open(fichier, encoding='utf-8'):
        if not ligne.strip() or ligne.startswith('#'): continue
        parts = [x.strip() for x in ligne.rstrip('\n').split('|')]
        brut, naissance, lieux = parts[0], parts[1], parts[2]
        ref = parts[3] if len(parts) > 3 else ''
        nom = beau_nom(brut)
        segs = [s.strip() for s in re.split(r';(?![^{]*\})', lieux) if s.strip()]
        lus = []
        annees = [int(m.group(1)) for m in (re.search(r'(\d{4})', re.sub(r'\{.*?\}', '', x)) for x in segs) if m]
        for s in segs:
            mc = re.search(r'\{(.*?)\}\s*$', s)
            ctx = mc.group(1).strip().rstrip('.') if mc else ''
            if mc: s = s[:mc.start()].strip()
            edtf, an, lieu = dates(s)
            if not ctx and contextes and an and lieu in G:
                c = choisir_contexte(contextes.get((cle_personne(brut), an), []), lieu, G[lieu][3], annees.count(an))
                ctx = (c[0].lower() + c[1:]) if c and not c[:2].isupper() else c
            if lieu not in G: inconnus.add(lieu); continue
            if not edtf: sans_date += 1; continue
            lus.append((lieu, edtf, an, ctx))
        autres = [G[l][3] for l, _, _, _ in lus]
        for lieu, edtf, an, ctx in lus:
            lon, lat, cert, lieu_fr = G[lieu]
            base = f"{prefixe}-{slug(brut)}-{slug(lieu)[:10]}"
            k = vus.get(base, 0); vus[base] = k + 1
            ident_fiche = base + (f"-{k + 1}" if k else '')
            if RELIGION.search(brut): theme = 'religion'
            elif (lieu, an) in EVENEMENTS: theme = 'evenement'
            elif lieu.startswith('Fort') or 'House' in lieu: theme = 'poste'
            else: theme = theme_defaut
            if ctx and re.search(r"\b(tué|tuée|massacr|bataille|combat|assassin|noyé|attaque|siège (?:du|de|d.)|capture|prise du fort)", ctx) and theme != 'religion': theme = 'evenement'
            fem = 'e' if re.search(r'Sœur|Mère|Marie|Zoé|Lisette|Reine|demoiselles|Charlotte|Louise|Josephte|Suzanne|Domitilde|Emilie|Élisabeth|Elizabeth|Henriette|Virginie|Marguerite|Adèle|Julie|Geneviève|Catherine|Paulette|\(f\)', brut) else ''
            mn = re.match(r'^(\d{4})(?:,\s*(.+))?$', naissance)
            ne = (f", né{fem} en {mn.group(1)}" + (f" à {mn.group(2)}" if mn.group(2) else '')) if mn else (f", né{fem} à {naissance}" if naissance else '')
            ailleurs = [a for a in autres if a != lieu_fr]
            quand = edtf.replace('/', '-') if '~' not in edtf else 'vers ' + edtf.replace('~', '').replace('/', '-')
            if ctx:
                if re.match(r"(sa|son|ses|le|la|les|l')\b", ctx) or re.search(r"\b(il|elle)\b", ctx[:70]):
                    phrase = f"{nom}{ne}. {ctx[0].upper() + ctx[1:]}."
                else:
                    phrase = f"{nom}{ne}{',' if ne else ''} {ctx}."
                desc = (f"{lieu_fr[0].upper() + lieu_fr[1:]}, {quand}. {phrase} "
                        f"D'après {livre['court']}."
                    + (f" Autres lieux de l'entrée : {', '.join(dict.fromkeys(ailleurs))}." if ailleurs else ''))
            else:
                desc = (f"D'après {livre['court']}, {nom}{ne}{',' if ne else ''} est associé{fem} à ce lieu ({lieu_fr}) en {quand}."
                    + (f" Autres lieux de l'entrée : {', '.join(dict.fromkeys(ailleurs))}." if ailleurs else ''))
            idf = ident(ref) if callable(ident) else ident
            url = f"https://archive.org/details/{idf}" + (f"?q={re.sub(r'[^A-Za-zÀ-ÿ]+', '+', brut.split(',')[0].strip())}" if lien_recherche else '')
            d, f, prec = bornes(edtf)
            out.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": {
                "id": ident_fiche, "nom": f"{lieu_fr[0].upper() + lieu_fr[1:]} : {nom}", "corpus": f"{CORPUS} · {livre['court']}", "theme": theme,
                "debut": d, "fin": f, "date_edtf": edtf, "precision": prec, "certitude": CERT[cert],
                "personnages": [nom], "description": desc,
                "sources": f"{livre['ref']}, {citer(brut, ref)} ; texte intégral : archive.org, {idf}.",
                "note": "Repérage dans le texte intégral (OCR) d'archive.org, à vérifier dans le livre ; localisation attribuée par l'atlas.",
                "livre": livre['court'],
                "voir_aussi": [{"url": url, "texte": f"Lire {livre['court']} sur archive.org →"}]}})
    return out, inconnus, sans_date
