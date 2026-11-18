const FFT = 'https://archive.org/details/frenchfurtraders0000unse';
const lienSrc = t => esc(t || '').replace(/(French Fur Traders and Voyageurs in the American West[^;]*?)\b(pp?\. (\d+)[^;.]*)/, (m, a, b, n) => `${a}<a href="${FFT}/page/${n}/mode/1up" target="_blank" rel="noopener">${b}</a>`);
// Salle de lecture multi-personnages : un onglet, une carte de parcours et une échelle de temps par personnage.
// Données : data/personnages/index.json et data/personnages/<id>.geojson
const CERT = { certaine: 'certaine', approximative: 'approximative', hypothetique: 'hypothétique' };
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
let INDEX = [], DOC = null, P = null, ETAPES = [], PHASES = {}, courant = -1, carte, carteOk = false;
const cache = {};

// Nuances d'une couleur de base, du clair au foncé, une par phase
function nuances(hex, n) {
  const r = parseInt(hex.slice(1, 3), 16), g = parseInt(hex.slice(3, 5), 16), b = parseInt(hex.slice(5, 7), 16);
  return Array.from({ length: n }, (_, i) => {
    const t = n === 1 ? 0 : -0.45 + 0.9 * i / (n - 1);   // -0.45 (clair) → +0.45 (foncé)
    const f = c => Math.round(t < 0 ? c + (255 - c) * -t : c * (1 - t));
    return '#' + [f(r), f(g), f(b)].map(v => v.toString(16).padStart(2, '0')).join('');
  });
}
const sombre = hex => { const v = parseInt(hex.slice(1), 16); return ((v >> 16) * .3 + ((v >> 8) & 255) * .59 + (v & 255) * .11) < 150; };

function onglets() {
  $('#onglets').innerHTML = INDEX.map(p => `<button type="button" role="tab" data-id="${p.id}" style="--c:${p.couleur}" title="${esc(p.nom)} — ${esc(p.auteur)}, p. ${esc(p.pages)} · ${p.etapes} étapes"><i></i>${esc(p.nom)}<small>${esc(p.vie)}</small></button>`).join('');
  document.querySelectorAll('#onglets button').forEach(b => b.onclick = () => ouvrir(b.dataset.id));
}

async function ouvrir(id, etapeId) {
  if (!cache[id]) cache[id] = await fetch(`data/personnages/${id}.geojson`).then(r => r.json());
  DOC = cache[id]; P = DOC.personnage;
  ETAPES = DOC.features.filter(f => f.geometry.type === 'Point').sort((a, b) => a.properties.ordre - b.properties.ordre);
  const ph = [...new Set(ETAPES.map(f => f.properties.phase))];
  const nu = nuances(P.couleur, ph.filter(x => x !== 'Mémoire').length);
  PHASES = {}; let k = 0; ph.forEach(x => PHASES[x] = x === 'Mémoire' ? '#8a9aa8' : nu[k++]);
  document.documentElement.style.setProperty('--perso', P.couleur);
  document.querySelectorAll('#onglets button').forEach(b => { const on = b.dataset.id === id; b.classList.toggle('actif', on); b.setAttribute('aria-selected', on); if (on) b.scrollIntoView({ inline: 'nearest', block: 'nearest' }); });
  $('#titre-perso').textContent = P.nom;
  $('#sous-titre').innerHTML = `${esc(P.vie || '')} · notice de ${esc(P.auteur)}, <a href="${FFT}/page/${parseInt(P.pages)}/mode/1up" target="_blank" rel="noopener" title="French Fur Traders and Voyageurs in the American West sur archive.org (emprunt)">p. ${esc(P.pages)}</a>`;
  document.title = `Salle de lecture — ${P.nom}`;
  courant = -1;
  recit(); frise(); majCarte();
  $('#fiche-salle').innerHTML = `<h2>${esc(P.nom)}</h2><p class="meta">${esc(P.vie || '')}</p><div class="filet">✦</div>
    <p class="description">${esc(P.chapeau || '')}</p>
    <p class="mini">${ETAPES.length} étapes localisées. Cliquez sur une étape du récit, un point numéroté ou la frise.</p>
    <div id="legende-phases"></div>`;
  legende();
  const i = ETAPES.findIndex(f => f.properties.id === etapeId);
  if (i >= 0) fiche(i); else history.replaceState(null, '', '#' + id);
}

