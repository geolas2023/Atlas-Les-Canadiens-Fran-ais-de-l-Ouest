# Frederic L. Billon, Annals of St. Louis in its Territorial Days, from 1804 to 1821 (Saint-Louis, 1888), PDF du Drive
# de l'auteur. L'outil du Drive n'en livre que le début (jusqu'à la section sur l'arpentage de 1817) : la suite est à découper.
# Corpus « Recherches », préfixe BL88.
from commun import Corpus
BL = "Billon, Frederic L. (1888), Annals of St. Louis in its Territorial Days, from 1804 to 1821, Saint-Louis, imprimé pour l'auteur"
C = Corpus('Recherches', 'BL88', BL, page_fmt='p. {}')
F = C.F
SL = (-90.1866, 38.6268)
F('01', "Saint-Louis : le premier grand jury américain, chez Émilien Yosti, en majorité francophone (18 décembre 1804)", 'evenement', '1804-12-18/1804-12-20', *SL, 'c', ['Auguste Chouteau', 'Jacques Clamorgan', 'David Delaunay', 'Antoine Soulard', 'Bernard Pratte', 'Joseph Brazeau', 'Antoine Vincent', 'Sylvestre Labadie', 'Joseph M. Papin', 'Jean-Baptiste Trudeau', 'François-Marie Benoist', 'Pierre Didier', 'Émilien Yosti', 'Guillaume Hébert', 'Hyacinthe Église', 'André Andreville', 'Hyacinthe Saint-Cyr', 'Louis Brazeau', 'Charles Desjarlais', 'Charles Gratiot'],
  "La première cour des sessions trimestrielles du district de Saint-Louis se réunit le 18 décembre 1804 dans la maison d'Émilien Yosti. Sur le banc siègent Auguste Chouteau, Jacques Clamorgan, David Delaunay et James Mackay. Le shérif présente 24 grands jurés, dont une majorité de francophones : Soulard, Pratte, Brazeau, Vincent, Labadie, Papin, Trudeau, Benoist, Didier, Yosti, Hébert, Église, Andreville, Saint-Cyr, entre autres. Les quatre absents sont mis à l'amende de cinq dollars. Charles Desjarlais devient connétable de Florissant. La cour loue à Clamorgan, pour quinze dollars par mois, une maison qui servira de prison.",
  '9-10')
F('02', "Saint-Louis : un juré qui ne parlait pas anglais à la première exécution du comté (août-septembre 1809)", 'evenement', '1809-08-21/1809-09-16', *SL, 'c', ['Alexis Lalande', 'Antoine Barada', 'Michel Honoré', 'Auguste Chouteau', 'Jean-Baptiste-Charles Lucas'],
  "John Long fils, qui avait tué son beau-père au moulin de Long (canton de Bonhomme), est jugé le 21 août 1809 par la cour d'Oyer and Terminer, où siège Auguste Chouteau comme assesseur. Il est condamné et pendu le 16 septembre, première exécution du comté. Parmi les douze jurés figurent Antoine Barada, Michel Honoré et Alexis Lalande. Billon note que Lalande jura plus tard qu'il ne parlait ni ne comprenait un mot d'anglais.",
  '15-16')
F('03', "Saint-Louis : l'association de William Clark, Manuel Lisa et Sylvestre Labadie pour la traite du haut Missouri (1809)", 'commerce', '1809', *SL, 'c', ['Manuel Lisa', 'Sylvestre Labadie', 'William Clark', 'George Drouillard'],
  "Billon, citant la Gazette, rapporte qu'au début de 1809 William Clark, Manuel Lisa et Sylvestre Labadie s'associent avec un capital de 27 000 dollars (9 000 chacun) pour traiter avec les nations du haut Missouri jusqu'aux montagnes. Il donne à cette société le nom d'American Fur Company. Deux ans plus tôt, au printemps 1807, Lisa et George Drouillard, ancien de l'expédition Lewis et Clark, avaient remonté le Missouri avec une cargaison de 16 000 dollars.",
  '32-33', "Billon appelle cette société American Fur Company ; il s'agit des débuts de la Missouri Fur Company (St. Louis Missouri Fur Company, 1809).")
fiches = C.fiches
