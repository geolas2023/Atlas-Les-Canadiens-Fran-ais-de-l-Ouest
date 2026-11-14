# Hafen (dir.), The Mountain Men and the Fur Trade of the Far West, vol. 2, 4-9 : index géographique et biographique (FR / EN)
import json, html, re
DOSSIERS = {'H6-371': 'provost'}  # Étienne Provost
A = '/home/claude/atlas-aubry/'
D = json.load(open('/home/claude/build/hafen_data.json', encoding='utf-8'))
PERS, EV, GZ = D['pers'], D['ev'], D['gaz']
SRC = "Hafen, LeRoy R. (dir.) (1965-1972), The Mountain Men and the Fur Trade of the Far West, Glendale, Arthur H. Clark, vol. 2, 4, 5, 6, 7, 8 et 9"
VOLS = [2, 4, 5, 6, 7, 8, 9]
# liens avec Aubry et avec les autres pages de l'atlas
AUBRY = [
 ('H4-173', "Consulté avec Aubry par Whipple à Albuquerque, le 7 novembre 1853 (Tassé, t. II, p. 242) ; participe en 1849 à la recherche de Mrs White, pour qui Aubry offre une récompense.", "Consulted together with Aubry by Whipple at Albuquerque, November 7, 1853 (Tassé, vol. II, p. 242); in 1849 joined the search for Mrs White, for whom Aubry offered a reward.", ['L15', 'L18']),
 ('H5-297', "Ami d'Aubry, voisin des Mercure sur la Plaza de Santa Fe ; ensemble chez Frémont à Taos (janvier 1849).", "Aubry's friend, neighbour of the Mercures on the Santa Fe Plaza; together at Frémont's in Taos (January 1849).", ['L14', 'L56']),
 ('H6-023', "Juge du procès Nangle (1849), où Aubry est partie.", "Judge in the Nangle case (1849), in which Aubry was a party.", ['L18']),
 ('H6-105', "Frémont loge chez lui à Taos quand Aubry et St. Vrain lui rendent visite (janvier 1849).", "Frémont was staying at his house in Taos when Aubry and St. Vrain visited (January 1849).", ['L14']),
 ('H6-371', "Mort à Saint-Louis le 3 juillet 1850, le jour où Aubry arrive à Independence ; même quartier de la rue Second que les patrons d'Aubry, sans contact documenté.", "Died at St. Louis on July 3, 1850, the day Aubry reached Independence; same Second Street quarter as Aubry's employers, no documented contact.", ['L100']),
 ('H6-299', "Maître de Rayado et de Cimarron, sur la route d'Aubry entre Santa Fe et la piste.", "Master of Rayado and Cimarron, on Aubry's road between Santa Fe and the trail.", []),
 ('H2-027', "Associé de St. Vrain ; tué à Taos en janvier 1847, pendant la première saison d'Aubry au Nouveau-Mexique.", "St. Vrain's partner; killed at Taos in January 1847, during Aubry's first season in New Mexico.", []),
 ('H6-061', "Maître du fort Bent, étape de la route de la montagne qu'Aubry emprunte et contourne.", "Master of Bent's Fort, on the mountain route Aubry used and bypassed.", []),
 ('H2-321', "Vasquez : la famille des épouses d'Elzéar Blanchard, patron d'Aubry à Saint-Louis ; un « Vasquez » croisé par Aubry en 1850.", "Vasquez: the family of the wives of Elzéar Blanchard, Aubry's St. Louis employer; a “Vasquez” met by Aubry in 1850.", ['L94', 'L95']),
 ('H9-091', "Chef de l'American Fur Co. ; Cyprien Chouteau, de la même famille, croise Aubry en 1852.", "Head of the American Fur Co.; Cyprien Chouteau, of the same family, met Aubry in 1852.", []),
 ('H9-283', "Gouverneur du Nouveau-Mexique pendant les deux dernières années d'Aubry (1853-1854).", "Governor of New Mexico during Aubry's last two years (1853-1854).", ['L11']),
 ('H4-261', "Traiteur de Taos et de Santa Fe, frère de Joseph (fondateur de Saint-Joseph) et de Louis Robidoux.", "Taos and Santa Fe trader, brother of Joseph (founder of St. Joseph) and of Louis Robidoux.", []),
]
TASSE = {'H4-173': 'leroux', 'H6-307': 'pmenard', 'H8-287': 'robidou', 'H8-175': 'fournier'}

