# Génère provost.html et provost-en.html : dossier Étienne Provost (v. 1785-1850).
# Enquête faite d'abord pour l'Atlas Aubry, retirée de cet atlas le 14 novembre 2026 (Aubry et Provost ne se connaissaient pas),
# complété par les fiches de l'atlas (Hafen MM, Atlas historique du Québec, Recherches PV-…).
# Relancer après scripts/ajouts_2026_11b.py :  python3 scripts/page_provost.py
import json, os, re, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(f'{R}/data/lieux.geojson', encoding='utf-8'))
F = {f['properties']['id']: f['properties'] for f in d['features']}
mm = sorted([p for p in F.values() if p['corpus'] == 'Hafen MM' and 'Etienne Provost' in (p.get('personnages') or [])],
            key=lambda p: (p['debut'], p['id']))
e = html.escape
STYLE = open(f'{R}/montagnards.html', encoding='utf-8').read()
STYLE = STYLE[STYLE.find('<style>'):STYLE.find('</style>') + 8]
AUBRY = 'https://geolas2023.github.io/Atlas-Aubry/'

def lien(i, txt=None):
    return f'<a href="index.html#{e(i)}">{e(txt or i)}</a>'

T = {
'fr': dict(
  titre="Étienne Provost (v. 1785-1850) · Les Canadiens français de l'Ouest", autre='provost-en.html', autre_nom='English', autre_lang='en',
  retour="← Retour à l'atlas des Canadiens français",
  h1="Étienne Provost <span>v. 1785-1850</span>",
  chapeau="Trappeur né à Chambly, Étienne Provost passe une quarantaine d'années dans l'Ouest : prisonnier des Espagnols au Nouveau-Mexique (1817), pionnier du bassin du Grand Lac Salé (la ville et la rivière Provo portent son nom), puis homme de confiance de l'American Fur Company sur le haut Missouri. Il meurt à Saint-Louis le 3 juillet 1850. Ce dossier réunit les fiches de l'atlas qui le concernent et l'enquête sur ses années à Saint-Louis.",
  h_carte="Sur la carte",
  carte=lambda: (f"<p>Son parcours, d'après la notice de LeRoy R. Hafen (<i>The Mountain Men</i>, vol. 6, p. 371-386), se suit sur la page <a href=\"montagnards.html#p=H6-371\">Les hommes des montagnes</a> (bouton « voir »). Les {len(mm)} lieux ont été repérés automatiquement dans la notice : ils sont datés et paginés, mais restent à vérifier.</p>"
                 f"<p>Autres fiches : {lien('AH-sf08', 'l’île Chouteau, sur l’Arkansas (1816-1817)')} (Atlas historique du Québec) ; à Saint-Louis, "
                 f"{lien('PV-02', 'la taverne et l’épicerie')}, {lien('PV-03', 'le Frenchtown de la rue Second')}, {lien('PV-05', 'le carrefour Second et Lombard')}, "
                 f"{lien('PV-04', 'le « Henry N. Provost » de 1851')} et {lien('PV-01', 'la mort et l’inhumation (3-4 juillet 1850)')}.</p>"),
  h_liste="Les lieux de la notice de Hafen", col=("Date", "Lieu", "Page"),
  h_stl="Saint-Louis : ce qu'on sait",
  stl=["<b>Un commerçant de la rue Second.</b> Selon Jack B. Tykal, Provost tient à Saint-Louis, à partir de 1827 environ, une taverne et une épicerie. Gilles Havard le situe dans le Frenchtown, au sud de la vieille cathédrale (rues Second et Third, entre Poplar et Lombard), d'après l'annuaire de 1847 et le recensement municipal de 1845.",
       "<b>Les Lambert.</b> Provost avait épousé Marie-Rose Lambert ; à sa mort, le registre de la cathédrale l'inscrit comme époux de « Maria Rose Lombard ». En 1845, l'annuaire place le café de Clément Lambert à l'angle nord-est des rues Second et Lombard, en face d'un « H. N. Provost », épicier, à l'angle sud-ouest.",
       "<b>Mais attention au prénom.</b> L'annuaire de 1851, publié après la mort d'Étienne, inscrit encore « Provost Henry N., mountain trader, 244 s Second ». Le Provost de l'angle Second et Lombard est donc vraisemblablement un autre homme, peut-être un parent.",
       "<b>Chambly.</b> Le quartier est aussi celui de Moïse Lamoureux, natif de Chambly comme Provost (angle nord-ouest des rues Second et Poplar en 1845)."],
  h_aubry="Provost et Aubry",
  aubry=f"<p>Les deux hommes étaient canadiens, catholiques de la même paroisse et liés au commerce de l'Ouest ; aucune source ne dit qu'ils se soient connus. Chaput et Tassé ne nomment jamais Provost, et les biographies de Provost (Hafen, Tykal, Havard) ne nomment pas Aubry. Le jour de la mort de Provost, le 3 juillet 1850, Aubry arrive à Independence au terme de son « retour éclair ». Voir la <a href=\"{AUBRY}reseau.html#provost\">page « Le réseau francophone »</a> de l'Atlas Aubry et son <a href=\"{AUBRY}plan-saint-louis.html#L100\">plan de Saint-Louis</a>.</p>",
  h_verif="À vérifier",
  verif=["l'entrée d'Étienne dans le <i>St. Louis Directory</i> de 1847 (p. 153) et dans le recensement municipal de 1845 (Missouri Historical Society) ;",
         "les registres de la vieille cathédrale (baptêmes, mariages, parrainages), pour voir qui entoure les Provost et les Lambert (parrainages, témoins) ;",
         "l'inventaire après décès de Provost (dossier de succession 3242, Missouri State Archives), qui peut nommer ses débiteurs et ses créanciers ;",
         "l'identité de Henry N. Provost, « mountain trader » (1851)."],
  h_sources="Sources",
  note_quartier="Le carrefour Second et Lombard est resté hors de la zone rasée en 1939-1942 pour le parc de la Gateway Arch, qui s'arrêtait à la rue Poplar.",
),
'en': dict(
  titre="Étienne Provost (c. 1785-1850) · French Canadians of the West", autre='provost.html', autre_nom='Français', autre_lang='fr',
  retour="← Back to the French-Canadian atlas",
  h1="Étienne Provost <span>c. 1785-1850</span>",
  chapeau="Born in Chambly, the trapper Étienne Provost spent some forty years in the West: a prisoner of the Spaniards in New Mexico (1817), a pioneer of the Great Salt Lake basin (the city and river of Provo bear his name), then a trusted man of the American Fur Company on the upper Missouri. He died in St. Louis on July 3, 1850. This page gathers the atlas entries about him and the inquiry into his St. Louis years.",
  h_carte="On the map",
  carte=lambda: (f"<p>His route, after LeRoy R. Hafen's sketch (<i>The Mountain Men</i>, vol. 6, p. 371-386), can be followed on the <a href=\"montagnards-en.html#p=H6-371\">Mountain Men</a> page (“show” button). The {len(mm)} places were extracted automatically from the sketch: they are dated and paged but remain to be checked.</p>"
                 f"<p>Other entries: {lien('AH-sf08', 'Chouteau’s Island on the Arkansas (1816-1817)')} (Atlas historique du Québec); in St. Louis, "
                 f"{lien('PV-02', 'the tavern and grocery')}, {lien('PV-03', 'the Second Street Frenchtown')}, {lien('PV-05', 'the corner of Second and Lombard')}, "
                 f"{lien('PV-04', 'the “Henry N. Provost” of 1851')} and {lien('PV-01', 'his death and burial (July 3-4, 1850)')}.</p>"),
  h_liste="Places in Hafen's sketch", col=("Date", "Place", "Page"),
  h_stl="St. Louis: what we know",
  stl=["<b>A Second Street shopkeeper.</b> According to Jack B. Tykal, Provost kept a tavern and grocery in St. Louis from about 1827. Gilles Havard places him in Frenchtown, south of the Old Cathedral (Second and Third streets, between Poplar and Lombard), from the 1847 directory and the 1845 municipal census.",
       "<b>The Lamberts.</b> Provost had married Marie-Rose Lambert; at his death, the cathedral register lists him as the husband of “Maria Rose Lombard.” In 1845 the directory places Clément Lambert's coffee-house at the northeast corner of Second and Lombard, facing an “H. N. Provost,” grocer, at the southwest corner.",
       "<b>But mind the first name.</b> The 1851 directory, published after Étienne's death, still lists “Provost Henry N., mountain trader, 244 s Second.” The Provost of Second and Lombard was therefore probably another man, perhaps a relative.",
       "<b>Chambly.</b> The neighbourhood was also that of Moïse Lamoureux, a native of Chambly like Provost (northwest corner of Second and Poplar in 1845)."],
  h_aubry="Provost and Aubry",
  aubry=f"<p>Both men were French Canadians, Catholics of the same parish and tied to the western trade; no source says they knew each other. Chaput and Tassé never name Provost, and Provost's biographers (Hafen, Tykal, Havard) do not name Aubry. On the day Provost died, July 3, 1850, Aubry reached Independence at the end of his “lightning return.” See the Aubry Atlas <a href=\"{AUBRY}reseau-en.html#provost\">French-speaking network</a> page and its <a href=\"{AUBRY}plan-saint-louis-en.html#L100\">map of St. Louis</a>.</p>",
  h_verif="To be checked",
  verif=["Étienne's entry in the <i>St. Louis Directory</i> of 1847 (p. 153) and in the 1845 municipal census (Missouri Historical Society);",
         "the Old Cathedral registers (baptisms, marriages, godparents), to see who surrounds the Provosts and the Lamberts;",
         "Provost's probate inventory (estate file 3242, Missouri State Archives), which may name his debtors and creditors;",
         "the identity of Henry N. Provost, “mountain trader” (1851)."],
  h_sources="Sources",
  note_quartier="The corner of Second and Lombard lay outside the area razed in 1939-1942 for the Gateway Arch grounds, which stopped at Poplar Street.",
)}
SOURCES = ["LeRoy R. Hafen, « Etienne Provost », dans <i>The Mountain Men and the Fur Trade of the Far West</i>, vol. 6, Glendale, Arthur H. Clark, 1968, p. 371-386.",
  "Jack B. Tykal, <i>Etienne Provost: Man of the Mountains</i>, Liberty (Utah), Eagle's View, 1989 ; et « Provost, Etienne », <i>Utah History Encyclopedia</i> (uen.org).",
  "Gilles Havard, <i>L'Amérique fantôme. Les aventuriers francophones du Nouveau Monde</i>, Paris, Flammarion, 2019, ch. 8 « L'homme des montagnes : Étienne Provost ».",
  "<i>The St. Louis Directory for the Years 1840-1</i> ; <i>Green's St. Louis Directory</i> for 1845 (p. 103 et 144) et for 1851 (p. 281).",
  "Alain Roy, « Sur la piste de Santa Fe, 1721-1880 », dans Y. Frenette, É. Rivard et M. St-Hilaire (dir.), <i>La francophonie nord-américaine</i>, PUL, 2012, p. 103.",
  "Missouri Historical Society, studio Sievers, photographie des nos 914-916 South Second, 27 juin 1952 (P0403-52375).",
  "Enquête d'O. J. Caron, faite d'abord pour l'Atlas Aubry et versée ici le 14 novembre 2026 : aucune source ne montre qu'Aubry et Provost se soient connus."]

