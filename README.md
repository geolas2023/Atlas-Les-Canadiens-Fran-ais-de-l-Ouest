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
| **Atlas Aubry** | 100 | Renvois courts vers les fiches de l'Atlas Aubry (identifiants `A-Lxx` inchangés) : nom, date, lieu, une phrase et un bouton vers la fiche complète, qui garde ses sources et ses images. |

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

## Hub entre les atlas : Atlas de l'Amérique française

Cet atlas est l'**accueil du réseau** « Atlas de l'Amérique française » : le panneau d'accueil présente les atlas du réseau d'après le registre `data/atlas.json` (une entrée par atlas : titre, description, adresse, couleur, pages ; `ici: true` pour cet atlas), et le bouton « ⚜ Les atlas » de l'en-tête y ramène. Les atlas de personnages et de familles (Aubry, Iberville, Jolliet, Robidoux) apparaissent sur la carte sous forme de renvois courts (`A-Lxx`, `I-Lxx`, `J-Lxx`, `R-Lxx`). L'ancienne adresse du portail (Atlas-de-l-Am-rique-fran-aise) redirige ici.

Chaque fiche vit dans un seul atlas ; les autres y renvoient par un lien profond, sans recopier le contenu. Les adresses des pages et les identifiants des fiches ne changent pas.

- Champ commun `voir_aussi` : liste de `{"url": …, "texte": …}`, affichée en boutons dans la fiche (les deux atlas).
- Liens profonds : `Atlas-Aubry/index.html#lieu=L78` ; `Atlas-Les-Canadiens-Fran-ais-de-l-Ouest/index.html#AH-sf08` ; `montagnards.html#p=H6-371` ; `salle.html#vasquez`.
- `scripts/hub.py` réduit le corpus Atlas Aubry à des renvois, crée les renvois des Atlas Iberville, Jolliet et Robidoux depuis leurs clones locaux (variables `IBERVILLE`, `JOLLIET`, `ROBIDOUX`) et pose les renvois des autres fiches (`VOIR_AUSSI`).
- Chaîne de production : `build.py` → `ajouts_2026_11.py` → `ajouts_2026_11b.py` → `hub.py` → `page_provost.py`.
- Pour un nouvel atlas de personnage : lui donner le même champ `voir_aussi` et un lien d'en-tête vers les autres atlas, puis ajouter ses renvois dans `hub.py`.

## Publier une nouvelle version

GitHub Pages laisse les navigateurs garder les fichiers en cache une dizaine de minutes. À chaque publication, changer le numéro `?v=` de `index.html` (scripts et feuille de style) : `js/atlas.js` le reprend pour charger les données (`lieux.geojson`, `themes.json`, `atlas.json`).

## Bibliothèque archive.org (en cours, par lots)

Dépouillement des livres du **domaine public** d'archive.org sur les francophones d'Amérique du Nord hors Québec : chaque livre forme un corpus `archive.org · <livre>` (groupe « Bibliothèque archive.org » du filtre Corpus).

- Méthode : lecture du texte intégral (OCR) par tranches ; une ligne par personne dans `scripts/sources_archive/<livre>.txt` (`NOM, Prénoms | naissance | lieu, année {contexte}; … | référence`) ; lieux résolus par `scripts/sources_archive/lieux_ouest.py` ; une fiche par lieu daté, avec le contexte de la présence (rôle, événement) paraphrasé du livre. Script : `scripts/ajouts_archive.py` (après `ajouts_2026_11b.py`, avant `hub.py`).
- Chaque fiche cite le livre (entrée ou page) et renvoie au livre sur archive.org (recherche du nom dans le texte). Repérage à vérifier ; localisation attribuée par l'atlas.
- Livres sous droit d'auteur (Hafen, *The Mountain Men* ; Lecompte) : prêt seulement sur archive.org, non lisibles ici ; à fournir en PDF.

