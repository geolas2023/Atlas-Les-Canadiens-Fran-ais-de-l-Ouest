// Salle de lecture : Maurice LeDuc — carte du parcours, récit, fiche et échelle de temps.
const BLEU = '#00a8e8';
const PHASES = {
  'Origines et trappe': '#9ad8f3', 'Fort LeDuc': '#00a8e8', 'Pueblo, Hardscrabble, San Gerónimo': '#0090c8',
  'Pueblo, Huerfano, Mora, Adobe Creek': '#3aa0c8', 'Dernières trappes': '#0077a8', 'Chez Maxwell': '#005f87',
  'Dernières années': '#064a6b', 'Mort': '#1d2633', 'Mémoire': '#8a9aa8'
};
const CERT = { certaine: 'certaine', approximative: 'approximative', hypothetique: 'hypothétique' };
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
let ETAPES = [], courant = -1, carte;

function fiche(i) {
  courant = i;
  const f = ETAPES[i], p = f.properties;
  $('#fiche-salle').innerHTML = `
    <p class="mini">Étape ${p.ordre} sur ${ETAPES.length} · ${esc(p.phase)}</p>
    <h2>${esc(p.nom)}</h2>
    <p class="meta">${esc(p.date_edtf)} · localisation <span class="badge ${esc(p.certitude)}">${esc(CERT[p.certitude])}</span></p>
    <div class="filet">✦</div>
    <p class="description">${esc(p.description)}</p>
    ${p.note ? `<p class="note"><strong>Note critique.</strong> ${esc(p.note)}</p>` : ''}
    <p class="sources"><strong>Sources.</strong> ${esc(p.sources)}</p>`;
  document.querySelectorAll('.etape').forEach(el => el.classList.toggle('active', +el.dataset.i === i));
  document.querySelectorAll('#frise .marque').forEach(el => el.classList.toggle('active', +el.dataset.i === i));
  $('#etape-courante').textContent = `${p.ordre}. ${p.date_edtf}`;
  document.querySelector(`.etape[data-i="${i}"]`)?.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  if (carte) {
    carte.getSource('sel').setData({ type: 'FeatureCollection', features: [f] });
    carte.flyTo({ center: f.geometry.coordinates, zoom: Math.max(carte.getZoom(), p.phase === 'Origines et trappe' ? 5 : 7.5), speed: 1.2 });
    // parcours parcouru jusqu'ici
    carte.getSource('parcouru').setData({ type: 'Feature', geometry: { type: 'LineString',
      coordinates: ETAPES.slice(0, i + 1).filter(e => e.properties.phase !== 'Mémoire').map(e => e.geometry.coordinates) } });
  }
  history.replaceState(null, '', '#' + p.id);
}

function recit(bib) {
  let html = '', phase = '';
  ETAPES.forEach((f, i) => {
    const p = f.properties;
    if (p.phase !== phase) { phase = p.phase; html += `<h3 class="phase">${esc(phase)}</h3>`; }
    html += `<div class="etape ${esc(p.certitude)}" data-i="${i}"><span class="num">${p.ordre}</span><span class="t">${esc(p.nom)}<span class="d">${esc(p.date_edtf)}</span></span></div>`;
  });
  $('#liste-etapes').innerHTML = html;
  document.querySelectorAll('.etape').forEach(el => el.onclick = () => fiche(+el.dataset.i));
  $('#biblio').innerHTML = bib.map(b => `<li>${esc(b)}</li>`).join('');
  $('#prec').onclick = () => fiche(courant <= 0 ? ETAPES.length - 1 : courant - 1);
  $('#suiv').onclick = () => fiche(courant >= ETAPES.length - 1 ? 0 : courant + 1);
  document.addEventListener('keydown', e => { if (e.key === 'ArrowRight') $('#suiv').click(); if (e.key === 'ArrowLeft') $('#prec').click(); });
  $('#legende-phases').innerHTML = '<p class="mini">Phases de vie</p>' + Object.entries(PHASES).map(([k, c]) => `<div class="leg-phase"><i style="background:${c}"></i>${esc(k)}</div>`).join('')
    + '<p class="mini" style="margin-top:.6rem">Pastille pleine : lieu certain · claire : approximatif · pointillée : hypothétique. Trait pointillé : parcours de vie reconstitué.</p>';
}

