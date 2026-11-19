# Coupures de presse du Drive de l'auteur (dossier FRENCH_CANADIAN_USA) sur la mémoire des pionniers canadiens-français.
# Corpus « Recherches », préfixe PRM.
from commun import Corpus
JOUR = "Le Jour (Montréal), 21 janvier 1939, p. 7 (coupure « Pionniers_CanadiensFrancais_NY », Drive de l'auteur)"
C = Corpus('Recherches', 'PRM', JOUR, page_fmt='{}')
F = C.F
F('01', "New York : le « Bal des Pionniers » canadien-français célèbre Aubry et les bâtisseurs d'empire (janvier 1939)", 'evenement', '1939-01', -73.9857, 40.7484, 'c', ['François-Xavier Aubry', 'Jacques Cartier'],
  "Le journal montréalais Le Jour annonce le bal annuel des Pionniers organisé à New York par la Société Saint-Jean-Baptiste et les Artisans canadiens-français de la ville. Le programme, rédigé en anglais pour les invités américains, rappelle que Détroit, Dubuque ou Saint-Paul ont été fondées par des bâtisseurs venus du Québec. Il présente François-Xavier Aubry, né à Maskinongé, comme l'un des plus célèbres traceurs de pistes, dont le nom fut donné à Aubry City en Arizona et au Colorado.",
  'p. 7', "Point placé au centre de Manhattan ; la salle n'est pas lisible dans la coupure.")
F('02', "Manchester (New Hampshire) : Paul Sauvé rend hommage aux pionniers canadiens-français des États-Unis (vers 1956)", 'evenement', '1956~', -71.4548, 42.9956, 'a', ['Paul Sauvé', 'Adolphe Robert', 'Josaphat-T. Benoît', 'François-Xavier Aubry', 'Joseph Robidoux', 'Prudent Beaudry', 'Jean-Baptiste Faribault', 'Pierre Ménard'],
  "Lors d'un banquet de l'Association canado-américaine à Manchester, présidé par le maire Josaphat-T. Benoît, le ministre québécois Paul Sauvé représente Maurice Duplessis. Il égrène les fondateurs canadiens-français de villes américaines : Mallet (Peoria), Bissot de Vincennes, Bourbonnais, Duluth, Le Sueur, Faribault et Prudent Beaudry, maire de Los Angeles. Il nomme aussi Joseph Robidou, explorateur des Rocheuses ; François-Xavier Aubry, qui traça la première route du Nouveau-Mexique au Pacifique ; et Pierre Ménard, premier lieutenant-gouverneur de l'Illinois. Il salue Adolphe Robert, qui dirige l'association depuis vingt ans.",
  'non paginé', "Coupure « PionniersCanadiens_USA » du Drive de l'auteur, journal montréalais non identifié ; la même page annonce le timbre américain de la fête du Travail (Camden, N.J.), ce qui situe l'article au début de septembre 1956 (à vérifier).",
  source="Coupure de presse montréalaise, « L'hon. P. Sauvé rend hommage à l'Association canado-américaine » (vers septembre 1956), Drive de l'auteur, dossier FRENCH_CANADIAN_USA")
fiches = C.fiches