function fiche(i) {
  courant = i;
  const f = ETAPES[i], p = f.properties;
  $('#fiche-salle').innerHTML = `
    <p class="mini">${esc(P.nom)} · étape ${p.ordre} sur ${ETAPES.length} · ${esc(p.phase)}</p>
    <h2>${esc(p.nom)}</h2>
    <p class="meta">${esc(p.date_edtf)} · localisation <span class="badge ${esc(p.certitude)}">${esc(CERT[p.certitude])}</span></p>
    <p class="mini">${f.geometry.coordinates[1].toFixed(3)}° N, ${Math.abs(f.geometry.coordinates[0]).toFixed(3)}° O</p>
    <div class="filet">✦</div>
    <p class="description">${esc(p.description)}</p>
    ${p.note ? `<p class="note"><strong>Note critique.</strong> ${esc(p.note)}</p>` : ''}
    <p class="sources"><strong>Sources.</strong> ${lienSrc(p.sources)}</p>`;
  document.querySelectorAll('.etape').forEach(el => el.classList.toggle('active', +el.dataset.i === i));
  document.querySelectorAll('#frise .marque').forEach(el => el.classList.toggle('active', +el.dataset.i === i));
  $('#etape-courante').textContent = `${p.ordre}. ${p.date_edtf}`;
  document.querySelector(`.etape[data-i="${i}"]`)?.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  if (carteOk) {
    carte.getSource('sel').setData({ type: 'FeatureCollection', features: [f] });
    carte.flyTo({ center: f.geometry.coordinates, zoom: Math.max(carte.getZoom(), 6.5), speed: 1.2 });
    carte.getSource('parcouru').setData({ type: 'Feature', geometry: { type: 'LineString',
      coordinates: ETAPES.slice(0, i + 1).filter(e => e.properties.phase !== 'Mémoire').map(e => e.geometry.coordinates) } });
  }
  history.replaceState(null, '', '#' + p.id);
}

function recit() {
  $('#chapeau').textContent = P.chapeau || '';
  let html = '', phase = '';
  ETAPES.forEach((f, i) => {
    const p = f.properties;
    if (p.phase !== phase) { phase = p.phase; html += `<h3 class="phase">${esc(phase)}</h3>`; }
    html += `<div class="etape ${esc(p.certitude)}" data-i="${i}"><span class="num">${p.ordre}</span><span class="t">${esc(p.nom)}<span class="d">${esc(p.date_edtf)}</span></span></div>`;
  });
  $('#liste-etapes').innerHTML = html;
  document.querySelectorAll('.etape').forEach(el => el.onclick = () => fiche(+el.dataset.i));
  let blocs = (DOC.blocs || []).map(b => `<details class="bloc-salle"><summary>${esc(b.titre)}</summary>${b.html}</details>`).join('');
  if ((DOC.inedits || []).length) blocs += `<details class="bloc-salle" open><summary>Pistes d'archives inédites</summary><p class="mini">Sources primaires citées dans les notes du livre, ou proposées par l'atlas, encore à dépouiller.</p><ul>${DOC.inedits.map(x => `<li>${esc(x)}</li>`).join('')}</ul></details>`;
  blocs += `<details class="bloc-salle" open><summary>Bibliographie</summary><ol class="biblio">${(DOC.bibliographie || []).map(b => `<li>${esc(b)}</li>`).join('')}</ol></details>`;
  $('#blocs').innerHTML = blocs;
  $('#etape-courante').textContent = 'Parcours complet';
}

function legende() {
  const el = $('#legende-phases'); if (!el) return;
  el.innerHTML = '<p class="mini">Phases de vie</p>' + Object.entries(PHASES).map(([k, c]) => `<div class="leg-phase"><i style="background:${c}"></i>${esc(k)}</div>`).join('')
    + '<p class="mini" style="margin-top:.6rem">Pastille pleine : lieu certain · claire : approximatif · blanche pointillée : hypothétique. Trait pointillé : parcours reconstitué.</p>';
}

