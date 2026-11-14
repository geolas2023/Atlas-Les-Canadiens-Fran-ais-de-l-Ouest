# « Les Canadiens de l'Ouest » de Joseph Tassé (1878), tomes I et II : données géographiques et page (FR / EN)
import json, html, re
from tasse1_data import SRC, P, E, I, I_EN, R
import tasse2_data as T2
A = '/home/claude/atlas-aubry/'
P2, E2, R2, X = T2.P2, T2.E2, T2.R2, T2.X
COUL = {p[0]: p[5] for p in P + P2}
NOM = {p[0]: p[1] for p in P + P2}
SRC2 = SRC.replace('t. I,', 't. II,')

def feats():
    F = []
    for tome, EE, pre, src in ((1, E, 'TA', SRC), (2, E2, 'TB', SRC2)):
        for k, (pid, lon, lat, d, an, lfr, len_, tfr, ten, pg) in enumerate(EE, 1):
            F.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]},
                      "properties": {"id": f"{pre}{k:03d}", "tome": tome, "personne": pid, "nom_personne": NOM[pid], "couleur": COUL[pid],
                                     "date": d, "annee": an, "lieu": lfr, "lieu_en": len_, "texte": tfr, "texte_en": ten,
                                     "pages": pg, "source": src + ", p. " + pg, "certitude": "approximative", "categorie": "biographie"}})
    for k, (lon, lat, nfr, nen, tfr) in enumerate(I, 1):
        F.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]},
                  "properties": {"id": f"TI{k:03d}", "tome": 1, "personne": "intro", "nom_personne": "Introduction", "couleur": '#555',
                                 "date": "", "annee": 0, "lieu": nfr, "lieu_en": nen, "texte": tfr, "texte_en": I_EN[nfr],
                                 "pages": "v-xlv", "source": SRC + ", introduction, p. v-xlv", "certitude": "approximative", "categorie": "etablissement"}})
    return F

