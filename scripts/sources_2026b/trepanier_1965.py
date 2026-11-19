# Léon Trépanier, « Un Montréalais du siècle dernier : l'immigrant juif Louis Marchand », Les Cahiers des Dix, n° 30 (1965),
# p. 131-148, PDF Érudit du Drive de l'auteur (dossier Aubry). Corpus « Recherches », préfixe TR65.
from commun import Corpus
TR = "Trépanier, Léon (1965), « Un Montréalais du siècle dernier : l'immigrant juif Louis Marchand », Les Cahiers des Dix, n° 30, p. 131-148"
C = Corpus('Recherches', 'TR65', TR, page_fmt='p. {}')
F = C.F
F('01', "La Nouvelle-Orléans : Lévi Koopman, dit Louis Marchand, jeune immigrant hollandais terrassé par la fièvre jaune (vers 1824-1825)", 'migration', '1824~/1826-11-08', -90.0650, 29.9580, 'a', ['Louis Marchand (Lévi Koopman)', 'Eustache Soupras'],
  "Né à Amsterdam en 1800 dans une famille juive de joailliers, Lévi Koopman porte le nom de Marchand adopté par son père sous le régime français. Après un séjour en Angleterre, il débarque à Charleston chez un cousin, puis gagne La Nouvelle-Orléans, attiré par sa population de langue française, malgré une épidémie de fièvre jaune. Il y tombe malade ; à sa sortie de l'hôpital, son infirmière s'est enfuie avec sa montre et son argent. Il fait ensuite commerce de toiles et de dentelles à New York avant de monter à Montréal en 1826. Commis du marchand Eustache Soupras à Saint-Mathias, baptisé par Mgr Lartigue en 1828, il est délégué de Saint-Mathias à l'assemblée des Six-Comtés (1837) et emprisonné comme patriote. Il meurt à Montréal en 1881.",
  '131-136', "Homonyme de Louis Marchand de Saint-Jean-sur-Richelieu (1789-1865), patron de François-Xavier Aubry ; aucun lien établi. Point placé à La Nouvelle-Orléans.")
fiches = C.fiches