// Échelle de temps propre au personnage (+ segment « mémoire » compressé s'il y a lieu)
function frise() {
  const svg = $('#frise'), W = svg.clientWidth || 1200, H = 92, G = 40, D = 30;
  const vie = ETAPES.filter(f => f.properties.phase !== 'Mémoire');
  const mem = ETAPES.length - vie.length;
  let A0 = Math.floor((Math.min(...vie.map(f => f.properties.debut)) - 2) / 5) * 5;
  let A1 = Math.ceil((Math.max(...vie.map(f => f.properties.fin)) + 2) / 5) * 5;
  const LW = W - G - D - (mem ? 130 : 0);
  const x = a => a <= A1 ? G + (a - A0) / (A1 - A0) * LW : G + LW + 30 + (Math.min(a, 1975) - 1900) / 75 * 80;
  let s = `<line x1="${G}" y1="44" x2="${G + LW}" y2="44" stroke="#8796ab" stroke-width="2"/>`;
  if (mem) {
    s += `<line x1="${G + LW + 30}" y1="44" x2="${G + LW + 110}" y2="44" stroke="#8796ab" stroke-width="2" stroke-dasharray="3 3"/>`;
    s += `<text x="${G + LW + 70}" y="86" text-anchor="middle">mémoire</text>`;
    [1900, 1950].forEach(a => { s += `<text x="${x(a)}" y="68" text-anchor="middle">${a}</text>`; });
  }
  const pas = A1 - A0 > 80 ? 10 : 5;
  for (let a = Math.ceil(A0 / pas) * pas; a <= A1; a += pas) {
    const big = a % (pas * 2) === 0;
    s += `<line x1="${x(a)}" y1="48" x2="${x(a)}" y2="${big ? 56 : 52}" stroke="#aab3c2"/>`;
    if (big) s += `<text x="${x(a)}" y="68" text-anchor="middle">${a}</text>`;
  }
  s += `<text x="${G}" y="12" fill="${P.couleur}" style="fill:${P.couleur};font-weight:bold">${esc(P.nom)} ${esc(P.vie || '')}</text>`;
  const occupe = []; let traits = '', marques = '';
  ETAPES.forEach((f, i) => {
    const p = f.properties, xm = x((p.debut + Math.min(p.fin, p.debut + 3)) / 2);
    let rang = 0; while (occupe.some(o => o.r === rang && Math.abs(o.x - xm) < 15)) rang++;
    occupe.push({ x: xm, r: rang });
    const yy = 44 + [0, -15, 15, -28, 28, -38, 38][Math.min(rang, 6)];
    const c = PHASES[p.phase], hyp = p.certitude === 'hypothetique';
    if (p.fin - p.debut > 1.5 && p.debut <= A1) traits += `<line x1="${x(p.debut)}" y1="${yy}" x2="${x(Math.min(p.fin, A1))}" y2="${yy}" stroke="${c}" stroke-width="3" opacity=".7" pointer-events="none"/>`;
    marques += `<g class="marque" data-i="${i}"><title>${esc(p.ordre + '. ' + p.nom + ' (' + p.date_edtf + ')')}</title>
      <circle cx="${xm}" cy="${yy}" r="7" fill="${hyp ? '#fff' : c}" stroke="#1d2633" stroke-width="1.5" ${hyp ? 'stroke-dasharray="2 2"' : ''}/>
      <text x="${xm}" y="${yy + 3}" text-anchor="middle" style="font-size:8px;fill:${hyp || !sombre(c) ? '#1d2633' : '#fff'};font-weight:bold">${p.ordre}</text></g>`;
  });
  s += traits + marques;
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
  svg.innerHTML = s;
  svg.querySelectorAll('.marque').forEach(g => g.onclick = () => fiche(+g.dataset.i));
}

function majCarte() {
  if (!carteOk) return;
  const pts = { type: 'FeatureCollection', features: ETAPES.map(f => ({ ...f, properties: { ...f.properties, couleur: PHASES[f.properties.phase], texte: sombre(PHASES[f.properties.phase]) ? '#fff' : '#1d2633' } })) };
  carte.getSource('etapes').setData(pts);
  carte.getSource('parcours').setData(DOC.features.find(f => f.geometry.type === 'LineString'));
  carte.getSource('parcouru').setData({ type: 'Feature', geometry: { type: 'LineString', coordinates: [] } });
  carte.getSource('sel').setData({ type: 'FeatureCollection', features: [] });
  ['parcours', 'parcouru'].forEach(l => carte.setPaintProperty(l, 'line-color', P.couleur));
  const b = new maplibregl.LngLatBounds(); ETAPES.forEach(f => b.extend(f.geometry.coordinates));
  carte.fitBounds(b, { padding: 50, duration: 600, maxZoom: 9 });
}

