# Les Canadiens français de l'Ouest — Atlas historique des francophones d'Amérique du Nord

Atlas Web interactif (MapLibre GL JS) des francophones (Canadiens français, Créoles du Missouri et de l'Illinois, Français, Suisses romands) et des événements qui les concernent en Amérique du Nord. La première version porte sur l'Ouest américain. Le site est publié avec GitHub Pages : `https://geolas2023.github.io/Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/`.

Projet parent : l'**Atlas Aubry** (François-Xavier Aubry, 1824-1854), dont les fiches ponctuelles sont intégrées ici.

## Corpus de cette version

| Corpus | Fiches | Contenu |
|---|---|---|
| **Cragin** | 183 | Dépouillement complet des *Early Far West Notebooks* de Francis W. Cragin (entrevues de pionniers, 1902-1923 ; transcription de Mrs. Shaw, PDF consultable de 333 pages). Toutes les mentions de francophones ont été géolocalisées : trappeurs et voyageurs (Lesperance, Ledoux, LeDuc, Levanway, Chalifoux, Lalande, Robidoux, Leroux, Janis, Provost…), familles (St. Vrain, Beaubien, Vasquez, Autobees, Lefebvre, Nolan, Gillette…), postes (fort St. Vrain, fort Vasquez, fort Uintah, fort Leche, Hardscrabble, El Pueblo), colonies (Butte Valley, La Porte, San Gerónimo), événements (révolte de Taos et de Mora en 1847, massacre du Pueblo, combats) et toponymes (Fontaine-qui-Bouille, Cache-la-Poudre, Duchesne). |
| **Recherches** | 7 | Traces francophones repérées dans la littérature et sur le Web au fil des recherches (Rio Colorado/Questa, Hardscrabble, Las Vegas, forts Robidoux…), sources citées dans chaque fiche. Corpus appelé à grandir. |
| **Hafen** | 39 | Francophones ayant une notice dans Hafen (dir.), *The Mountain Men and the Fur Trade of the Far West* (vol. I, IV-IX ; tables des matières des vol. II-III non trouvées). Un point par notice (lieu principal). Résumés d'après des sources générales : texte des notices non consulté (prêt contrôlé sur archive.org), à vérifier et enrichir dès que les PDF seront fournis. Déjà présents ailleurs dans l'atlas : LeDuc, Lesperance, Laforet, Lalande, Chat Dubray, Beauvais, Janis, A. Pike Vasquez, De Mun. |
| **Atlas Aubry** | 101 | Toutes les fiches ponctuelles (lieux et événements) de l'Atlas Aubry, avec leurs sources et leurs images. Les trajets (lignes) restent dans l'Atlas Aubry. |

Chaque fiche Cragin renvoie aux **pages du PDF** (`pages_pdf`) où se trouve le témoignage.

## Salle de lecture : Maurice LeDuc

`maurice-leduc.html` retrace en 30 étapes géolocalisées la vie du trappeur canadien-français Maurice LeDuc (v. 1800 - v. 1880), fondateur du fort LeDuc (Buzzard's Roost) sur l'Adobe Creek. On y trouve un récit par phases de vie, une carte du parcours (trait pointillé, puis parcours « déjà parcouru » en trait plein), une échelle de temps cliquable, les divergences entre les sources, des pistes généalogiques et une bibliographie. Données : `data/maurice-leduc.geojson`. LeDuc a une couleur réservée (bleu ciel `#00a8e8`) dans tout l'atlas : fiches liées, couche « Parcours de Maurice LeDuc » et bande de sa durée de vie sur l'échelle de temps.

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
scripts/              scripts de construction des données (dépouillement Cragin)
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
