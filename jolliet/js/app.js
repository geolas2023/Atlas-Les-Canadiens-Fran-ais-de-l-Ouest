// Atlas Jolliet — carte MapLibre + timeline + journal de bord
// Les entités ont des attributs numériques « debut » et « fin » (années décimales : 1697.68 = début septembre 1697).
// La timeline affiche toutes les entités commencées avant la date choisie (affichage cumulatif).
//
// Échelle de la timeline en deux segments :
//   - 1645 à 1667, par année (enfance et études à Québec), en segment compressé ;
//   - 1668 à 1700, par mois (voyages).
// La dernière position (max) = « toutes les dates ».
const AN_DEBUT = 1645, AN_DETAIL = 1668, AN_FIN = 1701;
const NB_ANNEES = AN_DETAIL - AN_DEBUT;                       // 23 positions annuelles (0 à 22)
const POS_MAX = NB_ANNEES + (AN_FIN - AN_DETAIL) * 12;        // 23 + 396 = 419
const MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
function lirePosition(v) {
  v = Number(v);
  if (v >= POS_MAX) return { libelle: 'Toutes les dates', borne: null };
  if (v < NB_ANNEES) return { libelle: `${AN_DEBUT + v}`, borne: AN_DEBUT + v + 1 };
  const m = v - NB_ANNEES;
  return { libelle: `${MOIS[m % 12]} ${AN_DETAIL + Math.floor(m / 12)}`, borne: AN_DETAIL + (m + 1) / 12 };
}

// Chapitres du livre d'Ernest Gagnon (2e éd., 1913), pour situer chaque entrée du journal
const CHAPITRES = [
  [1667.6, 'Ch. I · Naissance et jeunesse à Québec'],
  [1672.7, 'Ch. II · Au pays des grands lacs'],
  [1673.46, 'Ch. III · Vers le pays de la Folle Avoine'],
  [1673.8, 'Ch. IV-V · Sur les eaux du Mississipi'],
  [1674.9, 'Ch. VI-VII · Le retour à Québec'],
  [1675.7, 'Ch. VIII · Le second voyage et la mort de Marquette'],
  [1679.3, 'Ch. IX-X · Le mariage et la société de Québec'],
  [1680, 'Ch. XI · Le voyage à la baie d\'Hudson'],
  [1694, 'Ch. XII-XIII · Anticosti, Mingan et la guerre'],
  [1695, 'Ch. XIV · Le voyage au Labrador'],
  [9999, 'Ch. XV · Les dernières années']
];
const chapitre = t => CHAPITRES.find(([fin]) => t < fin)[1];

const VERSION = new URL(document.currentScript.src).searchParams.get('v') || '';

const carte = new maplibregl.Map({
  container: 'carte',
  style: 'https://tiles.openfreemap.org/styles/positron',
  center: [-76, 45],
  zoom: 3.3,
  attributionControl: { compact: true }
});
carte.addControl(new maplibregl.NavigationControl(), 'top-left');
carte.addControl(new maplibregl.ScaleControl({ unit: 'nautical' }), 'bottom-left');
// Légende en cartouche dans le coin supérieur droit (contenu défini dans index.html)
carte.addControl({
  onAdd() { const el = document.getElementById('legende-carte'); el.classList.add('maplibregl-ctrl'); return el; },
  onRemove() {}
}, 'top-right');
new ResizeObserver(() => carte.resize()).observe(document.getElementById('carte'));

// Couleurs d'encre par catégorie de lieu
const COULEURS = { combat: '#9a3322', fondation: '#3f5a2a', decouverte: '#2f4d63', port: '#6b5a3c', escale: '#6b5a3c',
                   naissance: '#1f2f3a', vie: '#1f2f3a', mort: '#1f2f3a', concession: '#3f5a2a', naufrage: '#9a3322' };
const couleurCategorie = ['match', ['get', 'categorie'], ...Object.entries(COULEURS).flat(), '#1f2f3a'];
const NOMS_CATEGORIE = { combat: 'combat', fondation: 'fondation', decouverte: 'découverte', port: 'port', escale: 'escale',
                         naissance: 'naissance', vie: 'vie à Québec', mort: 'mort', concession: 'seigneurie, concession', naufrage: 'naufrage' };
