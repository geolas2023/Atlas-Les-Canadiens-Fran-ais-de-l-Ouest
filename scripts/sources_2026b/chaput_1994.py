# Donald Chaput, Virgil Earp, Western Peace Officer, Norman, University of Oklahoma Press, 1996 (1re éd. Encampment, 1994).
# PDF du Drive de l'auteur (HISTOIRE_LIVRES/DONALD_CHAPUT), lu le 19 novembre 2026 par la visionneuse du Drive (276 p.) :
# recherche des noms francophones. Préfixe CP94.
from commun import Corpus
S = "Chaput, Donald (1996), Virgil Earp, Western Peace Officer, Norman, University of Oklahoma Press (1re éd. 1994)"
C = Corpus('Recherches', 'CP94', S, page_fmt='p. {} (PDF)')
F = C.F
F('01', "Tombstone : James Vizina, magnat minier, paie la caution des Earp ; ses chevalements servent de refuge aux agresseurs de Virgil (1881)", 'personne', '1881-11/1881-12-28', -110.067, 31.713, 'c', ['James Vizina', 'Virgil Earp', 'E. B. Gage'],
  "Après la fusillade de l'O.K. Corral (26 octobre 1881), quand il faut une caution pour les Earp, les magnats miniers de Tombstone E. B. Gage et James Vizina s'empressent d'y contribuer. Le 28 décembre 1881, quand le marshal Virgil Earp est criblé de chevrotines à l'angle de la Cinquième rue et d'Allen, entre l'Oriental et la brasserie Golden Eagle, ses agresseurs s'enfuient dans l'obscurité derrière les chevalements de la mine Vizina.",
  '152, 163', "Vizina est la graphie américaine de Vézina ; Chaput ne précise pas ses origines.")
F('02', "Désert entre Salt Lake City et San Bernardino : le journal de Mme J. A. Rousseau dans le convoi de Nicholas Earp (1864)", 'personne', '1864-05-12/1864-12', -116.0, 35.5, 'h', ['Mme J. A. Rousseau', 'Nicholas Earp', 'Wyatt Earp'],
  "Le convoi de quarante chariots et 150 personnes que conduit Nicholas Earp, père de Virgil et de Wyatt, part de Council Bluffs le 12 mai 1864 pour la Californie. Mme J. A. Rousseau, invalide, en tient le journal, publié en partie : elle juge le maître du convoi exigeant, bourru et désagréable ; les Rousseau partagent leur nourriture avec les Indiens qui suivent le convoi, ce que Earp refuse et réprouve.",
  '26, 42', "Journal publié dans le Quarterly de la San Bernardino County Museum Association (1958). Origine francophone des Rousseau non établie ; point hypothétique dans le désert Mojave.")
fiches = C.fiches