| Livre | Identifiant archive.org | Fiches |
|---|---|---|
| Morice, *Dictionnaire historique des Canadiens et des Métis français de l'Ouest* (1908) | `dictionnairehist00mori` | 715 (dont 457 avec contexte, `morice_1908_contextes.txt`) |
| Larpenteur, *Forty Years a Fur Trader on the Upper Missouri*, éd. Coues (1898), 2 vol. | `fortyyearsfurtra01larpiala`, `fortyyearsfurtra02larpiala` | 129 |
| Tassé, *Les Canadiens de l'Ouest* (1878), 2 tomes | `cihm_33778`, `cihm_33779` | 555 |
| Billon, *Annals of St. Louis in its Early Days under the French and Spanish Dominations* (1886) | `cihm_00427` | 430 |
| Hamon, *Les Canadiens-français de la Nouvelle-Angleterre* (1891) | `cihm_39098` | 183 |
| Dugas, *L'Ouest canadien* (1896) | `cihm_30150` | 102 |
| Dugas, *Histoire de l'Ouest canadien de 1822 à 1869* (1906) | `histoiredelouest00dugauoft` | 56 |
| Dugas, *Un voyageur des pays d'en haut* (1890) | `unvoyageurdespay00duga` | 23 |
| Dugas, *La première Canadienne du Nord-Ouest* (1883) | `lapremirecanadi00duga` | 38 |
| Dugas, *Monseigneur Provencher et les missions de la Rivière-Rouge* (1889) | `monseigneurprove00duga` | 86 |
| Houck, *A History of Missouri* (1908), vol. 1 | `historyofmissour01houc` | 265 |
| Houck, *A History of Missouri* (1908), vol. 2 | `historyofmissour02houc` | 338 |
| Houck, *A History of Missouri* (1908), vol. 3 | `historyofmissour03houc` | 125 |
| Houck, *The Spanish Regime in Missouri* (1909), vol. 1 | `spanishregimeinm01houc` | 325 |
| Houck, *The Spanish Regime in Missouri* (1909), vol. 2 | `spanishregimeinm02houc` | 177 |
| Chittenden, *The American Fur Trade of the Far West* (1902), vol. 1 | `americanfurtrade01chit` | 98 |
| Chittenden, *The American Fur Trade of the Far West* (1902), vol. 2-3 | `americanfurtrade00chit_0` | 52 |
| Franchère, *Narrative of a Voyage to the Northwest Coast of America* (trad. 1854) | `cihm_35175` | 42 |
| Masson, *Les Bourgeois de la Compagnie du Nord-Ouest* (1889), vol. 1 : liste des engagés de 1804, un point par département | `cihm_30414` | 656 |
| Masson (1889), vol. 1 : journaux de Malhiot (lac du Flambeau, 1804-1805), McDonnell (1793-1795), Larocque et Charles McKenzie (Mandanes, 1804-1806) | `cihm_30414` | 60 |
| Masson, *Les Bourgeois de la Compagnie du Nord-Ouest* (1890), vol. 2 : McDonald of Garth, Keith, Johnston, Wilcocke (mort de Frobisher), Cameron (Nipigon), James McKenzie (fort Chipewyan) | `cihm_30415` | 59 |
| Coues (dir.), *New Light on the Early History of the Greater Northwest* (1897), vol. 1 : journal d'Alexander Henry le jeune à la rivière Rouge (1799-1808) | `newlightonearlyh01henr` | 155 |
| Coues (dir.), *New Light* (1897), vol. 2 : Henry en Saskatchewan (1808-1811) et au fort George/Astoria (1813-1814), notes tirées de Thompson | `newlightonearlyh02henr` | 164 |
| Perrault, « Narrative of the Travels and Adventures of a Merchant Voyageur » (1783-1820), *Michigan Pioneer and Historical Collections*, vol. 37 (1910) | `michiganhistoric37michuoft` | 82 |
| Cox, *Adventures on the Columbia River* (1832) | `adventuresoncolu00coxr` | 48 |
| Ross, *The Fur Hunters of the Far West* (1855), 2 vol. | `cihm_40228`, `cihm_40229` | 12 |
| Burton, *Cadillac's Village, or Detroit under Cadillac* (1896) : lots du village et répertoire des habitants, 1701-1710 | `cadillacsvillage00burt` | 151 |
| Hamlin, *Legends of le Détroit* (1884) : légendes situées et notice des anciennes familles françaises | `legendsofledtr00haml` | 58 |
| « Cadillac Papers », *Michigan Pioneer and Historical Collections*, vol. 33 (1904) | `michiganhistoric33michuoft` | 62 |
| « Cadillac Papers » (suite) et « Detroit Rulers », *Michigan Pioneer and Historical Collections*, vol. 34 (1905) | `michiganhistoric34michuoft` | 49 |
| Ross et Catlin, *Landmarks of Detroit* (1898), partie historique jusqu'en 1832 | `landmarksofdetr00ross` | 44 |
| Andreas, *History of Chicago*, vol. 1 (1884) : Chicago français et métis jusqu'en 1832 | `historyofchicago01andr` | 40 |
| *Portrait and Biographical Record of Kankakee County* (1892) : Canadiens de Bourbonnais, Sainte-Anne et Kankakee | `portraitbiographica00lake` | 38 |
| `cu31924092232747` | 22 |
| `transactionsrepo00nebr` | 9 |
| `bwb_P8-BLU-581` | 9 |
| `cu31924028874141` | 7 |
| `collectionofnebr00daug` | 11 |
| Andreas (1882), transcription kancoll.org | 29 |
| `idahochronologyn00reesrich` | 12 |
| `historyofstateof00bros` | 14 |
| `illustratedhisto00slwe` | 15 |
| `driggs` | 13 |
| `historyofidahoge01hawl` | 11 |
| `OregonMissionsAndTravels` | 9 |
| `historyidaho1884` | 23 |
| `adventuresofcap00irvi` | 22 |
| `historyofwashing31banc` | 6 |
| `historyofwashing31banc` (Montana) | 46 |
| `IndianAndWhiteInTheNW` | 35 |


