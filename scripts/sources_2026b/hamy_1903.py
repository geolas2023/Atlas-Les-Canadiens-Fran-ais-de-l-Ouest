# Alfred Hamy, Au Mississipi : la première exploration (1673). Le père Jacques Marquette, de Laon, et Louis Jolliet, d'après
# M. Ernest Gagnon (Paris, J. Maisonneuve, 1903), PDF Google Books du Drive de l'auteur (fichier de plus de 10 Mo :
# seule la première moitié est lisible par l'outil du Drive). Corpus « Recherches », préfixe HM03.
from commun import Corpus
HM = "Hamy, Alfred (1903), Au Mississipi : la première exploration (1673). Le père Jacques Marquette, de Laon, et Louis Jolliet, d'après M. Ernest Gagnon, Paris, J. Maisonneuve"
C = Corpus('Recherches', 'HM03', HM, page_fmt='p. {}')
F = C.F
F('01', "Saint-Ignace : la mémoire de Marquette, des restes retrouvés (1877) aux statues du Capitole et de Marquette (vers 1903)", 'religion', '1877-09-03/1903', -84.7275, 45.8664, 'c', ['Jacques Marquette', 'Louis Jolliet', 'Alfred Hamy', 'Pierre Margry', 'Gabriel Gravier'],
  "Alfred Hamy écrit en 1903 pour tirer les deux explorateurs de l'oubli en France. Sa table des matières consacre des chapitres à la découverte des restes du père Marquette à Michillimackinac (Saint-Ignace), le 3 septembre 1877. D'autres traitent de la statue de marbre offerte par le Wisconsin au Capitole de Washington, de la statue de bronze de la ville de Marquette et du projet d'un grand monument à Michillimackinac. Dans son introduction, il reproche à Margry et à Gabriel Gravier d'avoir attribué à La Salle l'honneur d'avoir navigué le premier sur le Mississippi dès 1671.",
  '5-9 (table et introduction)', "Fiche fondée sur la table des matières et l'introduction ; les chapitres XVII à XIX ne sont pas dans la partie lisible du fichier.")
fiches = C.fiches
