# Robert Foxcurran, Michel Bouchard et Sébastien Malette, Songs Upon the Rivers: The Buried History of the French-Speaking
# Canadiens and Métis from the Great Lakes and the Mississippi across to the Pacific, Montréal, Baraka Books, 2016.
# PDF du Drive de l'auteur. Corpus « Recherches », préfixe FX16.
from commun import Corpus
FX = "Foxcurran, Robert, Michel Bouchard et Sébastien Malette (2016), Songs Upon the Rivers: The Buried History of the French-Speaking Canadiens and Métis, Montréal, Baraka Books"
C = Corpus('Recherches', 'FX16', FX, page_fmt='p. {}')
F = C.F
F('01', "Ecorse (Michigan) : la rivière aux Écorces et la donation potawatomie aux Saint-Cosme (1776)", 'etablissement', '1764~/1800~', -83.1460, 42.2445, 'a', ['Pierre Saint-Cosme', 'Amable Saint-Cosme', 'Dominique Saint-Cosme', 'Pierre LeBlanc', 'Jean-Baptiste Salliotte', 'Pierre-Michel Campau'],
  "Entre Détroit et Frenchtown, un groupe de cabanes deviendra Ecorse. Le nom viendrait de la rivière aux Écorces, où les Hurons-Wendats auraient enseveli leurs chefs enveloppés d'écorce de bouleau près des bancs de sable. Le 1er juillet 1776, les Potawatomis donnent à Pierre Saint-Cosme et à ses fils Amable et Dominique, « par amour et affection », la terre faisant face à la rivière de Détroit et à la rivière aux Écorces ; les premiers colons tiendront leurs titres de ses héritiers. Arrivent aussi à la fin du XVIIIe siècle Pierre LeBlanc, sans doute d'ascendance acadienne, marié à une femme de la nation des Renards, trappeur et traiteur, dont le fils métis devient constable, Jean-Baptiste Salliotte, une branche des Labadie (installés dès 1764 selon certains actes) et Pierre-Michel Campau. Les premiers feuillets de bien des titres de propriété sont en français.",
  '160-161', "D'après Warnes (2009), cité par les auteurs. Point à l'embouchure de l'Ecorse River.")
fiches = C.fiches
