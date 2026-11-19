# Carolyn Podruchny, Making the Voyageur World: Travelers and Traders in the North American Fur Trade, Lincoln,
# University of Nebraska Press, 2006. PDF du Drive de l'auteur. Corpus « Recherches », préfixe PD06.
from commun import Corpus
PD = "Podruchny, Carolyn (2006), Making the Voyageur World: Travelers and Traders in the North American Fur Trade, Lincoln, University of Nebraska Press"
C = Corpus('Recherches', 'PD06', PD, page_fmt='p. {}')
F = C.F
F('01', "Portage du lac la Pluie, « le bout des Terres » : les noms de lieux des voyageurs selon George Nelson", 'toponymie', '1803~/1825~', -93.400, 48.608, 'a', ['George Nelson', 'Chaurette', 'Beaubien'],
  "Commis de la Compagnie du Nord-Ouest au début du XIXe siècle, George Nelson relève les noms que les Canadiens donnent aux lieux de la route du lac Supérieur au lac Winnipeg. Le portage du lac la Pluie s'appelle « le bout des Terres », vieux nom qu'il croit antérieur à la Conquête, du temps où les traiteurs français n'allaient pas plus loin et prenaient les Grands Lacs pour des bras de la mer de l'Ouest. Le portage du Rocher à Chaurette rappelle un guide qui y brisa son canot et perdit sa cargaison ; à la chute à Jacqueau, les hommes font la course avec leurs charges ; au portage de la Barrière, des téméraires s'y tuent ; un portage d'île porte le nom de Beaubien, voyageur forcé par son bourgeois à sauter un rapide où plusieurs hommes se noyèrent. Nelson reproche aussi aux voyageurs de « pervertir » les noms autochtones.",
  '76-77', "Point au portage de Fort Frances (Ontario) ; les autres lieux cités jalonnent la route de la rivière Winnipeg sans être localisés par l'auteure.")
fiches = C.fiches