// Échelle de temps : 1790-1885 (vie), puis segment « mémoire » compressé (1900-1970)
function frise() {
  const svg = $('#frise'), W = svg.clientWidth || 1200, H = 92, G = 50, D = 70;
  const A0 = 1790, A1 = 1885, LW = (W - G - D - 120) ;
  const x = a => a <= A1 ? G + (a - A0) / (A1 - A0) * LW : G + LW + 30 + (Math.min(a, 1975) - 1900) / 75 * 80;
  let s = `<line x1="${G}" y1="44" x2="${G + LW}" y2="44" stroke="#8796ab" stroke-width="2"/>`;
  s += `<line x1="${G + LW + 30}" y1="44" x2="${G + LW + 110}" y2="44" stroke="#8796ab" stroke-width="2" stroke-dasharray="3 3"/>`;
  s += `<text x="${G + LW + 70}" y="86" text-anchor="middle">mémoire</text>`;
  // durée de vie documentée
  s += `<rect x="${x(1819)}" y="40" width="${x(1880) - x(1819)}" height="8" rx="4" fill="${BLEU}" opacity=".35"/>`;
  s += `<text x="${x(1819)}" y="12" fill="${BLEU}">départ de « Lacrosse » v. 1819</text>`;
  s += `<text x="${x(1880)}" y="12" text-anchor="end" fill="${BLEU}">mort v. 1880</text>`;
  for (let a = A0; a <= A1; a += 5) {
    const big = a % 10 === 0;
    s += `<line x1="${x(a)}" y1="${big ? 48 : 48}" x2="${x(a)}" y2="${big ? 56 : 52}" stroke="#aab3c2"/>`;
    if (big) s += `<text x="${x(a)}" y="68" text-anchor="middle">${a}</text>`;
  }
  [1900, 1950].forEach(a => { s += `<text x="${x(a)}" y="68" text-anchor="middle">${a}</text>`; });
  // marques des étapes (empilées si chevauchement)
  const occupe = [];
  ETAPES.forEach((f, i) => {
    const p = f.properties, xm = x((p.debut + Math.min(p.fin, p.debut + 3)) / 2);
    let rang = 0; while (occupe.some(o => o.r === rang && Math.abs(o.x - xm) < 15)) rang++;
    occupe.push({ x: xm, r: rang });
    const y = 44 - rang * 0 + (rang % 2 ? -1 : 1) * Math.ceil(rang / 2) * 0;
    const yy = 44 + [0, -15, 15, -28, 28][Math.min(rang, 4)];
    if (p.fin - p.debut > 1.5 && p.debut <= A1) s += `<line x1="${x(p.debut)}" y1="${yy}" x2="${x(Math.min(p.fin, A1))}" y2="${yy}" stroke="${PHASES[p.phase]}" stroke-width="3" opacity=".7"/>`;
    s += `<g class="marque" data-i="${i}"><title>${esc(p.ordre + '. ' + p.nom + ' (' + p.date_edtf + ')')}</title>
      <circle cx="${xm}" cy="${yy}" r="7" fill="${p.certitude === 'hypothetique' ? '#fff' : PHASES[p.phase]}" stroke="#063b52" stroke-width="1.5" ${p.certitude === 'hypothetique' ? 'stroke-dasharray="2 2"' : ''}/>
      <text x="${xm}" y="${yy + 3}" text-anchor="middle" style="font-size:8px;fill:${p.certitude === 'hypothetique' ? '#063b52' : '#fff'};font-weight:bold">${p.ordre}</text></g>`;
  });
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
  svg.innerHTML = s;
  svg.querySelectorAll('.marque').forEach(g => g.onclick = () => fiche(+g.dataset.i));
}

