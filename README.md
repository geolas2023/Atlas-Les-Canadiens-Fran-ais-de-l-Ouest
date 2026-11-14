# Les Canadiens français de l'Ouest — Atlas historique des francophones d'Amérique du Nord

Atlas Web interactif (MapLibre GL JS) des francophones (Canadiens français, Créoles du Missouri et de l'Illinois, Français, Suisses romands) et des événements qui les concernent en Amérique du Nord. La première version porte sur l'Ouest américain ; le deuxième lot de novembre 2026 l'étend au Midwest, à la Nouvelle-Angleterre, à la Louisiane et à la Nouvelle-France. La chronologie couvre 1560-2010. Le site est publié avec GitHub Pages : `https://geolas2023.github.io/Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/`.

Projet parent : l'**Atlas Aubry** (François-Xavier Aubry, 1824-1854), dont les fiches ponctuelles sont intégrées ici.

## Corpus de cette version

| Corpus | Fiches | Contenu |
|---|---|---|
| **Cragin** | 183 | Dépouillement complet des *Early Far West Notebooks* de Francis W. Cragin (entrevues de pionniers, 1902-1923 ; transcription de Mrs. Shaw, PDF consultable de 333 pages). Toutes les mentions de francophones ont été géolocalisées : trappeurs et voyageurs (Lesperance, Ledoux, LeDuc, Levanway, Chalifoux, Lalande, Robidoux, Leroux, Janis, Provost…), familles (St. Vrain, Beaubien, Vasquez, Autobees, Lefebvre, Nolan, Gillette…), postes (fort St. Vrain, fort Vasquez, fort Uintah, fort Leche, Hardscrabble, El Pueblo), colonies (Butte Valley, La Porte, San Gerónimo), événements (révolte de Taos et de Mora en 1847, massacre du Pueblo, combats) et toponymes (Fontaine-qui-Bouille, Cache-la-Poudre, Duchesne). |
| **Recherches** | 7 | Traces francophones repérées dans la littérature et sur le Web au fil des recherches (Rio Colorado/Questa, Hardscrabble, Las Vegas, forts Robidoux…), sources citées dans chaque fiche. Corpus appelé à grandir. |
| **Hafen** | 419 | (1) 396 étapes géolocalisées tirées des 22 notices et de l'introduction de *French Fur Traders and Voyageurs in the American West* (Hafen dir., 1995), lues intégralement : chaque fiche cite la page du livre et la source primaire donnée en note par l'auteur de la notice (identifiants `F-<personnage>-NN`). (2) 23 points provisoires (`H…`) pour les autres francophones ayant une notice dans *The Mountain Men and the Fur Trade of the Far West* (1965-1972), résumés d'après des sources générales, à vérifier. |
| **Hafen MM** | 2 129 | Dépouillement des vol. 2, 4-9 de *The Mountain Men* : lieux datés des biographies de 68 francophones (repérage automatique, page citée ; à vérifier). Remplace 21 points provisoires `H…`. Script : `scripts/ajouts_2026_11.py`, données sources : `scripts/sources_2026/`. |
| **Tassé** | 174 | Joseph Tassé, *Les Canadiens de l'Ouest* (1878), t. I et II : 35 vies, 158 étapes et 16 établissements, page citée. |
| **Illinois français** | 38 | Nouvelle-France, villages de Peoria (181 habitants, East 1933), Petit Canada de la Kankakee, presse française de l'Illinois (Cormier 1957), collège Saint-Viateur, archipel du Midwest (IFMidwest). |
| **Atlas historique du Québec** | 62 | Frenette, Rivard et St-Hilaire (dir.), *La francophonie nord-américaine* (PUL, 2012) : piste de Santa Fe, Pays d'en Haut, Détroit, Louisiane, Pays des Illinois, Métis, Nouvelle-Angleterre, Midwest, Plaines, Californie (identifiants `AH-…`). |
| **Franco-Amérique** | 26 | Louder et Waddell (dir.), *Franco-Amérique* (Septentrion, 2008) (`FA-…`). |
| **Nouvelle-France** | 36 | Margry, t. I (1876) ; Johnson, *French Pathfinders* (1905) ; Marchand, *Ghost Empire* (2005) (`NF-…`). |
| **Nouvelle-Angleterre** | 44 | Vermette, *A Distinct Alien Race* (2018) ; MacDonald (1898) ; Belisle (1907) (`NA-…`). |
| **Piste de l'Oregon** | 23 | Bergeron, *La légende de l'Oregon était vraie* (`OR-…`). |
| *compléments* | 41 | Illinois français : McQuillan (1979), Papen (2006) (`IF2-…`) ; Recherches : allocution de Worcester, *Le Progrès du Golfe* (1940) (`R2-…`) ; Étienne Provost à Saint-Louis, versé depuis l'Atlas Aubry (`PV-…`, 5 fiches, dont l'ancienne L100 ; dossier `provost.html` / `provost-en.html` généré par `scripts/page_provost.py`). Script : `scripts/ajouts_2026_11b.py` (à lancer après `ajouts_2026_11.py`), données : `scripts/sources_2026b/`. |
| **Atlas Aubry** | 101 | Toutes les fiches ponctuelles (lieux et événements) de l'Atlas Aubry, avec leurs sources et leurs images. Les trajets (lignes) restent dans l'Atlas Aubry. |

Chaque fiche Cragin renvoie aux **pages du PDF** (`pages_pdf`) où se trouve le témoignage.