const NOMS_MODE = { mer: 'route maritime', cote: 'cabotage', terre: 'canot et portages', fleuve: 'navigation fluviale' };
const ENCRE_MER = '#9a3322', ENCRE_TERRE = '#1f2f3a';
const estMer = ['in', ['get', 'mode'], ['literal', ['mer', 'cote']]];

carte.on('load', async () => {
  const [lieux, trajets] = await Promise.all([
    fetch(`data/lieux.geojson?v=${VERSION}`).then(r => r.json()),
    fetch(`data/trajets.geojson?v=${VERSION}`).then(r => r.json())
  ]);
  window.DONNEES = { lieux, trajets }; // utilisé par la visite animée (visite.js)
  const couchesDeBase = carte.getStyle().layers.map(l => l.id);
  carte.addSource('lieux', { type: 'geojson', data: lieux });
  carte.addSource('trajets', { type: 'geojson', data: trajets });

  // Fond satellite (Esri World Imagery), masqué par défaut
  carte.addSource('satellite', {
    type: 'raster', tileSize: 256, maxzoom: 19,
    tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
    attribution: 'Imagerie © Esri, Maxar, Earthstar Geographics et contributeurs'
  });
  carte.addLayer({ id: 'satellite', type: 'raster', source: 'satellite', layout: { visibility: 'none' } });

  // Routes : encre rouge et tirets pour la mer, encre brune et points pour les terres et les rivières.
  // Une ligne claire dessous détache le tracé du fond.
  carte.addLayer({
    id: 'trajets-halo', type: 'line', source: 'trajets',
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#eff0e4', 'line-width': 5, 'line-opacity': ['case', ['==', ['get', 'certitude'], 'hypothetique'], 0.35, 0.6] }
  });
  carte.addLayer({
    id: 'trajets-mer', type: 'line', source: 'trajets', filter: estMer,
    layout: { 'line-join': 'round' },
    paint: { 'line-color': ENCRE_MER, 'line-width': ['case', ['==', ['get', 'certitude'], 'hypothetique'], 1.6, 2.4],
             'line-dasharray': [3, 2], 'line-opacity': ['case', ['==', ['get', 'certitude'], 'hypothetique'], 0.6, 0.95] }
  });
  carte.addLayer({
    id: 'trajets-terre', type: 'line', source: 'trajets', filter: ['!', estMer],
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': ENCRE_TERRE, 'line-width': ['case', ['==', ['get', 'certitude'], 'hypothetique'], 2, 2.8],
             'line-dasharray': [0.1, 2], 'line-opacity': ['case', ['==', ['get', 'certitude'], 'hypothetique'], 0.6, 0.95] }
  });
  // Trajet sélectionné
  carte.addLayer({
    id: 'trajet-actif', type: 'line', source: 'trajets', filter: ['==', ['get', 'id'], ''],
    layout: { 'line-cap': 'round', 'line-join': 'round' },
    paint: { 'line-color': '#c8903e', 'line-width': 6, 'line-opacity': 0.55 }
  }, 'trajets-halo');

  // Lieux : pastille d'encre pleine si localisation certaine, cerclée sur vélin sinon
  carte.addLayer({
    id: 'lieux', type: 'circle', source: 'lieux',
    paint: {
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 2, 4.5, 8, 7.5],
      'circle-color': ['case', ['==', ['get', 'certitude'], 'certaine'], couleurCategorie, '#eff0e4'],
      'circle-stroke-color': couleurCategorie,
      'circle-stroke-width': ['case', ['==', ['get', 'certitude'], 'certaine'], 1.5, 2.5]
    }
  });
  // Les combats sont marqués d'un anneau supplémentaire
  carte.addLayer({
    id: 'lieux-anneau', type: 'circle', source: 'lieux', filter: ['==', ['get', 'categorie'], 'combat'],
    paint: { 'circle-radius': ['interpolate', ['linear'], ['zoom'], 2, 7.5, 8, 11.5], 'circle-color': 'rgba(0,0,0,0)',
             'circle-stroke-color': '#9a3322', 'circle-stroke-width': 1, 'circle-stroke-opacity': 0.8 }
  }, 'lieux');
  carte.addLayer({
    id: 'lieux-noms', type: 'symbol', source: 'lieux',
    layout: { 'text-field': ['get', 'nom'], 'text-size': ['interpolate', ['linear'], ['zoom'], 2, 10.5, 8, 13],
              'text-offset': [0, 1.1], 'text-anchor': 'top', 'text-font': ['Noto Sans Italic'], 'text-max-width': 9,
              'text-optional': true, 'symbol-sort-key': ['get', 'debut'] },
    paint: { 'text-color': '#1f2f3a', 'text-halo-color': '#eff0e4', 'text-halo-width': 1.6 }
  });

  ['lieux', 'trajets-mer', 'trajets-terre'].forEach(id => {
    carte.on('click', id, e => {
      const f = e.features[0];
      afficherFiche(f.properties, f.geometry.type);
      zoomerSur(f);
    });
    carte.on('mouseenter', id, () => { carte.getCanvas().style.cursor = 'pointer'; });
    carte.on('mouseleave', id, () => { carte.getCanvas().style.cursor = ''; });
  });

  // clic ailleurs que sur un lieu ou une route : le journal se referme
  carte.on('click', e => {
    if (!carte.queryRenderedFeatures(e.point, { layers: ['lieux', 'trajets-mer', 'trajets-terre'] }).length) fermerFiche();
  });

  appliquerFond = installerFonds(carte, couchesDeBase, 'satellite');
  await appliquerFond('parchemin');
  appliquerDate(curseur.value);

  // Cadrer la carte sur l'ensemble des données
  const b = new maplibregl.LngLatBounds();
  [...lieux.features, ...trajets.features].forEach(f => {
    (f.geometry.type === 'Point' ? [f.geometry.coordinates] : f.geometry.coordinates).forEach(xy => b.extend(xy));
  });
  window.LIMITES_DONNEES = b;
  carte.fitBounds(b, { padding: { top: 50, bottom: 50, left: 170, right: 270 }, duration: 0 });
  lireAncre();
  window.addEventListener('hashchange', lireAncre);
});

