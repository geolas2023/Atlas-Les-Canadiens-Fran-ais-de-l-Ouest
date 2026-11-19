# Robert Glass Cleland, This Reckless Breed of Men: The Trappers and Fur Traders of the Southwest (New York, Knopf, 1950),
# PDF fourni par l'auteur de l'atlas le 19 novembre 2026 (deux numérisations du même livre). Corpus « Recherches », préfixe CL50.
# Synthèse : la plupart des épisodes francophones (Chouteau-De Mun, Robidoux, St. Vrain, Pratte) sont déjà dans l'atlas ;
# on ne retient que ce que le livre ajoute. Résumés rédigés par l'atlas.
from commun import Corpus
CL = "Cleland, Robert Glass (1950), This Reckless Breed of Men: The Trappers and Fur Traders of the Southwest, New York, Alfred A. Knopf"
C = Corpus('Recherches', 'CL50', CL, page_fmt='p. {}')
F = C.F
F('01', "Rivière Umpqua : Joseph Lapoint, Toussaint Maréchal et Marion tués avec les hommes de Jedediah Smith (14 juillet 1828)", 'evenement', '1828-07-14', -123.9, 43.68, 'a', ['Joseph Lapoint', 'Toussaint Maréchal', 'Marion', 'Peter Ranne', 'Jedediah Smith', 'Michel Laframboise'],
  "Le 14 juillet 1828, sur l'Umpqua (Oregon), des Indiens (Kelawatsets) attaquent le camp de Jedediah Smith pendant son absence. Parmi les morts figurent des trappeurs francophones : Joseph Lapoint, l'un des chasseurs de Smith, Toussaint Maréchal et un certain Marion, ainsi que Harrison Rogers, Thomas Virgin, Peter Ranne et d'autres. Smith et trois survivants gagnent le fort Vancouver, où le docteur McLoughlin lance aussitôt une expédition de secours en appelant « Laframboise, Michel, Babtiste, Jacque » et ses autres hommes.",
  '112-113', "Position approximative du lieu du massacre, près de l'embouchure de la Smith dans l'Umpqua.")
F('02', "Rivière Bear (affluent de la Feather) : les brigades de Michel Laframboise et de John Work se rejoignent (16 janvier 1833)", 'exploration', '1833-01-16', -121.4, 39.0, 'a', ['Michel Laframboise', 'John Work', 'Josette Legacé'],
  "En 1832, Michel Laframboise, ancien de l'entreprise astorienne et l'un des traiteurs les plus hauts en couleur de la Compagnie de la Baie d'Hudson, entre dans la vallée du Sacramento par la piste de McLeod ; il atteint la baie de San Francisco le 15 octobre, visite les missions de San José, Sonoma et San Rafael et trappe les bras de la baie. Pendant l'hiver des crues, il remonte le Sacramento à la rencontre de la brigade de John Work ; les deux groupes se rejoignent le 16 janvier 1833 sur la Bear, affluent de la Feather. Au printemps, Work l'envoie chercher des munitions à la mission de Sonoma, puis au fort Ross des Russes.",
  '332-338', "Position approximative sur la basse Bear (Californie).")
F('03', "Brigade de la Baie d'Hudson en Californie : Josette Legacé, fille d'un trappeur français et d'une Nez-Percée (1832-1833)", 'famille', '1832-08/1833-10', -121.5, 38.6, 'h', ['Josette Legacé', 'John Work'],
  "L'épouse de John Work, Josette Legacé, fille d'un trappeur français et d'une Nez-Percée, est réputée pour sa beauté, son courage et son endurance. Elle accompagne son mari à la tête de la brigade de 1832-1833 en Californie : ni la faim, ni le danger, ni l'épidémie qui ravage alors la vallée du Sacramento ne la font rester au fort quand il part trapper.",
  '329', "Position hypothétique dans la vallée du Sacramento.")
fiches = C.fiches