## Salle de lecture : les traiteurs et voyageurs français

`salle.html` offre **un onglet par personnage** du livre *French Fur Traders and Voyageurs in the American West* (22 notices + introduction), chacun avec sa couleur propre, son récit chronologique par phases, sa carte de parcours (trait pointillé, puis trait plein « déjà parcouru »), son **échelle de temps** cliquable, une liste de **pistes d'archives inédites** (sources primaires citées en note par les auteurs, ou proposées par l'atlas) et sa bibliographie. Données : `data/personnages/index.json` et `data/personnages/<id>.geojson`. Adresses directes : `salle.html#chouteau`, `salle.html#vasquez-14`.

Maurice LeDuc (onglet `leduc`, bleu ciel `#00a8e8`, couleur réservée dans tout l'atlas) réunit les 30 étapes de la première salle et 33 étapes tirées de la notice de Janet Lecompte (p. 176-189) : Fort Manuel (1812), mariage de Taos (1823), Pegleg Smith, Gila, Ashley, Frémont (1843), mariage de San Miguel (1848), recensement de 1850, etc. L'ancienne adresse `maurice-leduc.html` redirige vers cet onglet.

**Traduction et droit d'auteur.** Les passages du livre sont résumés et traduits librement en français ; les citations sont très brèves et signalées. Les sources primaires (lettres, registres, journaux) sont décrites et localisées, non reproduites.

## Pages de lecture (novembre 2026)

`canadiens-ouest.html` (Tassé, t. I et II : carte, schémas des liens, 35 vies), `montagnards.html` (Hafen, vol. 2 et 4-9 : 229 biographies, 7 708 lieux datés, carte filtrable), `illinois-francais.html` (onze sources sur l'Illinois français et le Midwest, habitants de Peoria, presse). Chaque page a sa version anglaise (`-en.html`). Ces pages viennent de l'Atlas Aubry, qui ne garde que ce qui touche Aubry et son entourage ; elles sont générées par les scripts de l'Atlas Aubry (`vers_cf.py`). Données : `data/tasse*.geojson`, `data/hafen.geojson`, `data/hafen_personnes.json`, `data/illinois_francais.geojson`, `data/peoria_habitants.json`.

## Structure

```
index.html            page principale (carte, filtres, chronologie, fiches)
css/style.css         mise en page
js/atlas.js           carte, filtres, chronologie, fiches, recherche, index des personnages
js/fonds.js           fonds de carte d'époque (repris de l'Atlas Aubry)
data/lieux.geojson    points (EPSG:4326)
data/themes.json      libellés des thèmes
data/piste.geojson    contexte : relevé de la piste de Santa Fe (Atlas Aubry)
images/aubry/         documents de l'Atlas Aubry
scripts/              scripts de construction (Cragin, recherches, Hafen, ffv/ = un module par personnage du livre)
salle.html, js/salle.js, css/salle.css   salle de lecture multi-personnages
data/personnages/     un GeoJSON par personnage + index.json
```

## Modèle d'attributs (`data/lieux.geojson`)

| Champ | Exemple | Rôle |
|---|---|---|
| `id` | `C042`, `A-L01` | identifiant stable (C = Cragin, A- = Atlas Aubry) |
| `nom` | `Fort Vasquez (Platteville)` | libellé |
| `corpus` | `Cragin` / `Atlas Aubry` | source principale |
| `theme` | `poste`, `etablissement`, `famille`, `personnage`, `evenement`, `commerce`, `migration`, `exploration`, `religion`, `toponymie` | catégorie (couleur) |
| `debut`, `fin` | `1835.0`, `1860.5` | années décimales (filtrage chronologique) |
| `date_edtf` | `1847-01-19`, `1820~` | date documentée ([EDTF](https://www.loc.gov/standards/datetime/)) |
| `precision` | `jour` / `mois` / `annee` / `circa` | précision de la date |
| `certitude` | `certaine` / `approximative` / `hypothetique` | certitude de la **localisation** |
| `personnages` | `["Céran St. Vrain", "Felix St. Vrain"]` | personnes liées (index des personnages) |
| `description` | | résumé rédigé pour l'atlas |
| `sources` | | référence complète |
| `pages_pdf` | `63; 64` | pages du PDF des carnets Cragin |
| `note` | | note critique : divergences entre témoins, identification incertaine |
| `images` | `[{"src": "images/…", "legende": "…"}]` | documents (fiches Aubry) |

Les fiches qui partagent exactement le même point (Taos, Mora…) sont légèrement décalées à l'affichage ; un clic sur un groupe affiche la liste.

## Ajouter un corpus

Ajouter des entités dans `data/lieux.geojson` avec une nouvelle valeur de `corpus`, puis déclarer ce corpus dans l'objet `CORPUS` de `js/atlas.js` (libellé et couleur du contour).

## Tester en local

```
python -m http.server 8000
```

puis ouvrir http://localhost:8000.

## Publier

*Settings → Pages → Source : Deploy from a branch → `main` / `(root)`*.

## Avertissement

Les carnets de Cragin rapportent des souvenirs recueillis des décennies après les faits ; les informateurs se contredisent parfois (lieu et date de la mort de Maurice LeDuc ou de Joseph Levanway, par exemple). Ces divergences sont signalées dans les notes. Les récits d'O. P. Wiggins, réputé pour ses exagérations, sont marqués comme tels.