function lireAncre() {
  const m = decodeURIComponent(location.hash || '').match(/(?:lieu|trajet)=([LT]\d+)/);
  if (!m || !window.DONNEES) return;
  const f = [...window.DONNEES.lieux.features, ...window.DONNEES.trajets.features].find(x => x.properties.id === m[1]);
  if (f) { afficherFiche(f.properties, f.geometry.type); zoomerSur(f); }
}

// ---------- Timeline ----------
const curseur = document.getElementById('curseur');
const sortie = document.getElementById('date-affichee');
const btnLecture = document.getElementById('lecture');
function appliquerDate(v) {
  const { libelle, borne } = lirePosition(v);
  sortie.textContent = libelle;
  const f = borne === null ? null : ['<', ['get', 'debut'], borne];
  const et = base => f ? ['all', base, f] : base;
  ['lieux', 'lieux-noms'].forEach(id => carte.setFilter(id, f));
  carte.setFilter('lieux-anneau', et(['==', ['get', 'categorie'], 'combat']));
  carte.setFilter('trajets-halo', f);
  carte.setFilter('trajets-mer', et(estMer));
  carte.setFilter('trajets-terre', et(['!', estMer]));
}
curseur.max = POS_MAX;
curseur.value = POS_MAX;
curseur.addEventListener('input', () => appliquerDate(curseur.value));

