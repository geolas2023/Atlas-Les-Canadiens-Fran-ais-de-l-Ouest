# Compléments au corpus « Recherches » : deux textes de mémoire qui énumèrent les fondateurs canadiens de villes américaines.
#   « Allocution au banquet de Worcester » (extrait, p. 191 d'un recueil non identifié).
#   « Dr SAP », chronique « Histoire et légendes », Le Progrès du Golfe (Rimouski), 12 avril 1940.
from commun import Corpus
WO = "« Allocution au banquet de Worcester », extrait (p. 191) d'un recueil non identifié, s. d."
PG = "Dr SAP, « Histoire et légendes », Le Progrès du Golfe, Rimouski, 12 avril 1940, p. 1"
C = Corpus('Recherches', 'R2', PG)
F = C.F
NOTE = "Liste commémorative des « fondateurs » canadiens de villes américaines ; certaines attributions sont discutables."
F('01', 'Bourbonnais (Illinois) : Noël Levasseur et François Bourbonnais', 'toponymie', '1832~', -87.879, 41.152, 'c', ['Noël Levasseur', 'François Bourbonnais'],
  "La chronique rappelle que Noël Levasseur, de Yamaska, fonde Bourbonnais, nommée d'après François Bourbonnais, natif de Beauharnois.", '', NOTE)
F('02', 'Gervais (Minnesota) : Benjamin Gervais', 'toponymie', '1840~', -93.08, 45.02, 'h', ['Benjamin Gervais'],
  "Benjamin Gervais, baptisé à Louiseville, a laissé son nom à un lieu du Minnesota (lac Gervais, près de Saint Paul).", '', NOTE, source=WO)
F('03', 'Saint Paul : Vital Guérin', 'etablissement', '1839-10', -93.09, 44.95, 'c', ['Vital Guérin'],
  "Vital Guérin, de Saint-Rémi de Napierville, est présenté comme fondateur de la capitale du Minnesota, Saint Paul.", '', NOTE)
F('04', 'Ogdensburg : François Picquet', 'religion', '1749', -75.486, 44.694, 'c', ['François Picquet'],
  "Le sulpicien François Picquet, qui avait d'abord vécu à Oka, fonde la mission de La Présentation, origine d'Ogdensburg (New York).", '', NOTE, source=WO)
F('05', 'Sault-Sainte-Marie : Repentigny', 'poste', '1750~', -84.35, 46.5, 'a', ['Louis Le Gardeur de Repentigny'],
  "Repentigny, qui demeurait à Mascouche, est donné comme fondateur du Sault-Sainte-Marie, au Michigan.", '', NOTE, source=WO)
F('06', 'Superior (Wisconsin) : Jean-Baptiste Lefebvre', 'toponymie', '1853~', -92.104, 46.721, 'h', ['Jean-Baptiste Lefebvre'],
  "Jean-Baptiste Lefebvre, de Saint-Michel d'Yamaska, est présenté comme fondateur de Superior.", '', NOTE)
F('07', 'Green Bay : Jacques Porlier', 'personnage', '1791~', -88.02, 44.513, 'a', ['Jacques Porlier'],
  "Le Montréalais Jacques Porlier est donné comme fondateur de Green Bay ; Belisle (1907) en fait le premier maître d'école du Wisconsin.", '', NOTE)
F('08', 'Los Angeles : Prudent Beaudry, premier maire canadien', 'personnage', '1875', -118.243, 34.052, 'c', ['Prudent Beaudry'],
  "Né à Sainte-Anne-des-Plaines, Prudent Beaudry est rappelé comme maire de Los Angeles.", '', "L'allocution le dit « premier maire » de Los Angeles, ce qui est inexact.", source=WO)
F('09', 'Oregon : Norbert Blanchet, premier évêque', 'religion', '1845', -122.606, 45.357, 'a', ['François-Norbert Blanchet'],
  "L'allocution rappelle que Norbert Blanchet, né à Montmagny (Saint-Pierre-de-la-Rivière-du-Sud), fut le premier évêque de l'Oregon.", '', '', source=WO)
F('10', 'Aubry City (Arizona) et « Aubry City (Colorado) »', 'toponymie', '1854~', -113.7, 35.0, 'h', ['François-Xavier Aubry'],
  "Les deux textes affirment que François-Xavier Aubry, né à Maskinongé, a donné son nom à une « Aubry City » en Arizona et à une autre au Colorado.", '',
  "Affirmation en partie inexacte : aucune localité de ce nom n'est connue au Colorado. Les lieux qui portent son nom sont, en Arizona, Aubrey Landing (le port du Colorado, voir l'Atlas Aubry) et la vallée d'Aubrey, et au Kansas le fort Aubry. Localisation symbolique (Aubrey Valley, Arizona).")

fiches = C.fiches