## Un point par lieu et adresses précises

Sur la carte, les fiches qui partagent exactement les mêmes coordonnées forment un seul point, dont la taille dépend du nombre de fiches visibles (selon les filtres et la période). Un clic ouvre la liste des fiches du lieu, regroupées par décennie, avec un filtre rapide. Les points dont toutes les fiches ont une localisation hypothétique (région, district) sont dessinés en pâle avec un contour brun et signalés comme « localisation approximative ». Les adresses `index.html#ID` des fiches ne changent pas.

Quand une source donne une adresse précise, la fiche quitte le point générique de la ville et rejoint son propre emplacement. Pour Saint-Louis, les coins de rues cités par Billon (1886) sont reconstitués sur le quadrillage actuel du centre-ville (`scripts/sources_archive/adresses.py`, précision d'environ 50 m) ; la liste est dans `billon_1886_adresses.txt` (une ligne par adresse : nom, années, rues, angle, description, page).

Les concessions verbales de Laclède (1765), que Billon énumère par numéro d'îlot (p. 37-39), sont placées dans la bonne partie de leur îlot (moitié, quart ou sixième) grâce à `billon_1886_ilots.txt`. La numérotation des îlots a été reconstituée et recoupée avec une dizaine d'adresses données ailleurs par Billon : îlots 1 à 12 entre le fleuve et Main, du sud au nord (7 = place d'Armes) ; 27 à 41 entre Main et Second, du nord au sud (34 = îlot de Laclède) ; 52 à 64 entre Second et Third, du sud au nord (59 = îlot de l'église). Les îlots 13 à 26, 42 à 51 et au-delà de 64 (par exemple 18, 44 ou 82) restent non placés faute de repère sûr.
