# Michel Chaloult, Les « Canadiens » de l'expédition Lewis et Clark, 1804-1806 : la traversée d'un continent, Sillery,
# Septentrion, 2003. PDF du Drive de l'auteur, lu en partie par Drive (environ 160 000 caractères, non paginé).
# Corpus « Recherches », préfixe CH03.
from commun import Corpus
CH = "Chaloult, Michel (2003), Les « Canadiens » de l'expédition Lewis et Clark, 1804-1806 : la traversée d'un continent, Sillery, Septentrion"
C = Corpus('Recherches', 'CH03', CH, page_fmt='{}')
F = C.F
F('01', "Camp de la rivière Dubois : les huit engagés canadiens du canot rouge (mai 1804)", 'exploration', '1804-05-14/1805-04', -90.120, 38.800, 'c', ['Jean-Baptiste Deschamps', 'Charles Hébert', 'Jean-Baptiste La Jeunesse', 'La Liberté', 'Étienne Malbœuf', 'Pierre Pinaut', 'Paul Primeau', 'François Rivet', 'Pierre Roy'],
  "Le 14 mai 1804, quarante hommes quittent le camp de la rivière Dubois, face à l'embouchure du Missouri, sur un bateau à quille et deux grandes pirogues. Le patron Deschamps commande la pirogue rouge, montée par huit engagés canadiens recrutés jusqu'au premier hivernement : Charles Hébert, Jean-Baptiste La Jeunesse, La Liberté, Étienne Malbœuf, Pierre Pinaut, Paul Primeau, François Rivet et Pierre Roy. Les journaux des capitaines parlent peu d'eux ; la plupart hivernent chez les Mandanes et redescendent à Saint-Louis sur le bateau à quille au printemps 1805. Chaloult les distingue des Canadiens et Métis membres permanents du corps (Drouillard, Charbonneau, Cruzatte, Labiche, Lepage).",
  'chap. sur le départ (édition non paginée dans la copie lue)', "L'auteur suppose que la rivière Dubois porte le nom d'un voyageur canadien.")
F('02', "Rivière Chariton (Missouri) : les « Deux Charretiers », nom d'un ancien traiteur (10 juin 1804)", 'toponymie', '1804-06-10', -92.850, 39.330, 'a', ['Jean Chariton', 'Pierre Dorion'],
  "Le 10 juin 1804, l'expédition passe deux rivières à embouchure commune que Clark appelle « Charletons », les Deux Charretiers des voyageurs, dont le cours supérieur est fréquenté par les Iowas. Chaloult rattache probablement le nom à Jean Chariton, un ancien commerçant. Peu après, l'expédition croise deux radeaux de fourrures et de suif de bison menés par le vieux Pierre Dorion, qui vit depuis vingt ans chez les Sioux et que les capitaines retiennent comme interprète.",
  'notes 32-36 du chapitre', "Étymologie donnée comme probable par l'auteur. Point à l'embouchure de la Chariton, près de Glasgow.")
fiches = C.fiches