def build_geojson():
    F = feats()
    meta = {"source": SRC + " ; " + SRC2, "note": "Positions au niveau du lieu habité ou du poste, établies d'après les noms donnés par Tassé ; certitude approximative."}
    for nom, sel in (('tasse', F), ('tasse1', [f for f in F if f['properties']['tome'] == 1]), ('tasse2', [f for f in F if f['properties']['tome'] == 2])):
        json.dump({"type": "FeatureCollection", "name": nom, "metadata": meta, "features": sel},
                  open(A + f'data/{nom}.geojson', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    return len(F)

def gabarit(fr, titre, sous, page):
    src = open(A + ('hommes.html' if fr else 'hommes-en.html'), encoding='utf-8').read()
    tete = src[:src.find('<header')]
    tete = re.sub(r'<title>.*?</title>', f'<title>{titre} · Atlas Aubry</title>', tete)
    tete = tete.replace('</head>', '<link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.css">\n<script src="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.js"></script>\n</head>')
    autre = page.replace('.html', '-en.html') if fr else page
    nav = (f'<a class="lien-langue" href="{autre}" hreflang="en" lang="en">English</a><a href="index.html">← Retour à l\'atlas</a>' if fr else
           f'<a class="lien-langue" href="{autre}" hreflang="fr" lang="fr">Français</a><a href="index-en.html">← Back to the atlas</a>')
    return tete + f'<header class="barre">\n  <h1>{titre} <span>· {sous}</span></h1>\n  <span class="esp"></span>{nav}\n</header>\n'

def NOMC(i, PP):
    return next(q[1] for q in PP if q[0] == i)

POS1 = {'perrault': (110, 60), 'cadot': (330, 60), 'langlade': (560, 60), 'baby': (800, 60),
        'reaume': (110, 200), 'porlier': (400, 200), 'rolette': (700, 200), 'dubuque': (900, 200),
        'juneau': (110, 340), 'rainville': (400, 340), 'faribault': (700, 340), 'leclerc': (900, 340),
        'ducharme': (110, 470), 'lefebvre': (330, 470), 'provencal': (560, 470)}
POS2 = {'pmenard': (110, 60), 'fmenard': (110, 200), 'mbmenard': (330, 130), 'bogy': (110, 340), 'mallet': (330, 300), 'roy': (330, 440), 'robidou': (110, 470),
        'guerin': (560, 60), 'rolettef': (800, 60), 'riel': (1000, 60), 'beaubien': (560, 200), 'levasseur': (560, 340),
        'franchere': (800, 200), 'larocque': (1000, 200), 'pambrun': (800, 340), 'falcon': (1000, 340),
        'leroux': (560, 470), 'aubry': (800, 470), 'beaudry': (1000, 470), 'fournier': (330, 570)}

def schema(fr, PP=None, RR=None, pos=None):
    PP = PP or P; RR = RR or R; pos = pos or POS1
    W = max(x for x, y in pos.values()) + 140; H = max(y for x, y in pos.values()) + 60
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s" style="width:100%%;height:auto;background:#fffdf8;border:1px solid #c9bba3;font-family:Georgia,serif">'
         % (W, H, "Liens entre les personnages" if fr else "Ties between the people")]
    for k, (a, b, lfr, len_, pg) in enumerate(RR, 1):
        (xa, ya), (xb, yb) = pos[a], pos[b]
        mx, my = (xa+xb)/2, (ya+yb)/2
        o.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="#9a8a6e" stroke-width="1.8"/>')
        o.append(f'<g><title>{html.escape(lfr if fr else len_)} (p. {pg})</title><circle cx="{mx:.0f}" cy="{my:.0f}" r="9" fill="#f4efe6" stroke="#7a6a52"/><text x="{mx:.0f}" y="{my+3.5:.0f}" font-size="10" text-anchor="middle" fill="#3b3328">{k}</text></g>')
    for pid, (x, y) in pos.items():
        p = next(q for q in PP if q[0] == pid)
        o.append(f'<a href="#{pid}"><circle cx="{x}" cy="{y}" r="10" fill="{p[5]}" stroke="#fffdf8" stroke-width="2"/>')
        o.append(f'<text x="{x}" y="{y-15}" font-size="13" fill="#3b3328" text-anchor="middle" paint-order="stroke" stroke="#fffdf8" stroke-width="3">{html.escape(p[1])}</text>')
        o.append(f'<text x="{x}" y="{y+24}" font-size="10.5" fill="#6b604f" text-anchor="middle" paint-order="stroke" stroke="#fffdf8" stroke-width="3">{p[2]}</text></a>')
    o.append('</svg>')
    o.append('<ol class="liens-num" style="columns:2;font-size:.88rem;margin-top:.6rem">' + ''.join(
        f'<li><b>{html.escape(NOMC(a, PP))} – {html.escape(NOMC(b, PP))}</b> : {html.escape(lfr if fr else len_)} <span style="color:#6b604f">(p. {pg})</span></li>' for a, b, lfr, len_, pg in RR) + '</ol>')
    return '\n'.join(o)

def vies(fr, PP, EE, tome):
    h = ''
    idx = 'index.html' if fr else 'index-en.html'
    for pid, nom, dates, ofr, oen, c, rfr, ren, chap in PP:
        h += f'<div class="encadre" id="{pid}" style="border-left:5px solid {c}"><h3 style="margin-top:0">{html.escape(nom)} <span style="font-weight:normal;color:#6b604f">({dates} · {html.escape(ofr if fr else oen)})</span></h3>'
        r = html.escape(rfr if fr else ren)
        h += f'<p>{r}</p><ul>'
        for (q, lon, lat, d, an, lfr, len_, tfr, ten, p_) in sorted([e for e in EE if e[0] == pid], key=lambda e: e[4]):
            t = html.escape(tfr if fr else ten)
            t = re.sub(r'(fiche |record )(L\d+)', lambda m: f'{m.group(1)}<a href="{idx}#lieu={m.group(2)}">{m.group(2)}</a>', t)
            h += f'<li><b>{html.escape(lfr if fr else len_)}</b> · {d} · {t} <span style="color:#6b604f">(p. {p_})</span></li>'
        h += f'</ul><p class="source">Tassé, t. {"I" if tome == 1 else "II"}, {chap}.</p></div>\n'
    return h

def page(fr):
    T = (lambda a, b: a if fr else b)
    pg = 'canadiens-ouest.html'
    h = gabarit(fr, T("Les Canadiens de l'Ouest", "The Canadians of the West"), T("Joseph Tassé, 1878, tomes I et II", "Joseph Tassé, 1878, vols. I and II"), pg)
    idx = 'index.html' if fr else 'index-en.html'
    L = lambda i: f'<a href="{idx}#lieu={i}">{i}</a>'
    nb = len(E) + len(E2) + len(I)
    h += '<main>\n'
    h += T("<h2>Le livre</h2>", "<h2>The book</h2>")
    h += T(f"<p class=\"chapeau\">En 1878, le journaliste et député Joseph Tassé publie à Montréal <i>Les Canadiens de l'Ouest</i>, deux tomes de biographies de Canadiens français établis entre les Grands Lacs et le Pacifique. Le tome I raconte quinze vies, des Grands Lacs au haut Mississippi ; le tome II en raconte vingt, du Minnesota au Texas et de la Rivière-Rouge à la Californie, dont celle d'Aubry (p. 179-227), source principale de cet atlas. Les {nb} lieux qu'il nomme sont placés sur la carte ci-dessous, avec la page où il les mentionne.</p>",
           f"<p class=\"chapeau\">In 1878 the journalist and MP Joseph Tassé published in Montreal <i>Les Canadiens de l'Ouest</i>, two volumes of biographies of French Canadians settled between the Great Lakes and the Pacific. Volume I tells fifteen lives, from the Great Lakes to the upper Mississippi; volume II tells twenty, from Minnesota to Texas and from Red River to California, including Aubry's (pp. 179-227), this atlas's main source. The {nb} places he names are placed on the map below, with the page where he mentions them.</p>")
    h += T(f"<p><b>Le lien avec Aubry.</b> Trois fils relient directement ces vies à celle d'Aubry. <b>Antoine Leroux</b> : le 7 novembre 1853, à Albuquerque, Whipple consulte ensemble Aubry et Leroux avant de lancer son expédition du 35e parallèle ({L('L15')}). <b>Le haut Mississippi</b> : en octobre 1846, Aubry visite Galena, la Prairie-du-Chien, Saint-Pierre (Mendota) et la chute Saint-Antoine ({L('L04')} · {L('L05')} · {L('L06')} · {L('L07')}), où il « rencontre de nombreux Canadiens français » : ce sont Faribault, Provençal, Rainville, la famille Rolette et les fondateurs de Saint-Paul autour de Vital Guérin. <b>Maskinongé</b> : Tassé remercie l'abbé Bois, curé de la paroisse natale d'Aubry. D'autres croisements sont indirects : Félix St. Vrain, ami d'Antoine Leclerc, était le frère de Céran St. Vrain, l'ami d'Aubry ; Auguste Chouteau, acquéreur des mines de Dubuque, est de la famille des Chouteau de Saint-Louis ; Prudent Beaudry s'établit en 1852 à Los Angeles ({L('L46')}), où Aubry passe en 1853 et 1854.</p>",
           f"<p><b>The link with Aubry.</b> Three threads tie these lives directly to Aubry's. <b>Antoine Leroux</b>: on November 7, 1853, at Albuquerque, Whipple consulted Aubry and Leroux together before launching his 35th-parallel expedition ({L('L15')}). <b>The upper Mississippi</b>: in October 1846 Aubry visited Galena, Prairie du Chien, St. Peter (Mendota) and St. Anthony Falls ({L('L04')} · {L('L05')} · {L('L06')} · {L('L07')}), where he “met many French Canadians”: Faribault, Provençal, Rainville, the Rolette family and St. Paul's founders around Vital Guérin. <b>Maskinongé</b>: Tassé thanks Father Bois, priest of Aubry's home parish. Other crossings are indirect: Félix St. Vrain, Antoine Leclerc's friend, was the brother of Ceran St. Vrain, Aubry's friend; Auguste Chouteau, who bought into Dubuque's mines, was of the St. Louis Chouteau family; Prudent Beaudry settled in 1852 at Los Angeles ({L('L46')}), through which Aubry passed in 1853 and 1854.</p>")
    h += T('<p class="sommaire"><a href="#carte">La carte</a> · <a href="#liens1">Liens, tome I</a> · <a href="#liens2">Liens, tome II</a> · <a href="#vies1">Les quinze vies du tome I</a> · <a href="#vies2">Les vingt vies du tome II</a> · <a href="#intro">Les établissements de l\'introduction</a> · <a href="#donnees">Données et source</a></p>',
           '<p class="sommaire"><a href="#carte">The map</a> · <a href="#liens1">Ties, vol. I</a> · <a href="#liens2">Ties, vol. II</a> · <a href="#vies1">The fifteen lives of vol. I</a> · <a href="#vies2">The twenty lives of vol. II</a> · <a href="#intro">Settlements in the introduction</a> · <a href="#donnees">Data and source</a></p>')
    h += T('<h2 id="carte">La carte</h2>', '<h2 id="carte">The map</h2>')
    h += ('<div id="tomes-tasse" style="margin:.3rem 0 .5rem;font-size:.9rem">' +
          ''.join(f'<button type="button" data-t="{v}" style="margin-right:.4rem;padding:.2rem .7rem;border:1px solid #8a7a5f;background:{"#5a4d3b;color:#f4efe6" if v == "0" else "#f4efe6;color:#3b3328"};border-radius:4px;cursor:pointer;font-family:Georgia,serif">{l}</button>'
                  for v, l in (('0', T('Les deux tomes', 'Both volumes')), ('1', T('Tome I', 'Volume I')), ('2', T('Tome II', 'Volume II')))) + '</div>\n')
    h += '<div id="carte-tasse" style="height:600px;border:1px solid #c9bba3;border-radius:6px"></div>\n'
    h += '<div id="leg-tasse" style="margin:.5rem 0 1rem;font-size:.85rem"></div>\n'
    h += T("<p class=\"avert\">Chaque point est un lieu nommé par Tassé, placé au poste ou à l'établissement correspondant (position approximative). Les points cerclés de noir sont du tome II ; les gris, les établissements de l'introduction du tome I. Cliquez sur un nom pour n'afficher qu'une vie.</p>",
           "<p class=\"avert\">Each point is a place named by Tassé, placed at the corresponding post or settlement (approximate position). Points ringed in black are from volume II; grey points are settlements from volume I's introduction. Click a name to show a single life.</p>")
    h += T('<h2 id="liens1">Les liens entre eux : tome I</h2>', '<h2 id="liens1">The ties between them: volume I</h2>') + schema(fr)
    h += T('<h2 id="liens2">Les liens entre eux : tome II</h2>', '<h2 id="liens2">The ties between them: volume II</h2>') + schema(fr, P2, R2, POS2)
    h += T("<p><b>D'un tome à l'autre.</b></p><ul>", "<p><b>From one volume to the other.</b></p><ul>")
    for a, b, lfr, len_ in X:
        h += f'<li><a href="#{a}">{html.escape(NOM[a])}</a> – <a href="#{b}">{html.escape(NOM[b])}</a> : {html.escape(lfr if fr else len_)}</li>'
    h += T('<li>Quatre de ces hommes ont aussi leur biographie dans la série de Hafen : Leroux, Pierre Ménard, Joseph Robidoux et Fournier (« Old Pino » Fournaise). Voir <a href="montagnards.html">Les hommes des montagnes</a>.</li>', '<li>Four of these men also have a biography in Hafen\'s series: Leroux, Pierre Ménard, Joseph Robidoux and Fournier (“Old Pino” Fournaise). See <a href="montagnards-en.html">The Mountain Men</a>.</li>')
    h += '</ul>'
    h += T("<p class=\"avert\">Les liens tracés sont ceux que Tassé établit lui-même (page indiquée) : parenté, service, voisinage, même poste, même affaire. Survolez un numéro pour lire le lien.</p>", "<p class=\"avert\">The ties drawn are those Tassé himself establishes (page given): kinship, service, neighbourhood, same post, same affair. Hover over a number to read the tie.</p>")
    h += T('<h2 id="vies1">Les quinze vies du tome I</h2>', '<h2 id="vies1">The fifteen lives of volume I</h2>') + vies(fr, P, E, 1)
    h += T('<h2 id="vies2">Les vingt vies du tome II</h2>', '<h2 id="vies2">The twenty lives of volume II</h2>') + vies(fr, P2, E2, 2)
    h += T("<p class=\"avert\">Tome II, annexes (p. 381-401) : la liste des Canadiens français établis à Saint-Paul en 1850 (plus de quatre-vingts noms, dont Vital Guérin, Louis Robert et Joseph Rondeau), le traité de Chicago de 1833 et le journal d'Aubry de 1853, de la Californie au Nouveau-Mexique, déjà intégré à l'atlas.</p>",
           "<p class=\"avert\">Volume II, appendices (pp. 381-401): the list of French Canadians settled at St. Paul in 1850 (over eighty names, including Vital Guérin, Louis Robert and Joseph Rondeau), the 1833 Treaty of Chicago and Aubry's 1853 journal from California to New Mexico, already integrated into the atlas.</p>")
    h += T('<h2 id="intro">Les établissements de l\'introduction (tome I)</h2>', '<h2 id="intro">Settlements in the introduction (volume I)</h2>')
    h += T("<p>L'introduction (p. v-xlv) fait le tour des établissements français et canadiens de l'Ouest : la chaîne des postes de la Nouvelle-France, les villages des Illinois, Détroit, puis les communautés canadiennes de 1878, de l'Illinois au Minnesota et jusqu'au Nouveau-Mexique.</p><ul>",
           "<p>The introduction (pp. v-xlv) surveys the French and Canadian settlements of the West: the chain of New France posts, the Illinois villages, Detroit, then the Canadian communities of 1878, from Illinois to Minnesota and as far as New Mexico.</p><ul>")
    for lon, lat, nfr, nen, tfr in I:
        h += f'<li><b>{html.escape(nfr if fr else nen)}</b> · {html.escape(tfr if fr else I_EN[nfr])}</li>'
    h += '</ul>'
    h += T('<h2 id="donnees">Données et source</h2>', '<h2 id="donnees">Data and source</h2>')
    h += T(f"<p>Les {nb} lieux sont téléchargeables en GeoJSON : <a href=\"data/tasse.geojson\" download>tasse.geojson</a> (les deux tomes ; aussi <a href=\"data/tasse1.geojson\" download>tome I</a> et <a href=\"data/tasse2.geojson\" download>tome II</a>), avec les champs <code>tome</code>, <code>personne</code>, <code>date</code>, <code>lieu</code>, <code>texte</code>, <code>pages</code> et <code>source</code>. Sources : {html.escape(SRC)} ; {html.escape(SRC2)}. L'ouvrage, publié en 1878, est dans le domaine public. Les numéros de page sont ceux de l'édition imprimée ; quelques noms et dates sont mal lisibles dans les exemplaires numérisés et sont signalés comme tels.</p>",
           f"<p>The {nb} places can be downloaded as GeoJSON: <a href=\"data/tasse.geojson\" download>tasse.geojson</a> (both volumes; also <a href=\"data/tasse1.geojson\" download>vol. I</a> and <a href=\"data/tasse2.geojson\" download>vol. II</a>), with the fields <code>tome</code>, <code>personne</code>, <code>date</code>, <code>lieu</code>, <code>texte_en</code>, <code>pages</code> and <code>source</code>. Sources: {html.escape(SRC)}; {html.escape(SRC2)}. The book, published in 1878, is in the public domain. Page numbers are those of the printed edition; a few names and dates are poorly legible in the scanned copies and are flagged as such.</p>")
    h += """<script>
(function(){
const FR = %s;
const map = new maplibregl.Map({container:'carte-tasse', style:{version:8, sources:{t:{type:'raster', tiles:['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}'], tileSize:256, attribution:'Esri, HERE, Garmin, USGS'}}, layers:[{id:'t', type:'raster', source:'t', paint:{'raster-saturation':-0.5}}]}, center:[-98,42], zoom:3.3});
map.addControl(new maplibregl.NavigationControl());
let tome=0, pers=null;
const filtre=()=>{const f=['all']; if(tome) f.push(['==',['get','tome'],tome]); if(pers) f.push(['==',['get','personne'],pers]); map.setFilter('ta', f.length>1?f:null);};
fetch('data/tasse.geojson').then(r=>r.json()).then(g=>{
  const go=()=>{
  map.addSource('ta', {type:'geojson', data:g});
  map.addLayer({id:'ta', type:'circle', source:'ta', paint:{'circle-radius':['case',['==',['get','categorie'],'etablissement'],5,7], 'circle-color':['get','couleur'], 'circle-stroke-color':['case',['==',['get','tome'],2],'#1d1a16','#fffdf8'], 'circle-stroke-width':1.6, 'circle-opacity':0.9}});
  map.on('click','ta', e=>{const p=e.features[0].properties;
    const t=FR?p.texte:p.texte_en, l=FR?p.lieu:p.lieu_en;
    new maplibregl.Popup({maxWidth:'340px'}).setLngLat(e.lngLat).setHTML('<b>'+l+'</b><br><i>'+p.nom_personne+(p.date?' · '+p.date:'')+'</i><p style="margin:.4em 0">'+t+'</p><small>Tassé, t. '+(p.tome==2?'II':'I')+', p. '+p.pages+'</small>').addTo(map);});
  map.on('mouseenter','ta',()=>map.getCanvas().style.cursor='pointer'); map.on('mouseleave','ta',()=>map.getCanvas().style.cursor='');
  const leg=document.getElementById('leg-tasse'); const seen={}; const rows={1:document.createElement('div'),2:document.createElement('div')};
  [1,2].forEach(k=>{rows[k].style.cssText='display:flex;flex-wrap:wrap;gap:.25rem .8rem;margin:.2rem 0'; rows[k].innerHTML='<b style="margin-right:.3rem">'+(FR?'Tome ':'Vol. ')+(k==1?'I':'II')+' :</b>'; leg.appendChild(rows[k]);});
  g.features.forEach(f=>{const p=f.properties; if(seen[p.personne])return; seen[p.personne]=1;
    const b=document.createElement('a'); b.href='#carte'; b.style.cssText='cursor:pointer;text-decoration:none;color:inherit';
    b.innerHTML='<span style="display:inline-block;width:10px;height:10px;border-radius:50%%;background:'+p.couleur+';margin-right:4px;border:1px solid '+(p.tome==2?'#1d1a16':'#fffdf8')+'"></span>'+p.nom_personne;
    b.onclick=(ev)=>{ev.preventDefault(); const on=pers===p.personne; document.querySelectorAll('#leg-tasse a').forEach(x=>x.style.fontWeight='normal');
      if(on){pers=null; filtre();} else {pers=p.personne; b.style.fontWeight='bold'; filtre();
        const c=g.features.filter(x=>x.properties.personne===p.personne).map(x=>x.geometry.coordinates); const bb=c.reduce((a,x)=>[Math.min(a[0],x[0]),Math.min(a[1],x[1]),Math.max(a[2],x[0]),Math.max(a[3],x[1])],[180,90,-180,-90]);
        map.fitBounds([[bb[0],bb[1]],[bb[2],bb[3]]],{padding:60,maxZoom:7});}};
    rows[p.tome].appendChild(b);});
  document.querySelectorAll('#tomes-tasse button').forEach(bt=>bt.onclick=()=>{tome=+bt.dataset.t; pers=null;
    document.querySelectorAll('#leg-tasse a').forEach(x=>x.style.fontWeight='normal');
    document.querySelectorAll('#tomes-tasse button').forEach(x=>{const a=x===bt; x.style.background=a?'#5a4d3b':'#f4efe6'; x.style.color=a?'#f4efe6':'#3b3328';}); filtre();});
  };
  if(map.loaded()) go(); else map.on('load', go);
});
})();
</script>
""" % ('true' if fr else 'false')
    h += '</main>\n</body>\n</html>\n'
    return h

n = build_geojson()
for fr in (True, False):
    open(A + ('canadiens-ouest.html' if fr else 'canadiens-ouest-en.html'), 'w', encoding='utf-8').write(page(fr))
print('tassé t. I et II :', n, 'lieux ;', len(E), '+', len(E2), 'étapes,', len(I), 'établissements ;', len(R) + len(R2) + len(X), 'liens')