// Graduation : segment 1645-1667 compressé (par année), puis une année tous les 12 mois
(function graduer() {
  const g = document.getElementById('graduation');
  const POUCE = 18; // largeur du bouton du curseur (voir style.css)
  const position = v => `calc(${v / POS_MAX} * (100% - ${POUCE}px) + ${POUCE / 2}px)`;
  const trait = (v, cls) => { const t = document.createElement('span'); t.className = cls; t.style.left = position(v); g.appendChild(t); };
  const annee = (v, texte) => {
    const a = document.createElement('span');
    a.className = 'annee'; a.textContent = texte; a.style.left = position(v);
    a.title = `Aller à ${texte}`;
    a.addEventListener('click', () => { curseur.value = v; appliquerDate(v); });
    g.appendChild(a);
  };
  const bande = document.createElement('span');
  bande.className = 'segment-compresse'; bande.style.left = position(0);
  bande.style.width = `calc(${(NB_ANNEES - 0.5) / POS_MAX} * (100% - ${POUCE}px))`;
  bande.title = '1645-1667 : échelle compressée (une position par année)';
  g.appendChild(bande);
  for (let v = 0; v < NB_ANNEES; v++) trait(v, (AN_DEBUT + v) % 5 === 0 || v === 0 ? 'trait' : 'trait mineur');
  annee(0, '1645');
  trait(NB_ANNEES - 0.5, 'trait coupure');
  for (let v = NB_ANNEES; v < POS_MAX; v += 3) {
    const m = v - NB_ANNEES, a = AN_DETAIL + m / 12;
    trait(v, m % 12 === 0 ? 'trait' : 'trait mineur');
    if (m % 12 === 0 && a % 4 === 0) annee(v, `${a}`);
  }
})();

let minuterie = null;
btnLecture.addEventListener('click', () => {
  // « Suivre Jolliet » coché : visite animée (visite.js) ; sinon, simple défilement de la timeline
  if (document.getElementById('suivi').checked && typeof Visite !== 'undefined') { Visite.basculer(); return; }
  if (minuterie) { clearInterval(minuterie); minuterie = null; btnLecture.textContent = '▶'; return; }
  if (Number(curseur.value) >= Number(curseur.max)) curseur.value = curseur.min;
  btnLecture.textContent = '❚❚';
  minuterie = setInterval(() => {
    const v = Number(curseur.value) + 1;
    curseur.value = v; appliquerDate(v);
    if (v >= Number(curseur.max)) btnLecture.click();
  }, 250);
});

// ---------- Couches ----------
let appliquerFond = null;
document.querySelectorAll('input[name=fond]').forEach(r => r.addEventListener('change', e => { if (appliquerFond) appliquerFond(e.target.value); }));
document.getElementById('c-lieux').addEventListener('change', e => {
  ['lieux', 'lieux-anneau', 'lieux-noms'].forEach(id => carte.setLayoutProperty(id, 'visibility', e.target.checked ? 'visible' : 'none'));
});
document.getElementById('c-trajets').addEventListener('change', e => {
  ['trajets-halo', 'trajets-mer', 'trajets-terre', 'trajet-actif'].forEach(id => carte.setLayoutProperty(id, 'visibility', e.target.checked ? 'visible' : 'none'));
});

// ---------- Journal de bord (panneau documentaire) ----------
const echapper = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const NOMS_CERTITUDE = { certaine: 'localisation certaine', approximative: 'approximative', hypothetique: 'hypothétique' };
// Date EDTF -> date lisible (« 1697-09-05 » -> « 5 septembre 1697 » ; « ~ » = vers)
function dateLisible(edtf) {
  if (!edtf) return '';
  return String(edtf).split('/').map(d => {
    const approx = /[~?]/.test(d), [a, m, j] = d.replace(/[~?]/g, '').split('-').map(Number);
    const txt = j ? `${j === 1 ? '1er' : j} ${MOIS[m - 1]} ${a}` : m ? `${MOIS[m - 1]} ${a}` : `${a}`;
    return approx ? `vers ${txt}` : txt;
  }).join(' – ');
}

const ZOOM_POINT = 7;
function zoomerSur(f) {
  if (f.geometry.type === 'Point') {
    carte.flyTo({ center: f.geometry.coordinates, zoom: Math.max(carte.getZoom(), ZOOM_POINT), speed: 1.4, essential: true });
    return;
  }
  const b = new maplibregl.LngLatBounds();
  f.geometry.coordinates.forEach(xy => b.extend(xy));
  carte.fitBounds(b, { padding: { top: 60, bottom: 60, left: 60, right: 260 }, maxZoom: 7, essential: true });
}