async function demarrer() {
  INDEX = (await fetch('data/personnages/index.json').then(r => r.json())).personnages;
  onglets();
  const cible = INDEX.find(p => location.hash.slice(1).startsWith(p.id)) || INDEX.find(p => p.id === 'leduc') || INDEX[0];
  carte = new maplibregl.Map({ container: 'carte-salle', style: 'https://tiles.openfreemap.org/styles/positron', center: [-104.8, 38], zoom: 4, attributionControl: { compact: true } });
  carte.addControl(new maplibregl.NavigationControl(), 'top-right');
  carte.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-left');
  window.addEventListener('resize', () => DOC && frise());
  document.addEventListener('keydown', e => {
    if (!ETAPES.length) return;
    if (e.key === 'ArrowRight') fiche(courant >= ETAPES.length - 1 ? 0 : courant + 1);
    if (e.key === 'ArrowLeft') fiche(courant <= 0 ? ETAPES.length - 1 : courant - 1);
  });
  $('#prec').onclick = () => fiche(courant <= 0 ? ETAPES.length - 1 : courant - 1);
  $('#suiv').onclick = () => fiche(courant >= ETAPES.length - 1 ? 0 : courant + 1);
  await ouvrir(cible.id, location.hash.slice(1));
  carte.on('load', async () => {
    const base = carte.getStyle().layers.map(l => l.id);
    carte.addSource('satellite', { type: 'raster', tileSize: 256, tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'], attribution: 'Imagerie © Esri' });
    carte.addLayer({ id: 'satellite', type: 'raster', source: 'satellite', layout: { visibility: 'none' } });
    const vide = { type: 'FeatureCollection', features: [] };
    carte.addSource('parcours', { type: 'geojson', data: vide });
    carte.addSource('parcouru', { type: 'geojson', data: { type: 'Feature', geometry: { type: 'LineString', coordinates: [] } } });
    carte.addSource('etapes', { type: 'geojson', data: vide });
    carte.addSource('sel', { type: 'geojson', data: vide });
    carte.addLayer({ id: 'parcours', type: 'line', source: 'parcours', paint: { 'line-color': '#00a8e8', 'line-width': 2, 'line-dasharray': [2, 2], 'line-opacity': .6 } });
    carte.addLayer({ id: 'parcouru', type: 'line', source: 'parcouru', paint: { 'line-color': '#00a8e8', 'line-width': 4, 'line-opacity': .9 } });
    carte.addLayer({ id: 'sel', type: 'circle', source: 'sel', paint: { 'circle-radius': 16, 'circle-color': 'rgba(0,0,0,0)', 'circle-stroke-color': '#ffb000', 'circle-stroke-width': 3 } });
    carte.addLayer({ id: 'etapes', type: 'circle', source: 'etapes', paint: {
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 3, 7, 10, 11], 'circle-color': ['match', ['get', 'certitude'], 'hypothetique', '#ffffff', ['get', 'couleur']],
      'circle-stroke-color': '#1d2633', 'circle-stroke-width': 1.5, 'circle-opacity': ['match', ['get', 'certitude'], 'approximative', .85, 1] } });
    carte.addLayer({ id: 'etapes-num', type: 'symbol', source: 'etapes', layout: { 'text-field': ['to-string', ['get', 'ordre']], 'text-size': 10, 'text-allow-overlap': true },
      paint: { 'text-color': ['match', ['get', 'certitude'], 'hypothetique', '#1d2633', ['get', 'texte']] } });
    carte.addLayer({ id: 'lieux-noms', type: 'symbol', source: 'etapes', minzoom: 7, layout: { 'text-field': ['get', 'nom'], 'text-size': 11, 'text-offset': [0, 1.3], 'text-anchor': 'top', 'text-max-width': 14, 'text-optional': true }, paint: { 'text-color': '#1d2633', 'text-halo-color': '#fff', 'text-halo-width': 1.4 } });
    const fond = installerFonds(carte, base, 'satellite'); await fond('arpenteur');
    carte.on('click', 'etapes', e => fiche(ETAPES.findIndex(f => f.properties.id === e.features[0].properties.id)));
    carte.on('mouseenter', 'etapes', () => carte.getCanvas().style.cursor = 'pointer');
    carte.on('mouseleave', 'etapes', () => carte.getCanvas().style.cursor = '');
    carteOk = true; majCarte();
    if (courant >= 0) fiche(courant);
  });
  window.addEventListener('hashchange', () => {
    const h = location.hash.slice(1), p = INDEX.find(x => h.startsWith(x.id));
    if (p && (!P || p.id !== P.id)) ouvrir(p.id, h);
    else if (p) { const i = ETAPES.findIndex(f => f.properties.id === h); if (i >= 0 && i !== courant) fiche(i); }
  });
}
demarrer();