for lg, t in T.items():
    rows = ''.join(f"<tr><td>{e(p['date_edtf'])}</td><td>{lien(p['id'], re.sub(r' : Etienne Provost$', '', p['nom']))}</td><td>{e(re.search(r'mention p\. (\d+)', p['sources']).group(1) if re.search(r'mention p\. (\d+)', p['sources']) else '')}</td></tr>" for p in mm)
    page = f"""<!DOCTYPE html>
<html lang="{lg}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['titre']}</title>
<meta name="author" content="Olivier J. Caron, Département de géographie, UQAM">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&display=swap">
{STYLE}
</head>
<body>
<header class="barre"><h1>{t['h1']}</h1>
  <span class="esp"></span><a class="lien-langue" href="{t['autre']}" hreflang="{t['autre_lang']}" lang="{t['autre_lang']}">{t['autre_nom']}</a><a href="index.html">{t['retour']}</a></header>
<main>
<p class="chapeau">{t['chapeau']}</p>
<h2>{t['h_carte']}</h2>{t['carte']()}
<h2 id="saint-louis">{t['h_stl']}</h2><ul>{''.join(f'<li>{x}</li>' for x in t['stl'])}</ul><p class="source">{t['note_quartier']}</p>
<h2>{t['h_verif']}</h2><ul>{''.join(f'<li>{x}</li>' for x in t['verif'])}</ul>
<h2 id="hafen">{t['h_liste']}</h2><table><tr><th>{t['col'][0]}</th><th>{t['col'][1]}</th><th>{t['col'][2]}</th></tr>{rows}</table>
<h2>{t['h_sources']}</h2><ul class="source">{''.join(f'<li>{x}</li>' for x in SOURCES)}</ul>
</main>
</body>
</html>
"""
    open(f"{R}/{'provost.html' if lg == 'fr' else 'provost-en.html'}", 'w', encoding='utf-8').write(page)
print('provost.html et provost-en.html :', len(mm), 'lieux Hafen MM')