function afficherFiche(p, geom) {
  const estTrajet = geom === 'LineString' || p.type === 'trajet';
  if (carte.getLayer('trajet-actif')) carte.setFilter('trajet-actif', ['==', ['get', 'id'], estTrajet ? p.id : '']);
  const genre = estTrajet ? (NOMS_MODE[p.mode] || 'route') : (NOMS_CATEGORIE[p.categorie] || '');
  const panneau = document.getElementById('panneau');
  panneau.innerHTML = `
    <button type="button" class="fermer" aria-label="Fermer le journal" title="Fermer (Échap)">✕</button>
    <p class="chapitre">${echapper(chapitre(Number(p.debut)))}</p>
    <h2>${echapper(p.nom)}</h2>
    <div class="filet" aria-hidden="true">⚓</div>
    <p class="entree-date">${echapper(dateLisible(p.date_edtf))}</p>
    <p class="meta">
      ${genre ? `<span class="badge genre ${echapper(estTrajet ? p.mode : p.categorie)}">${echapper(genre)}</span>` : ''}
      <span class="badge ${echapper(p.certitude)}">${echapper(NOMS_CERTITUDE[p.certitude] || p.certitude)}</span>
    </p>
    ${p.description ? `<p class="description">${echapper(p.description)}</p>` : ''}
    ${p.note ? `<p class="note"><strong>Note critique :</strong> ${echapper(p.note)}</p>` : ''}
    <div class="sources"><strong>Source :</strong> ${echapper(p.sources)}</div>`;
  panneau.querySelector('.fermer').addEventListener('click', fermerFiche);
  panneau.classList.add('ouvert');
  panneau.scrollTop = 0;
}
// Texte d'introduction (bouton « À propos » de la légende)
function afficherApropos() {
  if (carte.getLayer('trajet-actif')) carte.setFilter('trajet-actif', ['==', ['get', 'id'], '']);
  const panneau = document.getElementById('panneau');
  panneau.innerHTML = `
    <button type="button" class="fermer" aria-label="Fermer" title="Fermer (Échap)">✕</button>
    <h2>Journal de bord</h2>
    <div class="filet" aria-hidden="true">⚓</div>
    <p class="description">Baptisé à Québec en 1645, mort en 1700 sans qu'on sache où, Louis Jolliet a descendu le Mississipi avec le père Marquette en 1673, gagné la baie d'Hudson par le Saguenay en 1679 et remonté la côte du Labrador en 1694. Seigneur d'Anticosti et de Mingan, il fut le premier hydrographe du roi né au Canada. Cet atlas suit ses voyages d'après Ernest Gagnon, <em>Louis Jolliet</em> (2e éd., Montréal, Beauchemin, 1913), le <em>Récit des voyages</em> du père Marquette (1855) et les documents conservés par Bibliothèque et Archives nationales du Québec.</p>
    <p>Cliquez sur un lieu ou une route pour ouvrir son entrée du journal. La timeline avance par année de 1645 à 1667 (enfance et études à Québec), puis par mois de 1668 à 1700. Le bouton ▶ lance le voyage : le canot ou le navire suit chaque route et la carte s'arrête à chaque étape.</p>
    <p class="avertissement">Les routes sont reconstituées par les grandes voies d'eau et les escales attestées ; le pointillé signale un tracé hypothétique. Chaque entrée renvoie aux pages de Gagnon, du <em>Récit</em> ou aux fichiers de BAnQ, et signale les incertitudes.</p>
    <div class="sources">Olivier J. Caron, Département de géographie, UQAM · Documents : BAnQ, P1000,S3,D1035.</div>`;
  panneau.querySelector('.fermer').addEventListener('click', fermerFiche);
  panneau.classList.add('ouvert');
  panneau.scrollTop = 0;
}
document.getElementById('btn-apropos').addEventListener('click', afficherApropos);
function fermerFiche() {
  const panneau = document.getElementById('panneau');
  panneau.classList.remove('ouvert');
  if (carte.getLayer('trajet-actif')) carte.setFilter('trajet-actif', ['==', ['get', 'id'], '']);
}
document.addEventListener('keydown', e => { if (e.key === 'Escape') fermerFiche(); });
