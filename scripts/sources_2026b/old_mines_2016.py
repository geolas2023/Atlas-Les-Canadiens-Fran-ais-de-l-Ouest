# News from Old Mines, bulletin de l'Old Mines French Project (dir. Will Thompson, University of Memphis), n° 3, printemps 2016
# (PDF du Drive de l'auteur, dossier SAINTE_GENEVIEVE_OLD_MINES_HISTORY), avec l'extrait de Moses Austin (1804). Préfixe OM16.
from commun import Corpus
OM = "News from Old Mines. The Newsletter of the Old Mines French Project, n° 3, printemps 2016"
AU = "Austin, Moses (1804), « Description of the Lead Mines in Upper Louisiana », American State Papers, 8e Congrès, 2e session, n° 103, extrait reproduit dans " + OM
C = Corpus('Recherches', 'OM16', OM, page_fmt='p. {}')
F = C.F
F('01', "La Vieille Mine (Old Mines) : quinze familles françaises fondent le village (février 1802)", 'etablissement', '1802-02/1804-11', -90.8457, 38.0103, 'c', ['Moses Austin', 'Philippe-François Renault'],
  "Dans sa description des mines de plomb de la Haute-Louisiane remise au Congrès en novembre 1804, Moses Austin explique que les « vieilles mines », ouvertes vers 1726 par Renault pour la Compagnie de Law, furent abandonnées lors de la découverte de la Mine à Burton (Potosi), à cinq milles au sud-ouest. En février 1802, quinze familles françaises s'y établissent et forment un village ; l'année suivante, la mine produit 360 000 livres de minerai, fondu surtout à la Mine à Burton faute d'autre fourneau qu'un « fourneau français ». Vingt-cinq à trente hommes au plus y travaillent.",
  '2-3', "Point au village d'Old Mines (comté de Washington, Missouri).", source=AU)
F('02', "Mine à Renault : la mine d'argent espérée de Philippe-François Renault (vers 1724-1725)", 'etablissement', '1724~/1725~', -90.80, 38.02, 'a', ['Philippe-François Renault'],
  "Selon Austin, la Mine à Renault, à six milles au nord de la Mine à Burton sur le ruisseau du même nom, fut découverte et ouverte vers 1724-1725 par Renault, qui espérait y trouver de l'argent ; en 1804, on ne l'exploitait plus depuis plus de soixante-dix ans. Arrivé au pays des Illinois au début des années 1720 avec une équipe de mineurs, Renault vivait à Saint-Philippe, village de sa création près du fort de Chartres, et rentra en France au début des années 1740. Son nom survit dans la Fourche à Renault et la « Brigade à Renault » des reconstituteurs.",
  '3, 6', "Point approximatif sur la Fourche à Renault, au nord de Potosi.", source=f"{AU} ; {OM}")
F('03', "Cimetières de la Vieille Mine : les croix de fer forgé des forgerons créoles", 'religion', '1800~/1950~', -90.8530, 38.0120, 'a', ['Kent Bone'],
  "L'historien amateur Kent Bone étudie les croix de fer forgées à la main qui marquent les tombes des cimetières de la Vieille Mine et du district minier : une simple traverse rivetée sur un montant dans le comté de Washington, des pièces soudées dans les comtés voisins, fichées dans un bloc de calcaire où l'on coulait du plomb fondu. Coutume des catholiques français, allemands et espagnols, transmise du Québec (L'Artisan forgeron), elle se maintient jusqu'au XXe siècle et disparaît avec les forgerons. Bone en a retrouvé de la vallée du Saint-Laurent à une ville métisse de la Saskatchewan, au Kankakee et aux villages cadiens de Louisiane.",
  '4, 6', "Point au cimetière de l'église Saint-Joachim d'Old Mines.")
fiches = C.fiches