async function demarrer() {
  const data = await fetch('data/maurice-leduc.geojson').then(r => r.json());
  ETAPES = data.features.filter(f => f.geometry.type === 'Point').sort((a, b) => a.properties.ordre - b.properties.ordre);
  const parcours = data.features.find(f => f.geometry.type === 'LineString');
  recit(data.bibliographie || []);
  frise(); window.addEventListener('resize', frise);

  carte = new maplibregl.Map({ container: 'carte-salle', style: 'https://tiles.openfreemap.org/styles/positron', center: [-104.8, 37.4], zoom: 5.2, attributionControl: { compact: true } });
  carte.addControl(new maplibregl.NavigationControl(), 'top-right');
  carte.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-left');
  carte.on('load', async () => {
    const base = carte.getStyle().layers.map(l => l.id);
    carte.addSource('satellite', { type: 'raster', tileSize: 256, tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'], attribution: 'Imagerie © Esri' });
    carte.addLayer({ id: 'satellite', type: 'raster', source: 'satellite', layout: { visibility: 'none' } });
    const pts = { type: 'FeatureCollection', features: ETAPES.map(f => ({ ...f, properties: { ...f.properties, couleur: PHASES[f.properties.phase] } })) };
    carte.addSource('parcours', { type: 'geojson', data: parcours });
    carte.addSource('parcouru', { type: 'geojson', data: { type: 'Feature', geometry: { type: 'LineString', coordinates: [] } } });
    carte.addSource('etapes', { type: 'geojson', data: pts });
    carte.addSource('sel', { type: 'geojson', data: { type: 'FeatureCollection', features: [] } });
    carte.addLayer({ id: 'parcours', type: 'line', source: 'parcours', paint: { 'line-color': BLEU, 'line-width': 2, 'line-dasharray': [2, 2], 'line-opacity': .55 } });
    carte.addLayer({ id: 'parcouru', type: 'line', source: 'parcouru', paint: { 'line-color': BLEU, 'line-width': 4, 'line-opacity': .9 } });
    carte.addLayer({ id: 'sel', type: 'circle', source: 'sel', paint: { 'circle-radius': 16, 'circle-color': 'rgba(0,0,0,0)', 'circle-stroke-color': '#ffb000', 'circle-stroke-width': 3 } });
    carte.addLayer({ id: 'etapes', type: 'circle', source: 'etapes', paint: {
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 4, 7, 10, 11], 'circle-color': ['get', 'couleur'],
      'circle-stroke-color': '#063b52', 'circle-stroke-width': 1.5, 'circle-opacity': ['match', ['get', 'certitude'], 'hypothetique', .55, 1] } });
    carte.addLayer({ id: 'etapes-num', type: 'symbol', source: 'etapes', layout: { 'text-field': ['to-string', ['get', 'ordre']], 'text-size': 10, 'text-allow-overlap': true }, paint: { 'text-color': '#fff' } });
    carte.addLayer({ id: 'lieux-noms', type: 'symbol', source: 'etapes', minzoom: 7, layout: { 'text-field': ['get', 'nom'], 'text-size': 11, 'text-offset': [0, 1.3], 'text-anchor': 'top', 'text-max-width': 14, 'text-optional': true }, paint: { 'text-color': '#063b52', 'text-halo-color': '#fff', 'text-halo-width': 1.4 } });
    const fond = installerFonds(carte, base, 'satellite'); await fond('arpenteur');
    carte.on('click', 'etapes', e => fiche(ETAPES.findIndex(f => f.properties.id === e.features[0].properties.id)));
    carte.on('mouseenter', 'etapes', () => carte.getCanvas().style.cursor = 'pointer');
    carte.on('mouseleave', 'etapes', () => carte.getCanvas().style.cursor = '');
    const b = new maplibregl.LngLatBounds(); ETAPES.filter(f => f.properties.phase !== 'Origines et trappe').forEach(f => b.extend(f.geometry.coordinates));
    carte.fitBounds(b, { padding: 50, duration: 0 });
    const id = location.hash.slice(1), i = ETAPES.findIndex(f => f.properties.id === id);
    if (i >= 0) fiche(i);
  });
}
demarrer();
