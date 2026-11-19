# James Adair, The History of the American Indians (1775), éd. Kathryn E. Holland Braund, Tuscaloosa, University of
# Alabama Press, 2005 (introduction et annotations). PDF du Drive de l'auteur. Corpus « Recherches », préfixe AD05.
from commun import Corpus
AD = "Adair, James (1775), The History of the American Indians, éd. Kathryn E. Holland Braund, Tuscaloosa, University of Alabama Press, 2005"
C = Corpus('Recherches', 'AD05', AD, page_fmt='p. {}')
F = C.F
F('01', "Camp des Shawnees de Pierre (Peter) Chartier, au nord-est des villages chicachas (1748)", 'personnage', '1748', -88.10, 34.75, 'h', ['Pierre Chartier', 'James Adair', 'James Glen', 'Vaudreuil'],
  "Pendant la guerre civile des Chactas, le traiteur James Adair accompagne une délégation chicacha jusqu'au camp des Shawnees de Peter Chartier, à une cinquantaine de milles au nord-est des villages chicachas. Selon Adair, Chartier travaille avec les Français à détourner les Creeks de l'alliance anglaise, et l'on comptait l'arrêter pour l'envoyer en Caroline du Sud ; selon le gouverneur Glen, il s'agissait plutôt de l'inviter à Charleston et de l'établir chez les Catawbas, mais Chartier refuse de descendre. Averti par les Alibamons, le gouverneur de la Louisiane, Vaudreuil, promet de surveiller l'affaire ; les gens de Chartier s'installent finalement chez les Creeks d'en haut.",
  '14-15', "Adair date l'épisode de 1747 ; Braund le place en 1748 d'après les lettres de Glen, qui écrit « Peter Shirtee ». Pierre Chartier, fils du traiteur Martin Chartier et d'une Shawnee, est un métis francophone. Position hypothétique.")
fiches = C.fiches
