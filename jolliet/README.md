# Atlas géohistorique — Louis Jolliet (1645–1700)

Atlas Web interactif (MapLibre GL JS) avec une carte, une timeline et un « journal de bord » documentaire. Même mécanique que l'[Atlas Iberville](https://github.com/geolas2023/Atlas-Iberville) et l'[Atlas Aubry](https://github.com/geolas2023/Atlas-Aubry) : habillage de carte ancienne, visite animée où le canot (rivières, portages) ou le navire (mer, cabotage) suit chaque route.

Louis Jolliet, baptisé à Québec le 21 septembre 1645, descend le Mississipi avec le père Jacques Marquette en 1673, gagne la baie d'Hudson par le Saguenay et le lac Mistassini en 1679, devient seigneur de Mingan et d'Anticosti, remonte la côte du Labrador en 1694 et finit hydrographe du roi à Québec. Il meurt en 1700, à une date et en un lieu incertains.

## Sources

- **Ernest Gagnon**, *Louis Jolliet, découvreur du Mississipi et du pays des Illinois, premier seigneur de l'île d'Anticosti*, 2e éd., Montréal, Beauchemin, 1913 ([archive.org : louisjollietdc00gagnuoft](https://archive.org/details/louisjollietdc00gagnuoft)). Ouvrage du domaine public, fil conducteur de l'atlas (chapitres affichés dans le journal).
- ***Récit des voyages et des découvertes du R. Père Jacques Marquette*** […], Albany, Weed, Parsons, 1855 ([archive.org : recitdesvoyagese00marq](https://archive.org/details/recitdesvoyagese00marq)) : itinéraire et dates du voyage de 1673, journal autographe de Marquette (1674-1675), voyage du père Allouez (1677).
- **Bibliothèque et Archives nationales du Québec**, *Documents officiels et Relations sur les voyages de Louis Jolliet*, fonds P1000, S3, D1035, fichiers 1 à 48 ([BAnQ numérique](https://numerique.banq.qc.ca/patrimoine/details/52327/3103023)) : adjudication de 1685 (fichiers 1-4), acte de mariage de 1675 (5-6), acte de baptême de 1645 (7-8), journal du voyage au Labrador de 1694 (9-12), *Relation de la découverte de la mer du Sud* et lettre de Jolliet du 10 octobre 1674 (manuscrit 13-28, édition de 1944 29-36, transcription 37-47).

Chaque entité renvoie aux pages ou aux fichiers utilisés (champ `sources`). Les descriptions sont des résumés rédigés pour l'atlas ; la `note` critique signale les localisations approximatives, les tracés reconstitués et les divergences entre sources (date du départ de Michillimakinac, lieu de l'hivernage de 1673-1674, lieu de la mort).

## Structure

```
index.html            page principale
css/style.css         mise en page et habillage (parchemin, cartouche, journal de bord)
js/fonds.js           fonds de carte : Parchemin (par défaut), Plan moderne, Satellite ; lignes de rhumb
js/app.js             carte, couches, timeline (1645-1667 par année, 1668-1700 par mois), fiches
js/visite.js          visite animée (canot ou navire selon le mode de la route)
data/lieux.geojson    46 lieux (points)
data/trajets.geojson  18 routes (lignes)
scripts/donnees.py    construit les deux GeoJSON (textes, dates, coordonnées, sources)
images/               canot, navire, rose des vents, ornements, bords brûlés
```

## Modèle d'attributs (compatible QGIS)

Identique à l'Atlas Iberville : `id` (L = lieu, T = trajet), `nom`, `debut` et `fin` (années décimales), `date_edtf`, `precision`, `certitude` (`certaine`, `approximative`, `hypothetique`), `categorie` pour les lieux (`decouverte`, `escale`, `concession`, `combat`, `naufrage`, `naissance`, `vie`, `mort`), `mode` pour les routes (`mer`, `cote`, `terre`, `fleuve`), `description`, `sources`, `note`.

## Tester en local

```
python -m http.server 8000
```

puis http://localhost:8000.

## Adresse

L'atlas est publié dans le dossier `jolliet/` du dépôt de l'Atlas de l'Amérique française : `https://geolas2023.github.io/Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/jolliet/`. Il peut être déplacé tel quel dans un dépôt `Atlas-Jolliet` (tous les chemins sont relatifs).
