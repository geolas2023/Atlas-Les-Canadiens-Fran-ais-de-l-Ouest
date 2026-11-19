# Maria R. Audubon (éd.), Audubon and his Journals, New York, Scribner, 1897, vol. 2 (« The Missouri River Journals »,
# notes d'Elliott Coues). PDF archive.org du Drive de l'auteur, lu en partie par Drive. Corpus « Recherches », préfixe AU43.
from commun import Corpus
AU = "Audubon, Maria R. (éd.) (1897), Audubon and his Journals, vol. 2, New York, Scribner"
C = Corpus('Recherches', 'AU43', AU, page_fmt='p. {}')
F = C.F
F('01', "Fort Union : le vieil Étienne Provost, chasseur d'Audubon (juin 1843)", 'personnage', '1843-06-12/1843-06-30', -104.040, 47.999, 'c', ['Étienne Provost', 'Bonaventure', 'Charles Larpenteur', 'Francis A. Chardon'],
  "Pendant le séjour d'Audubon au fort Union en juin 1843, le « vieux patron » Provost, qui a emmené une de ses filles sur le vapeur, est l'un des chasseurs de l'expédition. Il part avant l'aube de l'autre côté du Missouri avec Alexis, revient avec un cerf ou une biche, prépare la saumure où l'on conserve les antilopes, porte des messages au fort de l'opposition et fabrique des appeaux qui imitent le bêlement des faons pour attirer les biches. Le journal nomme aussi les chasseurs Alexis (dont la femme accompagne la troupe) et Bonaventure, « excellent tireur », Larpenteur qui ouvre les portes du fort au lever du soleil, et Chardon, qui part en barque pour le fort des Pieds-Noirs.",
  '30-65', "Lecture partielle du volume (environ 137 000 caractères). Point au fort Union.")
fiches = C.fiches