def geo():
    F = []
    for e in EV:
        p = PERS[e['id']]; g = GZ[e['lieu']]
        F.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [g[0], g[1]]},
                  "properties": {"p": e['id'], "nom": p['nom'], "v": p['vol'], "fr": p['fr'], "l": e['lieu'], "lf": g[3], "a": e['annee'],
                                 "ax": 1 if e['annee_explicite'] else 0, "pg": ', '.join(str(x) for x in sorted(e['pages'])), "t": e['types'], "n": e['n']}})
    json.dump({"type": "FeatureCollection", "name": "hafen_mountain_men",
               "metadata": {"source": SRC, "methode": "Lieux repérés automatiquement dans le texte des biographies au moyen d'un répertoire de 327 lieux de la traite des fourrures ; année = année de la phrase, ou à défaut la dernière année mentionnée (ax = 0). Positions au lieu nommé ; certitude approximative.",
                            "champs": {"p": "identifiant de la biographie (H volume-page)", "v": "volume", "fr": "francophone (1)", "l": "lieu (anglais)", "lf": "lieu (français)", "a": "année", "ax": "année explicite dans la phrase", "pg": "pages", "t": "nature de la mention", "n": "nombre de mentions"}},
               "features": F}, open(A + 'data/hafen.geojson', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump(PERS, open(A + 'data/hafen_personnes.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
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

def page(fr):
    T = (lambda a, b: a if fr else b)
    idx = 'index.html' if fr else 'index-en.html'
    L = lambda i: f'<a href="{idx}#lieu={i}">{i}</a>'
    nev = len(EV); npers = len(PERS); nfr = sum(1 for p in PERS.values() if p['fr'])
    h = gabarit(fr, T("Les hommes des montagnes", "The Mountain Men"), T("Hafen, 1965-1972, sept volumes", "Hafen, 1965-1972, seven volumes"), 'montagnards.html')
    h += '<main>\n'
    h += T(f"<h2>La série de Hafen</h2><p class=\"chapeau\">De 1965 à 1972, LeRoy R. Hafen a dirigé <i>The Mountain Men and the Fur Trade of the Far West</i>, dix volumes de biographies des trappeurs, traiteurs et guides de l'Ouest américain, écrites par une centaine d'historiens. Cette page indexe les sept volumes réunis ici (2, 4, 5, 6, 7, 8 et 9) : <b>{npers} biographies</b>, dont <b>{nfr} de francophones</b> (Canadiens, Créoles de Saint-Louis et de Louisiane, Français, Métis), et <b>{nev} lieux datés</b> repérés dans leur texte, chacun avec sa page.</p>",
           f"<h2>Hafen's series</h2><p class=\"chapeau\">From 1965 to 1972 LeRoy R. Hafen edited <i>The Mountain Men and the Fur Trade of the Far West</i>, ten volumes of biographies of the trappers, traders and guides of the American West, written by about a hundred historians. This page indexes the seven volumes gathered here (2, 4, 5, 6, 7, 8 and 9): <b>{npers} biographies</b>, <b>{nfr} of them of French speakers</b> (Canadians, St. Louis and Louisiana Creoles, French, Métis), and <b>{nev} dated places</b> found in their text, each with its page.</p>")
    h += T("<p><b>Et Aubry ?</b> Hafen ne nomme jamais Aubry dans ces sept volumes : arrivé dans l'Ouest en 1846, il appartient au commerce de Santa Fe plus qu'à la traite des fourrures. Mais une douzaine de ces hommes ont croisé sa route ou celle de ses proches (voir plus bas). Quatre figurent aussi chez Tassé : Antoine Leroux, Pierre Ménard, Joseph Robidoux, et « Old Pino » Fournaise, qui est le Jacques Fournier du tome II de Tassé, mort aux Bluffs de Kansas City en 1871.</p>",
           "<p><b>And Aubry?</b> Hafen never names Aubry in these seven volumes: arriving in the West in 1846, he belonged to the Santa Fe trade rather than the fur trade. But a dozen of these men crossed his path or that of his circle (see below). Four also appear in Tassé: Antoine Leroux, Pierre Ménard, Joseph Robidoux, and “Old Pino” Fournaise, who is the Jacques Fournier of Tassé's volume II, who died at the Kansas City bluffs in 1871.</p>")
    h += T('<p class="sommaire"><a href="#carte">La carte</a> · <a href="#aubry">Les liens avec Aubry</a> · <a href="#index">Les 229 biographies</a> · <a href="#lieux">Les lieux les plus cités</a> · <a href="#methode">Méthode et limites</a></p>',
           '<p class="sommaire"><a href="#carte">The map</a> · <a href="#aubry">Ties with Aubry</a> · <a href="#index">The 229 biographies</a> · <a href="#lieux">Most-cited places</a> · <a href="#methode">Method and limits</a></p>')
    # carte + contrôles
    h += T('<h2 id="carte">La carte</h2>', '<h2 id="carte">The map</h2>')
    sel = lambda i, opts: f'<select id="{i}" style="font-family:Georgia,serif;padding:.15rem">' + ''.join(f'<option value="{v}">{html.escape(l)}</option>' for v, l in opts) + '</select>'
    h += ('<div style="display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;font-size:.9rem;margin:.3rem 0 .5rem">'
          + f'<label>{T("Volume", "Volume")} ' + sel('f-vol', [('0', T('tous', 'all'))] + [(str(v), str(v)) for v in VOLS]) + '</label>'
          + f'<label><input type="checkbox" id="f-fr"> {T("francophones seulement", "French speakers only")}</label>'
          + f'<label>{T("Personne", "Person")} ' + sel('f-p', [('', T('toutes', 'all'))] + sorted(((k, p['nom']) for k, p in PERS.items()), key=lambda x: x[1].split()[-1])) + '</label>'
          + f'<label>{T("Années", "Years")} <input type="number" id="f-a0" value="1760" min="1760" max="1890" style="width:4.5rem"> – <input type="number" id="f-a1" value="1890" min="1760" max="1890" style="width:4.5rem"></label>'
          + f'<span id="f-n" style="color:#6b604f"></span></div>')
    h += '<div id="carte-hafen" style="height:620px;border:1px solid #c9bba3;border-radius:6px"></div>\n'
    h += T("<p class=\"avert\">La taille des cercles croît avec le nombre de mentions ; les cercles orangés sont les francophones. Choisissez une personne pour voir son parcours (les lieux dont l'année figure dans la phrase, reliés dans l'ordre chronologique) et la liste complète de ses lieux avec les pages ; une année entre parenthèses est déduite du contexte.</p>",
           "<p class=\"avert\">Circle size grows with the number of mentions; orange circles are French speakers. Pick a person to see their route (places whose year appears in the sentence, joined in chronological order) and the full list of their places with pages; a year in brackets is inferred from context.</p>")
    h += '<div id="parcours" style="font-size:.9rem"></div>\n'
    # Aubry
    # dossiers propres à une personne (pages générées à part, ex. scripts/page_provost.py)
    DOS = lambda k: (f' <small>(<a href="{DOSSIERS[k]}{"" if fr else "-en"}.html">{T("dossier", "file")}</a>)</small>' if k in DOSSIERS else '')
    h += T('<h2 id="aubry">Les liens avec Aubry</h2>', '<h2 id="aubry">Ties with Aubry</h2>')
    h += '<table><tr><th>%s</th><th>%s</th><th>%s</th></tr>' % (T('Personne (Hafen)', 'Person (Hafen)'), T('Le lien', 'The tie'), T('Fiches', 'Records'))
    for i, lfr, len_, fi in AUBRY:
        p = PERS[i]
        h += (f'<tr><td><a href="#carte" data-p="{i}" class="voir">{html.escape(p["nom"])}</a>{DOS(i)}<br><small>vol. {p["vol"]}, p. {p["page"]}-{p["fin"]}</small></td>'
              f'<td>{html.escape(lfr if fr else len_)}</td><td>{" ".join(L(x) for x in fi)}</td></tr>')
    h += '</table>'
    h += T('<p>Voir aussi <a href="reseau.html">Le réseau francophone</a> et <a href="canadiens-ouest.html">Les Canadiens de l\'Ouest</a> (Tassé, 1878).</p>',
           '<p>See also <a href="reseau-en.html">The French-speaking network</a> and <a href="canadiens-ouest-en.html">The Canadians of the West</a> (Tassé, 1878).</p>')
    # index
    h += T('<h2 id="index">Les 229 biographies</h2>', '<h2 id="index">The 229 biographies</h2>')
    h += T("<p>Classées par volume. « Lieux » donne le nombre de lieux datés relevés ; cliquez sur un nom pour afficher son parcours sur la carte. Les fleurons (⚜) marquent les francophones.</p>",
           "<p>Ordered by volume. “Places” gives the number of dated places found; click a name to show the route on the map. Fleurs-de-lis (⚜) mark French speakers.</p>")
    cnt = {}
    for e in EV: cnt[e['id']] = cnt.get(e['id'], 0) + 1
    for v in VOLS:
        h += f'<h3>{T("Volume", "Volume")} {v}</h3><table><tr><th>{T("Personne", "Person")}</th><th>{T("Dates", "Dates")}</th><th>{T("Rôle", "Role")}</th><th>{T("Pages et auteur", "Pages and author")}</th><th>{T("Lieux", "Places")}</th></tr>'
        for k, p in sorted(((k, p) for k, p in PERS.items() if p['vol'] == v), key=lambda x: x[1]['page']):
            extra = ''
            if k in TASSE:
                extra = f' · <a href="canadiens-ouest{"" if fr else "-en"}.html#{TASSE[k]}">Tassé</a>'
            h += (f'<tr><td>{"⚜ " if p["fr"] else ""}<a href="#carte" data-p="{k}" class="voir">{html.escape(p["nom"])}</a>{DOS(k)}{extra}</td><td>{p["dates"]}</td>'
                  f'<td>{html.escape(p["role"] if fr else p["role_en"])}</td><td>p. {p["page"]}-{p["fin"]}<br><small>{html.escape(p["auteur"])}</small></td><td>{cnt.get(k, 0)}</td></tr>')
        h += '</table>'
    # lieux
    h += T('<h2 id="lieux">Les lieux les plus cités</h2>', '<h2 id="lieux">Most-cited places</h2>')
    tot = {}
    for e in EV:
        tot.setdefault(e['lieu'], set()).add(e['id'])
    top = sorted(tot.items(), key=lambda x: -len(x[1]))[:40]
    h += '<ol style="columns:2;font-size:.9rem">' + ''.join(f'<li><b>{html.escape(GZ[n][3] if fr else n)}</b> : {len(s)} {T("biographies", "biographies")}</li>' for n, s in top) + '</ol>'
    # méthode
    h += T('<h2 id="methode">Méthode et limites</h2>', '<h2 id="methode">Method and limits</h2>')
    h += T(f"<ul><li><b>Repérage automatique.</b> Le texte numérisé des sept volumes a été découpé en biographies. Chaque phrase du texte courant (les notes et les références bibliographiques sont écartées) a été comparée à un répertoire de 327 lieux de la traite des fourrures : postes, forts, rendez-vous, rivières, cols, villes. Une mention = une personne, un lieu, une année, une page.</li><li><b>Années.</b> L'année est celle de la phrase ; à défaut, c'est la dernière année citée auparavant dans la biographie (champ <code>ax</code> = 0). Quelques mentions renvoient à un lieu cité sans que la personne y soit allée.</li><li><b>Homonymes.</b> « Fort William » désigne le fort Laramie, le fort Bent ou le fort William du lac Supérieur selon le contexte ; « Fort Union » le poste du Missouri ou le fort du Nouveau-Mexique (après 1851). Ces cas sont résolus par une règle simple et peuvent comporter des erreurs.</li><li><b>Rôles et dates.</b> Les rôles résumés dans l'index sont rédigés pour l'atlas ; la biographie de Hafen fait foi.</li><li><b>Volumes absents.</b> Les volumes 1 (introduction générale et premières biographies), 3 et 10 ne sont pas inclus.</li><li><b>Données.</b> <a href=\"data/hafen.geojson\" download>hafen.geojson</a> ({nev} lieux) et <a href=\"data/hafen_personnes.json\" download>hafen_personnes.json</a> (les {npers} biographies). Source : {html.escape(SRC)}.</li></ul>",
           f"<ul><li><b>Automatic extraction.</b> The scanned text of the seven volumes was split into biographies. Every sentence of the running text (notes and bibliographic references are left out) was matched against a gazetteer of 327 fur-trade places: posts, forts, rendezvous sites, rivers, passes, towns. One mention = one person, one place, one year, one page.</li><li><b>Years.</b> The year is that of the sentence; failing that, the last year mentioned earlier in the biography (field <code>ax</code> = 0). Some mentions refer to a place named without the person having gone there.</li><li><b>Homonyms.</b> “Fort William” means Fort Laramie, Bent's Fort or Fort William on Lake Superior depending on context; “Fort Union” the Missouri post or the New Mexico fort (after 1851). These cases are resolved by a simple rule and may contain errors.</li><li><b>Roles and dates.</b> The roles summarized in the index were written for the atlas; Hafen's biography is authoritative.</li><li><b>Missing volumes.</b> Volumes 1 (general introduction and first biographies), 3 and 10 are not included.</li><li><b>Data.</b> <a href=\"data/hafen.geojson\" download>hafen.geojson</a> ({nev} places) and <a href=\"data/hafen_personnes.json\" download>hafen_personnes.json</a> (the {npers} biographies). Source: {html.escape(SRC)}.</li></ul>")
    h += """<script>
(function(){
const FR=%s;
const map=new maplibregl.Map({container:'carte-hafen',style:{version:8,sources:{t:{type:'raster',tiles:['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}'],tileSize:256,attribution:'Esri, HERE, Garmin, USGS'}},layers:[{id:'t',type:'raster',source:'t',paint:{'raster-saturation':-0.5}}]},center:[-105,42],zoom:3.4});
map.addControl(new maplibregl.NavigationControl());
let G=null,P=null;
const $=i=>document.getElementById(i);
function filt(){
  const v=+$('f-vol').value, f=$('f-fr').checked, p=$('f-p').value, a0=+$('f-a0').value, a1=+$('f-a1').value;
  const c=['all',['<=',['to-number',['get','a'],0],a1]];
  if(a0>1760) c.push(['>=',['to-number',['get','a'],0],a0]);
  if(v) c.push(['==',['get','v'],v]); if(f) c.push(['==',['get','fr'],1]); if(p) c.push(['==',['get','p'],p]);
  map.setFilter('h',c);
  const n=G.features.filter(x=>{const q=x.properties,a=q.a||0;return (!v||q.v==v)&&(!f||q.fr==1)&&(!p||q.p==p)&&(a0<=1760||a>=a0)&&a<=a1;});
  $('f-n').textContent=n.length+(FR?' lieux':' places');
  const src=map.getSource('route');
  if(p){
    const s=n.filter(x=>x.properties.a&&x.properties.ax).sort((a,b)=>a.properties.a-b.properties.a);
    src.setData({type:'Feature',geometry:{type:'LineString',coordinates:s.map(x=>x.geometry.coordinates)}});
    const per=P[p];
    let h='<h3 style="margin:.6rem 0 .2rem">'+per.nom+' <small style="font-weight:normal">('+(per.dates||'')+') · vol. '+per.v_+'</small></h3><p style="margin:.2rem 0">'+(FR?per.role:per.role_en)+'</p><ol style="columns:2">';
    n.slice().sort((a,b)=>(a.properties.a||0)-(b.properties.a||0)).forEach(x=>{const q=x.properties;h+='<li>'+(q.a?(q.ax?q.a:'('+q.a+')'):'?')+' · <b>'+(FR?q.lf:q.l)+'</b> <span style="color:#6b604f">p. '+q.pg+'</span></li>';});
    $('parcours').innerHTML=h+'</ol>';
    if(n.length){const bb=n.reduce((a,x)=>{const c=x.geometry.coordinates;return [Math.min(a[0],c[0]),Math.min(a[1],c[1]),Math.max(a[2],c[0]),Math.max(a[3],c[1])]},[180,90,-180,-90]);map.fitBounds([[bb[0],bb[1]],[bb[2],bb[3]]],{padding:50,maxZoom:7});}
  } else { src.setData({type:'FeatureCollection',features:[]}); $('parcours').innerHTML=''; }
}
Promise.all([fetch('data/hafen.geojson').then(r=>r.json()),fetch('data/hafen_personnes.json').then(r=>r.json())]).then(([g,p])=>{
  G=g; P=p; for(const k in P) P[k].v_=P[k].vol+', p. '+P[k].page+'-'+P[k].fin;
  const go=()=>{
    map.addSource('h',{type:'geojson',data:g}); map.addSource('route',{type:'geojson',data:{type:'FeatureCollection',features:[]}});
    map.addLayer({id:'route',type:'line',source:'route',paint:{'line-color':'#8b2e1f','line-width':1.6,'line-dasharray':[2,1.5]}});
    map.addLayer({id:'h',type:'circle',source:'h',paint:{'circle-radius':['interpolate',['linear'],['get','n'],1,3.5,6,8],'circle-color':['case',['==',['get','fr'],1],'#c8641e','#3e5f7a'],'circle-opacity':0.55,'circle-stroke-color':'#fffdf8','circle-stroke-width':0.6}});
    map.on('click','h',e=>{const fs=e.features.slice(0,12);let h='';fs.forEach(f=>{const q=f.properties;h+='<div style="margin-bottom:.35em"><b>'+(FR?q.lf:q.l)+'</b> · '+(q.a||'?')+'<br><a href="#carte" onclick="document.getElementById(\\'f-p\\').value=\\''+q.p+'\\';document.getElementById(\\'f-p\\').dispatchEvent(new Event(\\'change\\'));return false;">'+q.nom+'</a> <small>(vol. '+q.v+', p. '+q.pg+')</small></div>';});
      if(e.features.length>12) h+='<small>+'+(e.features.length-12)+'</small>';
      new maplibregl.Popup({maxWidth:'320px'}).setLngLat(e.lngLat).setHTML(h).addTo(map);});
    map.on('mouseenter','h',()=>map.getCanvas().style.cursor='pointer'); map.on('mouseleave','h',()=>map.getCanvas().style.cursor='');
    ['f-vol','f-fr','f-p','f-a0','f-a1'].forEach(i=>$(i).addEventListener('change',filt));
    document.querySelectorAll('a.voir').forEach(a=>a.addEventListener('click',ev=>{$('f-p').value=a.dataset.p;$('f-vol').value='0';$('f-fr').checked=false;filt();}));
    const m=location.hash.match(/p=(H\\d-\\d{3})/); if(m){$('f-p').value=m[1];}
    filt();
  };
  if(map.loaded()) go(); else map.on('load',go);
});
})();
</script>
""" % ('true' if fr else 'false')
    h += '</main>\n</body>\n</html>\n'
    return h

n = geo()
for fr in (True, False):
    open(A + ('montagnards.html' if fr else 'montagnards-en.html'), 'w', encoding='utf-8').write(page(fr))
print('hafen :', len(PERS), 'biographies,', n, 'lieux')
